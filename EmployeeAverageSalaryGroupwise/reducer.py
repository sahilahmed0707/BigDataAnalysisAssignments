file1 = open("myfile.txt", "r")
average = {}
for line in file1:
  line = line.strip()
  key, value = line.split('\t')
  v = value.split(',')
  s=0
  for i in v:
    if i!="":
      s+=int(i)
  average[key] = s/(len(v)-1)
print("Average Salary for each blood group")
print(average)
