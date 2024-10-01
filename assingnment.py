class Student:
    def __init__(self, name, reg_no):
        self.name = name
        self.reg_no = reg_no

    def display_details(self):
        print(f"Student Name: {self.name}, Registration Number: {self.reg_no}")


student1 = Student("david", "REG12345")
student1.display_details()

student2 = Student("klein", "REG67890")
student2.display_details()

student3= Student("kizito","REG99002")
student3.display_details()