from PIL import Image
import os
import pygame
import sys

'''
Keys

Escape - close program
S - skip image

First click - define top left of new image
Second click - define bottom right of new image
'''

UNPROCESSED = 'unprocessed/'
PROCESSED = 'processed/'
USED = 'used/'
UNUSED = 'unused/'

upImg = os.listdir(UNPROCESSED)

print('{} unprocessed images'.format(len(upImg)))

# setup pygame window
WIDTH = 1200
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode([WIDTH,HEIGHT])

imageLoaded = False
newClick = False

click1 = 'none'
click2 = 'none'

running = True
while running:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_s:
                    imageLoaded = False
                    currentImg.save(UNUSED+currentFile)
                    os.remove(UNPROCESSED+currentFile)
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                newClick = True

        if not imageLoaded:
            if len(upImg) > 0:
                click1 = "none"
                click2 = "none"
                currentFile = upImg[0]
                currentImg = Image.open(UNPROCESSED+currentFile)
                pygameImg = pygame.image.load(UNPROCESSED+currentFile)
                del(upImg[0])
                imgW, imgH = currentImg.size
                imageLoaded = True
                screen.fill((255,255,255))
                topX = WIDTH/2-imgW/2
                topY = HEIGHT/2-imgH/2
                screen.blit(pygameImg, (topX,topY))
            else:
                running = False

        if newClick:
            pygame.draw.circle(screen, (255,105,180), click, 10, 0)
            newClick = False
            if click1 == "none":
                click1 = click
            elif click2 == "none":
                click2 = click

        if click1 != 'none' and click2 != 'none': # crop the image
            x1 = int(click1[0])
            y1 = int(click1[1])
            x2 = int(click2[0])
            y2 = int(click2[1])

            if x1 > x2:
                temp = x1
                x1 = x2
                x2 = temp
            if y1 > y2:
                temp = y1
                y1 = y2
                y2 = temp
            
            x1 = int(x1 - topX)
            y1 = int(y1 - topY)
            x2 = int(x2 - topX)
            y2 = int(y2 - topY)            
            
            if x1 < 0: x1 = 0
            if y1 < 0: y1 = 0
            if x2 > imgW-1: x2 = imgW-1
            if y2 > imgH-1: y2 = imgH-1

            croppedImg = currentImg.crop((x1,y1,x2,y2))

            newImg = croppedImg.resize((64,64), Image.ANTIALIAS)
            newImg.save(PROCESSED+currentFile)

            currentImg.save(USED+currentFile)
            os.remove(UNPROCESSED+currentFile)
                
            click1 = 'none'
            click2 = 'none'

            imageLoaded = False

    except:
        imageLoaded = False
        del(upImg[0])
          
    pygame.display.update()

pygame.display.quit()
pygame.quit()
sys.exit()
