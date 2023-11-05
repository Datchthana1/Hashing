import datetime as D
class Hashing:
    def __init__(self):
        self.Number = 0
        self.list = []
        self.index = {}
        self.text = ""
        self.StrNumber = ""

    def InputNumber(self):
        self.Number = input("Type your Number only 2 numbers : ")
        self.StrNumber = str(self.Number)
        self.Text = str(input("Type your word : "))

    def DirectHashing(self):
        Hashing.InputNumber(self)
        self.index = {self.Number : {self.Number : self.Text}}
        self.list.append(self.index)
        return self.list
    
    def SubTractionHashing(self):
        Hashing.InputNumber(self)
        x = D.datetime.now()
        Year = x.strftime("%Y")
        Address = f"{Year}{self.StrNumber}"
        self.index = {self.Number : {Address : self.Text}}
        self.list.append(self.index)
        return self.list
    
    def ModuleDivision(self):
        Hashing.InputNumber(self)
        Mod = int(input("Number for Mod : "))
        self.Module = int(self.Number) % Mod
        self.index = {self.Number : {self.Module : self.Text}}
        self.list.append(self.index)
        return self.list

    def Square(self):#หาวิธีของการหา Mid ไม่เป็น
        Hashing.InputNumber(self)
        self.MidSquare = (int(self.Number))**2
        self.index = {self.Number : {self.MidSquare : self.Text}}
        self.list.append(self.index)
        return self.list
    
H = Hashing()
while True:
    Again = "y"
    if Again == "y":
        while True:
            Choosing = 0
            Choose = int(input("หาวิธีการhashing\n1:DirectHashing\n2:SubTractionHashing\n3:ModuleDivision\n4:Square\nวิธีที่คุณเลือกคือ : "))
            if Choose == 1:
                print(H.DirectHashing())
                break
            elif Choose == 2:
                print(H.SubTractionHashing())
                break
            elif Choose == 3: 
                print(H.ModuleDivision())
                break
            elif Choose == 4:
                print(H.Square())
                break
            else:
                print("Invaild : PLease type Again")
        
        Again = str(input("Would you like to use again? (Y/N) : "))
        Again.lower()
    else: 
        break
