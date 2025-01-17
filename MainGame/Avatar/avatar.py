from email.policy import default
from os import environ
from turtle import Screen
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

pygame.init()

# Scale variables
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
AVATAR_SIZE = 100, 100

#HOME_CAPTION = "Arcade Menu"

global quit_avatar
global current_avatar
global tickets

# Starter tickets
tickets = 100

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
font = pygame.font.SysFont('monospace', 40)

# Open image files and scale to size
default_avatar = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/defaultAvatar.png'), (AVATAR_SIZE))
avatar1 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar1.png'), (AVATAR_SIZE))
avatar2 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar2.png'), (AVATAR_SIZE))
avatar3 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar3.png'), (AVATAR_SIZE))
avatar4 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar4.png'), (AVATAR_SIZE))
avatar5 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar5.png'), (AVATAR_SIZE))
avatar6 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar6.png'), (AVATAR_SIZE))
avatar7 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar5.png'), (AVATAR_SIZE))
avatar8 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar3.png'), (AVATAR_SIZE))
arrow = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/arrow.png'), (AVATAR_SIZE))
lock = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/lock.png'), (AVATAR_SIZE))
back = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/back.png'), (150, 80))

current_avatar = default_avatar

class AvatarSelect:

    def __init__(self, width = WINDOW_WIDTH, height = WINDOW_HEIGHT):
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
    
    def get_current_avatar(self):
        global current_avatar
        return current_avatar
    
    def get_tickets(self):
        global tickets
        return tickets
 
    def start_selection(self):
        from main_menu import ScreenItem
        pygame.display.set_caption("Avatar Select")
        global current_avatar
        global quit_avatar
        global tickets
        print (tickets)
        break_loops = False

        current_avatar = default_avatar
        temp_avatar = current_avatar
        avatar_1_redeemed = False
        avatar_2_redeemed = False
        temp_avatar_hide = True
        quit_avatar = False

        while quit_avatar == False and break_loops == False:

            # Handling user behaviour and interactions
            for event in pygame.event.get():
                # Quits avatar select
                if event.type == pygame.QUIT:
                    quit_avatar = True
                    break_loops = True
                    pygame.display.set_caption('Arcade Menu')

                # Looks for user clicking on different avatars
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if avatar_1_button.mouse_over_button(pygame.mouse.get_pos()):
                        if avatar_1_redeemed == True:
                            current_avatar = avatar1
                        elif avatar_1_redeemed == False:
                            if tickets >= 50:
                                avatar_1_redeemed = True
                                tickets = tickets - 50
                                current_avatar = avatar1
                        else:
                            print ("Insufficient tickets")
                    elif avatar_2_button.mouse_over_button(pygame.mouse.get_pos()):
                        if avatar_2_redeemed == True:
                            current_avatar = avatar2
                        elif avatar_2_redeemed == False:
                            if tickets >= 50:
                                avatar_2_redeemed = True
                                tickets = tickets - 50
                                current_avatar = avatar2
                        else:
                            print ("Insufficient tickets")
                    elif avatar_3_button.mouse_over_button(pygame.mouse.get_pos()):
                        current_avatar = avatar3
                    elif avatar_4_button.mouse_over_button(pygame.mouse.get_pos()):
                        current_avatar = avatar4
                    elif avatar_5_button.mouse_over_button(pygame.mouse.get_pos()):
                        current_avatar = avatar5
                    elif avatar_6_button.mouse_over_button(pygame.mouse.get_pos()):
                        current_avatar = avatar6
                    elif avatar_7_button.mouse_over_button(pygame.mouse.get_pos()):
                        current_avatar = avatar7
                    elif avatar_8_button.mouse_over_button(pygame.mouse.get_pos()):
                        current_avatar = default_avatar
                    # Back button clicked
                    elif return_button.mouse_over_button(pygame.mouse.get_pos()):
                        quit_avatar = True
                        break_loops = True
                        pygame.display.set_caption('Arcade Menu')

                # Looks for user hovering on different avatars
                if event.type == pygame.MOUSEMOTION:
                    if avatar_1_button.mouse_over_button(pygame.mouse.get_pos()):
                        if avatar_1_redeemed == True:
                            temp_avatar = avatar1
                            temp_avatar_hide = False
                        else:
                            temp_avatar = lock
                            temp_avatar_hide = False
                    elif avatar_2_button.mouse_over_button(pygame.mouse.get_pos()):
                        if avatar_2_redeemed == True:
                            temp_avatar = avatar2
                            temp_avatar_hide = False
                        else:
                            temp_avatar = lock
                            temp_avatar_hide = False
                    elif avatar_3_button.mouse_over_button(pygame.mouse.get_pos()):
                        temp_avatar = avatar3
                        temp_avatar_hide = False
                    elif avatar_4_button.mouse_over_button(pygame.mouse.get_pos()):
                        temp_avatar = avatar4
                        temp_avatar_hide = False
                    elif avatar_5_button.mouse_over_button(pygame.mouse.get_pos()):
                        temp_avatar = avatar5
                        temp_avatar_hide = False
                    elif avatar_6_button.mouse_over_button(pygame.mouse.get_pos()):
                        temp_avatar = avatar6
                        temp_avatar_hide = False
                    elif avatar_7_button.mouse_over_button(pygame.mouse.get_pos()):
                        temp_avatar = avatar7
                        temp_avatar_hide = False
                    elif avatar_8_button.mouse_over_button(pygame.mouse.get_pos()):
                        temp_avatar = default_avatar
                        temp_avatar_hide = False
                    else:
                        temp_avatar_hide = True

            self.display.fill('black')

            # Set positions for images
            current_avatar_display = ScreenItem(WINDOW_WIDTH/2-100, 80, current_avatar)
            avatar_1_button = ScreenItem(100,350,avatar1)
            avatar_2_button = ScreenItem(250,350,avatar2)
            avatar_3_button = ScreenItem(400,350,avatar3)
            avatar_4_button = ScreenItem(550,350,avatar4)
            avatar_5_button = ScreenItem(700,350,avatar5)
            avatar_6_button = ScreenItem(850,350,avatar6)
            avatar_7_button = ScreenItem(1000,350,avatar7)
            avatar_8_button = ScreenItem(1150,350,default_avatar)
            temp_avatar_button = ScreenItem(WINDOW_WIDTH/2+100, 80, temp_avatar)
            window.blit(arrow, (WINDOW_WIDTH/2-50, 100))
            return_button = ScreenItem(1100, 80, back)

            # Display images on screen
            current_avatar_display.update()
            avatar_1_button.update()
            avatar_2_button.update()
            avatar_3_button.update()
            avatar_4_button.update()
            avatar_5_button.update()
            avatar_6_button.update()
            avatar_7_button.update()
            avatar_8_button.update()
            return_button.update()

            # Display text
            message = font.render("Choose your avatar! Locked avatars cost 50 tickets.", True, 'white')
            ticket_display = font.render("Tickets:" + str(tickets), True, 'white')
            message_obj = ScreenItem(WINDOW_WIDTH/2, 500, message)
            ticket_display_obj = ScreenItem(WINDOW_WIDTH/2, 550, ticket_display)
            message_obj.update()
            ticket_display_obj.update()

            if temp_avatar_hide == False:
                temp_avatar_button.update()

            pygame.display.update()
        
        # Return to main menu
        while quit_avatar == True and break_loops == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_avatar = True
                    break_loops = True
                    pygame.display.set_caption('Arcade Menu')
                    
            self.display.fill('black')
            pygame.display.update()

        

