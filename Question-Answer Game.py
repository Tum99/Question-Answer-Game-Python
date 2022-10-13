print("Welcome to my quizz game. Let's see how well you know me")

playing = input("Are you ready for the game? ")
if playing.lower() != "yes":
    quit()
score = 0

question = input("What is my middle name? ")
if question.lower() == "cheptoo":
    print("Correct!")
    score += 1
else:
    print("Oops! You're wrong")

question = input("How old am I? ")
if question.lower() == str(23):
    print("Right!")
    score += 1
else:
    print("Oops! Not true.")

question = input("What's my favourite color? ")
if question.lower() == "black":
    print("Nailed it!")
    score += 1
else:
    print("Sorry! you're so wrong")

question = input("What is my favourite music band? ")
if question.lower() == "breaking benjamin":
    print("Heck yeah!!")
    score += 1
else:
    print("Nope")

question = input("Where is my hometown? ")
if question.lower() == "eldoret":
    print("You got it!")
    score += 1
else:
    print("Incorrect!")

print("You have answered "+ str(score)+ " questions right. Great job!")