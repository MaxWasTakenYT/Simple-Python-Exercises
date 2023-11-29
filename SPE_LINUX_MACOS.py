import os
import time

def clear_screen():
  os.system('clear')


def text_inverter_exercise():
  print("Text Inverter - Very Easy")
  time.sleep(0.5)
  print(
      "In this exercise, you are creating a simple program that inverts the text written in the terminal and displays it."
  )
  time.sleep(0.5)

  user_code = input("Write Python code to invert text: ")
  expected_output = input(
      "What should the inverted text be? (Expected Output): ")

  try:
    local_vars = {}
    try:
      exec(user_code, globals(), local_vars)
    except Exception as e:
      print("Error in your code:", e)
      print("Keep practicing! You can try again or choose another exercise.")
      return

    user_output = local_vars.get("result", None)

    if user_output == expected_output:
      print("Great job! Your code is correct.")
    else:
      print("Oops! Your code did not produce the expected output.")
    time.sleep(1)
  except Exception as e:
    print("Error in the exercise:", e)
    time.sleep(1)


def simple_calculator_exercise():
  print("Simple Calculator - Easy")
  time.sleep(0.5)
  print(
      "In this exercise, you are creating a simple calculator program that can perform basic operations."
  )
  time.sleep(0.5)

  user_code = input("Write Python code for a simple calculator: ")
  expected_output = input(
      "What should be the result of the calculation? (Expected Output): ")

  try:
    local_vars = {}
    try:
      exec(user_code, globals(), local_vars)
    except Exception as e:
      print("Error in your code:", e)
      print("Keep practicing! You can try again or choose another exercise.")
      return

    user_output = local_vars.get("result", None)

    if user_output == eval(expected_output):
      print("Great job! Your code is correct.")
    else:
      print("Oops! Your code did not produce the expected output.")
    time.sleep(1)
  except Exception as e:
    print("Error in the exercise:", e)
    time.sleep(1)


def password_generator_exercise():
  print("Password Generator - Medium")
  time.sleep(0.5)
  print(
      "In this exercise, you are creating a program that generates random passwords."
  )
  time.sleep(0.5)
  # Add exercise code here
  time.sleep(1)


def password_validator_exercise():
  print("Password Validator - Hard")
  time.sleep(0.5)
  print(
      "In this exercise, you are creating a program that checks the validity of passwords."
  )
  time.sleep(0.5)
  # Add exercise code here
  time.sleep(1)


def rock_paper_scissors_game():
  print("Rock, Paper, Scissors Game - Very Hard")
  time.sleep(0.5)
  print("In this exercise, you are creating a Rock, Paper, Scissors game.")
  time.sleep(0.5)
  # Add exercise code here
  time.sleep(1)


exercises = {
    "1": text_inverter_exercise,
    "2": simple_calculator_exercise,
    "3": password_generator_exercise,
    "4": password_validator_exercise,
    "5": rock_paper_scissors_game
}

current_exercise = None

while True:
  print("Welcome to Simple Python Exercises!")
  time.sleep(1.6)
  clear_screen()

  print("Remember to check the official GitHub repo for updates")
  time.sleep(1.3)
  clear_screen()

  print("Let's get started!")
  time.sleep(1)
  clear_screen()

  print("Here are the exercises:")
  time.sleep(0.3)

  for exercise_number, exercise_func in exercises.items():
    difficulty = {
        "1": "Very Easy",
        "2": "Easy",
        "3": "Medium",
        "4": "Hard",
        "5": "Very Hard"
    }[exercise_number]

    print(
        f"[{exercise_number}] {exercise_func.__name__.replace('_', ' ').title()} - {difficulty}"
    )

  print("[E] Reload Exercise List")
  print("[R] Retry Current Exercise"
        if current_exercise else "[R] Retry Current Exercise")
  print("[Q] Quit")

  choice = input("Choose the exercise by typing the number or a command: ")

  if choice in exercises:
    clear_screen()
    current_exercise = exercises[choice]
    current_exercise()
  elif choice == "E":
    clear_screen()
    continue
  elif choice == "R" and current_exercise:
    clear_screen()
    current_exercise()
  elif choice == "Q":
    break
  else:
    clear_screen()
    print("Invalid input. Please choose a valid exercise or command.")
