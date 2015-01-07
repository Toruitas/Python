__author__ = 'Stuart'

def make_file(filename1,filename2):
    with open(filename1,"w") as file: #'a' will create to a new file if it doesn't exist, otherwise will append
    # truncate an existing one
        for i in range(300):
            file.write(str(i)+'\n')
    with open(filename2,"w") as file2:
        string = "a big fat cat writes a string to write a longer string in a different program"
        increment = 0
        while len(string)>0 & increment <10:
            increment +=1
            if len(string) > 10:
                file2.write(string[:10] +'\n')
                string = string[10:]
            else:
                file2.write(string+'\n')
                string = ""
                break

make_file("powershell.txt","poowershell.txt")
print("" == True)
