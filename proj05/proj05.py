# Name:
# Date:

# proj05: functions and lists

# Part I
import random

def divisors(num):
    divisor = []
    for i in range(1, num+1):
        if num%i == 0:
            divisor.append(i)
    return divisor
print divisors(8)

def prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False

    return True

# Part II

def intersection():
    lst1 = random.sample(range(10), random.randint(1, 10))
    lst2 = random.sample(range(10), random.randint(1, 10))
    return list(set(lst1).intersection(lst2))
print intersection()

def find_ab(side1, side2, side3):
    ab = []
    if side1 > side2 and side1 > side3:
        ab.append(side2)
        ab.append(side3)
    elif side2 > side1 and side2>side3:
        ab.append(side1)
        ab.append(side3)
    else:
        ab.append(side2)
        ab.append(side1)
    return ab
print find_ab(3, 4, 5)
def find_c(side1, side2, side3):
    if side1 > side2 and side1>side3:
        return side1
    elif side2 > side1 and side2>side3:
        return side2
    else:
        return side3

def square(side):
    a = side**2
    return a

def pythagorean(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

def is_right(side1, side2, side3):
    ab_list = find_ab(side1, side2, side3)
    c = find_c(side1, side2, side3)
    if square(ab_list[0]) + square(ab_list[1]) == square(c):
        return True
    else:
        return False

# TESTS
# Feel free to add your own tests as needed!

print ("Divisors Tests")
# Test 1
if divisors(1) == [1]:
    print("Test 1: PASS")
else:
    print("Test 1: FAIL")

# Test 2
if divisors(8) == [1,2,4,8]:
    print("Test 2: PASS")
else:
    print("Test 2: FAIL")

# Test 3
if divisors(9) == [1,3,9]:
    print("Test 3: PASS\n")
else:
    print("Test 3: FAIL\n")

print("Prime Tests")
# Test 4
if prime(9):
    print("Test 4: FAIL")
else:
    print("Test 4: PASS")

# Test 5
if prime(7):
    print("Test 5: PASS\n")
else:
    print("Test 5: FAIL\n")

L1 = []
L2 = [3, 4]
L3 = [3, "a"]
L4 = [5, "b", 10, 7, "a"]
L5 = [5, 7, 11]

print("Intersection Tests")
# Test 6
if intersection(L1, L2) == []:
    print("Test 6: PASS")
else:
    print("Test 6: FAIL")

# Test 7
if intersection(L2, L3) == [3]:
    print("Test 7: PASS")
else:
    print("Test 7: FAIL")

# Test 8
if intersection(L2, L4) == []:
    print("Test 8: PASS")
else:
    print("Test 8: FAIL")

# Test 9
if intersection(L3, L4) == ["a"]:
    print("Test 9: PASS")
else:
    print("Test 9: FAIL")

# Test 10
if intersection(L4, L5) == [5, 7]:
    print("Test 10: PASS\n")
else:
    print("Test 10: FAIL\n")

print("Is_Right Tests")
# Test 11
if is_right(5, 3, 4):
    print("Test 11: PASS")
else:
    print("Test 11: FAIL")

# Test 12
if is_right(9, 3, 4):
    print("Test 12: FAIL")
else:
    print("Test 12: PASS")
print pythagorean(3, 4, 5)

