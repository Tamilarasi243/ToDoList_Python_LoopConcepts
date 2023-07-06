from colorama import Fore,init
init()
class toDo:
    def __init__(self):
        self.important_list=["Morning workout","Early morning wakeup","Medicine for skin disease","Art","Trekking","World's tour"]
        self.not_important_list=["Spending time with family","Listening to music","Playing game"]
        self.urgent_list=["Morning workout","Listening to music","Early morning wakeup","Medicine for skin disease"]
        self.not_urgent_list=["Art","Playing game","Trekking","World's tour","Spending time with family"]


    # Important and urgent list
    def I_U(self):
        print("Important and urgent list.....")
        for i in self.important_list:
            if i in self.urgent_list:
                print(Fore.GREEN+i)
    
    # Important and not urgent list
    def I_N_U(self):
        print("Important and not urgent list")
        for i in self.important_list:
            if i in self.not_urgent_list:
                print(Fore.BLUE+i)
    
    # Not important and urgent list
    def N_I_U(self):
        print("Not important and urgent list")
        for i in self.not_important_list:
            if i in self.urgent_list:
                print(Fore.YELLOW+i)
    
    # Not important and not urgent list
    def N_I_N_U(self):
        print("Not important and not urgent list")
        for i in self.not_important_list:
            if i in self.not_urgent_list:
                print(Fore.RED+i)
    
    def ExistingMethod(self,userChoice):
        if userChoice==1:
            self.I_U()
        elif userChoice==2:
            self.I_N_U()
        elif userChoice==3:
            self.N_I_U()
        elif userChoice==4:
            self.N_I_N_U()
        else:
            print("Choosed wrong choice.....")

    def AddDetailsMethod(self,userChoice):
        if userChoice==1:
            self.important_list.append(List)
            self.urgent_list.append(List)
            self.I_U()
        elif userChoice==2:
            self.important_list.append(List)
            self.not_urgent_list.append(List)
            self.I_N_U()
        elif userChoice==3:
            self.not_important_list.append(List)
            self.urgent_list.append(List)
            self.N_I_U()
        elif userChoice==4:
            self.not_important_list.append(List)
            self.not_urgent_list.append(List)
            self.N_I_N_U()
        else:
            print("Choosed wrong choice.....")


classObject=toDo()

while True:
    print(Fore.RESET+"TODO List")
    print("Existing List...Choose 1...\nAdd content to list...Choose 2...")
    existingOrAdd=int(input("Choose 1 or 2..."))

    if existingOrAdd==1:
        print("-"*75)
        print("1 Important and Urgent list\n2 Important and Not Urgent list\n3 Not Important and Urgent list\n4 Not Important and Not Urgent list")
        userChoice=int(input("Choose (1 or 2 or 3 or 4) "))
        print("-"*75)

        classObject.ExistingMethod(userChoice)
        
    elif existingOrAdd==2:
        List=input("Type things want to add in the list...").capitalize()
        print("1 Important and Urgent list\n2 Important and Not Urgent list\n3 Not Important and Urgent list\n4 Not Important and Not Urgent list")
        userChoice=int(input("Choose (1 or 2 or 3 or 4)..."))

        classObject.AddDetailsMethod(userChoice)

    else:
        print("Choosed wrong choice.....")

    continue_choice = input(Fore.RESET+"Do you want to continue choose(yes or no)...")
    if continue_choice.lower() != "yes":
        break