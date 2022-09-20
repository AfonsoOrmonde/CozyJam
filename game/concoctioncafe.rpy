#Script of the Minigame



label begin_minigame:
    scene table
    $coffee = 0
    $sugar = 0
    $chantilly = 0
    $cherry = 0
    $cinammon = 0
    $chocolate = 0
    $marshmallow = 0
    $milk = 0
    $completed = true

    "Main" "Ok let's do this. One normal coffee right away!"

    call screen cafe_escolha
    call screen acucar_escolha
    call screen leite_escolha
    call screen chocolate_escolha
    call screen additionals
    call compara_resposta

screen cafe_escolha:

    imagebutton:
        xanchor 0
        yanchor 0
        xpos 800
        ypos 600
        idle "coffee0_1.png"
        hover "coffee0_2.png"
        action [SetVariable("coffee", coffee+0), Return()]

    imagebutton:
        xanchor -2
        yanchor 0.5
        xpos -2
        ypos 0.28
        idle "coffee1_1.png"
        hover "coffee1_2.png"
        action [SetVariable("coffee", coffee+1), Return()]

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.28
        idle "coffee2_1.png"
        hover "coffee2_2.png"
        action [SetVariable("coffee", coffee+2), Return()]

    imagebutton:
        xanchor 0
        yanchor 0.5
        xpos 1500
        ypos 0.28
        idle "coffee3_1.png"
        hover "coffee3_2.png"
        action [SetVariable("coffee", coffee+3), Return()]

screen acucar_escolha:

    imagebutton:
        xanchor 0
        yanchor 0.5
        xpos 200
        ypos 0.28
        idle "sugar0_1.png"
        hover "sugar0_2.png"
        action [SetVariable("sugar", sugar+0),  Return()]

    imagebutton:
        xanchor 0
        yanchor 0
        xpos 200
        ypos 600
        idle "sugar1_1.png"
        hover "sugar1_2.png"
        action [SetVariable("sugar", sugar+1),  Return()]

    imagebutton:
        xanchor 0
        yanchor 0.5
        xpos 1200
        ypos 0.28
        idle "sugar2_1.png"
        hover "sugar2_2.png"
        action [SetVariable("sugar", sugar+2),  Return()]

    imagebutton:
        xanchor 0
        yanchor 0
        xpos 1200
        ypos 600
        idle "sugar3_1.png"
        hover "sugar3_2.png"
        action [SetVariable("sugar", sugar+3), Return()]

screen leite_escolha:

        imagebutton:
            xanchor 0
            yanchor 0.5
            xpos 200
            ypos 0.28
            idle "milk1_1.png"
            hover "milk1_2.png"
            action [SetVariable("milk", milk+1),  Return()]

        imagebutton:
            xanchor 0
            yanchor 0
            xpos 1000
            ypos 0
            idle "milk2_1.png"
            hover "milk2_2.png"
            action [SetVariable("milk", milk+0),  Return()]

screen chocolate_escolha:

        imagebutton:
            xanchor 0
            yanchor 0.5
            xpos 200
            ypos 0.28
            idle "chocolate1_1.png"
            hover "chocolate1_2.png"
            action [SetVariable("chocolate", chocolate+1),  Return()]

        imagebutton:
            xanchor 0
            yanchor 0
            xpos 1000
            ypos 0
            idle "chocolate2_1.png"
            hover "chocolate2_2.png"
            action [SetVariable("chocolate", chocolate+0),  Return()]

screen additionals:

    imagebutton:
        xanchor 0
        yanchor 0.5
        xpos 200
        ypos 0.28
        idle "cherry1_1.png"
        hover "cherry1_2.png"
        action [SetVariable("cherry", cherry+1),  Return()]

    imagebutton:
        xanchor 0
        yanchor 0
        xpos 200
        ypos 600
        idle "chantili1_1.png"
        hover "chantili1_2.png"
        action [SetVariable("chantilly", chantilly+1),  Return()]

    imagebutton:
        xanchor 0
        yanchor 0.5
        xpos 1200
        ypos 0.28
        idle "marshmallow1_1.png"
        hover "marshmallow1_2.png"
        action [SetVariable("marshmallow", marshmallow+1),  Return()]

    imagebutton:
        xanchor 0
        yanchor 0
        xpos 1200
        ypos 600
        idle "cinammon1_1.png"
        hover "cinammon1_2.png"
        action [SetVariable("cinammon", cinammon+1), Return()]

    imagebutton:
        xanchor 0
        yanchor 0
        xpos 600
        ypos 300
        idle "noadditionals_1.png"
        hover "noadditionals_2.png"
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
            completed = true
    else:
            "Main" "Oh no! SOmething went wrong!"
            completed = false

    jump begin_minigame
