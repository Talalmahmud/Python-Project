with open("text1.txt") as file1:
    list1 = file1.readlines()

with open("text2.txt") as file2:
    list2 = file2.readlines()

new_list = [ int(item) for item in list1 if item in list2]
print(new_list)
