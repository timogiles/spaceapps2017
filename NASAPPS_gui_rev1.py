#im importing all libs from my SOFBOARD sim11
import math 
from time import sleep
import pygame
from pygame.locals import *
import numpy 
from scipy import linspace, polyval, polyfit, sqrt, stats, randn
from scipy.integrate import quad , simps
from random import randint
import os

#pygame initialization-type tasks
pygame.init()
fps = pygame.time.Clock()

#the size of the pygame display window
#Be aware that the origin of the 'image coordinate' system is the top left of the image,
#with x increasing from 0 to 1366 in the rightward direction, and
#y increasing from 0 to 768 in the downward direction.
screenlength = 1366
screenwidth = 768

#we create the primary window object and fill it with white
window = pygame.display.set_mode((screenlength,screenwidth), pygame.FULLSCREEN)

window.fill(pygame.Color(255,255,255))

def Calculate_Sun_p(CellStart,CellStop, \
                  LightingStart, LightingStop, \
                  CoffeeStart, CoffeeStop, \
                  DryerStart,DryerStop, \
                  WasherStart, WasherStop, \
                  FridgeStart, FridgeStop, \
                  LaptopStart, LaptopStop):

    
    
	
    out1 = []
    out1.append([0, 27.3388888888889, 0])
    out1.append([0.0416666666666667, 24.6777777777778, 0])
    out1.append([0.0833333333333333, 22.0166666666667, 0])
    out1.append([0.125, 19.3555555555556, 0])
    out1.append([0.166666666666667, 16.6944444444444, 0])
    out1.append([0.208333333333333, 14.0333333333333, 0])
    out1.append([0.25, 11.3722222222222, 0])
    out1.append([0.291666666666667, 10.2219500964689, 1.34417231869112])
    out1.append([0.333333333333333, 10.1375278343533, 2.63668884899547])
    out1.append([0.375, 11.2442956287472, 3.82787890550506])
    out1.append([0.416666666666667, 13.3951502400114, 4.87196572237531])
    out1.append([0.458333333333333, 16.4028647576648, 5.72882562876454])
    out1.append([0.5, 20.0472836255565, 6.36552997900277])
    out1.append([0.541666666666667, 24.0837830964236, 6.75761058197826])
    out1.append([0.583333333333333, 28.2526719853125, 6.89])
    out1.append([0.625, 32.2891714561797, 6.75761058197826])
    out1.append([0.666666666666667, 35.9335903240713, 6.36552997900277])
    out1.append([0.708333333333333, 38.9413048417248, 5.72882562876454])
    out1.append([0.75, 41.092159452989, 4.87196572237531])
    out1.append([0.791666666666667, 42.1989272473829, 3.82787890550506])
    out1.append([0.833333333333333, 41.8145049852673, 2.63668884899547])
    out1.append([0.875, 37.9375661928473, 1.34417231869113])
    out1.append([0.916666666666667, 34.7164550817362, 8.44127285432039E-16])
    out1.append([0.958333333333333, 32.0553439706251, 0])
    out1.append([1, 29.3942328595139, 0])

    return out1

