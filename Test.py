""" x = 5
if x < 5:
    print("x is less than 5")
elif x > 5:
    print("x is greater than 5")
else:
    print("X is 5")

data = [2, 'rr', 456]
print(data)
print (data[0:3])
for x in data:
    print(x)

def printme(str):
    "This print me"
    print (str)
    return


printme(str="Hi")

def printdata(name, age=35):
    print('My name is ', name + '. I am ', str(age) + ' years old')
    return


printdata(name="Chamila", age=12)
printdata(name="Jeni")


def print_tuple_data(*tuplearg):
    print("Tuple arguments are", tuplearg)
    return


a = print_tuple_data(3,'ddd',333,'dds')
print(a)




def add_function(x,y):
   # print(x)
    return y
c = add_function(y=3,x=5)
print(c)


class Family(object):

    family_name = "Nadarajah"

    def __init__(self,name,age,position,favorite_color):
        self.name = name
        self.age = age
        self.position = position
        self.fav_color = favorite_color

    def family_members(name,age,position,fav_color):
        return name,age,position,fav_color

    def get_family_name(cls):
        return cls.family_name

    x = family_members('Nada', 35,'Father', 'red')
    y = get_family_name()

print(Family.x)
print(Family.y)


class Human(object): # need to be explicity defined
    #class atrributes: can be shared object atributes can share only with the object
    species = "H. sapiens" #class attribute
    def __init__(self, name): #constructor need to have at least 1 parameter
        self.name = name # object attributes

    def say(self, msg): #object method
        return "{name}: {message}".format(name=self.name,message=msg)

    @classmethod #class method
    def get_species(cls):
        return cls.species # current class attributes

    @staticmethod
    def grunt(): #need not to use param
        return "grunt"

i = Human(name="Ian")
print (i.say("hi"))

j = Human(name="Joel")
print(j.say("Hi"))

print (i.get_species())#class Att are shared by all the objects
print (j.get_species())#class Att are shared by all the objects

Human.species = "H. nendffdfdf"
print (i.get_species())#class Att are shared by all the objects
print (j.get_species())#class Att are shared by all the objects

Human.grunt()
print (Human.grunt()) #static method can acces throug class method



def sum_of_two_values(num1, num2):
    num3 = (int(num1) + int(num2))
    print(num3)
    print(num1 + num2)
    return
sum_of_two_values(input("Enter num1"),input("Enter num2"))


lower = 0
upper = 20
print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):

    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)"""