file1 = open("myfile.txt", "r")
a = {}
b = {}
for line in file1:
  line = line.strip()
  key, value = line.split('\t')
  v = value.split(',')
  print(v)
  if (key == 'a'):
    a[(int(v[0]), int(v[1]))] = int(v[2])
  elif (key == 'b'):
    b[(int(v[0]), int(v[1]))] = int(v[2])

result = 0
for i in range(0,3):
  for j in range(0,3):
    result = result + a[(i,j)]+b[(i,j)]
    print('({0},{1})\t{2}'.format(i,j,result))
    result = 0
