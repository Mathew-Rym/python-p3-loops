#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    for num in range(10,0,-1):
        print(num)
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    square_integers=[num*num for num in int_list]
    return square_integers

def fizzbuzz():
    # code goes here!
    for num in range(1,101):
        if num%3==0 and num%5==0:
            print("FizzBuzz")
        elif num%3==0 :
            print("Fizz")
        elif num%5==0:
            print("Buzz")
        else:
            print(num)
            

happy_new_year()
print(square_integers([2,3,4,5]))
fizzbuzz()