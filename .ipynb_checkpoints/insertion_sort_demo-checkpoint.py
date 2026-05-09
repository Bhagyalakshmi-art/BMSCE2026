import insertion_sort as in_so
import sys

numbers=[]
for i in range(1,len(sys.argv)):
    numbers.append(float(sys.argv[i]))
    
print("Numbers before sorting:\n",numbers)
in_so.insertion_sort(numbers)
print("Numbers after sorting:\n",numbers)

for i in range(len(numbers)):
    print('%-4d'%(numbers[i]),end=" ")
