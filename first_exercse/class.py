"""
contact class
상속받기 가능함.

"""

class Contact(object):

    def __init__(self, name, email, age, addr):
        self.name = name
        self.email = email
        self.age = age
        self.addr = addr

    def to_string(self):
        return self.name+ " "+ self.email + " " + self.age +" "+ self.addr


contact = Contact('jeong','jeong.inu@gmail.com',23,'seoul city')

print(contact.addr)

print(contact.to_string())