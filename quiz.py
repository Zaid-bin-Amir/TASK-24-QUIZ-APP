import json
import random
import os

QUESTIONS_FILE = "questions.json"


def load_questions(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, filename)
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except json.JSONDecodeError:
        print(f"Error: {filename} contains invalid JSON.")
    return []


def display_question(number, total, item):
    print(f"\nQuestion {number}/{total}")
    print(item["question"])
    for index, option in enumerate(item["options"], start=1):
        print(f"  {index}. {option}")


def get_user_answer(option_count):
    while True:
        raw = input(f"Your answer (1-{option_count}): ").strip()
        if not raw.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        choice = int(raw)
        if 1 <= choice <= option_count:
            return choice
        print(f"Please choose a number between 1 and {option_count}.")


def check_answer(item, choice):
    correct = item["answer"]
    if choice == correct:
        print("Correct!")
        return True
    print(f"Wrong! The correct answer was {correct}. {item['options'][correct - 1]}")
    return False


def get_grade(percentage):
    if percentage >= 90:
        return "Excellent"
    if percentage >= 70:
        return "Good"
    if percentage >= 50:
        return "Average"
    return "Needs Improvement"


def show_summary(score, total, wrong_questions):
    percentage = (score / total) * 100
    print("\n" + "=" * 40)
    print("FINAL RESULT")
    print("=" * 40)
    print(f"Total Questions : {total}")
    print(f"Correct Answers : {score}")
    print(f"Wrong Answers   : {total - score}")
    print(f"Score           : {percentage:.1f}%")
    print(f"Grade           : {get_grade(percentage)}")

    if wrong_questions:
        print("\nQuestions you got wrong:")
        for item in wrong_questions:
            correct = item["answer"]
            print(f"  - {item['question']}")
            print(f"    Correct answer: {item['options'][correct - 1]}")
    print("=" * 40)


def run_quiz(questions):
    random.shuffle(questions)
    score = 0
    wrong_questions = []
    total = len(questions)

    for number, item in enumerate(questions, start=1):
        display_question(number, total, item)
        choice = get_user_answer(len(item["options"]))
        if check_answer(item, choice):
            score += 1
        else:
            wrong_questions.append(item)

    show_summary(score, total, wrong_questions)


def ask_play_again():
    while True:
        reply = input("\nPlay again? (y/n): ").strip().lower()
        if reply in ("y", "yes"):
            return True
        if reply in ("n", "no"):
            return False
        print("Please enter y or n.")


def main():
    print("=" * 40)
    print("  WELCOME TO THE PYTHON CLI QUIZ")
    print("=" * 40)

    questions = load_questions(QUESTIONS_FILE)
    if not questions:
        return

    input("\nPress Enter to start the quiz...")

    while True:
        run_quiz(list(questions))
        if not ask_play_again():
            break

    print("\nThanks for playing. Goodbye!")


if __name__ == "__main__":
    main()