def Calculate_Sun(BatteryStart,phone_plugin,phone_unplug, \
                  light_plugin,light_unplug, \
                  coffee_plugin,coffee_unplug, \
                  dryer_plugin,dryer_unplug, \
                  washer_plugin,washer_unplug, \
                  fridge_plugin,fridge_unplug, \
                  laptop_plugin,laptop_unplug):
    #kWh usage of each item  
    phone_kwh = .03
    light_kwh = .15
    coffee_kwh = .1667
    dryer_kwh = 2.5
    washer_kwh = 0.3
    fridge_kwh = 1.0667
    laptop_kwh = .06
	
    time = []
    time.append(0)
    time.append(0.0416666666666667)
    time.append(0.0833333333333333)
    time.append(0.125)
    time.append(0.166666666666667)
    time.append(0.208333333333333)
    time.append(0.25)
    time.append(0.291666666666667)
    time.append(0.333333333333333)
    time.append(0.375)
    time.append(0.416666666666667)
    time.append(0.458333333333333)
    time.append(0.5)
    time.append(0.541666666666667)
    time.append(0.583333333333333)
    time.append(0.625)
    time.append(0.666666666666667)
    time.append(0.708333333333333)
    time.append(0.75)
    time.append(0.791666666666667)
    time.append(0.833333333333333)
    time.append(0.875)
    time.append(0.916666666666667)
    time.append(0.958333333333333)
    time.append(1)

    sun = []
    sun.append(0)
    sun.append(0)
    sun.append(0)
    sun.append(0)
    sun.append(0)
    sun.append(0)
    sun.append(0)
    sun.append(1.34417231869112)
    sun.append(2.63668884899547)
    sun.append(3.82787890550506)
    sun.append(4.87196572237531)
    sun.append(5.72882562876454)
    sun.append(6.36552997900277)
    sun.append(6.75761058197826)
    sun.append(6.89)
    sun.append(6.75761058197826)
    sun.append(6.36552997900277)
    sun.append(5.72882562876454)
    sun.append(4.87196572237531)
    sun.append(3.82787890550506)
    sun.append(2.63668884899547)
    sun.append(1.34417231869113)
    sun.append(8.44127285432039E-16)
    sun.append(0)
    sun.append(0)
    
    outval = []
    out1 = BatteryStart
    for i in range(len(sun)):
        out1 += sun[i]
        if (i >= phone_plugin and i < phone_unplug):
            out1 -= phone_kwh
        if (i >= light_plugin and i < light_unplug):
            out1 -= light_kwh
        if (i >= coffee_plugin and i < coffee_unplug):
            out1 -= coffee_kwh
        if (i >= dryer_plugin and i < dryer_unplug):
            out1 -= dryer_kwh
        if (i >= washer_plugin and i < washer_unplug):
            out1 -= washer_kwh
        if (i >= fridge_plugin and i < fridge_unplug):
            out1 -= fridge_kwh
        if (i >= laptop_plugin and i < laptop_unplug):
            out1 -= laptop_kwh
            
        outval.append([time[i],sun[i],out1]) 

    return outval
	
def updateGraph():
    #redraw the graph picture
    window.blit(graph,(250,10))
    #calculate power usage
    retval = Calculate_Sun(50,phone_plugin[1],phone_unplug[1], \
                           light_plugin[1],light_unplug[1], \
                           coffee_plugin[1],coffee_unplug[1], \
                           dryer_plugin[1],dryer_unplug[1], \
                           washer_plugin[1],washer_unplug[1], \
                           fridge_plugin[1],fridge_unplug[1], \
                           laptop_plugin[1],laptop_unplug[1])
    #determine graph scale
    maxnum=0
    for i in range(len(retval)):
        if retval[i][1] > maxnum:
            maxnum = retval[i][1]
        if retval[i][2] > maxnum:
            maxnum = retval[i][2]
    print "Maxnum = " + str(maxnum)
    maxscale = int(maxnum/10+1)*10
    print "Maxscale = " + str(maxscale)
    scalefactor = 455.0/maxscale
    print "ScaleFactor = " + str(scalefactor)
    #write graph scale label
    for i in range(26):
        label = myFont.render(str(i/25.0*maxscale),1,(0,0,0))
        window.blit(label,(285,470-((i*10)*1.82)))
    
    
    print(len(retval))
    for i in range(len(retval)-1):
        pygame.draw.line(window,0xff0000, [(retval[i][0]*1029)+312,481-(retval[i][1]*scalefactor)],[(retval[i+1][0]*1029)+312,481-(retval[i+1][1]*scalefactor)],3)
        pygame.draw.line(window,0x0000ff, [(retval[i][0]*1029)+312,481-(retval[i][2]*scalefactor)],[(retval[i+1][0]*1029)+312,481-(retval[i+1][2]*scalefactor)],3)
        

def ClickToHours(pos):
    #take an X pixel position and snap it to hours on the graph
    #return the new X pixel position and the hours
    new_hours = int((pos-312)/41.16+.5)
    new_pos = int((pos-312)/41.16+.5)*41.16+312
    valid = 1
    retval = [new_pos, new_hours, valid]
    return retval

#we initiate pygame
pygame.font.init()

