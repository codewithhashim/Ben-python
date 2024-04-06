questions = [
  {
    "question": "What is 2 + 2?",
    "options": ["3", "4", "5"],
    "answer": "4"
  },
  {
    "question": "Which is a JavaScript data type?",
    "options": ["String", "Blueprint", "Speaker"],
    "answer": "String"
  },
  {
    "question": "Which method can add an element to the end of an array in JavaScript?",
    "options": ["shift()", "unshift()", "push()"],
    "answer": "push()"
  }
]

def start_quiz():
  score = 0
  
  for i in range(len(questions)):
    user_answer = input(
      questions[i]["question"] + "\n" +
      "Options:\n" +
      "\n".join(questions[i]["options"]) +
      "\n\nEnter the correct answer:"
    )
    if user_answer.upper() == questions[i]["answer"].upper():
      print("Correct!")
      score += 1
    else:
      print(f"Wrong! The correct answer is {questions[i]['answer']}.")
  
  print(f"Quiz completed! Your score is {score}/{len(questions)}.")

start_quiz()
