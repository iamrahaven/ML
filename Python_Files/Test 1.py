Score=int(input("Enter the score:"))
if(Score<35):
    print("Poor Student")
elif(Score>=35 and Score<=70):
    print("Avg Student")
elif(70<Score<=100):
    print("Good Student")
else:
    print("Invalid Score")
 
