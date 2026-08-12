import csv 
import uuid

with open("data.csv", "r", encoding="utf-8") as fileRead:
    reader = csv.reader(fileRead)

with open("data.csv", "a", newline="", encoding="utf-8") as fileAppend:
    writer = csv.writer(fileAppend)

while(1):
    cmd = input()
  
    if cmd.split()[0] == "get" and cmd.split()[1] == "all":
        for line in reader:
            print(line)

    elif cmd.split()[0] == "add" and cmd.split()[2] == "to":

        details = cmd.split()[1]
        box = cmd.split()[3]
        id = uuid.uuid4()
        writer.writerow([box, details, id])
         
    elif cmd == "exit":
        break
    else:
        print("invalid command")