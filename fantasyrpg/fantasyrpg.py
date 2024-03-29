import pygame as py
import sys

py.init()

width = 800 
height = 600

imageCollection = dict()

screen = py.display.set_mode((width, height))
py.display.set_caption("fantasyrpg")

font = py.font.Font(None, 24)
textColor = (255, 255, 255)

def game():

    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

        # Clear the screen
        screen.fill((0, 0, 0))  # Fill with black



        # Update the display
        py.display.flip()

def actionMenu():
    
    menu = "Action Menu:\n1. Move\n2. Attack\n3. Use \n4. Info\n5. Quit"

    menuChoices = menu.split("\n")

    print(menuChoices)

    yOffset = 0

    for option in menuChoices:
        currOption = font.render(option, False, textColor)
        screen.blit(currOption, (10, yOffset))
        yOffset += currOption.get_height()

    py.display.flip()


def welcomeMessage():
    
    message = "Welcome to fantasyrpg"

    startTime = py.time.get_ticks()

    while py.time.get_ticks() - startTime < 2000:

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

        
        renderedText = font.render(message, False, textColor)
        screen.blit(renderedText, (10, 10))

        py.display.flip()

# Lets the user enter their command into the game
def textInput():

    font = py.font.Font(None, 18)

    inputText = ""
    input_rect = py.Rect(10, (height//3) * 2, width - 20, 20)
    cursor = py.Rect(input_rect.left + len(inputText), input_rect.y, 3, input_rect.height - 8)
    cursor_visible = True
    cursor_timer = 0

    while True:

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            elif event.type == py.KEYDOWN:
                if event.key == py.K_RETURN:
                    return inputText
                elif event.key == py.K_BACKSPACE:
                    inputText = inputText[:-1]
                else:
                    inputText += event.unicode

        screen.fill((0, 0, 0))

        # Render the input text
        rendered_text = font.render(inputText, True, textColor)
        py.draw.rect(screen, textColor, input_rect, 1)
        
        # Update the cursor location
        text_width, _ = font.size(inputText)
        cursor = py.Rect(input_rect.x + text_width + 5, input_rect.y, 3, input_rect.height)

        screen.blit(rendered_text, (input_rect.x + 5, input_rect.y + 4))

       
        # Activates the blinking cursor
        if py.time.get_ticks() - cursor_timer > 500:
            cursor_visible = not cursor_visible
            cursor_timer = py.time.get_ticks()

        if cursor_visible:
            py.draw.rect(screen, textColor, cursor)

        actionMenu()

        py.display.flip()

def main():

    welcomeMessage()

    while True:

        userInput = textInput()


main()
    