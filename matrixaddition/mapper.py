file1 = open("myfile.txt","w")
file = open("matrix.txt", "r")
for line in file:
    line = line.strip()
    entry = line.split(',')
    key = entry[0]
    value = line[2:]

    if(key=='a'):
      file1.write(key+"\t" + value)
      file1.write("\n")
    elif(key=='b'):
      file1.write(key+"\t" + value)
      file1.write("\n")
