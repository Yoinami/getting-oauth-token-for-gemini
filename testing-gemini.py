import google.generativeai as genai
import json
from getting_token import load_creds

creds = load_creds()
genai.configure(credentials=creds)

# The following code snippet is an example of how to use the generative model to generate a food suggestion based on user information.
def generate_food_suggestion(user_info: str):
    try:
        model = genai.GenerativeModel(model_name='tunedModels/food-suggestion-ai-v1-uss801z982xp') # The model name is the model ID of the model you want to use.
        result = model.generate_content(user_info)
        print(result.text)
        response = json.loads(result.text)
        return response
    
    except json.JSONDecoder as json_err:
        pass

    except Exception as e:
        pass

    return None


# Example usage
print(generate_food_suggestion(
    """{
  "weight": 60,
  "height": 165,
  "age": 25,
  "diseases": ["None"],
  "allergies": ["Peanuts"],
  "gender": "Female",
  "exercise": "High"
}"""
))