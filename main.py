from camera.camera import *
from config import *

result = capture("test1.jpg", "./")
print(result)
PROMPT="Describe this image in less than 10 words."
upload_image_to_gemini("test.jpg", PROMPT, GOOGLE_API_KEY)