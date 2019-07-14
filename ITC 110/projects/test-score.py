#test-score-eval.py

print("Enter 3 test scores")

scoreOne = float(input("Enter score 1: "))
scoreTwo = float(input("Enter score 2: "))
scoreThree = float(input("Enter score 3: "))
totalScore = scoreOne + scoreTwo + scoreThree
averageScore = round(totalScore / 3, 2)

print("Total Score: ", totalScore, "\nAverage Score: ", averageScore)

