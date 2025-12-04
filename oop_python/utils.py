import json
from data import save,load
from person import Person


data = load()
def add_person(data,name,age,email,city):
    p1 = Person(name,age,email,city)
    data.append(p1.to_dict())
    save(data)
    return data
def display_neatly(data):
    for p in data:
        print(f'Name: {p["name"]}')
        print(f'Age: {p["age"]}')
        print(f'Email: {p["email"]}')
        print(f'City: {p["city"]}')
        print("--------------------------")
def display_sorted_by_age(data):
    sorted_data = sorted(data,key=lambda x: x["age"])
    display_neatly(sorted_data)

def count_ppl_in_city(data,city):
    temp = 0
    temp_ppl = []
    found = False
    for p in data:
        if p["city"].lower() == city.lower():
            temp += 1
            temp_ppl.append(p["name"])
    for ppl in temp_ppl:
        print(f"{ppl}")
        found = True
    if found :print(f"These ppl live in {city}")