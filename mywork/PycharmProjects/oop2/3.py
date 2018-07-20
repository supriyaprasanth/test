try:
    file = open("abc.txt", "r+")
    file.read(print())
    file.write("Hello")
    file.close()

except FileNotFoundError:
    print("The file does  exists")
try:
    file = open("abc1.txt", "r+")
    file.read(print())
    file.write("Hello")
    file.close()

except FileNotFoundError:
    print("The file not exists")

try:
    file = open("abc1.txt", "r")
    file.read(print())
    file.write("Hello")
    file.close()
except:
    print("Wrong Mode")