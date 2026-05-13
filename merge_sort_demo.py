import merge_sort as ms
import sys
numbers=(int(value) for value in sys.argv[1:])

print("Numbers before sorting:\n",numbers)
ms.divide_array(numbers,0,len(numbers))
print("Numbers before sorting:\n",numbers)

for i in range(len(numbers)):
    print(numbers[i],end=" ")