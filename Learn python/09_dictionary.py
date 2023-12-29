Mydict={
    "pankha" : "fan",
    "khilona": "toy",
    "vastu": "item",
    "chehra": "face"
}
print('Options are :',Mydict.keys())
a=input('enter the hindi word ')
print("the mening of your word is :", Mydict.get(a)) #to avoid the error we using the Mydict.get(a) insted of Mydict[a]