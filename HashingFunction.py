import datetime as D
class Hashing:
    def __init__(self):
        self.Number = 0
        self.list = []
        self.index = {}
        self.text = ""
        self.StrNumber = ""
        self.MidSquareString = ""
        self.MidSquare = ""

    def InputNumber(self):
        while True:
            self.Number = input("Type your Number only 2 numbers : ")
            self.StrNumber = str(self.Number)                
            if len(self.StrNumber) == 2:
                self.Text = str(input("Type your word : "))
                break
            else:
                pass

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
        self.MidSquareString = str(self.MidSquare)
        self.Mid = self.MidSquareString[:2]
        self.index = {self.Number : {self.Mid : self.Text}}
        self.list.append(self.index)
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
            print(H.Square())
        else:
            print("Invalid : PLease type Again")
        Again = str(input("Would you like to use again? (y/n) : "))
        Again.lower()
    else: 
        break
