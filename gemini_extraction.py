import os
import time
import re
from typing import List, Dict
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or "AIzaSyAJ_JVUUIPT8LNc1dzpCFWyD5XB6YRHA1Q"
print(f"[DEBUG] GEMINI_API_KEY loaded: {bool(GEMINI_API_KEY)}")

def clean_json_response(content: str) -> str:
    """Clean the response content to extract valid JSON."""
    # Remove markdown code block formatting
    content = re.sub(r'```json\s*', '', content)
    content = re.sub(r'```\s*$', '', content)
    # Remove any leading/trailing whitespace
    content = content.strip()
    return content

def normalize_key(k):
    # Remove extra quotes, whitespace, and lowercase the key
    if isinstance(k, str):
        k = k.strip()
        if k.startswith('"') and k.endswith('"'):
            k = k[1:-1]
        k = k.strip().lower()
    return k

def clean_keys(triples):
    cleaned = []
    for t in triples:
        new_t = {normalize_key(k): v for k, v in t.items()}
        # Only keep if required keys are present
        if all(key in new_t for key in ("from", "to", "relation")):
            cleaned.append(new_t)
        else:
            print(f"[DEBUG] Skipping malformed triple: {t}")
    return cleaned

def extract_with_gemini(text: str, max_retries: int = 3) -> List[Dict]:
    print("[DEBUG] Gemini extraction called")
    if not GEMINI_API_KEY:
        print("[DEBUG] No Gemini API key found, skipping Gemini extraction.")
        return []
    genai.configure(api_key=GEMINI_API_KEY)
    
    # More explicit prompt with example
    prompt = (
        "Extract family relationships as a JSON array. Include both direct and indirect relationships. "
        "Format: [{{\"from\": \"name\", \"to\": \"name\", \"relation\": \"relation\", \"via\": [\"intermediate\", \"names\"]}}]. "
        "Example: If A is B's mother and B is C's mother, include both direct relationships and the indirect one (A is C's grandmother). "
        "Text: {text}\n"
        "Example output for 'A is B's mother. B is C's mother':\n"
        "[{{\"from\": \"A\", \"to\": \"B\", \"relation\": \"mother\"}}, "
        "{{\"from\": \"B\", \"to\": \"C\", \"relation\": \"mother\"}}, "
        "{{\"from\": \"A\", \"to\": \"C\", \"relation\": \"grandmother\", \"via\": [\"B\"]}}]"
    ).format(text=text)
    
    for attempt in range(max_retries):
        try:
            model = genai.GenerativeModel("models/gemini-1.5-flash")
            generation_config = genai.types.GenerationConfig(
                temperature=0.1,
                top_p=0.8,
                top_k=40,
                max_output_tokens=512,  # Reduced for faster processing
            )
            response = model.generate_content(
                prompt,
                generation_config=generation_config,
                safety_settings=[
                    {
                        "category": "HARM_CATEGORY_HARASSMENT",
                        "threshold": "BLOCK_NONE"
                    },
                    {
                        "category": "HARM_CATEGORY_HATE_SPEECH",
                        "threshold": "BLOCK_NONE"
                    },
                    {
                        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                        "threshold": "BLOCK_NONE"
                    },
                    {
                        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                        "threshold": "BLOCK_NONE"
                    }
                ]
            )
            content = response.text
            print(f"[DEBUG] Gemini raw response: {content}")
            
            # Clean and parse the response
            cleaned_content = clean_json_response(content)
            print(f"[DEBUG] Cleaned response: {cleaned_content}")
            
            import json
            triples = json.loads(cleaned_content)
            triples = clean_keys(triples)
            for t in triples:
                t['confidence'] = 0.99
            print(f"[DEBUG] Gemini extracted triples: {triples}")
            return triples
            
        except json.JSONDecodeError as e:
            print(f"[DEBUG] JSON parsing error (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                print("[DEBUG] Retrying with different prompt...")
                # Try a more explicit prompt on retry
                prompt = (
                    "Return ONLY a JSON array of family relationships, no markdown or other text. "
                    "Include both direct and indirect relationships with paths. "
                    "Format: [{\"from\": \"name\", \"to\": \"name\", \"relation\": \"relation\", \"via\": [\"intermediate\", \"names\"]}]. "
                    f"Text: {text}"
                )
                continue
            else:
                print("[DEBUG] Max retries reached for Gemini. Falling back to T5.")
                return []
            
        except Exception as e:
            error_str = str(e)
            print(f"[DEBUG] Gemini extraction error (attempt {attempt + 1}/{max_retries}): {error_str}")
            
            if "429" in error_str and "quota" in error_str.lower():
                if attempt < max_retries - 1:
                    # Extract retry delay from error if available
                    retry_delay = 10  # Default delay
                    if "retry_delay" in error_str:
                        try:
                            delay_match = re.search(r'seconds: (\d+)', error_str)
                            if delay_match:
                                retry_delay = int(delay_match.group(1))
                        except:
                            pass
                    
                    # Exponential backoff
                    wait_time = retry_delay * (2 ** attempt)
                    print(f"[DEBUG] Rate limited. Waiting {wait_time} seconds before retry...")
                    time.sleep(wait_time)
                    continue
                else:
                    print("[DEBUG] Max retries reached for Gemini. Falling back to T5.")
                    return []
            else:
                print(f"[DEBUG] Non-rate-limit error from Gemini: {error_str}")
                return []
    
    return [] 