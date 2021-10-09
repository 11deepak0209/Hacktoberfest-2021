print("Enter values for matrix - A")
m = int(input("Number of rows, m = "))
n = int(input("Number of columns, n = "))
array1=[[0 for j in range (0,n)] for i in range(0,m)]

for i in range(0,m):
	for j in range(0,n):
		print("Entry in row:",i+1,"column:",j+1)
		array1[i][j] = int(input())
print("Enter values for matrix - B")
p = int(input("Number of rows, m = "))
q = int(input("Number of columns, n = "))
array2 = [[0 for j in range(0,q)] for i in range(0,p)]

for i in range(0,p):
	for j in range (0,q):
		print("Entry in row:",i+1,"column:",j+1)
		array2[i][j] = int(input())
result=[[0 for j in range(0,q)] for i in range(0,m)]
print("Matrix - A =",array1)
print("Matrix - B =",array2)
if(n!=p):
	print("Cannot multiply the two matrices. Incorrect dimensions.")
	print("Matrix - A * Matrix- B = None")
	exit()
for i in range(0,m):
	for j in range(0,q):
		for k in range(0,n):
			result[i][j] += array1[i][k]*array2[k][j]
print("Matrix - A * Matrix- B =",result)			
		