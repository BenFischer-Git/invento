import csv
import uuid
import sys

def main():
    def getAll():
        with open("data.csv", "r", encoding="utf-8") as dataRead:
            reader = csv.reader(dataRead)
            for line in reader:
                print(line)

    def deleteAll():
        open("data.csv", "w+")

    def addItem(details, box):
        itemId = str(uuid.uuid4())
        with open("data.csv", "a", newline="", encoding="utf-8") as dataAppend:
            writer = csv.writer(dataAppend)
            writer.writerow([box, details, itemId])

    def getItem(details):
        with open("data.csv", "r", encoding="utf-8") as dataRead:
            reader = csv.reader(dataRead, delimiter=",")
            for line in reader:
                if details in dataRead:
                    print(line)

    while True:
        cmd = input().strip()
        parts = cmd.split()

        if parts[0] == "get" and parts[1] == "all" and len(parts) == 2:
            getAll()

        elif parts[0] == "delete" and parts[1] == "all" and len(parts) == 2:
            print(">>>confirm:")
            confirmation = input()
            if confirmation == "confirm":
                deleteAll()
                print("all items deleted")
            else:
                print(">>>wrong confirmation")

        elif parts[0] == "add" and parts[2] == "to" and len(parts) == 4:
            details = parts[1]
            box = parts[3]
            addItem(details, box)
            print(">>>item added")

        elif parts[0] == "get" and len(parts) == 2:
            details = parts[1]
            getItem(details)

        elif cmd == "exit":
            break

        else:
            print(">>>invalid command")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
