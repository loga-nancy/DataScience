import numpy as np

x=int(input("Enter Rows value:"))
y=int(input("Enter Columns value:"))
z=int(input("Enter input value:"))

def same(x,y,z):
    print(np.full((x,y),z))

same(x,y,z)