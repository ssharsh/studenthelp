from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key here (you can load from .env)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    tool = request.form["tool"]
    user_input = request.form["user_input"]

    if tool == "resume":
        prompt = f"Improve this resume for a professional job: {user_input}"
    elif tool == "email":
        prompt = f"Rewrite this email with a professional and friendly tone: {user_input}"
    elif tool == "contract":
        prompt = f"Summarize and clarify this contract: {user_input}"
    else:
        prompt = f"Enhance this text: {user_input}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        output = response.choices[0].message.content.strip()
    except Exception as e:
        output = f"Error: {str(e)}"

    return render_template("result.html", result=output)

if __name__ == "__main__":
    app.run(debug=True)
