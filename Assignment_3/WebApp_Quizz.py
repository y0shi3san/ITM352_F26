# Timer-Based Challenge Mode: give each question a countdown and end the quiz at zero.
# Progress Bar: show how many questions have been answered.
# November 18, 2026

import json
import os
import random
import time
from math import ceil
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
# Set FLASK_SECRET_KEY in the environment when running outside local development.
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", "dev-only-change-this")

QUESTION_TIME_LIMIT = 30
NUM_QUESTIONS_PER_QUIZ = 5

# Reuse the question categories and answers from Assignment 1.
question_file = Path(__file__).resolve().parents[1] / "Assignment_1" / "Questions.json"
with question_file.open(encoding="utf-8") as file:
    categories = json.load(file)["categories"]


@app.route("/")
def index():
    # Let players select one of the same categories used by the console quiz.
    return render_template(
        "index.html",
        categories=categories,
        time_limit=QUESTION_TIME_LIMIT,
        question_count=NUM_QUESTIONS_PER_QUIZ,
    )


@app.route("/start", methods=["POST"])
def start_quiz():
    # Reject categories that were not supplied by the page.
    category_name = request.form.get("category")
    if category_name not in categories:
        flash("Choose a category to start the quiz.", "error")
        return redirect(url_for("index"))

    category_questions = categories[category_name]
    if len(category_questions) < NUM_QUESTIONS_PER_QUIZ:
        raise ValueError(
            f"Category {category_name!r} has fewer than "
            f"{NUM_QUESTIONS_PER_QUIZ} questions."
        )

    # Pick a random set of questions and randomize each question's choices.
    selected_question_numbers = random.sample(
        range(len(category_questions)), k=NUM_QUESTIONS_PER_QUIZ
    )
    option_orders = [
        random.sample(range(len(category_questions[number]["options"])),
                      k=len(category_questions[number]["options"]))
        for number in selected_question_numbers
    ]

    # Store only question and option indexes so the quiz order stays fixed.
    session.clear()
    session["category"] = category_name
    session["question_order"] = selected_question_numbers
    session["option_orders"] = option_orders
    session["question_index"] = 0
    session["score"] = 0
    session["timed_out"] = False
    return redirect(url_for("quiz"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    # A quiz must be started from the home page to create its session state.
    if "question_order" not in session:
        return redirect(url_for("index"))

    question_index = session["question_index"]
    question_order = session["question_order"]
    total_questions = len(question_order)
    if question_index >= total_questions:
        return redirect(url_for("result"))

    if request.method == "POST":
        deadline = session.get("question_deadline")

        # Check the server-side deadline so a late answer cannot be accepted.
        if (
            request.form.get("timed_out") == "1"
            or deadline is None
            or time.time() >= deadline
        ):
            session["timed_out"] = True
            return redirect(url_for("result"))

        # Find this randomized question and compare the submitted choice.
        current_question = categories[session["category"]][
            question_order[question_index]
        ]
        answer = request.form.get("answer")
        correct_answer = current_question["answer"]
        if answer == correct_answer:
            session["score"] += 1
            flash("Correct!", "success")
        else:
            flash(f"Incorrect. The correct answer is {correct_answer!r}.", "error")

        # Advance to the next question and start its timer on the next page load.
        session["question_index"] += 1
        session.pop("question_deadline", None)
        if session["question_index"] >= total_questions:
            return redirect(url_for("result"))
        return redirect(url_for("quiz"))

    # Start a fresh timer the first time this question is displayed.
    deadline = session.get("question_deadline")
    if deadline is None:
        deadline = time.time() + QUESTION_TIME_LIMIT
        session["question_deadline"] = deadline

    # End the quiz if the question is revisited after its deadline.
    time_left = ceil(deadline - time.time())
    if time_left <= 0:
        session["timed_out"] = True
        return redirect(url_for("result"))

    # Use the saved indexes to keep the random order stable on refresh.
    current_question = categories[session["category"]][
        question_order[question_index]
    ]
    options = [
        current_question["options"][option_number]
        for option_number in session["option_orders"][question_index]
    ]
    return render_template(
        "quiz.html",
        question=current_question["question"],
        options=options,
        question_number=question_index + 1,
        completed_questions=question_index,
        total_questions=total_questions,
        time_left=time_left,
    )


@app.route("/result")
def result():
    # Show results only after the quiz is completed or the timer expires.
    if "question_order" not in session:
        return redirect(url_for("index"))
    total_questions = len(session["question_order"])
    if session["question_index"] < total_questions and not session["timed_out"]:
        return redirect(url_for("quiz"))

    return render_template(
        "result.html",
        score=session["score"],
        max_questions=total_questions,
        completed_questions=session["question_index"],
        timed_out=session["timed_out"],
        category=session["category"],
    )


if __name__ == "__main__":
    # Start the local Flask server when this file is run directly.
    app.run(debug=True)

