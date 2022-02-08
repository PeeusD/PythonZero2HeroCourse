''' Day 3 Assignment -
WAP to find from a dictionary how to print the key whose value is maximum '''

wrd = input("Enter any Word: ")
#replacing spaces with nothing
wrd = wrd.replace(" ", "")
emp_dic = {}  # declaring empty dict

for i in wrd:
  emp_dic[i] = emp_dic.get(i, 0) + 1
 
print(emp_dic)
max_key = max(emp_dic, key = emp_dic.get)
print(max_key)
