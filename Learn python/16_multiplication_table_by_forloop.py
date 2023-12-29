from stringprep import in_table_c5


a=int(input("Enter the number you want multiplication table of :"))
for i in range(1, 11):
    print(f"{a} X {i} = ",a*i)