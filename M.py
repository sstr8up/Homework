# sample_dict = {"name": "Kelly",
#                   "age": 25,
#                   "salary": 8000,
#                   "city": "New york"}
#
# keys = ["name", "salary", 'hair_color']
#
# nd = {key: sample_dict.get(key) for key in keys}
# print(nd)



# SampleDict = {"class A": {"student_1": {"name": "Mike",
#                                            "marks": {"physics": 70,
#                                                      "history": 80}},
#                              "student_2": {"name": "Jack",
#                                            "marks": {"physics": 80,
#                                                      "history": 75}}}}
#
# print(SampleDict["class A"]["student_1"]["marks"]["history"])



# n = int(input("n = "))
# m = int(input("m = "))
# d = min(n, m)
# while n % d != 0 or m % d != 0:
#     d -= 1
# print(d)




# fruits = [{'fruit': 'orange', 'price': 150}, {'fruit': 'apple', 'price': 100},  {'fruit': 'banana'}]
# t = sum(fruit.get('price', 0) for fruit in fruits)
# print(t)



# total = 0
# while True:
#     age1 = (input("age = "))
#     if age1 == "":
#         break
#     age = int(age1)
#     if 3 < age <= 12:
#         price = 14
#     elif 12 < age <= 65:
#         price = 23
#     elif 65 < age <= 110:
#         price = 18
#     else:
#         print("invalid age")
#
#     total += price
#
# print(total)


# word = input("word = ")
# text = ("")
# for i in word:
#     if i.isalpha():
#         text += i.lower()
# if text[::-1] == text:
#         print("yes")
# else:
#     print("no")


# m = int(input("m = "))
# n = int(input("n = "))
# d = min(m, n)
# while d % n == 0 or d % m == 0:
#     d -= 1
#     print(d)



# f = 2
# n = int(input("n = "))
# while f <= n:
#     if n % f == 0:
#         print(f)
#         n //= f
#     else:
#         f += 1


# n = (input("n = "))
# total = 0
# for i in n:
#     total += int(i)
# print(total)




# import math
# d = float(input("degree = "))
# radian = math.radians(d)
# print(math.sin(radian))
# print(math.cos(radian))



# import random
#
# user_score = 0
# computer_score = 0
# options = ("rock", "paper" , "scissors")
# while user_score < 5 and computer_score < 5:
#     user = input("choose = ")
#     if user not in options:
#         print("not a valid choice")
#         continue
#     computer = random.choice(options)
#     print(computer)
#
#     if user == computer:
#         print("its a tie")
#     elif (user == "rock" and computer == "scissors") or \
#          (user == "paper" and computer == "rock") or \
#          (user == "scissors" and computer == "rock"):
#         print("you win")
#         user_score += 1
#     else:
#         print("computer wins")
#         computer_score += 1
#
# if user_score == 5:
#     print("you won the game")
# else:
#     print("you lost the game")






# def math(a, b):
#     return list((a + b, a - b, a  * b, a / b))
# print(math(4, 2))



# def math(*args):
#     a = sum(args)
#     result = 1
#     for n in args:
#         result *= n
#     b = sorted(args)
#     if len(b) % 2 == 0:
#         return (b[len(b) // 2] + b[len(b) // 2 - 1]) / 2, a, result, a/2
#     else:
#         return b[len(b) // 2], a, result, a/2

# print(math(1, 2, 3, 4, 5))



# def power(x, y=2):
#     return x**y
#
# print(power(2, 3))




# import math
#
# def sq(s):
#     return s ** 2
#
# def rec(r, c):
#     return r * c
#
# def circ(i):
#     return math.pi * i ** 2
#
# def tri(t, m):
#     return t * m / 2
#
#
# b = ("square", "rectangle", "circle", "triangle")


# try:
#     n = input("type = ")
#     if n not in b:
#         raise ValueError("incorrect input")
#
#     if n == "square":
#         s = int(input("s = "))
#         print(sq(s))
#     elif n == "rectangle":
#         r = int(input("r = "))
#         c = int(input("c = "))
#         print(rec(r, c))
#     elif n == "circle":
#         i = int(input("i = "))
#         print(circ(i))
#     elif n == "triangle":
#         t = int(input("t = "))
#         m = int(input("m = "))
#         print(tri(t, m))
# finally:
#     print("program finished")



# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range (2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# a = range(2, 1000)
# print(list(filter(is_prime, a)))


# nums_1 = [1, 2, 3, 5, 7, 8, 9, 10]
# nums_2 = [1, 2, 4, 8, 9]

# print(list(filter(lambda x: x in nums_1, nums_2)))


# lst = [{'name': 'Arman', 'age': 23}, {'name': 'Bob', 'age': 19}, {'name': 'Anna'}]
# lst.sort(key = lambda x: x.get("age", 0))
# print(lst)




# def summ(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + summ(n // 10)
#
#
# print(summ(285))



# def count(n):
#     steps = 0
#     for i in range(1, len(n)):
#         while n[i] <= n[i - 1]:
#             n[i] += 1
#             steps += 1
#     return steps
#
#
# print(count([-10, 0, -2, 0]))


# def color_print(color = "white", ):
#     d = {"white": "97", "green": "92", "red": "91", "blue": "94", "black": "90"}
#     def dec(func):
#         def inner(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return f"\033[{d.get(color, "97")}m" + str(result) + "\033[0m"
#         return inner
#     return dec
#
#
# @color_print(color = "")
# def pow(a, b):
#     return a ** b, ("string colour")
#
# print(pow(3, 4))


