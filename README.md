# TASK-24-QUIZ-APP# CLI Quiz Application

A command-line quiz application built in Python. It loads questions from a JSON file, accepts answers from the user, calculates the score, and displays a detailed final result.

Built as part of the **Python Programming Track** internship assignment.

---

## Features

- Loads questions from an external `questions.json` file (questions are kept separate from program logic)
- 12 Python-related multiple-choice questions
- Question order is randomized on every run
- Input validation: handles non-numeric and out-of-range answers
- Instant feedback after every answer (shows the correct answer when wrong)
- Final result summary with total, correct, wrong, percentage and grade
- Review list of the questions you got wrong
- "Play again" option without restarting the program
- Graceful error handling for a missing or invalid JSON file

---

## Project Structure

```
quiz_app/
├── quiz.py          # Application logic
├── questions.json   # Question bank
└── README.md        # Project documentation
```

---

## Requirements

- Python 3.6 or higher
- No external libraries needed (uses only `json`, `random` and `os` from the standard library)

---

## How to Run

1. Download or clone the project and keep all files in the same folder.
2. Open a terminal in that folder.
3. Run:

```bash
python quiz.py
```

On some systems you may need to use `python3 quiz.py`.

---

## How It Works

1. The program loads all questions from `questions.json`.
2. Questions are shuffled into a random order.
3. Each question is displayed with numbered options.
4. The user enters the option number as their answer.
5. Invalid input is rejected and the user is asked again.
6. After the last question, the final result summary is displayed.

### Grading Scale

| Score        | Grade             |
|--------------|-------------------|
| 90% and above | Excellent        |
| 70% - 89%     | Good             |
| 50% - 69%     | Average          |
| Below 50%     | Needs Improvement |

---

## Sample Output

```
========================================
  WELCOME TO THE PYTHON CLI QUIZ
========================================

Press Enter to start the quiz...

Question 1/12
Which keyword is used to exit a loop immediately?
  1. stop
  2. exit
  3. break
  4. return
Your answer (1-4): 3
Correct!

...

========================================
FINAL RESULT
========================================
Total Questions : 12
Correct Answers : 9
Wrong Answers   : 3
Score           : 75.0%
Grade           : Good

Questions you got wrong:
  - Which symbol is used to start a comment in Python?
    Correct answer: #
========================================

Play again? (y/n):
```

---

## Adding Your Own Questions

Open `questions.json` and add a new entry using this format:

```json
{
    "question": "Your question here?",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "answer": 2
}
```

- `options` is a list of choices (any number of options works).
- `answer` is the **position** of the correct option, starting from **1**. In the example above, `2` means "Option 2" is correct.
- Separate entries with commas and keep the whole file wrapped in `[ ]`.

---

## Concepts Practiced

- **Dictionaries**: each question is stored as a dictionary
- **Lists**: the question bank and answer options
- **Loops**: quiz flow, input validation and replay
- **Functions**: the code is split into small, reusable functions
- **JSON**: reading data from a file with `json.load()`
- **Application flow**: start screen, quiz, result summary, replay

---

## Code Overview

| Function           | Purpose                                              |
|--------------------|------------------------------------------------------|
| `load_questions`   | Reads and returns questions from the JSON file       |
| `display_question` | Prints a question with its numbered options          |
| `get_user_answer`  | Reads and validates the user's input                 |
| `check_answer`     | Compares the answer and gives feedback               |
| `get_grade`        | Converts a percentage into a grade                   |
| `show_summary`     | Prints the final result and the wrong answers        |
| `run_quiz`         | Runs one complete round of the quiz                  |
| `ask_play_again`   | Asks whether the user wants another round            |
| `main`             | Entry point of the application                       |

---

## Possible Improvements

- Add quiz categories and difficulty levels
- Add a timer for each question
- Save high scores to a JSON file
- Let the user choose how many questions to attempt

---

## Author

**Zaid**
Python Programming Track Intern
