# Assignment 3: Quiz Web App

A Flask web version of the quiz. It includes a 15-second timer for each question, answer feedback, and a progress bar.

## Requirements

- Python 3
- Flask

## Setup

Run these commands in PowerShell from the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install Flask
```

If the `.venv` environment already exists, you can skip the first command.

## Run the app

From the repository root, run:

```powershell
.\.venv\Scripts\python.exe .\Assignment_3\Webapp.py
```

Keep the terminal open while playing. When Flask reports that the server is running, open [http://127.0.0.1:5000](http://127.0.0.1:5000) in a browser. Press `Ctrl+C` in the terminal to stop the server.

## Play

1. Select **General Knowledge** and start the quiz.
2. Answer each question before its 15-second countdown reaches zero.
3. Read the correct/incorrect feedback and watch the progress bar update.
4. The quiz ends when all questions are answered or a timer runs out.

## Project files

- `Webapp.py` contains the Flask routes, questions, scoring, and server-side timer checks.
- `templates/index.html` contains the start page.
- `templates/quiz.html` displays questions, the countdown, and progress bar.
- `templates/result.html` displays the final score and quiz status.

This uses Flask's development server and is intended for local coursework use.
