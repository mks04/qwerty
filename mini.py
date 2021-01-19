x = [6,5,3,12]
def get_min (x):
    mini = x[0]
    for i in x:
         if i < mini:
             mini = i
    return (mini)
print(get_min (x))
