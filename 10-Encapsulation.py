"""
The main idea behind encapsulation is that we want to protect our data
by using access modifiers which determine the access to our data .
Access Modifiers :
    * Public : any one can access the data
    * Private : data is only accessible inside class
    * Protected
once you encapsulated a variable you have to create an access point :
    *   Getter : retrieve variable value
    *   Setter : Change variable value
"""


class Student:
    def __init__(self, name="ahmed Basem", marks=50):
        # If a variable is prefixed by a single double underscore , variable is private
        self.__name = name
        self.__marks = marks

    def show_student_data(self):
        print(f"Name is {self.__name} and its marks is {self.__marks}")


s1 = Student(name="Ahmed Basem", marks=100)
s1.show_student_data()
try:
    print(s1.__name)
except:
    print("** You can't Acces this variable")
# doesn't block access to private data entirely. It just leaves it for the wisdom of the programmer
# Name mangling is the process of changing name of a member with double underscore to the form object._class__variable.
print(s1._Student__name)
