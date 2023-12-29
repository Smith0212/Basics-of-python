words=["motherfucker","fuck","bitch"]
with open("text.txt") as f :
    text = f.read()

for word in words:
    text = text.replace(word,"$@#%#")
    with open("text.txt","w") as f:
        f.write(text)