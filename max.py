x = [3,5,4,6,12,10]
def get_max (x):
    maxi = x[0]
    for i in x:
         if i > maxi:
             maxi = i
    return (maxi)
print (get_max(x))