#LOAD All the words that I display
myFont = pygame.font.SysFont("Times New Roman",20)
#att = myFont.render("oi mate",1,(0,0,0))

#LOAD ALL THE PICTURES THAT I WILL EVER DISPLAY
#absolute filepath to the folder containing all necessary pictures
#picsfilepath = "/home/ttestt/Desktop/NASAPPS/pics/"
dir_path = os.path.dirname(os.path.realpath(__file__))
print dir_path
picsfilepath = dir_path + "/Res/"

BACKGROUND = pygame.image.load(picsfilepath+"backgroundrev1.png").convert_alpha()
graph = pygame.image.load(picsfilepath+"BlankGraph3a.jpg").convert_alpha()
coffee_image = pygame.image.load(picsfilepath+"coffee.png").convert_alpha()
laptop_image = pygame.image.load(picsfilepath+"laptop.png").convert_alpha()
addition_image = pygame.image.load(picsfilepath+"addition.png").convert_alpha()
subtraction_image = pygame.image.load(picsfilepath+"subtraction.png").convert_alpha()
fridge_image = pygame.image.load(picsfilepath+"fridge.png").convert_alpha()
phone_image = pygame.image.load(picsfilepath+"phone.png").convert_alpha()
light_image = pygame.image.load(picsfilepath+"light.png").convert_alpha()
dryer_image = pygame.image.load(picsfilepath+"dryer.png").convert_alpha()
washer_image = pygame.image.load(picsfilepath+"washer.png").convert_alpha()

##initialize element variables##
#[x_pixel,graph_hours,valid]
phone_plugin = [0,0,0]
phone_unplug = [0,0,0]
light_plugin = [0,0,0]
light_unplug = [0,0,0]
coffee_plugin = [0,0,0]
coffee_unplug = [0,0,0]
dryer_plugin = [0,0,0]
dryer_unplug = [0,0,0]
washer_plugin = [0,0,0]
washer_unplug = [0,0,0]
fridge_plugin = [0,0,0]
fridge_unplug = [0,0,0]
laptop_plugin = [0,0,0]
laptop_unplug = [0,0,0]

#origin of the energy vs time graph 
graph_originx,graph_originy = 312,481
#the x pixel location of the 24 hr mark
graph_right = 1341
#the y pixel location of the 250 energy mark
graph_top = 26

#pixels as a function of 
pixels_v_time_m = (graph_right-graph_originx)/(24-0)
pixels_v_time_b = graph_originx

#general purpose counter that lets us get out of loops and stuff
counter = 0

laptop_plugin_image = pygame.image.load(picsfilepath+"LT_ON.PNG").convert_alpha()
laptop_unplug_image = pygame.image.load(picsfilepath+"LT_OFF.PNG").convert_alpha()
coffee_unplug_image = pygame.image.load(picsfilepath+"Coffee_OFF.PNG").convert_alpha()
coffee_plugin_image = pygame.image.load(picsfilepath+"Coffee_ON.PNG").convert_alpha()
fridge_unplug_image = pygame.image.load(picsfilepath+"fridge_off.PNG").convert_alpha()
fridge_plugin_image = pygame.image.load(picsfilepath+"fridge_on.PNG").convert_alpha()
phone_unplug_image = pygame.image.load(picsfilepath+"phone_off.PNG").convert_alpha()
phone_plugin_image = pygame.image.load(picsfilepath+"phone_on.PNG").convert_alpha()
light_unplug_image = pygame.image.load(picsfilepath+"light_off.PNG").convert_alpha()
light_plugin_image = pygame.image.load(picsfilepath+"light_on.PNG").convert_alpha()
dryer_unplug_image = pygame.image.load(picsfilepath+"dryer_off.PNG").convert_alpha()
dryer_plugin_image = pygame.image.load(picsfilepath+"dryer_on.PNG").convert_alpha()
washer_unplug_image = pygame.image.load(picsfilepath+"washer_off.PNG").convert_alpha()
washer_plugin_image = pygame.image.load(picsfilepath+"washer_on.PNG").convert_alpha()



