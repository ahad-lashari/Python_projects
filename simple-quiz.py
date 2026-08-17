# Function to run the quiz
def run_quiz():
    quiz_data = [
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["A) .pt", "B) .pyt", "C) .py", "D) .python"],
            "answer": "C",
        },
        {
            "question": "Which keyword is used to create a function in Python?",
            "options": ["A) func", "B) def", "C) function", "D) create"],
            "answer": "B",
        },
        {
            "question": "Which data structure stores items in a key-value format?",
            "options": ["A) List", "B) Tuple", "C) Dictionary", "D) Set"],
            "answer": "C",
        },
        {
            "question": "Which built-in function is used to get user input?",
            "options": ["A) get()", "B) read()", "C) scanf()", "D) input()"],
            "answer": "D",
        },
        {
            "question": "How do you insert comments in Python code?",
            "options": ["A) //", "B) #", "C) /* */", "D) <!-- -->"],
            "answer": "B",
        },
    ]
    score = 0
    total_questions = len(quiz_data)
    print("==========================================")
    print("       WELCOME TO THE PYTHON QUIZ        ")
    print("==========================================\n")
    for index, q in enumerate(quiz_data, start=1):
        print(f"Question {index}: {q['question']}")
        for option in q["options"]:
            print(f"   {option}")
        user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()
        if user_answer == q["answer"]:
            print("✓ Correct!\n")
            score += 1
        else:
            print(f"✗ Wrong! The correct answer was {q['answer']}.\n")

        print("-" * 40)
    print("\n==========================================")
    print(f"QUIZ FINISHED! Your Score: {score} / {total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    if percentage >= 80:
        print("Performance: Excellent!")
    elif percentage >= 50:
        print("Performance: Good job!")
    else:
        print("Performance: Needs Improvement. Keep practicing!")
    print("==========================================")
if __name__ == "__main__":
    run_quiz() 