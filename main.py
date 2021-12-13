#imports
import pygame
import time
#inits
pygame.init()
#globals
global loop
global cookie
global cookie1
global cookieper
global cookieper1
global a
global uprice1
global uprice12
global uprice2
global uprice22
global uprice3
global uprice32
global check
global tx
global cookieI
global uprice4
global uprice42
global var1
global var2
#variabls
var1 = 2
var2 = 1
font = pygame.font.Font('freesansbold.ttf', 32)
font1 = pygame.font.Font('freesansbold.ttf', 20)
loop = 1
cookie = 0
cookieI = cookie
cookie1 = cookie
cookieper = 1
cookieper1 = cookieper
check = 0
uprice1 = 75
uprice12 = uprice1
uprice2 = 3000
uprice22 = uprice2
uprice3 = 50000
uprice32 = uprice3
uprice4 = 500000
uprice42 = uprice4
#screen stuff
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 256)
green = (0, 256, 0)
surface = pygame.display.set_mode((400, 400))
surface.fill((0, 0, 0))
pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(30, 50, 400, 50))
pygame.display.flip()
pygame.display.update()
tx = 130
ty = 50
font1 = pygame.font.Font('freesansbold.ttf', 14)
#images
mac1 = pygame.image.load(r'macfnew.png').convert_alpha()
surface.blit(mac1, (100, 100))
mac = pygame.image.load(r'macf.png').convert_alpha()
surface.blit(mac, (100, 100))
#save
file1 = open("saveper.txt","r")
saveper = file1.readline()
cookieper = int(saveper) + 0
cookieper1 = cookieper
file1.close
file1 = open("saveco.txt","r")
saveco  = file1.readline()
cookie = int(saveco) + 0
cookieI = cookie
cookie1 = cookie
file1.close
fileu = open('saveu1.txt', 'r')
saveu1 = fileu.readline()
uprice1 = int(saveu1) + 0
uprice12 = uprice1
fileu.close
fileu = open('saveu2.txt', 'r')
saveu2 = fileu.readline()
uprice2 = int(saveu2) + 0
uprice22 = uprice2
fileu.close
fileu = open('saveu3.txt', 'r')
saveu3 = fileu.readline()
uprice3 = int(saveu3) + 0
uprice32 = uprice3
fileu.close
fileu = open('saveu4.txt', 'r')
saveu4 = fileu.readline()
uprice4 = int(saveu4) + 0
uprice42 = uprice4
fileu.close
#where do boxs go?
if cookie >= 100000000:
  tx = 80
if cookie >= 1000000000:
  tx = 60
if cookie >= 10000000000:
  tx = 40
if cookie >= 100000000000:
  tx = 20
if cookie >= 100000000000000:
  tx = 1
if cookie >= 1000000000000000:
  tx = 100
if cookie < uprice1 and cookie < uprice2 and cookie < uprice3 and cookie < uprice4:
  var1 = 2
if cookie > uprice1 or cookie > uprice2 or cookie > uprice3 or cookie > uprice4:
  var1 = 1
