import argparse
from openai import OpenAI
from typing import Dict, Any
from talklink.models import ClaimsData, Transcript, load_transcript_from_json
import json
import tiktoken

client = OpenAI()

system_prompt = """
### System Prompt: Enhanced Claim Extraction from Transcripts

#### Objective
You are an AI assistant tasked with extracting claims from conversation transcripts. All extracted claims must be **clear, self-contained, and contextually complete**, ensuring they are **isolated** and can be independently verified without referring back to the transcript.

#### Claim Types
- **Opinion**: Subjective beliefs or perspectives. For each opinion, cite the occurrence(s) in the transcript.
- **Fact**: Verifiable statements.
- **Prediction**: Claims about the future.
- **Evaluation**: Judgments or assessments.
- **Other**: If none of the above apply.

#### Input Format
You will receive a conversation transcript containing:
- Multiple **speakers**
- **Timestamps** for each utterance

**Example Input:**
```json
{
  "content_url": "file.mp3",
  "utterances": [
    {
      "start_time": 0.16,
      "end_time": 36.76,
      "text": "I'm very excited about robotics, but I think we should be realistic...",
      "speaker": "Harald Schafer"
    }
  ]
}
```

#### Example Output:
```json
{
  "utterances": [
    {
      "time_range": "00:00 - 00:05",
      "speaker": "Speaker 1",
      "claims": [
        {
          "type": "opinion",
          "text": "Fascism is a serious problem in modern society.",
          "occurrences": [
            {
              "utterance_index": 1,
              "timestamp": "00:02"
            }
          ]
        },
        {
          "type": "allegation",
          "text": "Donald Trump is a Nazi."
        },
        {
          "type": "evaluation",
          "text": "Many people distort reality to fit their personal narratives."
        }
      ]
    }
  ]
}
```

#### Processing Steps

For each **utterance**:

1. **Extract Claims**
   - Identify explicit and implicit **statements of belief, assertion, or evaluation** within the text.
   - Isolate each claim to ensure it can stand independently for verification.

2. **Reformat Claims**
   - **Rewrite in third person** (e.g., "I think it's a problem" → "It is a problem").
   - Ensure **each claim is complete and self-contained**, avoiding vague references and including necessary context.

3. **Classify Claims**
   - Assign one of the specified claim types.
   - For **opinion** claims, include an `"occurrences"` field detailing where in the transcript the opinion appears.

#### Rules & Constraints

- **Each claim must be self-contained** (avoid vague pronouns or references).
- **No extraneous text** outside the JSON response.
- **Maintain objectivity**—extract claims without interpreting **intent**.
- If an utterance **contains no claims**, return it with an **empty** `"claims"` array.
- **Use timestamps** (formatted as `"MM:SS"`) from the transcript when available.

#### Examples of Poor vs. Correct Claim Extraction

##### ❌ Poor Extraction (Vague, Lacks Context)
```json
{
  "claims": [
    { "type": "opinion", "text": "It was crazy." },
    { "type": "fact", "text": "That was a big mistake." }
  ]
}
```

##### ✅ Correct Extraction (Clear, Contextually Complete)
```json
{
  "claims": [
    { 
      "type": "opinion", 
      "text": "The company's decision to launch the product early was reckless.",
      "occurrences": [
        {
          "utterance_index": 3,
          "timestamp": "05:12"
        }
      ]
    },
    { 
      "type": "fact", 
      "text": "The government's withdrawal strategy in the conflict was a major mistake." 
    }
  ]
}
```
---
This ensures all extracted claims are **precise, self-contained, and meaningful**, suitable for independent verification or further research without requiring reference to the original conversation.
"""

def double_check_claims(chunk: Transcript, claims: ClaimsData) -> ClaimsData:
    print(f"Double checking claims for chunk {chunk.content_url}")
    validation_prompt = """
    ### Validation Prompt
    
    Please review the following claims extracted from the transcript. Ensure that each claim is self-contained and contextually complete. This means that you wouldn't need to directly look at the
    source transcript to understand the context of the claim, whether it's an opinion, fact, evaluation, etc.

    The start time and end time should not be included in the claim.text.
    **Claims Data:**
    {claims_data}

    **Transcript:**
    {transcript}
    """
    try:
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
            {"role": "system", "content": "You are a claims validation assistant."},
            {"role": "user", "content": validation_prompt.format(
                claims_data=json.dumps(claims.model_dump(), indent=4),
                transcript=json.dumps(chunk.model_dump(), indent=4)
            )}
        ],
        response_format=ClaimsData
    )
        
        return completion.choices[0].message.parsed
    except Exception as e:
        print(f"Failed to validate claims: {e}")
        return claims

def extract_claims_from_transcript_model(transcript: Transcript) -> ClaimsData:
    model = "gpt-4o"
    encoder = tiktoken.encoding_for_model(model)
    
    max_tokens = 15000

    claims_data = ClaimsData(utterances=[])
    start_index = 0
    end_index = 0

    print(f"Processing {len(transcript.utterances)} utterances")
    for i in range(len(transcript.utterances)):
        end_index = i
        chunk = Transcript(content_url=transcript.content_url, utterances=transcript.utterances[start_index:end_index])
        encoded_chunk = encoder.encode(chunk.model_dump_json())

        if len(encoded_chunk) > max_tokens or i == len(transcript.utterances) - 1:
            print(f"Processing chunk {start_index} to {end_index}")
            try:
                completion = client.beta.chat.completions.parse(
                    model=model,
                    messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": chunk.model_dump_json()}
                ],
                    response_format=ClaimsData
                )
                claims = completion.choices[0].message.parsed
            except Exception as e:
                print(f"Failed to extract claims: {e}")
                claims = ClaimsData(utterances=[])
            
            # Validate and refine claims
            # claims = double_check_claims(chunk, claims)

            claims_data.utterances.extend(claims.utterances)
            start_index = end_index

    print(f"Finished processing {len(claims_data.utterances)} utterances")
    return claims_data

def main(transcript_path: str, output_path: str):
    transcript = load_transcript_from_json(transcript_path)

    claims_data = extract_claims_from_transcript_model(transcript)

    with open(output_path, "w") as file:
        json.dump(claims_data.model_dump(), file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract claims from a transcript.")
    parser.add_argument("--transcript", required=True, help="Path to the transcript JSON file.")
    parser.add_argument("--output", required=True, help="Path to the output JSON file for extracted claims.")
    args = parser.parse_args()
    main(args.transcript, args.output)