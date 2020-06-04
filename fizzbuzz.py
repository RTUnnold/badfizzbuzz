# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".
# hint: lets try with no modulus operator

for n in range(1,101):
    fizz = (n - 3 * (n // 3))
    buzz = (n - 5 * (n // 5))
    
    if fizz == 0 and buzz == 0:
        print("FizzBuzz")
    elif fizz == 0:
        print("Fizz")
    elif buzz == 0:
        print("Buzz")

