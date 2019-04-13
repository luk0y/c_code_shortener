mk=""
hello=""
count=0
file1=input("Input the file location : ")#File location of the C source code which needs to be shortened
with open(file1) as data:
    for line in data:
        if(line[:-1] == "#include<stdlib.h>" or line[:-1] == "#include<stdio.h>" or line[:-1] =="#include <stdlib.h>" or line[:-1] =="#include <stdio.h>" or line[:-1] =="#include <string.h>" or line[:-1] == "#include<string.h>" or line[:-1] == "#include<ctype.h>" or line[:-1]=="#include <ctype.h>"):
            hello=hello+line[:-1]+"\n"
        else:
            if(line[0:3]==4*" "):
                line=line[0:3]
            for k in line:
                if(k!=';' and k!='	' and k!='\n'):
                    mk=mk+k
                elif(k==';' and k!='    ' and k!='\n'):
                    mk=mk+';'
mk=hello+mk
print(mk,"\n\nThe Shortened c source code will be saved in 1.c ")
file2 = open("1.c","w")#The shortened c source code will be saved in 1.c
file2.write(mk)
file2.close()
print("\n\n1.c file created\n\n")#Anything which is present in 1.c will be erased and new shortened code will added
