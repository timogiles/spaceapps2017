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

print "Hello World"


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


def Calculate_Sun(CellStart,CellStop, \
	LightingStart, LightingStop, \
	CoffeeStart, CoffeeStop, \
	DryerStart,DryerStop, \
	WasherSart, WasherStop, \
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
	
def updateGraph():
    #global window
    retval = Calculate_Sun(0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    #pygame.draw.line(window, 0x00ff00, [312,481], [1341,26], 3)
    print(len(retval))
    for i in range(len(retval)-1):
        pygame.draw.line(window,0xff0000, [(retval[i][0]*1029)+312,481-(retval[i][1]*1.82)],[(retval[i+1][0]*1029)+312,481-(retval[i+1][1]*1.82)],3)
        pygame.draw.line(window,0x0000ff, [(retval[i][0]*1029)+312,481-(retval[i][2]*1.82)],[(retval[i+1][0]*1029)+312,481-(retval[i+1][2]*1.82)],3)






#we initiate pygame
pygame.font.init()

#LOAD All the words that I display
myFont = pygame.font.SysFont("Times New Roman",23)
#att = myFont.render("oi mate",1,(0,0,0))

#LOAD ALL THE PICTURES THAT I WILL EVER DISPLAY

#absolute filepath to the folder containing all necessary pictures
dir_path = os.path.dirname(os.path.realpath(__file__))
print dir_path
picsfilepath = dir_path + "/Res/"
#helloworld = pygame.image.load(picsfilepath+"test1.PNG").convert_alpha()

BACKGROUND = pygame.image.load(picsfilepath+"backgroundrev1.png").convert_alpha()
graph = pygame.image.load(picsfilepath+"BlankGraph3.jpg").convert_alpha()
coffee_image = pygame.image.load(picsfilepath+"coffee.png").convert_alpha()
laptop_image = pygame.image.load(picsfilepath+"laptop.png").convert_alpha()
addition_image = pygame.image.load(picsfilepath+"addition.png").convert_alpha()
subtraction_image = pygame.image.load(picsfilepath+"subtraction.png").convert_alpha()

#origin of the energy vs time graph 
graph_originx,graph_originy = 312,481
#the x pixel location of the 24 hr mark
graph_right = 1341
#the y pixel location of the 250 energy mark
graph_top = 26

#we have two arrays that will hold the x and y slider positions of the LT sliders
#when a certain LTslider is not in use, it will be sent to position: x=2000 y=2000, which is off of the screen,
# so that the user cannot see it. 2000 was an arbitrarily chosen number. e.g. we could send
#sliders that are not in use to x=3000 y=3000 if we wanted to
#we also have a counter that keeps track of how many laptops are being 'used' during the day
LT_SLIDERX_ON = [2000,2000,2000,2000,2000,2000]
LT_SLIDERX_OFF = [2000,2000,2000,2000,2000,2000]
LT_SLIDERY = [2000,2000,2000,2000,2000,2000]
LT_COUNTER = 0

print "initial LTsliders:",LT_SLIDERX_ON,LT_SLIDERX_OFF,LT_SLIDERY

lt_slider1_ON_image = pygame.image.load(picsfilepath+"LT_1_ON.PNG").convert_alpha()
lt_slider1_OFF_image = pygame.image.load(picsfilepath+"LT_1_OFF.PNG").convert_alpha()
window.blit(lt_slider1_ON_image,(2000,2000))
window.blit(lt_slider1_OFF_image,(2000,2000))

#after loading all these words and images, we 'blit' them
#check the getting started with rasp pi book for what this means
#window.blit(helloworld,(50,50))
#window.blit(att,(500,500))
window.blit(BACKGROUND,(0,0))
window.blit(graph,(250,10))

window.blit(coffee_image,(75,625))
window.blit(addition_image,(140,625))
window.blit(subtraction_image,(5,625))

window.blit(laptop_image,(65,700))
window.blit(addition_image,(140,695))
window.blit(subtraction_image,(5,695))

while True:

    for event in pygame.event.get():

        #each time the user moves the mouse, gather its x,y coordinates
        if event.type == MOUSEMOTION:
            mouseX,mouseY = event.pos

        #if the user clicks the left mouse button, record the pixel coordinates on which the click happened    
        if event.type == MOUSEBUTTONDOWN:
            print mouseX,mouseY

            if (mouseX>=1356 and mouseX<=1366 and mouseY>=0 and mouseY<=10):
                quit()
			
            if (mouseX>=150 and mouseX<=213 and mouseY>=697 and mouseY<=749):
                print "add laptop"
                #We cant have more than 6 LTs
                if (LT_COUNTER<6): 
                    LT_COUNTER = LT_COUNTER + 1
                    #when the user creates a new laptop usage, we randomly place its starting and ending
                    #times
                    genx_i = randint(graph_originx,graph_originx+500)
                    genx_f = randint(graph_originx+500,graph_right-1)
                    geny = 700

                    #which LT slider do we need to display? LT1, LT2, LT3...?

                    if (LT_COUNTER==1):
                        LT_SLIDERX_ON[LT_COUNTER-1] = genx_i
                        LT_SLIDERX_OFF[LT_COUNTER-1] = genx_f
                        LT_SLIDERY[LT_COUNTER-1] = geny
                        print LT_SLIDERX_ON,LT_SLIDERX_OFF,LT_SLIDERY
                        window.blit(lt_slider1_ON_image,(genx_i,geny))
                        window.blit(lt_slider1_OFF_image,(genx_f,geny))

                
                    #print LT_SLIDERX
                    #print LT_SLIDERY
                    #window.blit(lt_slider1_ON_image,(500,700))
            if (mouseX>=10 and mouseX<=54 and mouseY>=699 and mouseY<=741):
                print "subtract laptop"
                #we cant subtract an LT if we dont currently have any
                if (LT_COUNTER>0):
                    LT_COUNTER = LT_COUNTER - 1

                    if (LT_COUNTER==0):
                        LT_SLIDERX_ON[LT_COUNTER] = 2000
                        LT_SLIDERX_OFF[LT_COUNTER] = 2000
                        LT_SLIDERY[LT_COUNTER] = 2000
                        window.blit(lt_slider1_ON_image,(2000,2000))
                        window.blit(lt_slider1_OFF_image,(2000,2000))
                        print LT_SLIDERX_ON,LT_SLIDERX_OFF,LT_SLIDERY

            if (mouseX>=142 and mouseX<=188 and mouseY>=631 and mouseY<=675):
                print "add coffee"
                updateGraph()
            if (mouseX>=12 and mouseX<=51 and mouseY>=631 and mouseY<=672):
                print "subtract coffee"
			
    
    pygame.display.update()

print "End Program"
