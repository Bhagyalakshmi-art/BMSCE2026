#The function will return the index of 1st occurence of the elemnet else -1
def sequentially_search(search_element):
    for i in range(len(elements)):
        if elements[i]==search_element:
            return i
    return -1    


input_size=int(input("Enter size of the list:"))
elements=[]
print(f"Enter the {input_size} elements of the list")
for i in range(input_size):
    element=float(input())
    elements.append(element)
print("User given elements are \n",elements)
search_element=float(input("Enter the element to be searched:"))
search_index=sequentially_search(search_element)
if search_index==-1:
    print(f"The search element {search_element} was not found.")
else:
    print(f"The serach element {search_element} was found at {search_index+1}")    
   