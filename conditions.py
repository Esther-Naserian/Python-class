def print_numbers(n):
    numbers=range(n)
    for number in numbers:
      print(number)

def print_even_numbers(n):
   numbers=range(n)
   for number in numbers:
      if number%2==0:
       print(number)
def add_or_even(n):
   numbers=range(n)
   for number in numbers:
      if number %2 ==0:
         print(f"{number} is even")
      else:
         print(f"{number} is odd")

def check_divisibility(n):
   numbers=range(n)
   for number in numbers:
        if number %3 ==0:
         print(f"{number} is divisibility by 3")
        elif number%5==0:
           print(f"{number} is divisible by 5")
        elif number%7==0:
           print(f"{number} is divisible by 7")
        else:
           print(f"{number} is not divible by3 ,5,7")
           
def  count_down(n):
   x=0
   while n>x:
      print(n)
      if n==5:
         break
      n-=1
def divisible_by_seven(n):
    x=1
    while x <=n:
       x+=1
       if x%7 !=0:
          continue
       print(f"{x} is divisible by 7")
#        #using whilwe,continue and if statements write a function that prints all the all old numbers beteween 0 and 1001

   
         
#create a function named fizzbuzz for the numbers divisible by 3 it prints fizz
#for numbers divisible by 5 it prints buzz
#for all the other numbers it prints fizzbuz use if ,else, elif
def fizzbuzz(n):
   numbers=range(n)
   for i in numbers:
      if i%5==0:
          print(f"{i} is buzz")
          if i%3==0:
             print(f"{i} is fizz")
      else:
         print("fizzbuz")



   

         
      