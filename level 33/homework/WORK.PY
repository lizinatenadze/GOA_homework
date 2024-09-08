def simple_calculator(y, x, a):
     
    if y == 0:
      return "wrong, you can't divide by 0"

    elif a == '+':
      return x + y
     
    elif a == '-':
      return x - y
     
    elif a == '*':
      return x * y
     
    elif a == '/':
      return x / y
             
    if y == 0:
      return "Wrong, you can't divide by 0."

try:
    x = float(input("Enter the first number: "))
    a = input("Enter action (+, -, *, /): ")
    y = float(input("Enter the second number: "))

except ValueError:
    print("Invalid input. Please enter numeric values.")

result = simple_calculator(x, y, a)
print("The result is:", result)

























# elif a == '+':
#     print("the answer is: " result)
     
# elif a == '-':
#     print("the answer is: " result_2)
     
# elif a == '*':
#     print("the answer is: " result_3)
     
# elif a == '/':
#     print("the answer is: " result_4)
# result = (x, '+', y)
# result_2 = (x, '-', y)
# result_3 = (x, '*', y)
# result_4 = (x, '/', y)









# # განსაზღვრეთ ფუნქცია სახელწოდებით simple_calculator, რომელიც იღებს სამ არგუმენტს:

# # num1: პირველი რიცხვი (მთლიანი ან float).
# # num2: მეორე რიცხვი (მთლიანი ან float).

# # ოპერაცია: სტრიქონი, რომელიც განსაზღვრავს შესასრულებლად ოპერაციას. ის შეიძლება იყოს „დამატება“, „გამოკლება“, „გამრავლება“ ან „გაყოფა“.
# # ფუნქციის შიგნით,

# # გამოიყენეთ if და elif განცხადებები, რათა დაადგინოთ რომელი ოპერაცია უნდა შეასრულოთ ოპერაციის არგუმენტის მნიშვნელობიდან გამომდინარე.

# # ფუნქციამ უნდა დააბრუნოს ოპერაციის შედეგი.

# # თუ ოპერაცია არის „გაყოფა“ და num2 არის 0, ფუნქციამ უნდა დააბრუნოს „შეცდომა: ნულზე გაყოფა შეუძლებელია“.
# # ჩაწერეთ კოდი, რომ გამოიძახოთ ფუნქცია სხვადასხვა ოპერაციებით და დაბეჭდოთ შედეგები.
