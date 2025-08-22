from dotenv import load_dotenv
import os
from groq import Groq 

load_dotenv()  # This will load your .env file variables into os.environ
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# print("API Key:", os.environ.get("GROQ_API_KEY"))


from flask import Flask, request, render_template

app = Flask(__name__)

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
