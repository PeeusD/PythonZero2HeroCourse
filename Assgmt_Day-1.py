# WAP to  Take multiple number as input and print sum. of the numbers
rep = int(input("How many multiple numbers u wanna input: "))
lst=[]
for i in range(rep):
    
    num=int(input("Enter your number: "))
    lst.append(num)


print(sum(lst))
