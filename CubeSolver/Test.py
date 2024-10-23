import numpy as np

"""
  Y
R G O B    
  W

"""

White=np.array([['W', 'W', 'W'],
             ['W', 'W', 'W'],
             ['W', 'W', 'W']])
Red=np.array([['R', 'R', 'R'],
             ['R', 'R', 'R'],
             ['R', 'R', 'R']])
Green=np.array([['G', 'G', 'G'],
             ['G', 'G', 'G'],
             ['G', 'G', 'G']])
Orange=np.array([['O', 'O', 'O'],
             ['O', 'O', 'O'],
             ['O', 'O', 'O']])
Blue=np.array([['B', 'B', 'B'],
             ['B', 'B', 'B'],
             ['B', 'B', 'B']])
Yellow=np.array([['Y', 'Y', 'Y'],
             ['Y', 'Y', 'Y'],
             ['Y', 'Y', 'Y']])

def show():
    print('       ', Yellow[0,:],'\n       ', Yellow[1,:],'\n       ', Yellow[2,:])
    for i in range(3):
        print(Red[i,:], Green[i,:],Orange[i,:],Blue[i,:])
    
    print('       ', White[0,:],'\n       ', White[1,:],'\n       ', White[2,:])


def F():        #Green side
    global White, Green, Red, Orange, Yellow
    Green=np.rot90(Green,-1)
    buffer=Yellow[2,:].copy()
    Yellow[2,:]=Red[:,2][::-1]
    Red[:,2]=White[0,:]
    White[0,:]=Orange[:,0][::-1]
    Orange[:,0] = buffer

def f():
    global White, Green, Red, Orange, Yellow
    Green=np.rot90(Green,1)
    buffer=Yellow[2,:].copy()
    Yellow[2,:]=Orange[:,0]
    Orange[:,0]=White[0,:][::-1]
    White[0,:]=Red[:,2]
    Red[:,2] = buffer[::-1]
    
def B():        #Blue side
    global Blue, Yellow, Orange, White, Red
    Blue=np.rot90(Blue, -1)
    buffer=Yellow[0,:].copy()
    Yellow[0,:]=Orange[:,2]
    Orange[:,2]=White[2,:][::-1]
    White[2,:]=Red[:,0]
    Red[:,0]=buffer[::-1]
    
def b():
    global Blue, Yellow, Orange, White, Red
    Blue=np.rot90(Blue, -1)
    buffer=Yellow[0,:].copy()
    Yellow[0,:]=Red[:,0][::-1]
    Red[:,0]=White[2,:]
    White[2,:]=Orange[:,2][::-1]
    Orange[:,2]=buffer
    
def U():        
    global Yellow, Green, Orange, Blue, Red
    Yellow=np.rot90(Yellow, -1)
    buffer=Green[0,:].copy()
    Green[0,:]=Orange[0,:]
    Orange[0,:]=Blue[0,:]
    Blue[0,:]=Red[0,:]
    Red[0,:]=buffer

def u():        #Yellow side
    global Yellow, Green, Orange, Blue, Red
    Yellow=np.rot90(Yellow, 1)
    buffer=Red[0,:].copy()
    Red[0,:]=Blue[0,:]
    Blue[0,:]=Orange[0,:]
    Orange[0,:]=Green[0,:]
    Green[0,:]=buffer
    
def D():
    global White, Green, Orange, Blue, Red
    White=np.rot90(White, -1)
    buffer=Green[2,:].copy()
    Green[2,:]=Red[2,:]
    Red[2,:]=Blue[2,:]
    Blue[2,:]=Orange[2,:]
    Orange[2,:]=buffer

def d():
    global White, Green, Orange, Blue, Red
    White=np.rot90(White, 1)
    buffer=Green[2,:].copy()
    Green[2,:]=Orange[2,:]
    Orange[2,:]=Blue[2,:]
    Blue[2,:]=Red[2,:]
    Red[2,:]=buffer
    
def L():        #Red side
    global Red, Green, Yellow, Blue, White
    Red=np.rot90(Red, -1)
    buffer=Yellow[:,0].copy()
    Yellow[:,0]=Blue[:,2][::-1]
    Blue[:,2]=White[:,0][::-1]
    White[:,0]=Green[:,0]
    Green[:,0]=buffer
    
def l():        #Red side
    global Red, Green, Yellow, Blue, White
    Red=np.rot90(Red, 1)
    buffer=Yellow[:,0].copy()
    Yellow[:,0]=Green[:,0]
    Green[:,0]=White[:,0]
    White[:,0]=Blue[:,2][::-1]
    Blue[:,2]=buffer[::-1]
    
def R():
    global Orange, Green, Yellow, Blue, White
    Orange=np.rot90(Orange, -1)
    buffer=Green[:,2].copy()
    Green[:,2]=White[:,2]
    White[:,2]=Blue[:,0][::-1]
    Blue[:,0]=Yellow[:,2][::-1]
    Yellow[:,2]=buffer
    
def r():
    global Orange, Green, Yellow, Blue, White
    Orange=np.rot90(Orange, 1)
    buffer=Green[:,2].copy()
    Green[:,2]=Yellow[:,2]
    Yellow[:,2]=Blue[:,0][::-1]
    Blue[:,0]=White[:,2][::-1]
    White[:,2]=buffer

for i in range(6):    
    R()
    U()
    r()
    u()
show()

moves={'R':R, 'r':r, 'L':L, 'l':l, 'U':U, 'u':u, 'D':D, 'd':d, 'F':F, 'f':f, 'B': B, 'b':b}

# steps=input('Enter steps: ')
steps='RUrfRUrurFRRuru'

for i in steps:
    moves[i]()
    
show()