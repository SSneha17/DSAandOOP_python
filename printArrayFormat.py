def printArray(input):
    l = len(input);
    output = ""
    for i in range(l):
        j=i+1;
        #k = i+2;
        
        if (not input[i].isdigit()):
            print(input[i])
            if(j<l and input[j].isnumeric()):
                if((j+1) <l and input[j+1].isnumeric()):
                    output+=input[i] * (int(input[j])*10 + int(input[j+1]))
                    print (output)
                else:
                    output+= input[i] * int(input[j])
            else:
                output+=input[i]
    print(output)

printArray("a1b5c10")

list = []
list.append(1)
list.append(5)
list.pop()
print(list)









