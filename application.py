import os

import openai
from flask import Flask, redirect, render_template, request, url_for


def create_app(**config_overrides):
    app = Flask(__name__)
    openai.api_key = os.getenv("OPENAI_API_KEY")

    @app.route("/", methods=("GET", "POST"))
    def index():
        if request.method == "POST":
            input_text = request.form["input_text"]
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=generate_prompt(input_text),
                temperature=0.6,
            )
            return redirect(url_for("index", result=response.choices[0].text))

        result = request.args.get("result")
        return render_template("index.html", result=result)

    return app


def generate_prompt(input_text):
    return f"Translate into natural Colombian Spanish: '{input_text}'"
