class Student:
    name="Raziah"
    code="004"
    school="AkiraChix"
    age= 20
    def __init__(self,firstname,lastname,age,country,code):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.country=country
        self.code=code
        mercy=Student(firstname="mercy",lastname="chemtai",age=23,country="kenya",code=48)

        aline=Student(firstname="aline",lastname="mutesi",age=24,country="rwanda",code=34)

        eshe=Student(firstname="eshe",lastname="aziz",age=23,country="kenya",code=48)

        mercy.code
        aline.country
        eshe.lastname

    def greet_student(self):
        greeting=f"Hello {self.firstname}, welcome to {self.school}.Your school code is {self.code}"      
        return greeting
        mercy.greet_student()

    # def greetings_student():
    #     greetings=f"Hello  you were born in{self.age}"



def initials(name): 
    return [i[0].upper() for i in name.split() ] 
     
while True: 
    the_name = input("enter a Name ") 
    if the_name == '': break 
    print(*initials(the_name),sep=',') 






        