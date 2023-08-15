def Calculator():
    counter=0
    while counter<2:
        counter +=1
        try:
            a=int(input("A:"))
            b=int(input("B:"))
            c=input("Add/Sub/Multi/Div:") 
            if(c=="Add" or c=="add"):
                print(a+b)
            elif(c=="Sub" or c=="sub"):
                print(a-b)
            elif(c=="Multi" or c=="multi"):
                print(a*b)
            elif(c=="Div" or c=="div"):
                if (b==0):
                    print("Division by zero is not allowed!")
                else:
                    print(a//b)
            else:
                print("Invalid Opreater:")
        except ValueError:
            print("Enter the Valid Value")
        except KeyboardInterrupt:
            print("Calculator terminated.")
            break
    
Calculator()