import csv 
import uuid

run = True

class invData:
    def __init__(self, name, box, id):
        self.name = name
        self.box = box
        self.id = id
    def getAll(self):
        id = uuid.uuid4()
        return [self.box, self.name, str(self.id)]


kabel = invData("kabel", 1, id)

data = kabel.getAll()

while(run):
    inp = input()
    print(inp)

    if inp.split()[0] == "get" and inp.split()[1] == "all":
        with open("data.csv", "r", encoding="utf-8") as fileRead:
            reader = csv.reader(fileRead)
            for line in reader:
                print(line)

    
    if inp == "exit":
        run = False



with open("data.csv", "a", newline="", encoding="utf-8") as fileAppend:
    writer = csv.writer(file)
    writer.writerow(data)