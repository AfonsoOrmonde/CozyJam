



label begin_minigame:
    scene table
    $coffee = 0
    $sugar = 0
    $chantilly = 0
    $cherry = 0
    $blend = 0
    $milk = 0
    "Main" "Ok let's do this. One normal coffee right away!"

label start_concoction :
    menu:
        "Coffee":
            $coffee += 1
            jump start_concoction
        "Milk" :
            $milk += 1
            jump start_concoction
        "Sugar":
            $sugar += 1
            jump start_concoction
        "Chantilly":
            $chantilly += 1
            jump start_concoction
        "Cherry":
            $cherry += 1
            jump start_concoction
        "Blend":
            $blend += 1
            jump start_concoction
        "Done":
            call compara_resposta


label compara_resposta:
    if coffee == cafe and milk == leite and blend == blend_r and sugar == acucar and chantili == chantilly and cherry == cereja:
            "Main" "Yay i got it right!"
    else:
            "Main" "Oh no! SOmething went wrong!"

    jump begin_minigame
