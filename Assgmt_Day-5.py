''' Day 5 Assignment -
WAP usins filter function to find the elements from list that are divisible by 3 & 5.'''

strt = int(input("Enter your starting range: "))
end = int(input("Enter your ending range: "))

lst = list(range(strt,end+1))  #adding 1 with end to include the last num
print(f'This is your new list --> {lst}')
result1 = list(filter(lambda x: (x % 3 == 0), lst)) 
result2 = list(filter(lambda x: (x % 5 == 0), lst)) 

print(f'{result1} >> These numbers can only divisible by 3 between {strt}-{end}') 
print(f'{result2} >> These numbers can only divisible by 5 between {strt}-{end}') 
