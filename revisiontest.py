# yes, this is basically the sample question but i'm currently remodelling it.
# closing the tab of the code of which i was working on was not the best choice.

print("Title of program: MCQ revision program")
print("Instructions : Answer with either 'a','b','c' or 'd' depending on which option you think is the correct answer and comments will be given to your choice.")
print()

question = 0
totalQn = 4
score = 0



if question == 0:
  
  print("Question "+str(question+1)+") "+ "If the base and height of a triangle is 3 and 6 respectively, what is the area of the triangle?")
  print("   a) 6")
  print("   b) 18")
  print("   c) 9")
  print("   d) 8")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Try to recall the formula for the area of a triangle."
  elif answer == "b":
    output = "Wrong. Remember to multiply it by half."
  elif answer == "c":
    output = "Yes, that's right!"
    score +=1
  elif answer == "d":
    output = "Wrong. I don't even know how you got this answer."
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(score) + "/" + str(totalQn))
  print()
  print()
  


question += 1

if question == 1:
  
  print("Question "+str(question + 1)+") "+ "What does 'amiable' mean?")
  print("   a) friendly and pleasant")
  print("   b) shiningly brilliant and clever")
  print("   c) harmful and evil")
  print("   d) fear and anxiety")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    score +=1
  elif answer == "b":
    output = "Wrong. That is the definition for 'scintillating'."
  elif answer == "c":
    output = "Wrong. That is the definition for 'sinister'."
  elif answer == "d":
    output = "Wrong. That is the definition for 'trepidation'."
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(score) + "/" + str(totalQn))
  print()
  print()
  
question += 1

if question == 2:
  
  print("Question "+str(question + 1)+") "+ "21 + y = 26 What is y?")
  print("   a) 5")
  print("   b) 47")
  print("   c) -5")
  print("   d) 26/21")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Awesome!"
    score +=1
  elif answer == "b":
    output = "No, its not addition"
  elif answer == "c":
    output = "Don't know how you get that but you should move 21 over"
  elif answer == "d":
    output = "Good that 21 is on the other side but its not divide. "
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(score) + "/" + str(totalQn))
  print()
  print()
  
  
question += 1

if question == 3:
  
  print("Question "+str(question + 1)+") "+ "What is a cause of water shortage?")
  print("   a) Limited land supply")
  print("   b) Public education")
  print("   c) External pressure")
  print("   d) Affluence")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Limited land supply is a cause of housing shortage, not water shortage."
  elif answer == "b":
    output = "Wrong. Public education is a solution to water shortage, not a cause."
  elif answer == "c":
    output = "Wrong. External pressure is a problem that historians face (which will be tested in the next question)."
  elif answer == "d":
    output = "Yes, that's right!"
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output)
  print()
  print("Your current score: " + str(score) + "/" + str(totalQn))
  if score == 4:
    print("Congrats, you got full marks, way to go!")
  elif score >= 2:
    print("Congrats, you passed, keep up the good work!")
  else:
    print("Continue to improve, you can do it!")
  print()
  
print("End of quiz!")
