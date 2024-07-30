import random
from datetime import datetime, timedelta
sin = {}
mod = {}

def create():
    global imi, mod,f,s
    imi = random.randint(100000, 999999)
    print(f"IMEI number:{imi}")
    print()
    print("Add Mobile features ")
    n = int(input("Enter the number of features: "))

    #sin = {}

    for i in range(1,n+1):
        f = input(f"Enter the {i} feature: ")
        s = input(f"Enter the status of {i} feature\n 1.Backlog\n 2.Scheduled\n 3.Testing\n 4.Completed\n")
        sin[f] = s

    mod[imi] = sin
    print()
    print(mod)

def update(imei):
    if imei in mod:
        print("Current Features:")
        print(mod[imei])
        print("Select the feature to edit:")
        feature_to_edit = input().lower() 
        if feature_to_edit in mod[imei]:
                new_value = input(f"Enter the new value for {feature_to_edit}: ")
                mod[imei][feature_to_edit] = new_value
                print("Features updated...")
                print()
        else:
                print("Invalid feature selected.")
    else:
            print("IMEI Number not found in the database.")
            print()

def delete(imei):
    global mod
    while True:
        print("1.To delete Model-IMEI  2.To delete single Feature   3.Exit")
        ch=int(input("Enter the choice: "))
        if ch==1:
            if imei in mod:
                del mod[imei]
                print(f"The Model with {imei} Deleted successfully.")
            else:
                print(f"The Model with {imei} not found")
        elif ch==2:
            print(mod[imei])
            f=input("enter the feature to delete: ")
            if f in mod[imei]:
                if len(mod[imei])==1:
                    del mod[imei]
                    print(f"The {imei}  with only 1 feature {f} so all Deleted successfully.") 
                else:
                    del mod[imei][f]
                    print(f"The {imei}  with feature {f} Deleted successfully.")   
            else:
                print("invalid Feature")
        elif ch==3:
            break    
                  
def released(imei):
    if all(value == '4' for value in mod[imei].values()):
        current_date = datetime.now()
        final_date = current_date + timedelta(days=1)
        print(f"The Model with {imei} is completed and will be released within 1 day, on {final_date.strftime('%Y-%m-%d')}")
    else:
        print(f"The Model with {imei} is still in Development")  

def display():
    for imei, features in mod.items():
        print(f"IMEI: {imei}")
        print("Features:")
        for feature, value in features.items():
            print(f"{feature}: {value}")

while True:
    print(" 1.To Create and Read\n 2.Update Features\n 3.Display\n 4.Release_Date\n 5.Delete\n 6.Exit")
    ch = int(input("Enter the choice: "))
    print()
    if ch == 1:
        create()
        print()
    elif ch == 2:
        if len(mod)==0:
            print("No features Added")
        else:
            imei_to_edit = int(input("Enter the IMEI of the mobile to edit features: "))
            print()
            update(imei_to_edit)
    elif ch == 3:
        if len(mod)==0:
                print("No features Added")
                print()
        else:
            display()
    elif ch==4:
        imi = int(input("Enter IMEI id to check Released Date: "))
        if imi in mod:
             released(imi)
        else:
            print("Invalid IMEI id")
        
    elif ch==5:
            if len(mod)==0:
                print("No features Added")
                print()
            else:
                imi = int(input("Enter IMIE id to delete: "))
                print()
                delete(imi) 
    elif ch == 6:
        break