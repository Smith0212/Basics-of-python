#write text in the file 
f=open("text.txt","w")
text=f.write("fuck you bitch!!")
f.close()

#read the content of file
f=open("text.txt","r")
text=f.read()
print(text)
f.close()

#for adding text in file
f=open("text.txt","a")
text=f.write("\n hello motherfucker")
f.close()