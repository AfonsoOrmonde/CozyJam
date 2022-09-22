label girl:

    if day == 1:
        call girl_1 from _call_girl_1
    elif day == 2:
        if girl_points == 1:
            call girl_2_1 from _call_girl_2_1
        else:
            call girl_2_2 from _call_girl_2_2
    elif day == 3:
        if girl_points == 2:
            call girl_3_1 from _call_girl_3_1
        else:
            call girl_3_2 from _call_girl_3_2
    elif day == 4:
        if girl_points == 2 or girl_points == 3:
            call girl_4_1 from _call_girl_4_1
        else:
            call girl_4_2 from _call_girl_4_2

    return

label girl_1:
    scene general_background with dissolve
    show girl_normal at Position(xpos = 1400, ypos=1050) with dissolve
    play music "audio/lofi_1.mp3" loop fadein 2

    Uk "H-Hi..."
    Mc "Hi, how can I help you?"
    Uk "..."
    Mc "Hello...?"
    Mc "What's your name?"

    hide girl_normal
    show girl_traumatized at Position(xpos=-183, ypos=1080)

    Brit "...Brittany."
    Brit "I'm tired..."
    Brit "I'm really, really... tired..."
    Brit "..."
    Brit "I'll never spend a sleepless night again."
    Brit "I'm so dizzy."

    menu:
        "Why would you spend a sleepless night?":
            hide girl_traumatized
            show girl_normal at Position(xpos=1400, ypos=1050)

            Brit "ah..."
            Brit "I have to study hard..."
            Brit "I have some important exams this week... for the University of Psychology..."
            Mc "Ah! for sure that seems important."

            hide girl_normal
            show girl_sad at Position(xpos=345, ypos=1075)

            Brit "Well, yes... If only my mom thought so..."
            Mc "What?..."
            Brit "..."
            hide girl_sad

        "Maybe you should get some sleep before going out...":
            hide girl_traumatized
            show girl_normal at Position(xpos=1400, ypos=1050)

            Brit "maybe you're right..."
            Brit "but I need to study... how could I study if I was sleeping?"
            Mc "do you need to study?"
            Brit "I have really important psych exams this week..."
            Mc "I'm sure you would be fine!"

            hide girl_normal
            show girl_sad at Position(xpos=345, ypos=1075)

            Brit "My mom doesn't say that..."
            Mc "What?..."
            Brit "..."
            hide girl_sad

        "...":
            "{i}This girl... She should definitely get some sleep..."
            hide girl_traumatized

    show girl_normal at Position(xpos=1400, ypos=1050)

    Mc "Ah... all right..."
    Mc "What can I get you?"
    Brit "I need something to keep me awake..."
    Brit "Something… strong."
    Brit "The stronger, more bitter you have."
    Mc "All right... are you sure it's safe?"

    hide girl_normal
    show girl_happy at Position(xpos=865, ypos=1063)

    Brit "Yes... I think so..."
    Mc "If you say..."

    "{i}I'll give her what she wants, but…she should definitely get some sleep."

    call begin_minigame
    call compara_girl1
    play music "audio/lofi_1.mp3" loop fadein 2
    scene general_background with dissolve

    if completed == 1:
        $ girl_points += 1
        hide girl_happy
        show girl_drinking at Position(xpos=330, ypos=1050)

        Brit "hum"

        hide girl_drinking
        scene general_background_girl
        show girl_happy at Position(xpos=865, ypos=1063)

        Brit "I feel better already..."
        Brit "The strength of this one... is on point."
        Brit "I finally have the energy to study again!"
        Mc "Maybe you should sleep a little before..."

        hide girl_happy
        show girl_traumatized at Position(xpos=-183, ypos=1080)

        Brit "..."

        hide girl_traumatized
        show girl_normal at Position(xpos=1400, ypos=1050)

        Brit "Or maybe I should go to them..."
        Mc "... ???"

        play sound "audio/coins.mp3" noloop

        Brit "T-take it here... and see you later."
        Mc "Thank you... you?"

        hide girl_normal with dissolve

        "{i}Well, that was definitely random..."

    else:
        hide girl_happy
        show girl_drinking at Position(xpos=330, ypos=1050)

        Brit "hum"

        hide girl_drinking
        scene general_background_girl
        show girl_normal at Position(xpos=1400, ypos=1050)

        Brit "Ahm..."
        Brit "That's not... strong enough..."
        Brit "I can still feel my eyes closing."
        Brit "How would I study without something strong?"
        Mc "I'm sorry, I thought I was strong enough for you..."
        Brit "It's still good coffee, it's just not something to keep me awake."

        play sound "audio/coins.mp3" noloop

        Brit "H-here, take it."
        Mc "Thank you, I'll make sure the next one is better"

        hide girl_normal with dissolve


    return

