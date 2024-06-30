msg = """
1) Display The Books
2) Insert a Book
3) Return The Book
4) Delete The Book
5) Exit
"""

a=['Soulless Dead','A Symphony of Souls','The Dance of Shadows','The Language of Rain']
def display():
    
    for i in a:
        print(i) 

def insert():
    i=input("Enter the book to be added:")
    a.insert(0,i)
    print("Books after added")
    for p in a:
        
        print(p)
    
def retun():
    r=input("Enter the book name: ")
    a.append(r)
def dele():
    print("The books in the self")
    for i in a:
        print(i)
    d=input("Enter the book to be deleted:")
    a.remove(d)
    print("The books after deleted")
    for u in a:
        print(u)
    

while True:
    print(msg)
    c = int(input("Enter your choice:"))
    if c == 1:
        display()
    elif c== 2:
        insert()
    elif c == 3:
        retun()
    elif c == 4:
        dele()
    elif c == 5:
        print("Thanks Visit again")
        exit
        break
    else: 
        print("Invalid operation...")
        exit
        break
    