# import math
#
# def dec(func):
#     def inner(a, b):
#         a_log = math.log2(a)
#         b_log = math.log2(b)
#         result = func(a_log, b_log)
#         return math.log2(result)
#     return inner


# @dec
# def f(a, b):
#     return a - b
#
#
# print(f(1024, 64))



# def cache(func):
#     d = {}
#
#     def inner(*args, **kwargs):
#         n = (args, tuple(kwargs.items()))
#         if n not in d:
#             d[n] = func(*args, **kwargs)
#         return d[n]
#
#     return inner


# @cache
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)
#
# print(fib(100))



# import my_pack
# print(my_pack.file_1.summa(4, 5))


# from tqdm import tqdm
#
# s = 0
# for i in tqdm(range(1, 100_000_001)):
#     s += i
# print(s)


# from faker import Faker
#
# f = Faker(locale = "hy_am")
# for i in range(1, 11):
#     print(i, f.name(), f.address())



# from faker import Faker
#
# f = Faker(locale = "hy_am")
# for i in range(1, 11):
#     print(i, f.name(), f.last_name(), f.date_of_birth(), f.country(), f.city(), f.color(), f.job())

# from datetime import datetime
#
# def time(f):
#     def inner(*args, **kwargs):
#         h = datetime.now().hour
#         if 10 <= h < 19:
#             return f(*args, **kwargs)
#         else:
#             print("sorry its too late")
#     return inner
#
# @time
# def f(a):
#     print(f'Welcome {a}!')
#
# f("Davo")



# import pickle
#
# with open('data.pkl', 'rb') as f:
#     odd_numbers = pickle.load(f)
#
# div = [num for num in odd_numbers if num % 3 == 0]
#
# average = sum(div) / len(div)
# print(average)



# dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
#
# dict_2 = {}
#
# for value in dict_1.values():
#     dict_2[value] = len(value)
#
# print(dict_2)


# def filter(dict):
#     result = {}
#     for key, values in dict.items():
#         odd_values = [num for num in values if num % 2 == 1]
#         result[key] = odd_values
#     return result
# data = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}
# filtered_data = filter(data)
# print(filtered_data)



# def ar(num):
#     d = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
#     roman = ""
#     i = 0
#     for a, r in d.items():
#         count = num // a
#         roman += count * r
#         num %= a
#     return roman



# PARADIGM

# class Dog:
#     legs = 4
#     tail = 1
#
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def sit(self):
#         print(f"{self.name} sits")
#
#     def __str__(self):
#         return f"{self.name}, {self.age}"
#
#
#
# d1 = Dog("Max", 5, "Black")
# d2 = Dog("sharik", 10, "white")
# print(d1)
# print(d1.color)
# d1.sit()



# class Car:
#     def __init__(self, company, model, year, petrol, litre_per_100km):
#         self.company = company
#         self.model = model
#         self.year = year
#         self.petrol = petrol
#         self.litre_per_100km = litre_per_100km
#         self.km = 0
#
#     def description(self):
#         return f"{self.company}, {self.model}"
#
#     def mileage(self):
#         return f"{self.km} km"
#
#     def go(self, km):
#         need_p = self.litre_per_100km * km / 100
#         if need_p <= self.petrol:
#             self.km += km
#             self.petrol -= need_p
#             print(f"{self.description()}, is ridden {km} km")
#         else:
#             km_pos = self.petrol * 100 / self.litre_per_100km
#             self.km += km_pos
#             self.petrol = 0
#             print(f"{self.description()}, is ridden {km_pos} km. No Petrol. Left {km - km_pos} km.")
#
#
# c1 = Car("Audi", "R8", 2016, 20, 15)
# c1.go(50)
# print(c1.mileage(), c1.petrol)
# c1.go(100)
# print(c1.mileage(), c1.petrol)



import math
import sys

class Triangle:
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

        if not self.is_valid():
            print("Not a valid triangle")
            sys.exit()


    def is_valid(self):
        return (self.side_1 + self.side_2 > self.side_3 and self.side_1 + self.side_3 > self.side_2 and self.side_2 + self.side_3 > self.side_1)

    def triangle_type(self):
        if self.side_1 == self.side_2 == self.side_3:
            return "equal side triangle"
        elif (self.side_1 == self.side_2 or self.side_1 == self.side_3 or self.side_2 == self.side_3):
            return "equal angle triangle"
        else:
            return "None order triangle"

    def is_right_triangle(self):
        sides = sorted([self.side_1, self.side_2, self.side_3])
        a, b, c = sides[0], sides[1], sides[2]
        return round(a ** 2 + b ** 2, 5) == round(c ** 2, 5)

    def angles(self):
        a = self.side_1
        b = self.side_2
        c = self.side_3

        angle_A = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
        angle_B = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
        angle_C = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

        angle_A_deg = round(math.degrees(angle_A), 2)
        angle_B_deg = round(math.degrees(angle_B), 2)
        angle_C_deg = round(math.degrees(angle_C), 2)

        return angle_A_deg, angle_B_deg, angle_C_deg


    def Sides(self):
        return f"{self.side_1}, {self.side_2}, {self.side_3}"

    def P(self):
        return f"{self.side_1} + {self.side_2} + {self.side_3}"

    def S(self):
        s = (self.side_1 + self.side_2 + self.side_3) / 2
        area = math.sqrt(s * (s - self.side_1) * (s - self.side_2) * (s - self.side_3))
        return area

t = Triangle(3, 4, 5)
print(t.side_1, t.side_2, t.side_3)
print(t.triangle_type())
print(t.is_right_triangle())
print(t.S(), 2)
print(t.P(), 2)
print(t.angles())























