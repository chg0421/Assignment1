import re
from View import View


class Validator:

    def validate_bmi(bmi):
        bmi_values = ['Normal', 'Overweight', 'Obesity', 'Underweight']
        if bmi in bmi_values:
            print("Valid")

        else:
            print("invalid")

    def validate_sales(sales):
        check = re.compile('[0-9]{2,3}')
        if re.fullmatch(check, sales):
            print("Valid Data")
            return True
        else:
            print("Invalid")
            return False


test = Validator
test.validate_bmi(input("Enter Employee BMI"))
test.validate_sales(input("Enter Employee Sales"))


