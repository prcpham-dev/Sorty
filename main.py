from camera.camera import *
from camera.config import *

result = capture("test1.jpg", "./")
print(result)
PROMPT="""
You are a waste-sorting assistant.

Analyze the image and identify up to 5 distinct trash items.

For each item:
- Name the object briefly (1-3 words)
- Assign exactly ONE bin from the following list:
  - recycle
  - waste
  - cutlery
  - compost

Rules:
- Do NOT explain your reasoning.
- Do NOT include items you are unsure about.
- Do NOT invent new bin types.
- If an item has multiple parts, list each part separately.

Language requirement:
- Answer in English only
- Do NOT include emojis
- Language informal, friendly
- Limit your answer to max 50 words, the shorter the better
"""

upload_image_to_gemini(result, PROMPT, GOOGLE_API_KEY)