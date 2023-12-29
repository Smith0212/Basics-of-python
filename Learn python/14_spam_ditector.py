text=input('Enter the text :\n')
if ("subscibe this" in text):
    spam=True
elif("make a lot of money" in text):
    spam=True
elif("click here" in text):
    spam=True
elif("buy now" in text):
    spam=True
else:
    spam=False

if (spam):
    print('this taxt is spam')
else:
    print('Not spam')
