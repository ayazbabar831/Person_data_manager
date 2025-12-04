class Person:
    def __init__(self,name,age,email,city):
        self.name = name
        self.age = age
        self.email = email
        self.city = city

    def to_dict(self):
        return {
            "name":self.name,
            "age":self.age,
            "email":self.email,
            "city":self.city
        }
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"City: {self.city}")