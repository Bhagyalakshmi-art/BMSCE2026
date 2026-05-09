input_array=input("Enter the elements in array:").split()
length_array=len(input_array)
for i in range(0,length_array-1):
    for j in range(0,length_array-1-i):
        if input_array[j]>input_array[j+1]:
            input_array[j],input_array[j+1]=input_array[j+1],input_array[j]
print(input_array)            
            
