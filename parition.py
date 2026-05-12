def parition_array(numbers,low,high):
       
    pivot=numbers[high] #last element as refrence element
    i=low #to access each element in array
    j=low #to know the index of pivot element

    for i in range(low,high):
        if numbers[i]<pivot:
            numbers[i],numbers[j]=numbers[j],numbers[i]
            j+=1
    numbers[high],numbers[j]=numbers[j],numbers[high]
    return j