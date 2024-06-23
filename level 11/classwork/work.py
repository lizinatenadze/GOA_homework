

# ask the user to enter the savings
savings = input("enter your savings: *")

# convert the user input into a float value and ubdate the variable

savings2 = float(savings)

# savings grow after 1 year at a 5% annual rate

balance = savings2 * 1.05

# convertthe balance into a string and ubdate the variable

balance = str(balance)

# concatenate the 2 strings to produse a message

message = 'amount in 1 year: ' + balance

# display the message


print(message)
















