#test-score-eval.py

print("Enter 3 test scores")

scoreOne, scoreTwo, scoreThree = eval(input("Enter 3 scores seperated by commas: "))
totalScore = scoreOne + scoreTwo + scoreThree
averageScore = round(totalScore / 3, 2)

print("Total Score: ", totalScore, "\nAverage Score: ", averageScore)

