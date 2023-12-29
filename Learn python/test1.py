# Write a program in python to perform liner search.

def linear_search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            return True
    return False

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 5

if linear_search(list, n):

    print("Found")
else:
    print("Not Found")

    

