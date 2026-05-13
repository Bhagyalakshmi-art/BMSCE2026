import parition as pt
import sys

numbers=[int(value) for value in sys.argv[1:]]
# for in range(1,len(sys.argv)):
#     numbers.append(float(sys.argv[i]))
        
print("Numbers before sorting:\n",numbers)
pt.parition_array(numbers,0,len(numbers))
print("Numbers before sorting:\n",numbers)

for i in range(len(numbers)):
    print(numbers[i],end=" ")