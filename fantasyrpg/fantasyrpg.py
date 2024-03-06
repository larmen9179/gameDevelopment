import pygame as py
import sys

py.init()

width = 800 
height = 600

imageCollection = dict()

screen = py.display.set_mode((width, height))
py.display.set_caption("fantasyrpg")

font = py.font.Font(None, 24)
text_color = (255, 255, 255)


def game():
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

        # Clear the screen
        screen.fill((0, 0, 0))  # Fill with black

        # Add your drawing or game logic here

        # Update the display
        py.display.flip()

def mainMenu():
    pass

def main():

    while True:

        userInput = text_input()

        print(userInput)


def text_input():
    input_text = ""
    input_rect = py.Rect(10, (height//3) * 2, width - 20, 40)
    cursor = py.Rect(input_rect.left + len(input_text), input_rect.y, 3, input_rect.height - 8)
    cursor_visible = True
    cursor_timer = 0

    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            elif event.type == py.KEYDOWN:
                if event.key == py.K_RETURN:
                    return input_text
                elif event.key == py.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill((0, 0, 0))

        # Render the input text
        rendered_text = font.render(input_text, True, text_color)
        py.draw.rect(screen, text_color, input_rect, 2)
        
        # Update the cursor location
        text_width, _ = font.size(input_text)
        cursor = py.Rect(input_rect.x + text_width + 5, input_rect.y, 3, input_rect.height)

        screen.blit(rendered_text, (input_rect.x + 5, input_rect.y + 11))

       
        # Activates the blinking cursor
        if py.time.get_ticks() - cursor_timer > 500:
            cursor_visible = not cursor_visible
            cursor_timer = py.time.get_ticks()

        if cursor_visible:
            py.draw.rect(screen, text_color, cursor)


        py.display.flip()



main()
    