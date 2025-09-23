import json
import inspect

from tapestrysdk import image_to_text

# Hardcoded token and system prompt
token = "sk-tvyod3gap-mfwkw5wu"
system_prompt = ""

print("adding a line")
def extract_info_from_image(user_prompt, document,name):
    try:
        result = image_to_text(token, user_prompt, document, name, system_prompt)
        return result
    except Exception as e:
        
        return {"error": str(e)}