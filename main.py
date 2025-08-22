from flask import Flask, request, render_template
import os
from dotenv import load_dotenv
from groq import Groq  # Replace with your actual import

load_dotenv()
app = Flask(__name__)

client = Groq(api_key=os.environ.get("GROK_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    user_question = ""
    if request.method == "POST":
        user_question = request.form.get("question")
        if user_question:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": user_question}],
                model="llama-3.3-70b-versatile",
            )
            response_text = chat_completion.choices[0].message.content

    return render_template("index.html", question=user_question, response=response_text)


if __name__ == "__main__":
    app.run(debug=True)
