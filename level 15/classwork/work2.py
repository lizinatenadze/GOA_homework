#დაწერეთ პროგრამა, რომელიც მოუწოდებს მომხმარებელს შეიყვანოს ნივთების რაოდენობა, რომლის შეძენაც სურს.დარწმუნდით, რომ მომხმარებელი შეიყვანს დადებითი რიცხვს.თითოეული ნივთისთვის, შესთავაზეთ მომხმარებელს შეიყვანოს ფასი.დარწმუნდით,რომ მომხმარებელი შეიყვანოს დადებითი რიცხვს პროდუქტის ფასისთვის.გამოთვალეთ და აჩვენეთ ყველა ელემენტის მთლიანი ღირებულება.



bag = int(input('how much bag do you want? '))
shoe = int(input('how much shoe do you want? '))
hat = int(input('how much hat do you want? '))
phone = int(input('how much phone do you want? '))


price1 = int(input('chose a good price for you: '))
price2 = int(input('chose a good price for you: '))
price3 = int(input('chose a good price for you: '))
price4 = int(input('chose a good price for you: '))

bag_price = (bag * price1 )
shoe_price = (shoe * price2)
hat_price = (hat * price3)
phone_price = (phone * price4)

print(bag_price)
print(shoe_price)
print(hat_price)
print(phone_price)