#boxs
text = font1.render(str(cookieper) + ' MACPS', True, (255, 255, 255))
textRect = text.get_rect()
surface.blit(text, (155, 30), textRect)
text = font.render(str(cookieI) + ' boxs!!', True, (255, 255, 255))
textRect = text.get_rect()
surface.blit(text, (tx, ty), textRect)
#game-loop
pygame.display.set_caption('mac and clicker  ' + str(cookieI) + ' boxs')
pygame.display.set_icon(mac)
while loop == 1:
  events = pygame.event.get()
  file2 = open('saveco.txt', 'w')
  file2.write(str(cookie))
  file2.close
  file3 = open('saveper.txt', 'w')
  file3.write(str(cookieper))
  file3.close
  file3 = open('saveu1.txt', 'w')
  file3.write(str(uprice1))
  file3.close
  file3 = open('saveu2.txt', 'w')
  file3.write(str(uprice2))
  file3.close
  file3 = open('saveu3.txt', 'w')
  file3.write(str(uprice3))
  file3.close
  file3 = open('saveu4.txt', 'w')
  file3.write(str(uprice4))
  file3.close
  if cookie < 100000000:
    tx = 130
  if cookie >= 100000000:
    tx = 80
  if cookie >= 1000000000:
    tx = 60
  if cookie >= 10000000000:
    tx = 40
  if cookie >= 100000000000:
    tx = 20
  if cookie >= 100000000000000:
    tx = 1
  if cookie >= 1000000000000000:
    tx = 100
  for event in events:  
    if event.type == pygame.MOUSEBUTTONDOWN:
      spot = pygame.mouse.get_pos()
      if spot[0] > 137 and spot[1] > 97 and spot[0] < 251 and spot[1] < 295:
        cookie = cookie1 + int(cookieper)
        cookie1 = cookie
        cookieI = cookie
        if cookie > 999999999999999:
          cookieI = 'infinite'
        if cookie <= 999999999999999:
          cookieI = cookie
        print(str(cookie) + ' boxs')
        pygame.display.set_caption('mac and clicker  ' + str(cookieI) + ' boxs')
        #macps
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 20, 400, 60))
        pygame.display.flip()
        textRect = text.get_rect()
        text = font1.render(str(cookieper) + ' MACPS', True, (255, 255, 255))
        textRect = text.get_rect()
        surface.blit(text, (155, 30), textRect)
        #boxs
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 45, 400, 60))
        pygame.display.flip()
        textRect = text.get_rect()
        text = font.render(str(cookieI) + ' boxs!', True, (255, 255, 255))
        textRect = text.get_rect()
        surface.blit(text, (tx, ty), textRect)
    if event.type == pygame.KEYDOWN:
      #upgrades
      if event.key == pygame.K_r:
        res = input('do you really want to restart type "RESTART" exactly to restart!! -->')
        if res == 'RESTART':
          cookie = 0
          cookie1 = cookie
          cookieper = 1
          cookieper1 = cookieper
          uprice1 = 75
          uprice12 = uprice1
          uprice2 = 3000
          uprice22 = uprice2
          uprice3 = 50000
          uprice32 = uprice3
          uprice4 = 500000
          uprice42 = uprice4
      if event.key == pygame.K_u:
        a = input(' (' + str(uprice1) + ' boxs: 1) for +1 MACPC \n (' + str(uprice2) + ' boxs: 2) for +8 MACPC \n (' + str(uprice3) + ' boxs: 3) for +15 MACPC \n (' + str(uprice4) + ' boxs: 4) for +25 MACPC \n put number directly next to arrow --->')
        #upgrade1
        if a == '1':
          if int(cookie) >= uprice1:
            check = 2
          if int(cookie) < uprice1:
            check = 1
          if check == 2:
            cookieper = cookieper1 + 1
            cookieper1 = cookieper
            cookie = cookie1 - uprice1
            cookie1 = cookie
            uprice1 = uprice12 * 2
            uprice12 = uprice1
            print('New MACPC(mac and cheese per click) ' + str(cookieper) + '!!!')
            print(str(cookie) + ' boxs')
            pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 25, 400, 40))
            pygame.display.flip()
            text = font1.render(str(cookieper) + ' MACPS', True, (255, 255, 255))
            textRect = text.get_rect()
            surface.blit(text, (155, 30), textRect)
          if check == 1:
            print('Sorry cant afford')
          check = 1
        #upgrade2
        if a == '2':
          if int(cookie) > uprice2:
            check = 2
          if int(cookie) < uprice2:
            check = 1
          if check == 2:
            cookieper = cookieper1 + 8
            cookieper1 = cookieper
            cookie = cookie1 - uprice2
            cookie1 = cookie
            uprice2 = uprice22 * 2
            uprice22 = uprice2
            print('New MACPC(Mac and cheese per click) ' + str(cookieper) + '!!!')
            print(str(cookie) + ' boxs')
            pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 25, 400, 40))
            pygame.display.flip()
            text = font1.render(str(cookieper) + ' MACPS', True, (255, 255, 255))
            textRect = text.get_rect()
            surface.blit(text, (155, 30), textRect)
          if check == 1:
            print('Sorry cant afford')
          check = 1
        #upgrade3
        if a == '3':
          if int(cookie) > uprice3:
            check = 2
          if int(cookie) < uprice3:
            check = 1
          if check == 2:
            cookieper = cookieper1 + 15
            cookieper1 = cookieper
            cookie = cookie1 - uprice3
            cookie1 = cookie
            uprice3 = uprice32 * 2
            uprice32 = uprice3
            print('New MACPC(Mac and cheese per click) ' + str(cookieper) + '!!!')
            print(str(cookie) + ' boxs')
            pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 25, 400, 40))
            pygame.display.flip()
            text = font1.render(str(cookieper) + ' MACPS', True, (255, 255, 255))
            textRect = text.get_rect()
            surface.blit(text, (155, 30), textRect)
          if check == 1:
            print('Sorry cant afford')
          check = 1
        #upgrade4
        if a == '4':
          if int(cookie) > uprice4:
            check = 2
          if int(cookie) < uprice4:
            check = 1
          if check == 2:
            cookieper = cookieper1 + 25
            cookieper1 = cookieper
            cookie = cookie1 - uprice4
            cookie1 = cookie
            uprice4 = uprice42 * 2
            uprice42 = uprice4
            print('New MACPC(Mac and cheese per click) ' + str(cookieper) + '!!!')
            print(str(cookie) + ' boxs')
            pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 25, 400, 40))
            pygame.display.flip()
            text = font1.render(str(cookieper) + ' MACPS', True, (255, 255, 255))
            textRect = text.get_rect()
            surface.blit(text, (155, 30), textRect)
          if check == 1:
            print('Sorry cant afford')
          check = 1
        if a == 'Dev-Tools':
          check = 2
          if check == 2:
            print(cookieper)
            cookieper = cookieper1 + 10000000000000
            cookieper1 = cookieper
            print('New MACPC(Mac and cheese per click) ' + str(cookieper) + '!!!')
            print(str(cookie) + ' boxs')
            pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 25, 400, 40))
            pygame.display.flip()
            text = font1.render(str(cookieper) + ' MACPS', True, (255, 255, 255))
            textRect = text.get_rect()
            surface.blit(text, (155, 30), textRect)
          if check == 1:
            print('Sorry cant afford')
          check = 1
    #rectangle
      pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 50, 400, 50))
      pygame.display.flip()
      #can you afford?
      #1
    #text1
    cookieI = cookie
    if cookie > 999999999999999:
        cookieI = 'infinite'
    if cookie <= 999999999999999:
      cookieI = cookie
    if var1 == 1:
      if cookie > uprice1 or cookie > uprice2 or cookie > uprice3 or cookie > uprice4:
        var1 = 2
        print('you have a avalible upgrade!!!!')
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 340, 400, 400))
        pygame.display.flip()
        textRect = text.get_rect()
        text = font1.render('you have a avalible upgrade!!!', True, (255, 255, 255))
        textRect = text.get_rect()
        surface.blit(text, (100, 350), textRect)
    if var1 == 2:
      if cookie < uprice1 and cookie < uprice2 and cookie < uprice3 and cookie < uprice4:
        var1 = 1
        print('you no longer have any upgrades avaliable')
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 340, 400, 400))
        pygame.display.flip()
        textRect = text.get_rect()
        text = font1.render('you have no avalible upgrades', True, (255, 255, 255))
        textRect = text.get_rect()
        surface.blit(text, (100, 350), textRect)

  
  if event.type == pygame.QUIT:
    pygame.quit()
    loop = 2
  mac = pygame.image.load(r'macf.png').convert_alpha()
  time.sleep(.035)
  surface.blit(mac, (100, 100))
  pygame.display.update()
  #this is to round number to 350 lines!!