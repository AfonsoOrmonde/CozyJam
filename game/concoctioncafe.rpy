#Script of the Minigame



label begin_minigame:
    scene table
    $coffee = 0
    $sugar = 0
    $chantilly = 0
    $cherry = 0
    $blend = 0
    $milk = 0
    "Main" "Ok let's do this. One normal coffee right away!"
    call screen cafe_escolha
    call screen acucar_escolha
    hide screen acucar_escolha
    call compara_resposta

screen cafe_escolha:

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
        xanchor 0.25
        yanchor 0.5
        xpos 0.25
        ypos 0.28
        idle "sugar1_1.png"
        hover "sugar1_2.png"
        action [SetVariable("sugar", sugar+1), Jump ("end")]

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.28
        idle "sugar2_1.png"
        hover "sugar2_2.png"
        action [SetVariable("sugar", sugar+2), Jump ("end")]

    imagebutton:
        xanchor 0.7
        yanchor 0.5
        xpos 0.7
        ypos 0.28
        idle "sugar3_1.png"
        hover "sugar3_2.png"
        action [SetVariable("sugar", sugar+3), Jump ("end")]

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
    if coffee == cafe and milk == leite and blend == blend_r and sugar == acucar and chantili == chantilly and cherry == cereja:
            "Main" "Yay i got it right!"
    else:
            "Main" "Oh no! SOmething went wrong!"

    jump begin_minigame
