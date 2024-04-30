# import os
# os.chdir(r'D:\Coding\UpFlairs\Assingenment 3')
file= open('dome.txt','r')
list1= list(file.read().split('\n'))
print(list1)
print(len(list1[0]))
print(len(list1[1]))
print(len(list1[2]))