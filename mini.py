x = [6,5,3,12]
def fun ():
    mini = x[0]
    for i in x:
         if i < mini:
             mini = i
    print(mini)
fun ()
