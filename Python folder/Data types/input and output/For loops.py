#1.print numbers from 1 to 5
#2.find the maximum value in a list using for loop
#3.count the number of vowels in a string using for loop
#4.Find and print the common elements between two lists using for loop
#5.print the reverse of a string using a for loop
#6.generate a list of sequence for numbers from 1 to 10 using for loop
#7.count the number of words in a sequence using for loop
#8.generate a list of prime numbers with a given range using a loop
#9.calculate the sum of the first n natural numbers using for loop
#10.calculate the factorial of a number using a for loop with specified steps

#1.
for i in range(1,6):
    print(i)

#2.
numbers = [10,25,7,40,15]

maximum = numbers[0]

for i in numbers:
    if i > maximum:
        maximum = i
print("Maximum value is:",maximum)

#3.
text = input("Enter a string: ")
count = 0
for i in text:
    if i in "aeiouAEIOU":
        count = count + 1

print("Number of vowels:",count)

#4.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

for i in list1:
    if i in list2:
        print(i)

#5.
text = input("Enter a string:")

reverse = ""

for i in text:
    reverse = i + reverse

print("Reverse:", reverse)

#6.
numbers = []
for i in range(1,11):
    numbers.append(i)
print(numbers)

#7.
text = input("Enter a sentence:")
words = text.split()
count = 0
for i in words:
    count = count  + 1
print("Number of words:",count)

#8.
start = 1
end = 20
for num in range(start, end + 1):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        print(num)

#9.
n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum:", sum)

#10.
n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print("Factorial:", factorial)


# WHILE LOOP

# 1. Basic counting: Write a while loop that counts from 1 to 10 and
#    prints each number.

# 2. Using a while loop to calculate the factorial of a given number.

# 3. Write a while loop program that prints all even numbers between 1 to 50.

# 4. Generate a multiplication table for a given number using while loop.

# 5. Write a program using a while loop to generate the first n terms of
#    the Fibonacci sequence.

# 6. Build a program that checks if a given number is prime using while loop.

# 7. Create a program that converts a given integer into words.
#    Example: 123 -> One hundred twenty three

# 8. Write a program to reverse a given string using a while loop.

# 9. Write a program that converts a binary number to its decimal
#    equivalent using while loop.

# 10. Create a program that calculates and prints the prime factorization
#     of a given number using a while loop.



#1.
i = 1

while i <= 10:
    print(i)
    i = i + 1

#2.
n = int(input("Enter a number: "))

factorial = 1
i = 1

while i <= n:
    factorial = factorial * i
    i = i + 1

print("Factorial:", factorial)

#3.
i = 2

while i <= 50:
    print(i)
    i = i + 2

#4.
n = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i = i + 1

#5.
n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a)
    
    c = a + b
    a = b
    b = c
    
    i = i + 1

#6.
n = int(input("Enter a number: "))

i = 2
count = 0

while i <= n:
    if n % i == 0:
        count = count + 1
    
    i = i + 1

if count == 1:
    print("Prime number")
else:
    print("Not a prime number")

#7.
n = int(input("Enter a number: "))

ones = ["", "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine"]

tens = ["", "", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"]

if n == 0:
    print("zero")

elif n < 10:
    print(ones[n])

elif n < 20:
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    print(teens[n - 10])

else:
    if n >= 100:
        print(ones[n // 100], "hundred", end=" ")
        n = n % 100

    if n >= 20:
        print(tens[n // 10], end=" ")
        n = n % 10

    if n > 0:
        print(ones[n])

#8.
text = input("Enter a string: ")

reverse = ""
i = len(text) - 1

while i >= 0:
    reverse = reverse + text[i]
    i = i - 1

print("Reverse:", reverse)

#9.
binary = int(input("Enter a binary number: "))

decimal = 0
base = 1

while binary > 0:
    digit = binary % 10
    decimal = decimal + digit * base
    
    binary = binary // 10
    base = base * 2

print("Decimal:", decimal)

#10.
n = int(input("Enter a number: "))

i = 2

while i <= n:
    while n % i == 0:
        print(i)
        n = n // i
    
    i = i + 1