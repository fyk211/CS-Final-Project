import os
global screen
screen=0
global coin
coin=0
path = os.getcwd()+"/"
coin_img=loadImage(path+"coin.png")
global ans_x
global ans_y
global ans_h
global ans_w
ans_x=0
ans_y=0
ans_h=0
ans_w=0
global click
click=0

global life
life=3

class Coin:
    global coin
    def __init__(self): 
           
        image(coin_img, 750, 50, 100, 100)
        fill(255, 215, 0)
        textSize(70)
        textFont(mono)
        text(": "+str(coin),850, 120)
        
class Lives:
    
    def __init__(self,number):
        fill(0)
        textSize(30)
        textFont(mono)
        self.number=number

        text("Lives:"+str(self.number),35,550)
        
        
            
        
class Button:
    global ans_x
    global ans_y
    global ans_h
    global ans_w
    global click
    def __init__(self, txt, x, y, h, w, clr_box, clr_text, font_size=48, ans=0):
        self.txt=txt
        self.x=x
        self.y=y
        self.h=h
        self.w=w
        self.clr_box=clr_box
        self.clr_text=clr_text
        self.font_size=font_size
        self.ans=ans
        self.qsn=0
        
    def display(self):
        global click
        global coin
        fill(self.clr_box[0], self.clr_box[1], self.clr_box[2])
        noStroke()
        rect(self.x,self.y,self.w,self.h,10)
        fill(self.clr_text[0], self.clr_text[1], self.clr_text[2])
        textFont(mono)
        textSize(self.font_size)
        text(self.txt,self.x+20,self.y+70)

        if(mouseX>self.x and mouseX <self.x+self.w and mouseY>self.y and mouseY <self.y+self.h):
                stroke(255,255,0)
                strokeWeight(10)
                fill(self.clr_box[0], self.clr_box[1], self.clr_box[2])
                rect(self.x,self.y,self.w,self.h, 15)
                fill(self.clr_text[0], self.clr_text[1], self.clr_text[2])
                textFont(mono)
                textSize(self.font_size+10)
                text(self.txt,self.x+20,self.y+70)

        if flag==0:
            global screen
            global flag
            global coin
            if(mouseX>self.x and mouseX <self.x+self.w and mouseY>self.y and mouseY <self.y+self.h ):
                stroke(255,20,147)
                strokeWeight(10)
                fill(self.clr_box[0], self.clr_box[1], self.clr_box[2])
                rect(self.x,self.y,self.w,self.h, 15)
                fill(self.clr_text[0], self.clr_text[1], self.clr_text[2])
                textFont(mono)
                textSize(self.font_size+10)
                text(self.txt,self.x+20,self.y+70)
                
                if self.ans==1:
                    screen+=1
                
                    flag=1
                    click=0
                if screen!=1 and self.ans==1:
                    coin+=10    
                    
        if(mouseX>self.x and mouseX <self.x+self.w and mouseY>self.y and mouseY <self.y+self.h and click==1):
            stroke(255,20,147)
            strokeWeight(10)
            fill(self.clr_box[0], self.clr_box[1], self.clr_box[2])
            rect(self.x,self.y,self.w,self.h, 15)
            fill(self.clr_text[0], self.clr_text[1], self.clr_text[2])
            textFont(mono)
            textSize(self.font_size+10)
            text(self.txt,self.x+20,self.y+70)
            global life
            if self.ans==0:
                life-=1
                click=0
                


class Basic:
    def __init__(self):
        self.img = loadImage(path+"onion.jpg")
  
    def display(self):
        image(self.img, 350, -10, 300, 200)
        
    def question(self):
        fill(51, 153, 255)
        textSize(70)
        textFont(mono)
        text("Q1: What is                ?",35,120)


question=0
flag=1

def mousePressed():
    global click
    click=1
    global ans_x
    global ans_y
    global ans_h
    global ans_w
    if(mouseX>ans_x and mouseX <ans_x+ans_w and mouseY>ans_y and mouseY <ans_y+ans_h ):
        global flag
        flag=0
    
    
    
def setup():

    size(1000,600)
    background(240, 255, 240)
    global mono
    mono = loadFont("InkFree-70.vlw")



def draw():
    global screen
    global mono
    global ans_x
    global ans_y
    global ans_h
    global ans_w
    global life
    if screen==0:   #Start Page
        global flag
        fill(175, 100, 220)
        textSize(80)
        textFont(mono)
        text("aN eAsY QuIZz", 220, 250)
        fill(255,255,224)
        noStroke()
        rect(320,350,300,75,20)
        fill(255,105,180)
        textSize(70)
        textFont(mono)
        text("START!!",340,410)
        button_start=Button("START",320, 350, 75, 300 ,[255,255,224], [255, 20, 147],48, 1 )
        ans_x=320
        ans_y=350
        ans_h=75
        ans_w=300
        button_start.display()
        
        
        if flag==0:
            
            '''if(mouseX>320 and mouseX <620 and mouseY>350 and mouseY <425) and screen==0:
                stroke(255,20,147)
                strokeWeight(10)
                rect(320,350,300,75)
                fill(255,20,147)
                textFont(mono)
                text("START!!",340,410)
                screen+=1
                flag=1'''
            

                
    
    
    

    if screen==1:  #1st Question
        background(240, 255, 240)
        ans_x=150
        ans_y=350
        ans_h=100
        ans_w=300
        
        coin1=Coin()
        basic=Basic()
        basic.display()
        basic.question()
        button3=Button("SHALLOTS", 150, 350, 100, 300, [255,222,173], [255,20,147], 43, 1 )
        button3.display()
        button1=Button("     28", 150, 200, 100, 300, [255,222,173], [255,20,147] )
        button1.display()
        button2=Button("CARROT", 550, 200, 100, 300, [255,222,173], [255,20,147] )
        button2.display()
        button4=Button("  3.14", 550, 350, 100, 300, [255,222,173], [255,20,147] )
        button4.display()
        
            
    if screen==2:
        
        background(240, 255, 240)
        text("yay", 100, 200)
        
    if screen!=0:
        gamelife=Lives(life)

    if life==0:
        background(240, 255, 240)
        text("GAME OVER!!", 300, 350)
    
    if screen!=0:
        coin1=Coin()
        global coin
    
            