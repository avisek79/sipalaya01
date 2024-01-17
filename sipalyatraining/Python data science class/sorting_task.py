list_1=[1,2,3,4,5,6,7,8,9,10,11,12,13,16,18,24,14,46,33,28,29,22,56,67,45,88]
list_odd=[]
list_even=[]
list_sorted=[]
list_sorted_1=[]
for i in range(len(list_1)):
    # for j in range(i+1, len(list_1)):
        if list_1[i]%2!=0:
            list_odd.append(list_1[i])
# print(list_odd)
list_odd.sort()
# print(list_odd)
list_odd=list_odd[::-1]
list_sorted.append(list_odd)
print(list_sorted)
                   

for j in range(len(list_1)):
      if list_1[j]%2==0:
            list_even.append(list_1[j])
# print(list_even)
list_even.sort()
# print(list_even)
list_even=list_even[::-1]

list_sorted_1.append(list_even)
print(list_sorted_1)

list_concatinated=",".join(map(str,(list_sorted+list_sorted_1)))

print(" ")
print("the final output is",list_concatinated)

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 18, 24, 14, 46, 33, 28, 29, 22, 56, 67, 45, 88]

# list_odd = sorted([x for x in list_1 if x % 2 != 0], reverse=True)
# list_even = sorted([x for x in list_1 if x % 2 == 0], reverse=True)

# list_sorted = [list_odd]
# list_sorted_1 = [list_even]

# list44=list_sorted_1+list_sorted

# print("The final output is:", list44)

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 18, 24, 14, 46, 33, 28, 29, 22, 56, 67, 45, 88]

# list_odd = sorted([x for x in list_1 if x % 2 != 0], reverse=True)
# list_even = sorted([x for x in list_1 if x % 2 == 0], reverse=True)

# list_concatenated = list_odd + list_even

# print("Concatenated list:", list_concatenated)

