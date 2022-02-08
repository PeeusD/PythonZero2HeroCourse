''' Day 2 Assignment -
 Wap to detect Lottery Prize for any lucky user 
 Conditions--> to input specific letter and you have to give prize who selects any given letters ----
 'h' or 'e' or 'o' or 'c' or 'd'
 '''
print("-------Welcome to Loterry Prize------")
wrd = "hello coders"

st = input("Choose correct given--> 'h' or 'e' or 'o' or 'c' or 'd' < --- character to win the lottery ").lower()
for i in wrd:
    if st ==i and st == 'h' or 'e' or 'o' or 'c' or 'd':
        print("congratulation, you are a winner")
        
    else:
        print("Better luck next time")
        break


