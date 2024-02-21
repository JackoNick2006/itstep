# class Student:
#     def __init__(self, height = 160):
#         self.height = height
#
# nick = Student()
# kate = Student(height=170)
# Chiril = Student(height=2024)
# print(nick.height)
# print(kate.height)
# print(Chiril.height)

# Ex 2
# class Student:
#     amount_of_students = 0
#     def __init__(self, height = 160):
#         self.height = height
#         Student.amount_of_students+=1
#
# nick = Student()
# kate = Student(height=170)
# Chiril = Student()
# print(nick.amount_of_students)
# print(Student.amount_of_students)
# print(kate.height)

#Ex 3
# class Student:
#     height = 160
#     def __init__(self):
#         print(self.height)
#         Student.height+=10
#
# nick = Student()
# kate = Student()

#Ex 3
# class Student:
#     def __init__(self):
#         self.height = 170
#     height = 160
#     def printer(self):
#         print(self.height)
# nick = Student()
# nick.printer()

#Ex 4
# x = 10
# class Locker:
#     print(x)
#     def func_1(self):
#         # x=20
#         print(x)
#         def func_2():
#             # x=30
#             print(x)
#         func_2()
# some_object = Locker()
# some_object.func_1()

#Ex 5
# class Student:
#     amount_of_students = 0
#     def __init__(self, height = 160):
#         self.height = height
#         Student.amount_of_students+=1
#     def grow(self, height=1):
#         self.height+=height
# nick = Student()
# kate = Student(height=170)
# nick.grow(height=15)
# print(kate.height)
# print(nick.height)
# print(Student.amount_of_students)
# jora = Student()
# print(Student.amount_of_students)

#Ex 6
# class Student:
#     def __init__(self, name=None):
#         self.name = name
#     def __str__(self):
#         return f"I am a student. My name is {self.name}"
# nick = Student(name="Nick")
# print(nick)

#Ex 7
# class Student:
#     def __init__(self, name = None):
#         self.name = name
#     def __str__(self):
#         if self.name:
#             return f"I am a student. My name is {self.name}."
#         else:
#             return f"I am a student. I have no name."
# alice = Student(name="Alice")
# print(alice)
# unknown_student = Student()
# print(unknown_student)

#Ex 8
# import random
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.gladness = 50
#         self.progress = 0
#         self.alive = True
#     def to_study(self):
#         print("Este timpul sa invat!")
#         self.progress+=0.12
#         self.gladness-=5
#     def to_sleep(self):
#         print("Voi dormi!")
#         self.gladness-=3
#     def to_chill(self):
#         print("Timp de odihna!")
#         self.gladness+=5
#         self.progress-=0.1
#     def is_alive(self):
#         if self.progress < -0.5:
#             print("DEAD...")
#             self.alive=False
#         elif self.gladness <= 0:
#             print("Depresie...")
#         elif self.progress > 5:
#             print("O murit de fericire")
#             self.alive=False
#     def end_to_play(self):
#         print(f"Fericire = {self.gladness}")
#         print(f"Progres = {round(self.progress, 2)}")
#     def live(self, day):
#         day = "Ziua "+str(day)+" din viata lui "+self.name+" "
#         print(f"{day:=^50}")
#         live_cube = random.randint(1, 3)
#         if live_cube == 1:
#             self.to_study()
#         elif live_cube == 2:
#             self.to_sleep()
#         elif live_cube == 3:
#             self.to_chill()
#         self.end_to_play()
#         self.is_alive()
# nick = Student(name="Vlad")
# for day in range(365):
#     if nick.alive == False:
#         break
#     nick.live(day)