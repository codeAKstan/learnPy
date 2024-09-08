class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        return f'my name is {self.name} and I am {self.age} years old'
    
    def isAdult(self):
        return self.age >= 18



class Employee(Person):
    def __init__(self, name, age, jobTitle):
        super().__init__(name, age)
        self.jobTitle = jobTitle

    def whatisYourJob(self):
        return f'my job is {self.jobTitle}'
    
emp = Employee("john", 24, "engineer")
print(emp.whatisYourJob())