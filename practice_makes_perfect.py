"""
These are exercises from 'Learn Python' on Codecademy, from
the lesson 'Practice Makes Perfect'. 
"""
# Main function 


def main():


    print "Hello World"

    user_choice = raw_input("Choose a function to run: ")

    options = {
            1 : is_even,
            2 : is_int,
            3 : digit_sum, 
            4 : factorial, 
            5 : is_prime, 
            6 : reverse, 
            7 : anti_vowel, 
            8 : scrabble_score, 
            9 : censor, 
            10 : count,
            11 : purify, 
            12 : product, 
            13 : remove_duplicates,
            14 : median
            }

    if user_choice == 1:
        i = raw_input("Enter an integer to check if it's even: ")
        options[1](i)
    else:
        print "Not possible"



if __name__=="__main__":
    main()

"""====================Content======================"""
## 1. is_even(x) -> int
## 2. is_int(x) -> int or float
## 3. digit_sum(n) -> large int
#     digit_sum2(n)
## 4. factorial(x) -> int
#     factorial2(x)
## 5. is_prime(x) -> positive int
## 6. reverse(text) -> String
#     reverse2(text)
## 7. anti_vowel(text) -> String
## 8. scrabble_score(word) -> String
## 9. censor(text,word) -> String, Substring
## 10. count(sequence, item) -> int[],int
## 11. purify(lst) -> int[]
## 12. product(lst) -> int[]
## 13. remove_duplicates(lst) -> int[]
## 14. median(lst) -> int[]
"""================================================="""

## 1. Determines whether input x is an even number
def is_even(x):
    if x%2==0:
        return True
    return False

## 2. Determines whether input x is an Integer
""" We'll say that a number with a decimal part that is all 
0s is also an integer, such as 7.0. 
This means that, for this lesson, you can't just test the 
input to see its of type int. """
def is_int(x):
    absolute = abs(x)
    rounded = round(absolute)
    return absolute - rounded == 0

## 3. Takes a positive number n as input and returns the sum 
#    of all that number's digits. 
"""For example, digit_sum(1234) should return 1+2+3+4.
Below, digit_sum(n) achieves that by manipulating the modulo 
and floor division of given input n. """
def digit_sum(n):
    sum = 0
    while n > 10:
        sum += n%10
        n = n//10
    return sum
"""The following function achieves that by casting input n 
from an integer to string for iteration, and then each item
in the iteration casted back to int() for summation"""
def digit_sum2(n):
    sum = 0
    for item in str(n):
        sum += int(item)
    return sum
    
## 4. Calculate the factorial of a non-negative integer x
"""The following function calculates factorial using recursion"""
def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)
"""The following function calculates factorial using a while-
loop"""
def factorial2(x):
    fact = 1
    while x > 0:
        fact *= x
        x -= 1
    return fact

## 5. Determine whether a number is a prime numer
"""A prime number is a positive integer greater than 1 that has 
no positive divisors other than 1 and itself"""
def is_prime(x):
    if x < 2:
        return False
    for n in range(2,x):
        if x%n == 0:
            return False
    return True

## 6. Reverse a String 
"""By "pre"pending in a new String in iteration loop"""
def reverse(text):
    str = ""
    for i in text:
        str = i + str
    return str
"""By recursion"""
def reverse2(text):
    if len(text) == 0:
        return ""
    return reverse2(text[1:]) + text[0]
## 7. Return the text with all of the vowels removed
"""Uses boolean 'x in "aieouAEIOU"'  """
def anti_vowel(text):
    str = ""
    for x in text:
        if (not x in "aeiouAEIOU"):
            str += x
    return str

## 8. Return the equivalent scrabble score for input word
def scrabble_score(word):
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
    total = 0
    for x in word.lower():
        total += score[x]
    return total

## 9. Return 'text' with the 'word' replaced with asterisks
"""for example ("this hack is wack hack", "hack") returns 
"this **** is wack ****"   """
def censor(text, word):
    split = text.split()
    result= []
    if text_word != word:
        result.append(text_word)
    else:
        result.append("*"*len(word))
    return " ".join(result)


## 10. Return the number of times the item occurs in the list
"""count([1,2,1,1],1) should return 3"""
def count(sequence, item):
    count = 0
    for i in sequence:
        if (it == item):
            count += 1
    return count


## 11. Return the list with all the odd numbers removed
def purify(lst):
    res = []
    for ele in lst:
        if ele % 2 == 0:
            res.append(ele)
    return res

## 12. Returns the product of all the elements in the list
""" Uses recursion """
def product(lst):
    if len(lst) == 1:
        return lst[0]
    return product(lst[1:])*lst[0]

## 13. Removes duplicate elements of the integer list
"""([1,1,2,2]) should return [1,2] """
def remove_duplicates(lst):
    dup = []
    for n in lst:
        if not n in dup:
            dup.append(n)
    return dup

## 14. find the median in integer array
""" It is important to divide by 2.0 since that yields float"""
def median(lst):
    size = len(lst)
    lst = sorted(lst)
    if (len(lst)%2 == 0):
        return (lst[size/2-1]+lst[size/2])/2.0
    else:
        return lst[(size-1)/2]

