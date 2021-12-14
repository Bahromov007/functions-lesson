# velocity1 = 70
# velocity2 = 100
# time = 2
# distance = (velocity1 + velocity2) * time
# print(distance)

# def calculateDistance(v1, v2, t):
#     return (v1 + v2) * t
# d = calculateDistance(70, 100, 2)
# print(d)

# def calculateDistance(v1, v2, t):
#     return (v1 + v2) * t
# print(calculateDistance(70, 100, 2))

# def CalculateDistance(vel1, vel2, time):
#     return (vel1 + vel2) * time
# vel1 = int(input('Enter velocity 1: '))
# vel2 = int(input('Enter velocity 2: '))
# time = int(input('Enter time: '))
# print(CalculateDistance(vel1, vel2, time))


# def CalculateSquare(x):
#     return x * x
# print(CalculateSquare(10))

# def CalcPower(base, expo):
#     return base ** expo
# print(CalcPower(3, 4))

# def reverseList(list):
#     return list[::-1]
# print(reverseList([1, 2, 3]))

# def calcOppositeNum(num):
#     return 1 / num 
# print(calcOppositeNum(10))

# def calcSum(num1, num2):
#     return num1 + num2
# print(calcSum(2, 3))

# def CalcSum(a, b, *c):
#     acc = 0
#     for num in c:
#         acc += num 
#     return a + b + acc
# print(CalcSum(2, 3, 4, 5, 6, 7))

# def sayHello(name, surname):
#     print(f'Hello, {surname} {name}')
# sayHello('Abdulkhakim', 'Bakhromov')


# mentor = {
#     "name" : "Abdulkhakim",
#     "surname" : 'Bakhromov',
#     "age" : 15,
#     "isMarried" : False
# }
# print(mentor.get("name"))
# for key in mentor:
#     print(key, mentor[key])

# def abc(**args):
#     return(args)
# print(abc(a = 4, b = 6, c = 3))

# def abc(**args):
#     acc = 0
#     for key in args:
#         acc += args[key]
#     return acc
# print(abc(a = 4, b = 6, c = 3))

# def min(a, b):
#     if a < b: return a
#     elif a == b: return 'Equal'
#     else: return b 

# print(min(10,5))
# print(min(20,10))
# print(min(10,10))


# print(eval('1+2'))

# def calculator(a, b, action):
#     if action == 'add': return eval(f'{a} + {b}')
#     if action == 'subtract': return (f'{a} + {b}')
#     if action == 'multiply': return (f'{a} * {b}')
#     if action == 'divide': return (f'{a} / {b}')

# print(calculator('1', '3', 'add'))
# print(calculator('1', '3', 'subtract'))       
# print(calculator('1', '3', 'multiply'))
# print(calculator('1', '3', 'divide'))

# def Calcdistance(time, speed):
#     return time * speed
# time = int(input('Enter time: '))
# speed = int(input('Enter speed: '))
# print(Calcdistance(time, speed))


# ask nums, find x/y * z , if y = 0 - ask again

# def calctask(x, y, z):
#     while True:
#         if y == 0:
#                 y = int(input('Enter 2nd number: ')) 
#         else: return (x / y) * z 
# x = int(input('Enter 1st number: '))
# y = int(input('Enter 2nd number: '))
# z = int(input('Enter 3rd number: '))
# print(calctask(x, y, z))

#  ask num, calc pow1/2, if pow not full num - ask again
