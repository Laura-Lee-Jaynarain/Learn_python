def say_hi(name):
    if name == '':
        print(" you didnt enter your name")
    else:
        print("Hi there")
        for letter in name:
            print(letter)

# call function Say_hi()
name = input("Enter your name: ")
say_hi(name)
