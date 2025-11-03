# Summation of all even number from 1 to 100
# total summation of even numbers are 2550
# total summation of odd numbers are 2500

def sum_even(n):
    sum = 0
    i = 0
    while i <= n:
        if i % 2 == 0:
            sum+=i
        i+=1; 
    return sum

def sum_odd(n):
    sum = 0
    i = 0
    while i <= n:
        if not i % 2 == 0:
            sum+=i
        i+=1; 
    return sum


print(sum_even(100))
print(sum_odd(100))