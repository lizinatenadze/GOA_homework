# შექმენით ფუნქცია რომელშიც გადაცემთ ლისტს, შემდეგ კი ეს ლისტი დაპრინტეთ უკუღმა


def print_list(l):

    for item in reversed(l):
        print(item)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_list(my_list)
