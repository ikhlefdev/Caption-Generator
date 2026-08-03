
def generate_caption(product, platform, tone, feature, cta_type):
    hashtag = f"#{product.replace(' ', '')} #{platform.replace(' ', '')} #{feature.replace(' ', '')}"
    match tone:
        case "excited":
            return f"Get ready for the ultimate {product} experience on {platform}! This {feature} {product} is a game-changer. Don't miss out, {cta_type}! {hashtag}"
        case "neutral":
            return f"Check out the {product} on {platform}! This {feature} is a great addition. {cta_type}! {hashtag}"
        case "professional":
            return f"Introducing the {product} on {platform}. This {feature} {product} is designed for professionals. {cta_type} to learn more. {hashtag}"
        case _:
            return "Invalid tone selected"



from dotenv import load_dotenv
import os
from google import genai

os.environ["HTTP_PROXY"] = "http://192.168.49.1:8282"   
os.environ["HTTPS_PROXY"] = "http://192.168.49.1:8282"
def generate_ai_caption(product, platform, tone, feature, cta_type):
# Load environment variables from .env file
   load_dotenv()
   api_key = os.getenv("GEMINI_API_KEY")
   client = genai.Client(api_key=api_key)
   response =client.models.generate_content(
      
      model="gemini-3.6-flash",
      contents=f"Generate a caption for a {product} on {platform} with a {tone} tone, highlighting the {feature} feature, and including a {cta_type} call-to-action and generate relevant hashtags.",
    )

   return response.text

