#FILE HANDLING
#file--> file is a collection of data and information stored in a disk permanently
#file-->1) Text file
        #       -->used to store in the form of characters
        #2) Binary file
        #       -->used to store in the form of byte    
        #       

#Store data:file Handling,Database
#FIle ahandling--> used to perform a function such as create, read, write,open,update,append

'''
syntax
open()
statement operation for file handling
close()
'''
#mode--> purpose of opening file
#X-->create

#Syntax--> f=open("filename",mode="r")

# f=open("A:\\sipalya\\sipalyatraining\\msg.txt",mode="x")

'''# f=open("msg.txt","a")
f=open("msg.txt","r+")
# a=f.readlines()
# print(a)

f.write("\n this is put file okay\n")
f.write("once again praftice")

# print(a)'''

#VARIABLE
f=open("msg.txt","r")
print(f.name)
print(f.buffer)
print(f.mode)
print(f.encoding)
print(f.closed)

#METHODS
f=open("msg.txt","r")
a=f.readable()
b=f.writable()
print(a)
print(b)

#File close
try:
    f=open("msg.txt","r")
    f.write("hello people")
    f.close()
except:
    print("you must write w")
finally:
    f.close()
    print("this is most iunp code")

#with statement
with open("msg.txt","w") as f:
    f.write("welcome to siphalaya")
# print(f.closed)
