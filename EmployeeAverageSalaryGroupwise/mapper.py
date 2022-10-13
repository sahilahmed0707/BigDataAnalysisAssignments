file1 = open("myfile.txt","w")
file = open("employee_data.csv", "r")
dict = {}
for line in file:
    line = line.strip()
    entry = line.split(',')
    if(entry[0]==''):
        continue
    if entry[2] in dict:
        dict[entry[2]].append(entry[6])
    else:
        dict[entry[2]] = list(entry[6]) 
    
for group in dict:
    file1.write(group+"\t")
    for i in dict[group]:
        file1.write(i+",")
    file1.write("\n")

