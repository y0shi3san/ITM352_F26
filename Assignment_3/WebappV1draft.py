# Timer-Based Challenge Mode: give each question a countdown and end the quiz at zero.
# Progress Bar: show how many questions have been answered.
# Kaili Takara
# November 18, 2026


import os
import time
from math import ceil

from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
# Use an environment variable for the secret key outside local development.
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", "dev-only-change-this")

QUESTION_TIME_LIMIT = 15
CATEGORY_NAME = "General Knowledge"

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Madrid", "London", "Berlin", "Paris"],
    },
    {
        "question": "What planet is known as the Red Planet?",
        "options": ["Venus", "Saturn", "Jupiter", "Mars"],
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "Jane Austen", "Mark Twain", "William Shakespeare"],
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Pb", "Ag", "Fe", "Au"],
    },
]
max_questions = len(questions)


@app.route("/")
def index():
    # Show the category selector and explain the timer before the quiz starts.
    return render_template(
        "index.html",
        categories=[CATEGORY_NAME],
        question_count=max_questions,
        time_limit=QUESTION_TIME_LIMIT,
    )


@app.route("/start", methods=["POST"])
def start_quiz():
    # Start a fresh attempt after the player selects the available category.
    if request.form.get("category") != CATEGORY_NAME:
        flash("Choose a category to start the quiz.", "error")
        return redirect(url_for("index"))

    session.clear()
    session["category"] = CATEGORY_NAME
    session["score"] = 0
    session["question_number"] = 0
    session["timed_out"] = False
    return redirect(url_for("quiz"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    # A quiz must be started before a question can be displayed.
    if "question_number" not in session:
        return redirect(url_for("index"))

    question_number = session["question_number"]
    if question_number >= max_questions:
        return redirect(url_for("result"))

    if request.method == "POST":
        deadline = session.get("question_deadline")

        # Check the server deadline so late answers are not accepted.
        if (
            request.form.get("timed_out") == "1"
            or deadline is None
            or time.time() >= deadline
        ):
            session["timed_out"] = True
            return redirect(url_for("result"))

        # The original quiz uses the last option as the correct answer.
        correct_answer = questions[question_number]["options"][-1]
        if request.form.get("answer") == correct_answer:
            session["score"] += 1
            flash("Correct!", "success")
        else:
            flash(f"Incorrect. The correct answer is {correct_answer!r}.", "error")

        # Advance to the next question and start its timer when it is displayed.
        session["question_number"] += 1
        session.pop("question_deadline", None)
        if session["question_number"] >= max_questions:
            return redirect(url_for("result"))
        return redirect(url_for("quiz"))

    # Give each question a fresh deadline the first time it is displayed.
    deadline = session.get("question_deadline")
    if deadline is None:
        deadline = time.time() + QUESTION_TIME_LIMIT
        session["question_deadline"] = deadline

    time_left = ceil(deadline - time.time())
    if time_left <= 0:
        session["timed_out"] = True
        return redirect(url_for("result"))

    return render_template(
        "quiz.html",
        question=questions[question_number]["question"],
        options=questions[question_number]["options"],
        question_number=question_number + 1,
        completed_questions=question_number,
        total_questions=max_questions,
        time_left=time_left,
    )


@app.route("/result")
def result():
    # Show results only after all questions are answered or time runs out.
    if "question_number" not in session:
        return redirect(url_for("index"))
    if session["question_number"] < max_questions and not session["timed_out"]:
        return redirect(url_for("quiz"))

    return render_template(
        "result.html",
        score=session["score"],
        max_questions=max_questions,
        completed_questions=session["question_number"],
        timed_out=session["timed_out"],
        category=session["category"],
    )


if __name__ == "__main__":
    # Start Flask's local development server when this file runs directly.
    app.run(debug=True)
