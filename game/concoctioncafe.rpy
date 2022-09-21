label begin_minigame:
    scene black
    $coffee = 0
    $sugar = 0
    $chantilly = 0
    $cherry = 0
    $cinammon = 0
    $chocolate = 0
    $marshmallow = 0
    $milk = 0

    $completed = 0

    $ coffee_none_idle = "coffee_1_idle.png"
    $ coffee_1_idle = "coffee_1_idle.png"
    $ coffee_2_idle = "coffee_2_idle.png"
    $ coffee_3_idle = "coffee_3_idle.png"
    $ sugar_none_idle = "coffee_1_idle.png"
    $ sugar_1_idle = "sugar_1_idle.png"
    $ sugar_2_idle = "sugar_2_idle.png"
    $ sugar_3_idle = "sugar_3_idle.png"
    $ milk_none_idle = "milk_none_idle.png"
    $ milk_idle = "milk_idle.png"
    $ chocolate_none_idle = "chocolate_none_idle.png"
    $ chocolate_idle = "chocolate_idle.png"
    $ cinnamon_idle = "cinnamon_idle.png"
    $ chantilly_idle = "chantilly_idle.png"
    $ marshmallow_idle = "marshmallow_idle.png"
    $ cherry_idle = "coffee_1_idle.png"
    $ no_toppings_idle = "coffee_1_idle.png"

    $ coffee_none_hover = "coffee_1_hover.png"
    $ coffee_1_hover = "coffee_1_hover.png"
    $ coffee_2_hover= "coffee_2_hover.png"
    $ coffee_3_hover = "coffee_3_hover.png"
    $ sugar_none_hover = "coffee_1_hover.png"
    $ sugar_1_hover = "sugar_1_hover.png"
    $ sugar_2_hover = "sugar_2_hover.png"
    $ sugar_3_hover = "sugar_3_hover.png"
    $ milk_none_hover = "milk_none_hover.png"
    $ milk_hover = "milk_hover.png"
    $ chocolate_none_hover = "chocolate_none_hover.png"
    $ chocolate_hover = "chocolate_hover.png"
    $ cinnamon_hover = "cinnamon_hover.png"
    $ chantilly_hover = "chantilly_hover.png"
    $ marshmallow_hover = "marshmallow_hover.png"
    $ cherry_hover = "coffee_1_hover.png"
    $ no_toppings_hover = "coffee_1_hover.png"

    call screen cafe_escolha
    call screen acucar_escolha
    call screen leite_escolha
    call screen chocolate_escolha
    call screen additionals

    return

screen cafe_escolha:

    imagebutton:
        xanchor 0
        yanchor 0
        xpos 180
        ypos -240
        idle coffee_none_idle
        hover coffee_none_hover
        focus_mask True
        action [SetVariable("coffee", coffee+0), Return()]

    imagebutton:
        xanchor -2
        yanchor 0.5
        xpos 0.30
        ypos 0.28
        idle coffee_1_idle
        hover coffee_1_hover
        focus_mask True
        action [SetVariable("coffee", coffee+1), Return()]

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 1680
        ypos 0.28
        idle coffee_2_idle
        hover coffee_2_hover
        focus_mask True
        action [SetVariable("coffee", coffee+2), Return()]

    imagebutton:
        xanchor 0
        yanchor 0.5
        xpos 885
        ypos 0.28
        idle coffee_3_idle
        hover coffee_3_hover
        focus_mask True
        action [SetVariable("coffee", coffee+3), Return()]

screen acucar_escolha:

    imagebutton:
        xanchor 0
        yanchor 0.5
        xpos 200
        ypos 0.28
        idle sugar_none_idle
        hover sugar_none_hover
        focus_mask True
        action [SetVariable("sugar", sugar+0),  Return()]

    imagebutton:
        xanchor 0
        yanchor 0
        xpos 560
        ypos 30
        idle sugar_1_idle
        hover sugar_1_hover
        focus_mask True
        action [SetVariable("sugar", sugar+1),  Return()]

    imagebutton:
        xanchor 0
        yanchor 0.5
        xpos 820
        ypos 600
        idle sugar_2_idle
        hover sugar_2_hover
        focus_mask True
        action [SetVariable("sugar", sugar+2),  Return()]

    imagebutton:
        xanchor 0
        yanchor 0
        xpos 1000
        ypos 70
        idle sugar_3_idle
        hover sugar_3_hover
        focus_mask True
        action [SetVariable("sugar", sugar+3), Return()]

