# FizzBuzz – Print numbers from 1 to 50. 
# For multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz". 
# For numbers which are multiples of both 3 and 5, print "FizzBuzz".

results = range(1, 51)
for value in results:
    if value % 3 == 0 and value % 5 == 0: 
        print("FizzBuzz")
    elif value % 3 == 0:
        print("Fizz")
    elif value % 5 == 0 :
        print("Buzz")
    else:
        print(value)