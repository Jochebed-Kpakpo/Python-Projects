# for range of numbers from 1 to 1000
for x in range(1, 1001):
    if x % 3 == 0 and x % 5 == 0:
          print("Fizzbuzz")
    elif x % 3 == 0: 
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
