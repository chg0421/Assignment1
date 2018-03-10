class Employee:

    def __init__(self, emp_id, gender, age, sales, bmi, salary, birthday):
        self.emp_id = emp_id
        self.gender = gender
        self.age = age
        self.sales = sales
        self.bmi = bmi
        self.salary = salary
        self.birthday = birthday

    def display_employee(self):
        # print("Employee ID:", self.emp_id, ", Employee Gender:", self.gender)

        print("Employee Details ")
        print("ID: ", self.emp_id)
        print("Gender: ",self.gender)
        print("Age: ", self.age)
        print("Sales: ", self.sales)
        print("BMI: ", self.bmi)
        print("Salary: ", self.salary)
        print("Birthday: ", self.birthday)


emp1 = Employee('A001', 'M', 35, 999, 'Normal', 50000, 30/1/1989)
emp1.display_employee()


# class Employee:
#
#     def __init__(self):
#         self.emp_id = ""
#         self.gender = ""
#         self.sales = ""
#         self.age = ""
#         self.bmi = ""
#         self.salary = ""
#         self.birthday = ""
#
#     def display_employee(self):
#         print ("Employee ID: ",self.emp_id)
#         print ("Gender : ", self.gender)
#         print ("Age : ", self.age)
#         print ("Sales : ", self.sales)
#         print ("BMI : ", self.bmi)
#         print ("Salary: ", self.salary)
#         print ("Birthday : ", self.birthday)
#
#     @staticmethod
#     def add_employee(self):
#         emp_id = input("Employee ID: ")
#         gender = input("Gender : ")
#         age = input("Age : ")
#         sales = input("Sales : ")
#         bmi = input("BMI : ")
#         salary = input ("Salary: ")
#         birthday = input ("Birthday : ")
#         print(emp_id, gender, age, sales, bmi, salary, birthday)
#         return emp_id, gender, age, sales, bmi, salary, birthday
#
#
# emp1 = Employee()
# #emp1.display_employee()
# x= emp1.add_employee('A001')
# emp1.display_employee(x)









