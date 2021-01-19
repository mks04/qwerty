x = [3,5,4,6,12,10]
def fun ():
    maxi = x[0]
    for i in x:
         if i > maxi:
             maxi = i
    print(maxi)
fun ()