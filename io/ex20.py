from sys import argv

script, filename = argv


print("Do you want to Erase the file:")
print("If yes hit RETURN else hit CTRL-C")

raw_input(">")

read_f = open(filename, 'r')
temp = read_f.read()
print(temp)
read_f.close()

# filename1 = "test1.txt"
target = open(filename, "w")

line1 =raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Closing the file")
target.close()

target = open(filename, 'r')
# for line in "Hi"
line = target.readline()
while line:
    print(line)
    line = target.readline()

target.close()

