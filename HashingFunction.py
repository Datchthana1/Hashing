import datetime as D
import json as js
class Hashing:
    def __init__(self):
        self.Number = 0
        self.list = []
        self.index = {}
        self.FirstName = ""
        self.LastName = ""
        self.Age = 0
        self.BirthDate = 0
        self.Text = ""
        self.Encrypt_data = 0

    def InputName(self):
        self.FirstName = str(input("First Name : "))
        self.Lastname = str(input("Last Name : "))
        self.BirthDate = str(input("Type your birthday (27062004) : "))
        self.Age = str(input("Age : "))
        self.Text = str(input("Type your word for input : "))
        self.FullName = f"{self.FirstName} {self.LastName} your age is {self.Age}"
        print(self.FullName)

    def EncyptData(self):
        self.Encrypt_data = self.BirthDate[1:4]
        return self.Encrypt_data
    
    def DumpsJSON(self):
        JsonString = js.dumps(self.list)
        return JsonString
    
    def DirectHashing(self):
        Hashing.InputName(self)
        self.index = {self.Encrypt_data : {Hashing.EncyptData(self) : {"FirstName" : self.FirstName,"Lastname" : self.LastName,"Age" : self.Age,"Text" : self.Text}}}
        self.list.append(self.index)
        Hashing.DumpsJSON(self)
        return self.list
    
    def SubTractionHashing(self):
        Hashing.InputName(self)
        x = D.datetime.now()
        Year = x.strftime("%Y")
        Address = f"{Year}{Hashing.EncyptData(self)}"
        self.index = {self.Encrypt_data : {Address : {"FirstName" : self.FirstName,"Lastname" : self.LastName,"Age" : self.Age,"Text" : self.Text}}}
        self.list.append(self.index)
        Hashing.DumpsJSON(self)
        return self.list
    
    def ModuleDivision(self):
        Hashing.InputName(self)
        Mod = int(input("Number for Mod : "))
        self.Module = int(Hashing.EncyptData(self)) % Mod
        self.index = {self.Encrypt_data : {self.Module : {"FirstName" : self.FirstName,"Lastname" : self.LastName,"Age" : self.Age,"Text" : self.Text}}}
        self.list.append(self.index)
        Hashing.DumpsJSON(self)
        return self.list
    
    def MIDSquare(self):
        Hashing.InputName(self)
        self.MidSquare = (int(Hashing.EncyptData(self)))**2
        self.MidSquareString = str(self.MidSquare)
        self.Mid = self.MidSquareString[2:4]
        self.index = {self.Encrypt_data : {self.Mid : {"FirstName" : self.FirstName,"Lastname" : self.LastName,"Age" : self.Age,"Text" : self.Text}}}
        self.list.append(self.index)
        Hashing.DumpsJSON(self)
        return self.list
    
H = Hashing()
Again = "y"
while True:
    if Again == "y":
        Choosing = 0
        Choose = int(input("หาวิธีการhashing\n1:DirectHashing\n2:SubTractionHashing\n3:ModuleDivision\n4:Square\nวิธีที่คุณเลือกคือ : "))
        if Choose == 1:
            print(H.DirectHashing())
        elif Choose == 2:
            print(H.SubTractionHashing())
        elif Choose == 3: 
            print(H.ModuleDivision())
        elif Choose == 4:
            print(H.MIDSquare())
        else:
            print("Invalid : PLease type Again")
        Again = str(input("Would you like to use again? (y/n) : "))
        Again = Again.lower()
    else: 
        print(H.DumpsJSON())
        break