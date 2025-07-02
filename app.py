from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

generation_config = genai.types.GenerationConfig(
    temperature=0.5, max_output_tokens=2048
)
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", generation_config=generation_config
)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    response_text = None
    if request.method == "POST":
        prompt = request.form["prompt"]

        try:
            response_object = model.generate_content(prompt)
            response_text = response_object.text
        except ValueError:
            response_text = "Long prompt detected. Please shorten your input."
            print("Response: ", response_object.prompt_feedback)
        except Exception as e:
            response_text = f"Ocorreu um erro inesperado: {e}"
            print(f"Erro: {e}")

    return render_template("index.html", response=response_text)


if __name__ == "__main__":
    app.run(debug=True)
