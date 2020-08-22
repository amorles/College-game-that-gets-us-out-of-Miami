# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define cas = Character("Castor")
define sis = Character("Little Sister")
define p = Character("Joe Smo")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene fgo room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show castor

    # These display lines of dialogue.

    cas "Hmph, you dare to stand in front of me?"

    cas "I have a hot sister. Test"

    cas "Second test."

    cas "Thirs test. My twin is still hot."

label hotsisterscene:

    scene bedroom

    "'Stupid brother!'"

    "Oh boy. Here she is again."

    show sister

    sis "B-baka! Why did you have my underwear?!?!"

    jump ch1
