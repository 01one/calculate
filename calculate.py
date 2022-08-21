#  Copyright 2022 Mahid
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY
import pygame,sys
from pygame.locals import*
pygame.init()
clock=pygame.time.Clock()
screen_width=800
screen_height=600
white=(255,255,255)
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Calculate")


white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
image=pygame.image.load('background.png')
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)
button_position=[
pygame.Rect(28,230,106,61),
pygame.Rect(148,230,106,61),
pygame.Rect(268,230,106,61), 
pygame.Rect(390,230,106,61),
pygame.Rect(509,230,106,61), 
pygame.Rect(629,230,106,61),
pygame.Rect(42,313,106,61),
pygame.Rect(161,313,106,61),
pygame.Rect(280,313,106,61),
pygame.Rect(399,313,106,61),
pygame.Rect(518,313,106,61),
pygame.Rect(651,313,106,144),
pygame.Rect(26,396,106,61),
pygame.Rect(145,396,106,61),
pygame.Rect(264,396,106,61),
pygame.Rect(383,396,106,61),
pygame.Rect(502,396,106,61),
pygame.Rect(652,484,106,61)]


def hover_effect(place,color,button):
	draw_cover=pygame.draw.rect(place,color,button,5)



def display_text(position_x=78,position_y=65,text='',font_size=40):
	display_font=font=pygame.font.Font('Genos-Bold.ttf',font_size)
	display_text=display_font.render(text,True,white)
	screen.blit(display_text,(position_x+10,position_y+10))

