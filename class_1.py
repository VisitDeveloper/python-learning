# /////////////////////////////////////////////////////////////////////////////////////////////////
# تعریف کلاس و تابع سازنده در پایتون
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y        
#     def move(self):
#         print('move')

#     def draw(self):
#         print('draw')


# /////////////////////////////////////////////////////////////////////////////////////////////////
#  نحوه استفاده از کلاس خیلی مهم 
# point = Point()
# اضافه کردن متغیر به یک کلاس
# point.x = 10
# point.y = 20
# print(point.x)
# point.draw()

# point2 = Point()
# # این خط به ارور میخوریم چون دو تا اینستنس از یک کلاس با هم دیگر متفاوت هستند
# print(point2.x)



# /////////////////////////////////////////////////////////////////////////////////////////////////
# ارسال متغییر به تابع سازنده یک کلاس
# point = Point(10,20)
# print(point.x)

# /////////////////////////////////////////////////////////////////////////////////////////////////
# ارث بری در پایتون 
class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal):
    pass
    def wild(self):
        print('wild wild')

class Cat(Dog):
    pass
    def catwalk(self):
        print('cat walk')

cater = Cat()
cater.catwalk()
cater.walk()
cater.wild()