screen leite_escolha:

        imagebutton:
            xanchor 0
            yanchor 0.5
            xpos 1000
            ypos 50
            idle milk_idle
            hover milk_hover
            focus_mask True
            action [SetVariable("milk", milk+1),  Return()]

        imagebutton:
            xanchor 0
            yanchor 0
            xpos 200
            ypos -500
            idle milk_none_idle
            hover milk_none_hover
            focus_mask True
            action [SetVariable("milk", milk+0),  Return()]

screen chocolate_escolha:

        imagebutton:
            xanchor 0
            yanchor 0.5
            xpos 300
            ypos 30
            idle chocolate_idle
            hover chocolate_hover
            focus_mask True
            action [SetVariable("chocolate", chocolate+1),  Return()]

        imagebutton:
            xanchor 0
            yanchor 0
            xpos -450
            ypos -515
            idle chocolate_none_idle
            hover chocolate_none_hover
            focus_mask True
            action [SetVariable("chocolate", chocolate+0),  Return()]

screen additionals:

    imagebutton:
        xanchor 0
        yanchor 0.5
        xpos 400
        ypos 0.28
        idle cherry_idle
        hover cherry_hover
        focus_mask True
        action [SetVariable("cherry", cherry+1),  Return()]

    imagebutton:
        xanchor 0
        yanchor 0
        xpos -200
        ypos -540
        idle chantilly_idle
        hover chantilly_hover
        focus_mask True
        action [SetVariable("chantilly", chantilly+1),  Return()]

    imagebutton:
        xanchor 0
        yanchor 0.5
        xpos 50
        ypos 390
        idle marshmallow_idle
        hover marshmallow_hover
        focus_mask True
        action [SetVariable("marshmallow", marshmallow+1),  Return()]

    imagebutton:
        xanchor 0
        yanchor 0
        xpos -380
        ypos 60
        idle cinnamon_idle
        hover cinnamon_hover
        focus_mask True
        action [SetVariable("cinammon", cinammon+1), Return()]

    imagebutton:
        xanchor 0
        yanchor 0
        xpos 50
        ypos -230
        idle no_toppings_idle
        focus_mask True
        hover no_toppings_hover
        action  Return()

        #adicionar imagebutton separado de choolate e de uma opcao de de nenhum additional



    #menu:
    #    "Coffee":
    #        $coffee += 1
    #        jump start_concoction
    #    "Milk" :
    #        $milk += 1
    #        jump start_concoction
    #    "Sugar":
    #        $sugar += 1
    #        jump start_concoction
    #    "Chantilly":
    #        $chantilly += 1
    #        jump start_concoction
    #    "Cherry":
    #        $cherry += 1
    #        jump start_concoction
    #    "Blend":
    #        $blend += 1
    #        jump start_concoction
    #    "Done":
    #        call compara_resposta



label compara_resposta:
    if coffee == cafe and milk == leite and cinammon == canela and marshmallow == marxmallow and sugar == acucar and chantili == chantilly and cherry == cereja and chocolate == chocolate_r:
            "Main" "Yay i got it right!"
            $ completed = 1
    else:
            "Main" "Oh no! Something went wrong!"
            $ completed = 0

    jump begin_minigame



label compara_tia1:
    if (coffee == 1 and (sugar == 2 or sugar == 3)) or (coffee == 2 and (sugar == 2 or sugar == 3)) or (coffee == 3 and sugar == 3):
        $ completed = 1
    else:
        $ completed = 0

    return

label compara_tia2:
    if (coffee == 1 and (sugar == 2) and (chocolate == 1 or chantilly == 1 or marshmallow == 1)) or (coffee == 2 and (sugar == 3 or sugar == 2) and (chocolate == 1 or chantilly == 1 or marshmallow == 1)):
        $ completed = 1
    else:
        $ completed = 0

    return

label compara_tia3:
    if ((coffee == 1 orcoffee == 2 or coffee = 3) and sugar == 1 and milk == 1 and chocolate == 0 and chantilly == 0 and marshmallow == 0):
        $ completed = 1
    else:
        $ completed = 0

    return

label compara_tia4:
    if ((coffee == 1 or coffee == 2 or coffee == 3) and sugar == 0 and chocolate == 0 and chantilly == 0 and cherry == 0 and marshmallow == 0):
        $ completed = 1
    else:
        $ completed = 0

    return
