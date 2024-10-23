import Test
import numpy as np

def F():        #Green face
    global White, Green, Red, Orange, Yellow
    Green=np.rot90(Green,-1)
    buffer=Yellow[2,:].copy()
    Yellow[2,:]=Red[:,2]
    Red[:,2]=White[0,:]
    White[0,:]=Orange[:,0]
    Orange[:,0] = buffer

def f():        #Green face
    global White, Green, Red, Orange, Yellow
    Green=np.rot90(Green,1)
    buffer=Yellow[2,:].copy()
    Yellow[2,:]=Orange[:,0]
    Orange[:,0]=White[0,:]
    White[0,:]=Red[:,2]
    Red[:,2] = buffer