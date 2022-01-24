

def menu():
    print("="*50)
    print("welcome to employee management system")
    print('''
                    || MENU ||
                    1. Add employee.
                    2. Update employee.
                    3. Remove.
                    4. Show all.    
    
    ''')
    print("="*50)

def add_employee():
    pass

def update():
    pass

def remove():
    pass

def show_all():
    pass

while True:
    menu()
    Get_ip=input("Enter your choice you want to perform :-")

    if(Get_ip=='1'):
        add_employee()
    elif(Get_ip=='2'):
        update()
    elif(Get_ip=='3'):
        remove()
    elif(Get_ip=='4'):
        show_all()
    else:
        print("You have enter invalid input....")

    get_ch=input('Do you want to continue Y/N:-')
    get_ch= get_ch.lower()
    if(get_ch!= 'y'):
        break