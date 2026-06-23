print("------Suhas-Infra-Patan-----")
print("-----Machine Department-----")


class  Machine:
    def __init__(self,Machine_id,Machine_Name,Machine_Type,Machine_Status):
        self.Machine_id = Machine_id
        self.Machine_Name = Machine_Name
        self.Machine_Type = Machine_Type
        self.Machine_Status = Machine_Status

    def display(self):
        print('Machine ID :',self.Machine_id)
        print('Machine Name Is :', self.Machine_Name)
        print('Machine Categoery is :',self.Machine_Type)
        print('Machine Status (Avaliable Yes/ No):',self.Machine_Status)

list_Machine = []

def add_Machine():

    Machine_id = input("Enter A Machine ID :")
    Machine_Name = input("Enter A Machine Name :")
    Machine_Type = input("Enter A Machine Categoery Is : ")
    Machine_Status = input("Enter A Machine Status (Available Yes/No) :")

    machine = Machine(Machine_id,Machine_Name,Machine_Type,Machine_Status)
    list_Machine.append(machine)

    print("Machine Add !!")

def save_to_file():

    with open("list-of-Machine.txt","w+") as file:
        for Machine in list_Machine:
            file.write(
                f"{Machine.Machine_id},"
                f"{Machine.Machine_Name},"
                f"{Machine.Machine_Type},"
                f"{Machine.Machine_Status}\n"

            )
    print("Machine Save")


def view_Machine():

    if len(list_Machine) == 0:
        print('No Machine In List')

    else:
        for Machine in list_Machine:
            Machine.display()


def search_Machine():

    search_id = input("Enter A Search Machine Id :")

    for machine in list_Machine:
        if machine.Machine_id == search_id:
            machine.display()
            return
    
    print("Machine Not list")


def Delate_Machine():

    Del_id = input("Enter A Machine ID Which Delete The Machine :")

    for machine in list_Machine:
        if machine.Machine_id == Del_id:
            list_Machine.remove(machine)
            print("Delete The Machine")
            return
        
    print("Machine Not Availabe In the list")


while True:

    print("####### Machine Management System ######")
    print('1.Add MAchine')
    print('2.save TO Machine')
    print('3.View Machine')
    print('4.Search Machine')
    print('5.Delete Machine')
    print('6.Exit')

    Choice = input("Enter A Choice Id :")


    if Choice == '1':
        add_Machine()

    elif Choice == '2':
        save_to_file()

    elif Choice =='3':
        view_Machine()

    elif Choice =='4':
        search_Machine()

    elif Choice =='5':
        Delate_Machine()

    elif Choice =='6':
        print('End Programe')
        break
    
    else:
        print('Wroung Choice plz Correct Input ')
    

    



   




  