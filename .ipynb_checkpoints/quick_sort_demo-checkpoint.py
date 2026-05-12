import sys
import quick_sort as qs

numbers=[int(value) for value in sys.argv[1:]]
print("Numbers before sorting:\n",numbers)
qs.quick_sort(numbers,0,len(numbers)-1)
print("Numbers after sorting:\n",numbers)

    