x_i=''
message=''
current_button=''
game_running=True
while game_running:
	clock.tick(25)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
			
		mouse_position=pygame.mouse.get_pos()
		if event.type==pygame.MOUSEMOTION:
			for i in range(len(button_position)):
				if button_position[i].collidepoint(mouse_position):
					current_button=i

		if event.type==pygame.MOUSEBUTTONDOWN:
			for i in range(len(button_position)):
				if button_position[i].collidepoint(mouse_position):
					if event.button==1:
						message=''
						if i==12:
							x_i=''
							
						elif i==17:
							if len(x_i)==1:
								if x_i=='.':
									x_i='0'
									
							if len(x_i)>1:
								z=['+','-','*','/']
								if x_i[-1] in z:
									len_x_i=len(x_i)-1
									x_i=x_i[:len_x_i]
							try:	
								x_i=x_i
								z=['+','-','*','/',]
								n=[]
								le=len(x_i)
								for i in range(le):
									if x_i[i] in z:
										n.append(x_i[i])
								nw=x_i
								l=len(n)
								for i in range(l):
									nw=nw.replace(n[i],'n')          
								new=nw.split('n')
								o=[]
								for item in new:
									o.append(str(item))
								x_i2=o[0]
								for i in range(len(n)):
									x_i2=x_i2+n[i]+o[i+1]
									


								try:
									x_i=str(eval(x_i2))
								except:
									message='Error'
							except:
								pass
						elif i<9:
							i=i+1
							x_i=x_i+str(i)
						elif i==9:
							x_i=x_i+str(0)
						elif i==10:
							if len(x_i)==0:
								x_i=x_i+'-'
							else:
								xii=x_i[::-1]
								operators=["+","-","*","/","."]
								if xii[0] not in operators:
									x_i=x_i+'-'
						elif i==11:
							if len(x_i)==0:
								x_i=x_i
							else:
								xii=x_i[::-1]
								operators=["+","-","*","/","."]
								if xii[0] not in operators:
									x_i=x_i+'+'
						elif i==13:
							x_i=x_i[:-1]
						elif i==14:
							c=x_i.count(".")
							if c<1:
								x_i=x_i+'.'
						elif i==15:
							if len(x_i)==0:
								x_i=x_i
							else:
								xii=x_i[::-1]
								operators=["+","-","*","/","."]
								if xii[0] not in operators:
									x_i=x_i+'/'
						elif i==16:
							if len(x_i)==0:
								x_i=x_i
							else:
								xii=x_i[::-1]
								operators=["+","-","*","/","."]
								if xii[0] not in operators:
									x_i=x_i+'*'

		elif	event.type==pygame.KEYDOWN:
			if	event.key==pygame.K_DELETE:
				current_button=12
				x_i=''
			elif event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
				current_button=17
				if len(x_i)==1:
					if x_i=='.':
						x_i='0'
						
				if len(x_i)>1:
					z=['+','-','*','/']
					if x_i[-1] in z:
						len_x_i=len(x_i)-1
						x_i=x_i[:len_x_i]
				try:	
					x_i=x_i
					z=['+','-','*','/']
					n=[]
					le=len(x_i)
					for i in range(le):
						if x_i[i] in z:
							n.append(x_i[i])
					nw=x_i
					l=len(n)
					for i in range(l):
						nw=nw.replace(n[i],'n')          
					new=nw.split('n')
					o=[]
					for item in new:
						o.append(str(item))
					x_i2=o[0]
					for i in range(len(n)):
						x_i2=x_i2+n[i]+o[i+1]

					try:
						x_i=str(eval(x_i2))
					except:
						message='Error'
				except:
					pass
					
			

			elif event.key==pygame.K_0 or event.key==pygame.K_KP0:
				current_button=9
				x_i=x_i+str(0)
			elif event.key==pygame.K_1 or event.key==pygame.K_KP1:
				current_button=0
				x_i=x_i+str(1)
			elif event.key==pygame.K_2 or event.key==pygame.K_KP2:
				current_button=1
				x_i=x_i+str(2)
			elif event.key==pygame.K_3 or event.key==pygame.K_KP3:
				current_button=2
				x_i=x_i+str(3)
			elif event.key==pygame.K_4 or event.key==pygame.K_KP4:
				current_button=3
				x_i=x_i+str(4)
			elif event.key==pygame.K_5 or event.key==pygame.K_KP5:
				current_button=4
				x_i=x_i+str(5)
			elif event.key==pygame.K_6 or event.key==pygame.K_KP6:
				current_button=5
				x_i=x_i+str(6)
			elif event.key==pygame.K_7 or event.key==pygame.K_KP7:
				current_button=6
				x_i=x_i+str(7)
			elif event.key==pygame.K_8 or event.key==pygame.K_KP8:
				current_button=7
				x_i=x_i+str(8)
			elif event.key==pygame.K_9 or event.key==pygame.K_KP9:
				current_button=8
				x_i=x_i+str(9)
				
				
			elif event.key==pygame.K_MINUS or event.key==pygame.K_KP_MINUS:
				current_button=10
				if len(x_i)==0:
					x_i=x_i+'-'
				else:
					xii=x_i[::-1]
					operators=["+","-","*","/","."]
					if xii[0] not in operators:
						x_i=x_i+'-'
			elif event.key==pygame.K_PLUS or event.key==pygame.K_KP_PLUS:
				current_button=11
				if len(x_i)==0:
					x_i=x_i
				else:
					xii=x_i[::-1]
					operators=["+","-","*","/","."]
					if xii[0] not in operators:
						x_i=x_i+'+'
			elif event.key==pygame.K_BACKSPACE:
				current_button=13
				
				x_i=x_i[:-1]
			elif event.key==pygame.K_PERIOD or event.key==pygame.K_KP_PERIOD:
				current_button=14
				c=x_i.count(".")
				if c<1:
					x_i=x_i+'.'
			elif event.key==pygame.K_SLASH or event.key==pygame.K_KP_DIVIDE:
				current_button=15
				if len(x_i)==0:
					x_i=x_i
				else:
					xii=x_i[::-1]
					operators=["+","-","*","/","."]
					if xii[0] not in operators:
						x_i=x_i+'/'
			elif event.key==pygame.K_ASTERISK or event.key==pygame.K_KP_MULTIPLY:
				current_button=16
				if len(x_i)==0:
					x_i=x_i
				else:
					xii=x_i[::-1]
					operators=["+","-","*","/","."]
					if xii[0] not in operators:
						x_i=x_i+'*'						

	screen.blit(image,(0,0))
	try:
		button_now=int(current_button)
		hover_effect(place=screen,color=(8,149,255,20),button=button_position[button_now])
	except:
		pass
	text=x_i
	text=text.replace('/','÷')
	text=text.replace('*','×')
	text_l=len(text)
	if text_l<28:
		display_text(text=text)
	elif text_l<38:
		display_text(text=text,position_y=50,font_size=30)
	elif text_l<74:
		display_text(text=text[:38],position_y=50,font_size=30)
		display_text(text=text[38:],position_y=70,font_size=30)
	elif text_l<111:
		display_text(text=text[:38],position_y=30,font_size=30)
		display_text(text=text[38:75],position_y=50,font_size=30)
		display_text(text=text[75:],position_y=70,font_size=30)
		
	else:
		display_text(text=text[:38],position_y=30,font_size=30)
		display_text(text=text[38:75],position_y=50,font_size=30)
		display_text(text=text[75:111],position_y=70,font_size=30)
		display_text(text=text[111:],position_y=90,font_size=30)
		
	
	pygame.display.update()