label girl_2_1:
    scene general_background with dissolve
    show girl_normal with dissolve
    play music "audio/lofi_1.mp3" loop fadein 2

    Brit "Hi..."
    Mc "Oh it's you again!"
    Brit "...yeah"
    Mc "How were your exams?"

    hide girl_normal
    show girl_happy at Position(xpos=865, ypos=1063)

    Brit "A-actually they went really well..."
    Brit "Your coffee helped me a lot… i could study for SO long"
    Brit "I-i hope I can get a good mark!"

    hide girl_happy
    show girl_sad at Position(xpos=345, ypos=1075)

    Brit "..."
    Brit "...if only... if only my mom..."

    menu:
        "Your mom...?":
            Brit "..."
            Brit "It's just that...my mom doesn't support me that much..."
            Brit "I can get the best grade on tests she still thinks I'm a loser..."
            Mc "Oh..."

            hide girl_sad
            show girl_normal at Position(xpos=1400, ypos=1050)

            Brit "She says im shy and that being too focus make me lonely..."
            Mc "Well, you can be shy but that doesn't make you a loser..."
            Brit "...Thats the first time someone says that to me..."
            Mc "But maybe you should rest sometimes..."
            Brit "A-anyways... I still get to teach a lot of things to my little brother..."
            Brit "He's so curious and has always so much energy..."

            hide girl_normal
            show girl_happy at Position(xpos=865, ypos=1063)

            Brit "Totally like me... hahaha... haha..."
            Mc "Ahaha, yes."
            "{i}Totally like her"
            hide girl_happy

        "You don't seem very happy about your exams tho...":
            Brit "I am happy about my exams..."
            Brit "It's just that my mom don't find it so important as me..."
            Brit "She thinks im too lonely and shy because i study too much..."
            Mc "Well, you sure study a lot..."
            Mc "But that don't make you a loser."

            hide girl_sad
            show girl_normal at Position(xpos=1400, ypos=1050)

            Brit "T-thanks... I guess..."
            Brit "You know i have a little brother? He always asks me about what im doing..."
            Brit "...and i always teach him different things."
            Mc "That's so nicee!"
            Brit "He´s the most curious person i have ever known..."
            Mc "Keep teaching him a lot of stuff, im sure one day he'll be gratefull."
            hide girl_normal

        "I'm really happy you did well in your exams.":
            hide girl_sad
            show girl_normal at Position(xpos=1400, ypos=1050)
            Brit "T-thanks. I put a lot of effort in those exams..."
            Mc "You are going to be really successful if you keep it like that!"
            Brit "..."
            Brit "T-thank you..."
            hide girl_normal

    show girl_normal at Position(xpos=1400, ypos=1050)

    Mc "I'm glad you're okay despite all the difficulties..."
    Mc "Anyways... what can i get you this time?"
    Brit "Honestly im still tired from the nights lost to study and too this thing with my mom..."
    Brit "Can i get something strong with just a little bit of sweetness? Just a little bit..."
    Brit "Also, something fruity too."
    Mc "Of course!"
    Mc "Strong with a little bit of sweetness."

    call begin_minigame
    call compara_girl2
    scene general_background with dissolve
    play music "audio/lofi_1.mp3" loop fadein 2

    if completed == 1:
        $ girl_points += 1
        hide girl_normal
        show girl_drinking at Position(xpos=330, ypos=1050)

        Brit "Hum."

        hide girl_drinking
        scene general_background_girl
        show girl_happy at Position(xpos=865, ypos=1063)

        Brit "Hmmmm..."
        Brit "The perfect amount of sweetness. Delicious!"
        Mc "Thank you!"

        hide girl_happy
        show girl_normal at Position(xpos=1400, ypos=1050)

        Brit "The coffee and the weather are creating a perfect mood to read my favorite book: \"The Secret History\", by Donna Tartt."
        Brit "Do you know it?"
        Mc "You really are talkative today!"
        Brit "I'm going to present it to my friends in my secret philosophy club..."
        Mc "...?? what?"

        hide girl_normal
        show girl_traumatized at Position(xpos=-183, ypos=1080)

        Brit "Oh... aghr... hm..."
        Brit "Oh oh, I wasn't supposed to say this"

        play sound "audio/coins.mp3" noloop

        Brit "Byee"

        hide girl_traumatized

        "{i}Again? A philosophy club?"
        "{i}Why would she be embarased about it?"
        "{i}Weird..."

    else:
        hide girl_normal
        show girl_drinking at Position(xpos=330, ypos=1050)

        Brit "Hum."

        hide girl_drinking
        show girl_normal at Position(xpos=14000, ypos=1050)

        Brit "Oh..."
        Brit "I-i asked for a little bit of sweetness..."
        Mc "I'm sorry… thought it was the way you wanted..."
        Brit "It's ok, but i just needed a little bit of something sweet."
        Brit "M-maybe the next time you could do it like that..."
        Brit "Anyways, take my money, it was still a decent coffee."

        play sound "audio/coins.mp3" noloop

        Brit "See you tomorrow."
        Mc "Bye!"

        hide girl_normal


    return

