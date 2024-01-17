# #1.Create a list by picking an odd-index items from the first list and even index items from the second in one third list 

first_list=[1,2,0,5,7,3,2,16,34,12,16,13,19,49,29]
second_list=[7,14,18,19,25,23,0,4,5,1]
third_list=[]
a=[third_list.append(i) for i in first_list if i%2!=0]
b=[third_list.append(k) for k in second_list if k%2==0]
print(third_list)

# #2.Get all values from the dictionary and add them to a list but don’t add duplicates

dict1={"name":"Abhishek","age":23,"place":"balkumari","class":"python","course":"data science","coffee":"machiato","phone":"9862410179","permanent address":"Damak","course":"python"}
list1=[]
k=dict1.values()
set_convert=set(k)
# print(set_convert)
print(f"list items is :\n {list(set_convert)}")

#3.Remove duplicates from a list and create a tuple and find the minimum and maximum number
list1=[1,3,4,1,67,87,3,45,65,23,89,9,87,67,65,23,15,12,23,23,12,76,64,89]
set_conv=set(list1)
tup=tuple(set_conv)
print(tup)
print("the minimum value is", min(tup))
print("the maximum value is",max(tup))

