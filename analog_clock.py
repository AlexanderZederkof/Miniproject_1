import pygame 
import math
from datetime import datetime

# Screen settings
pygame.init()
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
screen.fill([237, 218, 9])

# Clock colors 
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (237, 218, 9)

# Clock dimensions
clock_size = 400
clock_radius = clock_size / 2  
center = (screen_size[0] / 2, screen_size[1] / 2)

center_image = pygame.image.load('jurassic_park.png')  # Load file from local directory
center_image = pygame.transform.scale(center_image, (380, 380))  # Scale the image 
center_image_rect = center_image.get_rect(center=center)  # Position the image at the center

# Function to draw the clock face
def draw_clock_face():

    # Draw the image at the center of the clock face (note to self, has to be first as it is in the background)
    screen.blit(center_image, center_image_rect)

    # Draw clock border
    pygame.draw.circle(screen, black, center, clock_radius, 10)

    # Hour marks on clock face
    for angle in range(0, 360, 30):
        # Starting offset (adjust fraction to control how much of the middle is empty)
        start_offset = [0.8 * clock_radius * math.cos(math.radians(angle)), 
                        0.8 * clock_radius * math.sin(math.radians(angle))]
        # Ending offset (adjust length to not show in the outer rim (Starwars reference because I am a nerd))
        end_offset = [0.98 * clock_radius * math.cos(math.radians(angle)), 
                      0.98 * clock_radius * math.sin(math.radians(angle))]
        
        # New positions
        new_start_position = (center[0] + start_offset[0], center[1] + start_offset[1])
        end_position = (center[0] + end_offset[0], center[1] + end_offset[1])

        # Draw the hour lines on clock face
        pygame.draw.line(screen, white, new_start_position, end_position, 5)

    # Minute marks on clock face
    for angle in range(0, 360, 6):
        # Starting offset (adjust fraction to control how much of the middle is empty)
        start_offset = [0.9 * clock_radius * math.cos(math.radians(angle)), 
                        0.9 * clock_radius * math.sin(math.radians(angle))]
        # Ending offset (adjust length to not show in the outer rim (Starwars reference because I am a nerd))
        end_offset = [0.98 * clock_radius * math.cos(math.radians(angle)), 
                      0.98 * clock_radius * math.sin(math.radians(angle))]
        
        # New positions
        new_start_position = (center[0] + start_offset[0], center[1] + start_offset[1])
        end_position = (center[0] + end_offset[0], center[1] + end_offset[1])

        # Draw minute marks on clock face
        pygame.draw.line(screen, white, new_start_position, end_position, 2)

 

# Function to draw clock hands
def draw_hand(angle, length, width, color):
    end_x = center[0] + length * math.cos(math.radians(angle))
    end_y = center[1] + length * math.sin(math.radians(angle))
    pygame.draw.line(screen, color, center, (end_x, end_y), width)

    # Draw clock center circle
    pygame.draw.circle(screen, yellow, center, 10)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Initial drawing of the clock face
    draw_clock_face()

    # Get the current time
    now = datetime.now()
    second = now.second
    minute = now.minute
    hour = now.hour

    # Calculations for clock arms (note to self: we use 270 degrees due to the fact that the 3 o clock position is the 0 degrees, as 3 o clock is the standard positon in geometry)
    second_angle = 270 + (second * 6)  # 6 degrees per second
    minute_angle = 270 + (minute * 6) + (second / 60 * 6)  # 6 degrees per minute
    hour_angle = 270 + ((hour % 12 + minute / 60) * 30) # 30 degrees per hour

    draw_hand(hour_angle, clock_radius * 0.5, 8, white)    # Hour hand
    draw_hand(minute_angle, clock_radius * 0.75, 6, white)  # Minute hand
    draw_hand(second_angle, clock_radius * 0.85, 2, yellow)  # Second hand


    pygame.display.flip()