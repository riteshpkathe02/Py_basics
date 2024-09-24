# f = open(r"C:\Users\PC1\Desktop\Python_Basics\funny.txt","r")
# f_out= open(r"C:\Users\PC1\Desktop\Python_Basics\funny_mod.txt","w")
# for line in f:
#     tokens=line.split(' ') #Words are separated by space & that splitted line stored in tokens variable
#     f_out.write("Wordcount: "+str(len(tokens))+'_____'+line)
# f.close()
# f_out.close()

with open(r"C:\Users\PC1\Desktop\Python_Basics\funny.txt","r") as f:
    with open(r"C:\Users\PC1\Desktop\Python_Basics\funny_mod.txt","w") as f_out:
        for line in f:
            tokens=line.split(' ') #Words are separated by space & that splitted line stored in tokens variable
            f_out.write("Wordcount: "+str(len(tokens))+'    '+line)