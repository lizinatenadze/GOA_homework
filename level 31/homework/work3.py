#შექმენით ფუნქცია, რომელიც მომხმარებელს შეკითხება პაროლს, სანამ სოწორს არ ჩაწერს მომხმარებელი.



def password(correct):
    while True:
        password = input("enter password: ")
        if password == correct:
            print("the answer corrrect.")
            break
        else:
            print("incorrect try again.")

correct = "yO58582u##ARe))gR::OS@S*"  
password(correct)






