nums = []

def readFile():
    try:
        file = open("Sample File.txt",'r')
        for i in range(10):
            number = int(file.readline())
            nums.append(number)
        file.close()
    except:
        print("File not found")

def writeFile():
    try:
        file = open("Sample File.txt",'w')
        for i in range(10):
            number = int(input("Gimme a number: "))
            file.write(str(number)+"\n")
        file.close()
    except:
        print("File not found")


def appendFile():
    try:
        file = open("Sample File.txt",'a')
        for i in range(10):
            pass
    except:
        print("File not found")
