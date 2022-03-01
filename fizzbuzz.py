# FizzBuzz
# Ask the user for a number
# Print a list of all numbers from 1 to that number:
#   If the number is divisible by 2, print Fizz
#   If the number is divisible by 3, print Buzz
#   If the number is divisible by both, print FizzBuzz
#   If the number is divisible by neither, print the number

n = 1 
userinput = int(input('Please enter a number: '))
while n <= userinput:
    if n % 2 == 0 and n % 3 == 0:
        print('FizzBuzz')
    elif n % 2 == 0:
        print('Fizz')
    elif n % 3 == 0:
        print('Buzz')
    else:
        print(n)
    n += 1