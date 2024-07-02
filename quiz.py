print("Welcome to the wiseso quize \n")

n = input("Do u want to test your knowledge ? (Yes/ No): ")

if n != "yes":
    quit()
    
print(" \n Ok lets test your knowledge")

sum =0

print("""1. In what year did the Great October Socialist Revolution take place? 
a) 1917
b) 1923
c) 1914
d) 1920""")
a = input("Enter the option: ")
if a.lower() == "a":
    print("Correct \n")
    sum += 1
else:
    print("incorrect")
    print("The corect option is a \n")
    
print("""2. What is the largest lake in the world?
a) Caspian Sea
b) Baikal
c) Lake Superior
d) Ontario""")
a = input("Enter the option: ")
if a.lower() == "b":
    print("Correct \n")
    sum +=1

else:
    print("incorrect ")
    print("The corect option is b \n")
    
print("""3. Which planet in the solar system is known as the “Red Planet”?
a) Venus
b) Earth
c) Mars
d) Jupiter""")
a = input("Enter the option: ")
if a.lower() == "c":
    sum +=1
    print("Correct \n")
else:
    print("incorrect ")
    print("The corect option is c \n")
    
    
print("""4. Who wrote the novel “War and Peace”?
a) Anton Chekhov
b) Fyodor Dostoevsky
c) Leo Tolstoy
d) Ivan Turgenev""")
a = input("Enter the option: ")
if a.lower() == "c":
    sum +=1
    print("Correct \n")
else:
    print("incorrect ")
    print("The corect option is c \n")
    
print("""5. What is the capital of Japan?
a) Beijing
b) Tokyo
c) Seoul
d) Bangkok""")
a = input("Enter the option: ")
if a.lower() == "b":
    sum +=1 
    print("Correct \n")
else:
    print("incorrect ")
    print("The corect option is b \n")
    
print("Your total score" ,(sum))
    