#after loading all these words and images, we 'blit' them
#check the getting started with rasp pi book for what this means
#window.blit(helloworld,(50,50))
#window.blit(att,(500,500))
def RedrawScreen():
    window.blit(BACKGROUND,(0,0))
    window.blit(graph,(250,10))
    
    #draw the washer
    window.blit(washer_image,(68,230))
    window.blit(addition_image,(140,230))
    window.blit(subtraction_image,(5,230))
    
    #draw the dryer
    window.blit(dryer_image,(75,305))
    window.blit(addition_image,(140,305))
    window.blit(subtraction_image,(5,305))
    
    #draw the light
    window.blit(light_image,(75,385))
    window.blit(addition_image,(140,390))
    window.blit(subtraction_image,(5,390))
    
    #draw the phone
    window.blit(phone_image,(70,475))
    window.blit(addition_image,(140,475))
    window.blit(subtraction_image,(5,475))
    
    #draw the fridge 
    window.blit(fridge_image,(70,550))
    window.blit(addition_image,(140,550))
    window.blit(subtraction_image,(5,550))
    
    #draw the cofee
    window.blit(coffee_image,(75,625))
    window.blit(addition_image,(140,625))
    window.blit(subtraction_image,(5,625))
    
    #draw the laptop
    window.blit(laptop_image,(65,700))
    window.blit(addition_image,(140,695))
    window.blit(subtraction_image,(5,695))

    updateGraph()

    if (laptop_plugin[2] == 1):
        window.blit(laptop_plugin_image,(laptop_plugin[0],700))
        window.blit(laptop_unplug_image,(laptop_unplug[0],700))
    if (coffee_plugin[2] == 1):
        window.blit(coffee_plugin_image,(coffee_plugin[0],625))
        window.blit(coffee_unplug_image,(coffee_unplug[0],625))
    if (fridge_plugin[2] == 1):
        window.blit(fridge_plugin_image,(fridge_plugin[0],550))
        window.blit(fridge_unplug_image,(fridge_unplug[0],550))
    if (phone_plugin[2] == 1):
        window.blit(phone_plugin_image,(phone_plugin[0],475))
        window.blit(phone_unplug_image,(phone_unplug[0],475))
    if (light_plugin[2] == 1):
        window.blit(light_plugin_image,(light_plugin[0],385))
        window.blit(light_unplug_image,(light_unplug[0],385))
    if (dryer_plugin[2] == 1):
        window.blit(dryer_plugin_image,(dryer_plugin[0],305))
        window.blit(dryer_unplug_image,(dryer_unplug[0],305))
    if (washer_plugin[2] == 1):
        window.blit(washer_plugin_image,(washer_plugin[0],230))
        window.blit(washer_unplug_image,(washer_unplug[0],230))

RedrawScreen()        

#################
### MAIN LOOP ###
#################

