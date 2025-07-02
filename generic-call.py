from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

generation_config = genai.types.GenerationConfig(
    temperature=0.1,
    max_output_tokens=300 
)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

response = model.generate_content("Crie uma chamada de marketing de uma linha para um café espacial")
print(response.text)