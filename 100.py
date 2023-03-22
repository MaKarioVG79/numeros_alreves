
def createList(n):
    lst = []
    for i in range(n+1):
        lst.append(i)
    return(lst)

alreves = createList(100)

print ("Lista del 0 al 100", alreves)
print(" ")

alreves.reverse()

print(" ")
print ("Lista del 100 al 0", alreves)