while True:

    for event in pygame.event.get():

        #each time the user moves the mouse, gather its x,y coordinates
        if event.type == MOUSEMOTION:
            mouseX,mouseY = event.pos

        #if the user clicks the left mouse button, record the pixel coordinates on which the click happened    
        if event.type == MOUSEBUTTONDOWN:
            print mouseX,mouseY

            ### QUIT ###
            
            if (mouseX>=1356 and mouseX<=1366 and mouseY>=0 and mouseY<=10):
                quit()

            ### LAPTOP ###

            if (mouseX>=150 and mouseX<=213 and mouseY>=697 and mouseY<=749):
                print "add laptop"

                counter = 0
                while True:
                    
                    for event in pygame.event.get():

                        if event.type == MOUSEMOTION:
                            mouseX,mouseY = event.pos

                        if (event.type == MOUSEBUTTONDOWN and counter==0):
                            mouseX_click1 = mouseX
                            mouseY_click1 = mouseY
                            print mouseX_click1, mouseY_click1
                            counter = counter + 1
                            print "counter:",counter
                            continue

                        if (event.type == MOUSEBUTTONDOWN and counter==1):
                            mouseX_click2 = mouseX
                            mouseY_click2 = mouseY
                            print mouseX_click2, mouseY_click2
                            counter = counter + 1
                            print "counter:",counter
                            break
                        
                    #gets us out of the while
                    if (counter==2):
                        counter = 0
                        break
           
                #the y pixel location of the laptop plugin and unplug
                geny = 700
                laptop_plugin = ClickToHours(mouseX_click1)
                laptop_unplug = ClickToHours(mouseX_click2)
                #window.blit(laptop_plugin_image,(laptop_plugin[0],700))
                #window.blit(laptop_unplug_image,(laptop_unplug[0],700))
                #updateGraph()
                RedrawScreen()

            ### COFFEE ###
            
            if (mouseX>=142 and mouseX<=188 and mouseY>=631 and mouseY<=675):
                print "add coffee"

                counter = 0
                while True:
                    
                    for event in pygame.event.get():

                        if event.type == MOUSEMOTION:
                            mouseX,mouseY = event.pos

                        if (event.type == MOUSEBUTTONDOWN and counter==0):
                            mouseX_click1 = mouseX
                            mouseY_click1 = mouseY
                            print mouseX_click1, mouseY_click1
                            counter = counter + 1
                            print "counter:",counter
                            continue

                        if (event.type == MOUSEBUTTONDOWN and counter==1):
                            mouseX_click2 = mouseX
                            mouseY_click2 = mouseY
                            print mouseX_click2, mouseY_click2
                            counter = counter + 1
                            print "counter:",counter
                            break
                        
                    #gets us out of the while
                    if (counter==2):
                        counter = 0
                        break
                   

                #the y pixel location of the coffee plugin and unplug
                geny = 625
                coffee_plugin = ClickToHours(mouseX_click1)
                coffee_unplug = ClickToHours(mouseX_click2)
                #window.blit(coffee_plugin_image,(coffee_plugin[0],625))
                #window.blit(coffee_unplug_image,(coffee_unplug[0],625))
                #updateGraph()
                RedrawScreen()
                
            ### FRIDGE ###
            
            if (mouseX>=142 and mouseX<=195 and mouseY>=552 and mouseY<=608):
                print "add fridge"

                counter = 0
                while True:
                    
                    for event in pygame.event.get():

                        if event.type == MOUSEMOTION:
                            mouseX,mouseY = event.pos

                        if (event.type == MOUSEBUTTONDOWN and counter==0):
                            mouseX_click1 = mouseX
                            mouseY_click1 = mouseY
                            print mouseX_click1, mouseY_click1
                            counter = counter + 1
                            print "counter:",counter
                            continue

                        if (event.type == MOUSEBUTTONDOWN and counter==1):
                            mouseX_click2 = mouseX
                            mouseY_click2 = mouseY
                            print mouseX_click2, mouseY_click2
                            counter = counter + 1
                            print "counter:",counter
                            break
                        
                    #gets us out of the while
                    if (counter==2):
                        counter = 0
                        break
                   

                #the y pixel location of the coffee plugin and unplug
                geny = 550
                fridge_plugin = ClickToHours(mouseX_click1)
                fridge_unplug = ClickToHours(mouseX_click2)
                #window.blit(fridge_plugin_image,(fridge_plugin[0],550))
                #window.blit(fridge_unplug_image,(fridge_unplug[0],550))
                #updateGraph()
                RedrawScreen()

            ### PHONE ###
            
            if (mouseX>=140 and mouseX<=192 and mouseY>=478 and mouseY<=527):
                print "add phone"

                counter = 0
                while True:
                    
                    for event in pygame.event.get():

                        if event.type == MOUSEMOTION:
                            mouseX,mouseY = event.pos

                        if (event.type == MOUSEBUTTONDOWN and counter==0):
                            mouseX_click1 = mouseX
                            mouseY_click1 = mouseY
                            print mouseX_click1, mouseY_click1
                            counter = counter + 1
                            print "counter:",counter
                            continue

                        if (event.type == MOUSEBUTTONDOWN and counter==1):
                            mouseX_click2 = mouseX
                            mouseY_click2 = mouseY
                            print mouseX_click2, mouseY_click2
                            counter = counter + 1
                            print "counter:",counter
                            break
                        
                    #gets us out of the while
                    if (counter==2):
                        counter = 0
                        break
                   
                #the y pixel location of the coffee plugin and unplug
                geny = 475
                phone_plugin = ClickToHours(mouseX_click1)
                phone_unplug = ClickToHours(mouseX_click2)
                #window.blit(phone_plugin_image,(phone_plugin[0],475))
                #window.blit(phone_unplug_image,(phone_unplug[0],475))
                #updateGraph()
                RedrawScreen()

            ### LIGHT ###
            
            if (mouseX>=141 and mouseX<=195 and mouseY>=392 and mouseY<=446):
                print "add light"

                counter = 0
                while True:
                    
                    for event in pygame.event.get():

                        if event.type == MOUSEMOTION:
                            mouseX,mouseY = event.pos

                        if (event.type == MOUSEBUTTONDOWN and counter==0):
                            mouseX_click1 = mouseX
                            mouseY_click1 = mouseY
                            print mouseX_click1, mouseY_click1
                            counter = counter + 1
                            print "counter:",counter
                            continue

                        if (event.type == MOUSEBUTTONDOWN and counter==1):
                            mouseX_click2 = mouseX
                            mouseY_click2 = mouseY
                            print mouseX_click2, mouseY_click2
                            counter = counter + 1
                            print "counter:",counter
                            break
                        
                    #gets us out of the while
                    if (counter==2):
                        counter = 0
                        break
                   

                #the y pixel location of the coffee plugin and unplug
                geny = 385
                light_plugin = ClickToHours(mouseX_click1)
                light_unplug = ClickToHours(mouseX_click2)
                #window.blit(light_plugin_image,(light_plugin[0],385))
                #window.blit(light_unplug_image,(light_unplug[0],385))
                #updateGraph()
                RedrawScreen()

            ### DRYER ###
            
            if (mouseX>=142 and mouseX<=196 and mouseY>=307 and mouseY<=359):
                print "add dryer"

                counter = 0
                while True:
                    
                    for event in pygame.event.get():

                        if event.type == MOUSEMOTION:
                            mouseX,mouseY = event.pos

                        if (event.type == MOUSEBUTTONDOWN and counter==0):
                            mouseX_click1 = mouseX
                            mouseY_click1 = mouseY
                            print mouseX_click1, mouseY_click1
                            counter = counter + 1
                            print "counter:",counter
                            continue

                        if (event.type == MOUSEBUTTONDOWN and counter==1):
                            mouseX_click2 = mouseX
                            mouseY_click2 = mouseY
                            print mouseX_click2, mouseY_click2
                            counter = counter + 1
                            print "counter:",counter
                            break
                        
                    #gets us out of the while
                    if (counter==2):
                        counter = 0
                        break
                   

                #the y pixel location of the coffee plugin and unplug
                geny = 305
                dryer_plugin = ClickToHours(mouseX_click1)
                dryer_unplug = ClickToHours(mouseX_click2)
                #window.blit(dryer_plugin_image,(dryer_plugin[0],305))
                #window.blit(dryer_unplug_image,(dryer_unplug[0],305))
                #updateGraph()
                RedrawScreen()

            ### WASHER ###
            
            if (mouseX>=141 and mouseX<=193 and mouseY>=234 and mouseY<=282):
                print "add dryer"

                counter = 0
                while True:
                    
                    for event in pygame.event.get():

                        if event.type == MOUSEMOTION:
                            mouseX,mouseY = event.pos

                        if (event.type == MOUSEBUTTONDOWN and counter==0):
                            mouseX_click1 = mouseX
                            mouseY_click1 = mouseY
                            print mouseX_click1, mouseY_click1
                            counter = counter + 1
                            print "counter:",counter
                            continue

                        if (event.type == MOUSEBUTTONDOWN and counter==1):
                            mouseX_click2 = mouseX
                            mouseY_click2 = mouseY
                            print mouseX_click2, mouseY_click2
                            counter = counter + 1
                            print "counter:",counter
                            break
                        
                    #gets us out of the while
                    if (counter==2):
                        counter = 0
                        break
                   

                #the y pixel location of the coffee plugin and unplug
                geny = 230
                washer_plugin = ClickToHours(mouseX_click1)
                washer_unplug = ClickToHours(mouseX_click2)
                #window.blit(washer_plugin_image,(washer_plugin[0],230))
                #window.blit(washer_unplug_image,(washer_unplug[0],230))
                #updateGraph()
                RedrawScreen()
    
    pygame.display.update()

print "End Program"
