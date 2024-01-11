# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Elysia", color="#4f20a6")
define me = Character("Me", color="#31bae8")
define bc = Character("Demon Lord", color="#ff0000")

bg background
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg background

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mc happy
    show me happy

    # These display lines of dialogue.

    "Hi, im the narrator"
    
    mc "Im Elysia"

    me "And im you"

    bc "And im the demon lord "
    bc  "MUUH HAA HAAA HAAAAH"

    show me green scared

    bc "fear me"


    # This ends the game.

    return
