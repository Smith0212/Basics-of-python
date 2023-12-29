f=open("text.txt","r")
a=f.read()
if "hello" in a :
    print("hello is present in text")
else :
    print("hello is not present in text")
f.close()