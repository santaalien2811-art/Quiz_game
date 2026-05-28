questions = ("How many elements in the periodic table?: ",
             "what is the hardest material according to the mohs scale?: ",
             "What is the hottest planet in the solar system?: ",
             "What is the fake version of gold?: ",
             "what part of planet earth has the highest mass?: ")

options = (("A. 118", "B. 120", "C. 115", "D. 110"),
           ("A. Quartz", "B. Granite", "C. Diamond", "D. Ruby"),
           ("A. Mercury", "B. Venus", "C. Jupiter", "D. Earth"),
           ("A. Iron", "B. Copper", "C. Silver", "D. Pyrite"),
           ("A. Mantle.", "B. Core", "C. Lithosphere", "D Crust"))

answers = ("A", "C", "B", "D", "A")
guesses = []
score = 0
question_num = 0
for question in questions:
 print("*********************************************")
 print(question)
 for option in options[question_num]:
  print(option)
 
 guess = input("Enter you answer (A, B, C ,D): ").upper()   
 guesses.append(guess)
 if guess == answers[question_num]:
  score += 1
  print("*********************************************")
  print("CORRECT!")
 else:
  print("*********************************************")
  print(f"INCORRECT The correct answer is {answers[question_num]} ")

 question_num += 1




print("------------------------------------------------")
print("                     RESULTS                    ")
print("------------------------------------------------")



score = int(score / len(questions) * 100 )

print(f"Your score is {score}%")