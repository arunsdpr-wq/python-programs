file=open("prg13.txt","w")

file.write('1st line \n')
file.write('2nd line \n')
file.write('3rd line \n')
file.write('4th line \n')
file.writelines("See you soon! \n Over and out.")

file=open("prg13.txt","r")
# print("Readline :")
# line=file.readline()
# print(line)

# print("Readlines :")
# line=file.readlines()
# for li in line:
#     print(li,end="")

print("Read:")
l=file.read().splitlines();
print(l)
file.close();
