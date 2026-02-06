import tkinter as tk
from PIL import Image, ImageTk
STEP=10
def move(event):
    global games
    if event.keysym == "Up":
        games.moves(0, -STEP,bis)
        
    elif event.keysym == "Down":
        games.moves( 0, STEP,bis)
        
    elif event.keysym == "Left":
        games.moves( -STEP, 0,bis)
        
    elif event.keysym == "Right":
        games.moves(STEP, 0,bis)
        




class game_board:
    def __init__(self, w, h, colors,labels):
        self.w = w
        self.h = h
        self.colors = colors
        self.labels = labels
        self.root = tk.Tk()
        self.root.title(self.labels)

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

            
    def addbmp(self,x,y,n):
            # desenhar no canvas
            a=self.canvas.create_image(x, y, image=self.bmp[n], anchor="nw")
            self.abmp.append(a)
    
    def moves(self,x,y,n):
        self.canvas.move(self.abmp[n], x, y)
    def keyhandle(self):
        # Capturar teclas
        self.root.bind("<Up>", move)
        self.root.bind("<Down>", move)
        self.root.bind("<Left>", move)
        self.root.bind("<Right>",move)
    def starts(self):
        self.keyhandle()
        self.root.mainloop()


# -------------------------------
l = ["pin.png", "bit.png"]
bis=0
bbis=1
pines=0
games = game_board(640, 480, "black","My game")
games.loads(l)
games.addbmp(0,0,bbis)
for n in range(10):
    games.addbmp(n*40,80,pines)
        

games.starts()

