import json
data = []
def load(filepath = "oop_python/person_data.json"):
    try:
        with open(filepath,"r") as f:
           return json.load(f)
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        print("file does not exist")
        return []

def save(data,filepath="oop_python/person_data.json"):
    with open(filepath,"w") as f:
        json.dump(data,f,indent=4)


