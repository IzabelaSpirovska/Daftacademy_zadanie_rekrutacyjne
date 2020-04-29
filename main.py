file = open(''path/to/file.txt'','r').read()
print(file)
 
table = file.split('\n')
rdy_table = []
 
for lines in table:
    rdy_table.append(lines.strip().split())
 
result = int(rdy_table[0][0])
path = rdy_table[0][0]
 
n = 0
m = 2
 
for i in range(1,len(rdy_table)):
    oryginal_table = rdy_table[i]
    loop_table = rdy_table[i][n:m]
    sorted_table = sorted(loop_table)
    smallest_element = sorted_table[0]
   
    if int(loop_table[0]) < int(loop_table[1]):
        n = n
        m = m
    else:
        n += 1
        m += 1
       
    path += sorted_table[0]
    result += int(sorted_table[0])
 
print(path)
print(result)
