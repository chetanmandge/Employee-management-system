
employee_DB=[['chetan',101,'IT','Pune']]
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
    employee=[]
    E_name=input('Enter employee Name :-')
    E_id=input('Enter employee ID :-')
    E_dept=input('Enter employee Dept :-')
    E_location=input('enter employee location :-')

    employee.append(E_name)
    employee.append(E_id)
    employee.append(E_dept)
    employee.append(E_location)


    employee_DB.append(employee)
    print(f"employee {E_name} is successfully added in DB ")
    print(employee_DB)

def update():

    pass

def remove():
    get_ip=input("enter employee name you want to remove:-")
    if(get_ip in employee_DB):
        del employee_DB[get_ip]

def show_all():
    for x in employee_DB:
        print("name:-",x[0])
        print("ID:-", x[1])
        print("Dept:-", x[2])
        print("Location:-", x[3])
        print("="*20)



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