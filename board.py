import tkinter as tk
from PIL import Image, ImageTk
import random
import time
STEP=10
l = ["backgr.png","bit.png","pin.png" ]
pii=10
bis=1
bbis=pii+1
pines=2
ccounter=0
def move(event):
    global games,bbis,ccounter
    if event.keysym == "Up":
        games.moves(0, -STEP,bbis)
        
    elif event.keysym == "Down":
        games.moves( 0, STEP,bbis)
        
    elif event.keysym == "Left":
        games.moves( -STEP, 0,bbis)
        
    elif event.keysym == "Right":
        games.moves(STEP, 0,bbis)
    elif event.keysym == "space":
        
        games.reportposxy()
    
    t=games.colision(bbis,1,bbis)
    
    if t!=-1:
        ccounter=ccounter+1
        games.scoreplus(100)
        games.moves(int(-(games.w*1.5)),0,t)
        if ccounter==bbis-1:
            print("game over")
#import game_board
class game_board:
    def __init__(self, w, h, colors,labels):
        self.w = w
        self.h = h
        self.colors = colors
        self.labels = labels
        self.root = tk.Tk()
        self.root.title(self.labels)
        self.xy=[]
        self.canvas = tk.Canvas(
            self.root,
            width=self.w,
            height=self.h,
            bg=self.colors,
            highlightthickness=0
        )
        self.canvas.pack()

        self.bitmaps = []
        self.bmp = []   # referência às PhotoImage (IMPORTANTE)
        self.abmp = []
        self.scores=0
        self.posxy=[]
    def score(self,n):
        self.scores=n
        self.labels = "score : " + str(self.scores)
        self.root.title(self.labels)
    def scoreplus(self,n):
        self.scores=self.scores+n
        self.score(self.scores)
    def addbmp(self,x,y,n):
            # desenhar no canvas
            xxyy=[x]+[y]
            self.posxy=self.posxy+[xxyy]
            a=self.canvas.create_image(x, y, image=self.bmp[n], anchor="nw")
            self.abmp.append(a)
    def randoms(self,m,n):
        xxx=self.w//10
        yyy=self.h//10
        for nn in range(m):
            x=int(random.random()*xxx)*10
            y=int(random.random()*yyy)*10
            self.addbmp(x,y,n)
    def loads(self, l: list):
        self.bitmaps = l

        

        for ll in l:
            img = Image.open(ll).convert("RGBA")
            data = img.getdata()
            new_data = []

            for pixel in data:
                # preto puro fica transparente
                if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                    new_data.append((0, 0, 0, 0))
                else:
                    new_data.append(pixel)

            img.putdata(new_data)

            tk_img = ImageTk.PhotoImage(img)
            self.bmp.append(tk_img)  # manter referência
        games.addbmp(0,0,0)
    def setpos(self,x,y,n):
        counter=0
        posxy=[]
        #print("change"+str(x)+" : "+str(y))
        for a in self.posxy:
            if counter==n:
                xxyy=[x]+[y]
                posxy=posxy+[xxyy]
            else:
                posxy=posxy+[a]
            counter=counter+1
        self.posxy=posxy
        
    
    def moves(self,x,y,n):
        self.canvas.move(self.abmp[n], x, y)
        xx=self.posxy[n][0]
        yy=self.posxy[n][1]
        xx=xx+x
        yy=yy+y
        self.setpos(xx,yy,n)
    def keyhandle(self):
        # Capturar teclas
        self.root.bind("<Up>", move)
        self.root.bind("<Down>", move)
        self.root.bind("<Left>", move)
        self.root.bind("<Right>",move)
        self.root.bind("<space>",move)
    def loadmaps(self,s:str):
        h=[]
        xy=[]
        xxyy=[]
        xxx=0
        yyy=0
        counter=0
        f1=open(s,"r")
        ss=f1.read()
        f1.close()
        arr=ss.split("\n")
        for b in arr:
            xxyy=[]
            for c in b:
                d:int=ord(c)-65
                if d<0:
                    u=0
                elif d==0:
                    xxyy=xxyy+[int(0)]
                else:
                    
                    xxyy=xxyy+[int(d)]
                    counter=counter+1
                xxx=xxx+1
            xy=xy+[xxyy]
            yyy=yyy+1
            xxx=0         
        self.xy=xy    
    def setxy(self,xxxx,yyyy,n):
        arrays=self.xy
        xy=[]
        xxyy=[]
        xxx=0
        yyy=0
        counter=0
        for b in arrays:
            xxyy=[]
            for c in b:
            
                if xxxx==xxx and yyyy==yyy:
                    xxyy=xxyy+[n]
                else:
                
                    xxyy=xxyy+[c]
                    counter=counter+1
                xxx=xxx+1
            xy=xy+[xxyy]
            yyy=yyy+1
            xxx=0         
                
        self.xy = xy
    def reportcsv(self):
        arrays=self.xy
        xy=[]
        xxyy=[]
        xxx=0
        yyy=0
        counter=0
        for b in arrays:
            xxyy=[]
            counter=0
            for c in b:
            
                if counter!=0:
                    print(" , ",end="")
                
                
                print(chr((c & 0xff)+65),end="")
                counter=counter+1
                xxx=xxx+1
            print("")
            
            yyy=yyy+1
            xxx=0         
                
        self.xy = xy
    def colision(self,n,n1,n2):
        xx=self.posxy[n][0]
        yy=self.posxy[n][1]
        
        for nn in range(n1,n2):
            #print(nn)
            x=self.posxy[nn][0] 
            y=self.posxy[nn][1]
            if abs(xx-x)<30 and abs(yy-y)<30:
                return nn
        return -1    
    def reportposxy(self):
        print(self.posxy)
    def report(self):
        print(self.xy)
    def starts(self):
        self.keyhandle()
        self.root.mainloop()


# -------------------------------

games = game_board(640, 480, "black","My game")
games.loads(l)
games.randoms(pii,pines)
games.addbmp(0,0,bis)        
games.loadmaps("level.txt")
games.setxy(0,0,255)
games.reportcsv()
games.reportposxy()
games.starts()