label girl_2_2:
    scene general_background with dissolve
    show girl_normal with dissolve
    play music "audio/lofi_1.mp3" loop fadein 2

    Brit "Hi..."
    Mc "Oh its you again!"
    Brit "...Yeah."
    Mc "How were your exams?"
    Brit "They were okay..."
    Brit "I had some problems trying to keep myself awake to study, the coffee didn't do much for me..."
    Brit "But I hope I'll get a good grade."

    hide girl_normal
    show girl_sad at Position(xpos=345, ypos=1075)

    Brit "..."
    Brit "If only... if only my mom..."

    menu:
        "Your mom...?":
            Brit "..."
            Brit "It's just that…my mom doesn't support me that much..."
            Brit "I can get the best grade on tests she still thinks i'm a loser..."
            Mc "Oh..."

            hide girl_sad
            show girl_normal at Position(xpos=1400, ypos=1050)

            Brit "She says I'm shy... and says that being too focus makes me lonely..."
            Mc "Well, you can be shy but that doesn't make you a loser..."
            Brit "Thats the first time someone says that to me..."
            Mc "But maybe you should rest sometimes..."
            Brit "..."
            Brit "Well… maybe you're right..."
            hide girl_normal

        "I'm really happy you did well in your exams":
            hide girl_sad
            show girl_normal at Position(xpos=1400, ypos=1050)

            Brit "T-thanks... I put a lot of effort in those exams..."
            Mc "You are going to be really successful if you keep it like that!"

            hide girl_normal
            show girl_happy at Position(xpos=865, ypos=1063)

            Brit "..."
            Brit "T-thank you..."
            hide girl_happy

    show girl_normal at Position(xpos=1400, ypos=1050)

    Mc "Anyways... I'm glad you're okay despite all the difficulties… what can i get you this time?"
    Brit "Honestly I'm still tired from the nights lost to study and too this thing with my mom..."
    Brit "Can i get something strong with just a little bit of sweetness? just a little bit."
    Brit "And something fruity on top."
    Mc "Of course."
    Mc "Strong black with a little bit of sweetness."
    Mc "I'll be right back."

    call begin_minigame
    call compara_girl2
    scene general_background
    play music "audio/lofi_1.mp3" loop fadein 2

    if completed == 1:
        $ girl_points += 1
        hide girl_normal
        show girl_drinking at Position(xpos=330, ypos=1050)

        Brit "Hum."

        hide girl_drinking
        scene general_background_girl
        show girl_happy at Position(xpos=865, ypos=1063)

        Brit "Hmmmm..."
        Brit "The perfect amount of sweetness...delicious!"
        Mc "Thank you!"
        Brit "The coffee and the weather are creating a perfect mood to read my favorite book: \"The Secret History\", by Donna Tartt..."
        Brit "Do you know it?"
        Mc "You really are talkative today!"

        hide girl_happy
        $ girl_points += 1
        hide girl_normal
        show girl_drinking at Position(xpos=330, ypos=1050)

        Brit "Hum."

        hide girl_drinking
        show girl_normal at Position(xpos=1400, ypos=1050)

        Brit "I'm going to present it to my friends in my secret philosophy club..."
        Mc "...?? what?"

        hide girl_normal
        $ girl_points += 1
        hide girl_normal
        show girl_drinking at Position(xpos=330, ypos=1050)

        Brit "Hum."

        hide girl_drinking
        show girl_traumatized at Position(xpos=-183, ypos=1080)

        Brit "Oh... aghr... hm..."
        Brit "Oh oh, I wasn't supposed to say this"

        play sound "audio/coins.mp3" noloop

        Brit "Byee!"

        hide girl_traumatized

        "{i}Again? A philosophy club?"
        "{i}Why would she be embarased about it?"
        "{i}Weird..."

    else:
        hide girl_normal
        show girl_drinking at Position(xpos=330, ypos=1050)

        Brit "Hum."

        hide girl_drinking
        show girl_normal at Position(xpos=14000, ypos=1050)

        Brit "Oh..."
        Brit "I-i asked for a little bit of sweetness..."
        Mc "I'm sorry… thought it was the way you wanted..."
        Brit "It's ok, but i just needed a little bit of something sweet."
        Brit "M-maybe the next time you could do it like that..."

        play sound "audio/coins.mp3" noloop

        Brit "Anyways, take my money, it was still a decent coffee..."
        Mc "Thank you so much!"

        hide girl_normal

    return

label girl_3_1:

    return

label girl_3_2:

    return

label girl_4_1:

    return

label girl_4_2:

    return
