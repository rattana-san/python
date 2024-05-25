#printing fizz when the number's a multiple of 3
#print 'buzz' when it's a multiple of 5
#from 1-100

a = 3
b = 5

for i in range(101):
    if i % a == 0:
      print("Fizz")
    elif i % b == 0:
       print("Buzz")
    else:
       print(i)
