a=[] 
sum=0
avg=0
count=0
print("Enter Marks:")
for Loop in range(5): 
    Num=int(input("Enter Number:"+str(Loop+1))) 
    a.append(Num)
    sum=sum+Num 
    count=count+1 
    avg=sum/count 
print("Total:",sum)
print("Count:",count)
print("Average:",avg)