#Starting with creating  Class and Object then  accessing Class Values values with calling it(attributes)
class Student:
    roll = " "
    gpa = " "


zubayer = Student()
zubayer.roll = 1811000
zubayer.gpa = 4.12
print(f"Roll : {zubayer.gpa} , GPA : {zubayer.gpa}")

tonmoy = Student()
tonmoy.roll = 1911562106
tonmoy.gpa = 4.00
print(f"Roll : {tonmoy.gpa} ,  GPA : {tonmoy.gpa}")

mamun = Student()
mamun.roll = 18111111
mamun.gpa = 3.95
print(f"Roll : {mamun.gpa} , GPA : {mamun.gpa}")

############################################################

#2nd part use function to avoid print randomly

""""class Student:
    roll = " "
    gpa = " "

    def display (self) :
        print(f"Roll : {self.gpa} , GPA : {self.gpa}")

zubayer = Student()
zubayer.roll = 1811000
zubayer.gpa = 4.12
zubayer.display()

tonmoy = Student()
tonmoy.roll = 1911562106
tonmoy.gpa = 4.00
tonmoy.display()

mamun = Student()
mamun.roll = 18111111
mamun.gpa = 3.95
mamun.display()"""

#############################################################################

#3rd creating extra function set value to avoid randomly calling class value

""""class Student:
    roll = " "
    gpa = " "

    def set_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa


    def display (self) :
        print(f"Roll : {self.gpa} , GPA : {self.roll}")


zubayer = Student()
zubayer.set_value(1365469,4.2)
zubayer.display()


tonmoy = Student()
tonmoy.set_value(1911562106,4.1)
tonmoy.display()


mamun = Student()
mamun.set_value(18111111,4.0)
mamun.display()'''''

#########################################################################

#4th init method for avoiding extra function set value

"""class Student:
    roll = " "
    gpa = " "

    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display (self) :
        print(f"Roll : {self.gpa} , GPA : {self.roll}")

zubayer = Student(1365469,4.2)
zubayer.display()

tonmoy = Student(1911562106,4.1)
tonmoy.display()

mamun = Student(18111111,4.0)
mamun.display()"""""

