import json

def add_person():
    

    name = input("What is your name: ")
    age = input("Enter your age: ")        
    email = input("Enter your email: ")        
    city = input("Enter your city: ")     

    data.append({"name":name,"age":age,"email":email,"city":city})    

    with open("person_data.json","w") as file:
        json.dump(data,file,indent=4)


def display():
    
    for person in data:
        for k,v in person.items():
            print(f"{k}: {v}")
def search():
    by_name = input("enter the name of the peson you are searching: ")
    for person in data:
        if by_name == person["name"]:
            for k,v in person.items():
                print(f"{k}: {v}")

def update():
    with open("person_data.json","w") as file:
        by_name = input("enter the name of the peson you want to update: ")
        for person in data:
            if by_name == person["name"]:
                choice  = input("what do you want to update")
                match choice:
                    case "name":
                        new_name = input("enter new name")
                        person["name"] = new_name
                        json.dump(data,file,indent=4)
                    case "age":
                        new_age = input("enter new age")
                        person["age"] = new_age
                        json.dump(data,file,indent=4)
                    case "email":
                        new_email = input("enter new email")
                        person["email"] = new_email
                        json.dump(data,file,indent=4)
                    case "city":
                        new_city = input("enter new city")
                        person["city"] = new_city
                        json.dump(data,file,indent=4)



def delete():
    by_name = input("enter the name of the peson you want to delete: ")
    new_data = [x for x in data if x["name"]!= by_name]
    with open("person_data.json","w") as file:
        json.dump(new_data,file,indent=4)


while True:
    with open("person_data.json","r") as file:
            contents = file.read()
            if contents == "":
                data = []
            else:
                data = json.loads(contents)

    print("------------------------Welcome To Person Data Manager--------------------------------")
    print("What do you want to do?")
    print("1.Add a Person")
    print("2.Display info")
    print("3.Search by name")
    print("4.update info")
    print("5.delete a person")
    print("0.exit....")
    
    choice = int(input("enter your choice:"))
    
    match choice:
        case 1:
            add_person()
        case 2:
            display()
        case 3:
            search()
        case 4:
            update()
        case 5:
            delete()
        case 0:
            print("exiting......")
            exit()
        case _:
            print("invalid choice")











