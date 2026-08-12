import csv 
import uuid

run = True

class invData:
    def __init__(self, name, box, id):
        self.name = name
        self.box = box
        self.id = id
    def getAll(self):
        return [self.box, self.name, str(self.id)]

id = uuid.uuid4()

kabel = invData("kabel", 1, id)

data = kabel.getAll()

while(run):
    inp = input()
    print(inp)

    if inp.split()[0] == "add":
        print("space")
    if inp == "exit":
        run = False



with open("data.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(data)