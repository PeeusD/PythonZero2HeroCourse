''' Day 4 Assignment -
 Wap to find factoirial of a number....'''


def find_fact():
    n = int(input("Enter a number to find factorial: "))
    f = 1
    while 1 < n:
        f = f * n
        n -= 1
    print("Factorial of inputed number :", f)
    
find_fact()
