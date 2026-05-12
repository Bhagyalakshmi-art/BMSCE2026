numbers=list(map(int,input("Enter the numbers:").split()))
for u in range(len(numbers)):
    min_index=u
    for j in range(u+1,len(numbers)):
        if numbers[j]<numbers[min_index]:
            min_index=j
        numbers[u],numbers[min_index]=numbers[min_index],numbers[u]
            
print(numbers)
    
        