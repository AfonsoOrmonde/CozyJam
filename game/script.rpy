# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# The game starts here.

label start:
    $acucar = 0
    $cafe = 0
    $chantili = 0
    $leite = 0
    $cereja = 0
    $blend_r = 0
    call begin_minigame

    return
