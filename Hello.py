def hello():
    print("Hello AkiraChix")

def hello(name):
    print(f"Hello {name}")
def year_of_birth(name,age):
    print(f"Hello {name} you have born in{2024-age}")

def my_country(country="uganda"):
    print(f"Hello AkiraChix from {country}")
def greet(*names):
     for name in names :
         print(f"Hello {name}greege")
def  create_sentence(**words):
      sentence= " "
      for word in words.values():
          sentence += word
          sentence += " "
      return sentence

def sum_and_greet(*args,**kwargs):
    total= 0
    for  x in  args:
        total +=x

    f=kwargs["firstname"]
    l=kwargs["lastname"]
    greeting=f"Hello {f} the sum of your numbers is{total}"
    return greeting
    