label kid:

    if day == 1:
        call kid_1
    if day == 2:
        if kid_points == 1:
            call kid_2_1
        else:
            call kid_2_2
    if day == 3:
<<<<<<< HEAD
        if kid_points == 2:
=======
        if kid_points == 2
>>>>>>> main
            call kid_3_1
        else:
            call kid_3_2

    return



label kid_1:

    scene general_background with dissolve
    show kid_normal at Position(xpos = 0.70) with dissolve

    Kid "..."
    Mc "..."
    hide kid_normal
    show kid_normal at Position(xpos = 0.70)
    Kid ".........."
    Mc "................."
    hide kid_normal
    show kid_normal at Position(xpos = 0.70)
    Kid "........................"

    menu:
        "Sorry can I hel-":
            hide kid_normal
            show kid_happy at Position(xpos = 0.70) with hpunch
            Kid "BEAUTIFUL DAY ISN'T IT?!"
            Mc "Someone's awfully energetic huh?"
            Kid "Yep yep, my nana tells me the same, but she says im just like a squirrel!"
            "{i}Dont know if thats a complement."

        "...":
            show kid_happy at Position(xpos = 0.70) with hpunch
            Kid "Wow i really can't get a word out of you, hehe!"
            Mc "{i}Where are this kid's parents?"

        "Where are your paren-":
            hide kid_normal
            show kid_happy at Position(xpos = 0.70) with hpunch
            Kid "NOT HERE!!"
            Mc "{i} Figured as much."

    hide kid_happy
    show kid_normal at Position(xpos = 0.70)
    Kid "I was playing over there at the tree when I saw you and thought you looked real fun!"
    Mc "Fun?"
    hide kid_normal
    show kid_happy at Position(xpos = 0.70) with hpunch
    Kid "YEAH!"
    hide kid_happy
    show kid_normal at Position(xpos = 0.70)
    Kid "My nana always told me that all stories start with a \" fateful encounter \" whatever that means, HAHA!"

    menu:
        "Whats your nana's name?":
            Kid "Oh, her name's Tilda."

        "What other things does your nana tell you?":
            Kid "All kinds of stuff! Fairytales, legends... sometimes even horror stories, hehe."
            Mc "I see, sounds nice."
            Kid "Yeah!"

    Kid "..."
    Mc "..."
    hide kid_happy
    show kid_normal at Position(xpos = 0.70)
    Kid ".........."
    Mc "................."
    hide kid_normal
    show kid_normal at Position(xpos = 0.70)
    Kid "........................"

    menu:

        "Are you gonna ask some-":
            hide kid_normal
            show kid_happy at Position(xpos = 0.70) with hpunch
            Kid "YOU KNOW WHAT WOULD BE NICE?!"
            Mc "{i}Here we go again."
        "...":
            hide kid_normal
            show kid_happy at Position(xpos = 0.70) with hpunch
            Kid "Ok I think I'm starting to learn how you work."
            Mc "{i} I doubt it but let's roll with it."
            Kid "Let's see if this place is as legendary as our \"fateful encounter\"!"

    hide kid_happy
    show kid_normal at Position(xpos = 0.70)
    Kid "My nana told me once about this magic chocolate milk ya know!"
    Mc "Chocolate milk?"
    Kid "And she said that this hero travelled through entire lands of the softest of candy to reach it!"
    Mc "What are you tal-"
    Kid "AND THAT HE COULD ASK FOR ANY WISH HE WANTED ONCE HE PUT SOME OF THE SOFT CANDY IN THE MILK!!!"
    Mc "Huh?"
    Kid "Can you make the legendary wish milk please?"
    Mc "Coming right up."
    "{i}I think i got it."
    "{i}Maybe..."

    call begin_minigame
    call compara_kid1
    scene general_background

    hide kid_normal
    show kid_happy at Position(xpos = 0.70)
    Kid "Thank you!"

    menu:
        "You're welcome.":
            Kid "Hehe. You're nice!"

        "You better pay for that.":
            Kid "Yes, yes, don't worry!"

        "...":
            Kid "Bottoms up!"
    hide kid_happy
    show kid_drinking at Position(xpos = 0.70)

    Kid "*gulp* *gulp* *gulp*"

    if completed == 1:
        $kid_points += 1
        hide kid_drinking
        show kid_happy at Position(xpos = 0.70) with hpunch
        Kid "WOW!!!"
        Kid "This has to be it!"
        Mc "I'm glad you liked it!"
        Kid "Now I definity need to be come back here!"
        menu:
            "You're always welcome.":
                Kid "Thank you! I'll probably come by tommorrow!"

            "Don't forget to pay.":
                Kid "Of course not don't worry my nana raised no villain."
                Uk "{i}You're still pretty young though."

            "Liked it that much huh?":
                "It's legendary!"

        Kid "The best part it's that it's super close to nana so i can come by more times, hehe!"
        Kid "Welp, see you tommorrow!"
        Kid "Oh! And here you go!"
        Mc "Thank you!"
        Kid "I hope to see you tommorrow more powefu than ever coffee hero!"
        Mc "Coffee hero?"
        Kid "Yes, you are my assistant hero in my journey?"
        Mc "What journey?"
        Kid "You'll know soon enough!"
        Kid "Bye Hero!"
        hide kid_happy with dissolve
        "{i}Aaaand he's gone. Wow he IS fast."
        "{i}Oh, never got his name did I?"

    elif completed == 0:
        hide kid_drinking
        show kid_disgusted at Position(xpos = 0.70)
        Kid "Blah! This is so not legendary!"
        "{i}What did he want then?"
        Kid "I dont know if it's the candy that ain't right or maybe the chocolate?"
        hide kid_disgusted
        show kid_happy at Position(xpos = 0.70) with hpunch
        Kid "Well... no matter!"
        Kid "Heroes do have their hardships after all!"
        Mc "Heroes?"
        Kid "Yeah heroes!"
        "{i}The kid sure is lively."
        Kid "I'll comeback tommorrow to see how much your powers have increased, hahah!"
        Kid "SO LONG HERO!"
        hide kid_happy with dissolve
        Mc "Wai-"
        "{i}Never got to know his name."

    return

label kid_2_1:

    show kid_normal at Position(xpos = 0.70) with dissolve
    Kid"..."
    menu:
        "...":
            Kid "Hehe, yep I'm really starting to get you."
            "{i} I think I'm the one starting to get you."

        "Hello the-":
            hide kid_normal
            show kid_happy at Position(xpos = 0.70) with hpunch
            Kid "HELLO COFFEE HERO!"
            Mc "Hello.... kid?"
    Mc "I have never asked your name have I?"
    hide kid_happy
    show kid_normal at Position(xpos = 0.70)
    Kid "Oh it's easy and simple. Try to guess!"
    menu:
        "John?":
            hide kid_normal
            show kid_happy at Position(xpos = 0.70) with hpunch
            John"DING DING DING"
        "Andy?":
            hide kid_normal
            show kid_happy at Position(xpos = 0.70) with hpunch
            Kid"Nope. Wrong!"
            John "It's John."
        "Leonard":
            hide kid_normal
            show kid_happy at Position(xpos = 0.70) with hpunch
            Kid"Nope. Wrong!"
            John "It's John."

    Mc "Nice and simple."
    hide kid_normal
    show kid_sad at Position(xpos = 0.70) with hpunch
    John "I dont know. Don't really like it."
    Mc "Well what is your surname?"
    hide kid_sad
    show kid_normal at Position(xpos = 0.70) with hpunch
    John "Oh that's Dream."
    Mc "John Dream?"
    John "Yeah!"
    John "Ok so today I need to ask you something."
    Mc "What is it?"
    John "I need you to make a special coffee."
    Mc "Aren't you too young to drink coffee?"
    hide kid_normal
    show kid_disgusted at Position(xpos = 0.70)
    John "It's for my nana! I wouldn't like that stuff!"
    Mc"Where is your nana?"
    hide kid_disgusted
    show kid_sad at Position(xpos = 0.70) with hpunch
    John "Oh... she's in... the hospital."
    menu:

        "What? Is she okay?":
            hide kid_sad
            show kid_normal at Position(xpos = 0.70)
            John"Huh? Oh yeah of course everything is fine."

        "{i} Better not ask about it.":
            hide kid_sad
            show kid_normal at Position(xpos = 0.70)
            John "Still not talking. You're cool, somehow."

        "Oh I see. She works there?":
            hide kid_sad
            show kid_normal at Position(xpos = 0.70)
            John "Huh? Oh no she is living there for now."
            Mc "Oh I see."

    Mc "So what is it gonna be?"
    John "Oh yeah! So my nana told me about this bitter coffee!"
    John "But it was so bitter it could destroy everything in it's path!!!"
    John "And in it there was but one single cinammon stick, drifting."
    Mc "Okay! Coming right up!"
    call begin_minigame
    call compara_kid2
    scene general_background

    if completed == 1:
        $kid_points += 1

        hide kid_normal
        show kid_drinking at Position(xpos = 0.70)
        John "Hmmmmm!"
        hide kid_drinking
        show kid_happy at Position(xpos = 0.70) with hpunch
        Mc "Didn't you say it wasn't for you?"
        John "I had to try it, right? How else would I know if your powers increased?"
        John "Also, it was only a little."
        Mc "You liked it?"
        hide kid_normal
        show kid_disgusted at Position(xpos = 0.70)
        John"Nope, hated it! But, I know this is what nana wants."
        Mc"I'm glad that is the case."
        hide kid_disgusted
        show kid_normal at Position(xpos = 0.70)
        John"Yep well, see you tommorrow!"
        Mc "{i}Wow, tommorrow again?"
        John"And umm... hey"
        Mc "???"
        hide kid_normal
        show kid_happy at Position(xpos = 0.70)
        John "Thank you! For making this for nana!"
        hide kid_happy
        Mc "Huh? He seemed different there."
        "{i}Wait... he never paid did he?"

    elif completed == 0:
        hide kid_normal
        show kid_drinking at Position(xpos = 0.70)
        John "Hmmmmm!"
        hide kid_drinking
        show kid_sad at Position(xpos = 0.70)
        John "I don't think this is it."
        Mc "I'm sorry little guy..."
        hide kid_sad
        show kid_normal at Position(xpos = 0.70)
        John "Oh no problem. Nana probably wants this as well. She will be happy don't worry!"
        John "Welp, gotta run! Nana doesn't like cold drinks!"
        Mc "Stay safe!"
        "{i}Hmmm, he seemed different."
        "{i}Wait... he never paid did he?"
    return

label kid_2_2:
    show kid_normal at Position(xpos = 0.70) with dissolve
    Kid"..."
    menu:
        "...":
            Kid "Hehe, yep I'm really starting to get you."
            "{i} I think I'm the one starting to get you."

        "Hello the-":
            hide kid_normal
            show kid_happy at Position(xpos = 0.70) with hpunch
            Kid "HELLO COFFEE HERO!"
            Mc "Hello.... kid?"
    Mc "I have never asked your name have I?"
    hide kid_happy
    show kid_normal at Position(xpos = 0.70)
    Kid "Oh it's easy and simple. Try to guess!"
    menu:
        "John?":
            hide kid_normal
            show kid_happy at Position(xpos = 0.70) with hpunch
            John"DING DING DING"
        "Andy?":
            hide kid_normal
            show kid_happy at Position(xpos = 0.70) with hpunch
            Kid"Nope. Wrong!"
            John "It's John."
        "Leonard":
            hide kid_normal
            show kid_happy at Position(xpos = 0.70) with hpunch
            Kid"Nope. Wrong!"
            John "It's John."

    Mc "Nice and simple."
    hide kid_normal
    show kid_sad at Position(xpos = 0.70) with hpunch
    John "I dont know. Don't really like it."
    Mc "Well what is your surname?"
    hide kid_sad
    show kid_normal at Position(xpos = 0.70) with hpunch
    John "Oh that's Dream."
    Mc "John Dream?"
    John "Yeah!"
    John "Ok so today I need to ask you something."
    Mc "What is it?"
    John "I need you to make a special coffee."
    Mc "Aren't you too young to drink coffee?"
    hide kid_normal
    show kid_disgusted at Position(xpos = 0.70)
    John "It's for my nana! I wouldn't like that stuff!"
    Mc"Where is your nana?"
    hide kid_disgusted
    show kid_sad at Position(xpos = 0.70)
    John "Oh...she's back at home."
    menu:
        "You don't seem very happy about it.":
            hide kid_sad
            show kid_happy at Position(xpos = 0.70) with hpunch
            "What do you mean!? I AM SMILLING LIKE THE SUN!"

        "{i}Better not ask about it.":
            hide kid_sad
            show kid_happy at Position(xpos = 0.70) with hpunch
            "But well that's that!"

    Mc "So what is it gonna be?"
    John "Oh yeah! So my nana told me about this bitter coffee!"
    John "But it was so bitter it could destroy everything in it's path!!!"
    John "And in it there was but one single cinammon stick, drifting."
    Mc "Okay! Coming right up!"
    call begin_minigame
    call compara_kid2
    scene general_background

    if completed == 1:
        $kid_points += 1

        hide kid_normal
        show kid_drinking at Position(xpos = 0.70)
        John "Hmmmmm!"
        hide kid_drinking
        show kid_happy at Position(xpos = 0.70) with hpunch
        Mc "Didn't you say it wasn't for you?"
        John "I had to try it, right? How else would I know if your powers increased?"
        John "Also, it was only a little."
        Mc "You liked it?"
        hide kid_normal
        show kid_disgusted at Position(xpos = 0.70)
        John"Nope, hated it! But, I know this is what nana wants."
        Mc"I'm glad that is the case."
        hide kid_disgusted
        show kid_normal at Position(xpos = 0.70)
        John"Yep well, see you tommorrow!"
        Mc "{i}Wow, tommorrow again?"
        John"And umm... hey"
        Mc "???"
        hide kid_normal
        show kid_happy at Position(xpos = 0.70)
        John "Thank you! For making this for nana!"
        hide kid_happy
        Mc "Huh? He seemed different there."
        "{i}Wait... he never paid did he?"

    elif completed == 0:
        hide kid_normal
        show kid_drinking at Position(xpos = 0.70)
        John "Hmmmmm!"
        hide kid_drinking
        show kid_sad at Position(xpos = 0.70)
        John "I don't think this is it."
        Mc "I'm sorry little guy..."
        hide kid_sad
        show kid_normal at Position(xpos = 0.70)
        John "Oh no problem. Nana probably wants this as well. She will be happy don't worry!"
        John "Welp, gotta run! Nana doesn't like cold drinks!"
        Mc "Stay safe!"
        "{i}Hmmm, he seemed different."
        "{i}Wait... he never paid did he?"

    hide kid_normal
    return

<<<<<<< HEAD
=======


>>>>>>> main
label kid_3_1:
    "{i}Hmm it's quite now."
    "{i}There's something missing, something... noisy."
    John"HEYYYYYYYYYYYYYY!"
    "{i} I knew it."
    show kid_happy in Position(xpos = 0.7) with hpunch
    John"How are you doing coffee hero?!"
    menu:
        "Hi kiddo":
            John "Awwww, c'mon I'm not a kid I'm your partner"
            hide kid_happy
            show kid_normal in Position(xpos = 0.7)

        "Hi John":
            hide kid_happy
            show kid_disgusted in Position(xpos = 0.7)
            John "Ahhhhh, I can't get used to yu calling me that."
            hide kid disgusted
            show kid_normal in Position(xpos = 0.7)

        "Hi Dream":
            John"Hello hero!! You remembered my name"
            hide kid_happy
            show kid_normal in Position(xpos = 0.7)

        "...":
            John"One day hero, one day I wil get a reaction from you!"
            hide kid_happy
            show kid_normal in Position(xpos = 0.7)
    John "Oh yeah here."
    Mc "Oh, you decided to pay."
    John "Yeah, nana gave me an earful when I came back yesterday and still had the money."
    John "I sweear it wasn't on purpose!"
    "{i} Should I ask?"

    menu:
<<<<<<< HEAD
        "How is your nana?":
=======
        "How is your nana?"
>>>>>>> main
            John "What? Oh she is a-okay! Feeling much better after your coffee! Hehe."
            Mc "I see, I'm glad."
            menu:
                "When will she leave the hospital?":
                    John "Hmmmmm. We still don't know, could be a while though."
                    Mc "Hm..."
                    menu:
                        "Why is she there?":
                            hide kid_normal
                            show kid_sad at Position(xpos = 0.70)
                            John "..."
                            "{i} Maybe too soon..."
                            Mc "Well what is it gonna be today?"
                        "{i}Better leave it at that.":
                            Mc "Well what is it gonna be today?"
                            hide kid_sad
                            show kid_normal at Position(xpos = 0.70)


    John"Oh yeah I forgot!"
    John"Do you see this?"
    Mc "Yeah, the necklace."
    John "YES! My nana gave it to me."
    Mc "Oh ok."
    Mc "This gonna be another sto-"
    hide kid_normal
    show kid_happy at Position(xpos = 0.70) with hpunch
    John "SO ANYWAY!!!!"
    "{i}Called it."
    John "Yesterday my nana told me a dinossaur story."
    John "She said it was a reward for bringing her coffee so she told me the story of the hero again."
    John "Supposedlyyyy, the hero's wish was to save the queen's grandson from this big evil dinossaur!"
    Mc "Dont you mean drag-"
    hide kid_happy
    show kid_happy at Position(xpos = 0.70) with hpunch
    John "DINOSSAUR!!!"
    Mc "Oooook then."
    hide kid_happy
    show kid_normal at Position(xpos = 0.70)
    John "The hero was given by the coffee mug a super bitter coffee that was disguised with sweetness."
    John "It is said that the coffee was super bitter but then had this white foam on top and chocolate as well!"
    John "HOW COOL IS THAT!!"
    John "Nana said i could only know the rest of the story if I brought her the drink though!"
    John "I'm counting on you coffee hero!!"

    call begin_minigame
    call compara_kid3

    if completed == 1:
        $kid_points += 1

        hide kid_normal
        show kid_drinking at Position(xpos = 0.70)
        John "Hmmmmm!"
        hide kid_drinking
        show kid_happy at Position(xpos = 0.70) with hpunch
        John "Yep this must be it!!!"
        John "Good job coffee hero!"
        Mc "I'm glad I got it right."
        John "Ok hero I gotta run. Way too curious about the ending of the story!"
        Mc "Payment."
        John "Oh... you're right. There you go!"
        Mc "Thank you!"
        hide kid_happy
        show kid_sad at Position(xpos = 0.70)
        John "Oh and ummm. Coffee hero?"
        Mc "Yes?"
        John "Have you ever... lost something forcefully?"
        Mc "How so?"
        John "Like you never did anything to lose it."
        John "And... you can't do anything while you lose it..."
        menu:
            "Is everything ok?":
                John "Just... forget it. It's nothing."
                hide kid_sad
                show kid_happy at Position(xpos = 0.70)
                John "Bye Hero!"
                hide kid_happy

            "Yes, I have.":
                John "Hm... I see. Did you find it?"
                menu:
                    "No.":
                        John "I see..."
                        hide kid_sad
                        show kid_happy at Position(xpos = 0.70)
                        John "Well I gotta go!"
                        John "Bye Hero!"
                        hide kid_happy

                    "Yes":
                        hide kid_sad
                        show kid_happy at Position(xpos = 0.70)
                        John "That's good! That's very good!"
                        John "Well I gotta go!"
                        John "Bye Hero!"
                        hide kid_happy


            "No I haven't.":
                John "Oh... I'm sorry I asked a weird question."
                hide kid_sad
                show kid_happy at Position(xpos = 0.70)
                John "Well I gotta go!"
                John "Bye Hero!"
                hide kid_happy

            "...":
                John "Well I can never get a word out of you can I, hehe."
                hide kid_sad
                show kid_happy at Position(xpos = 0.70)
                John "Well I gotta go!"
                John "Bye Hero!"
                hide kid_happy

        if completed == 0:
            hide kid_normal
            show kid_drinking at Position(xpos = 0.70)
            John "Hmmmmm!"
            hide kid_drinking
            show kid_sad at Position(xpos = 0.70)
            John "I don't think this is it."
            Mc "I'm sorry little guy..."
            hide kid_sad
            show kid_normal at Position(xpos = 0.70)
            John "Oh no problem. Nana probably wants this as well. She will be happy don't worry!"
            Mc "But what about the story?"
            John "Dont worry really. She might tell me a new one!"
            Mc "You are always happy huh?"
            John "I... I guess."
            John "Welp, gotta run! Nana doesn't like cold drinks!"
            hide kid_happy
            show kid_sad at Position(xpos = 0.70)
            John "Oh and ummm. Coffee hero?"
            Mc "Yes?"
            John "Have you ever... lost something forcefully?"
            Mc "How so?"
            John "Like you never did anything to lose it."
            John "And... you can't do anything while you lose it..."
            John "You know what forget I asked!"
            hide kid_sad
            Mc "Hey wai-"

        "{i} And he's gone. There's something more about him."
        return

<<<<<<< HEAD
    return

label kid_3_2:
=======
label kid_3_2:

>>>>>>> main
    "{i}Hmm it's quite now."
    "{i}There's something missing, something... noisy."
    John"HEYYYYYYYYYYYYYY!"
    "{i} I knew it."
    show kid_happy in Position(xpos = 0.7) with hpunch
    John"How are you doing coffee hero?!"
    menu:
        "Hi kiddo":
            John "Awwww, c'mon I'm not a kid I'm your partner"
            hide kid_happy
            show kid_normal in Position(xpos = 0.7)

        "Hi John":
            hide kid_happy
            show kid_disgusted in Position(xpos = 0.7)
            John "Ahhhhh, I can't get used to yu calling me that."
            hide kid disgusted
            show kid_normal in Position(xpos = 0.7)

        "Hi Dream":
            John"Hello hero!! You remembered my name"
            hide kid_happy
            show kid_normal in Position(xpos = 0.7)

        "...":
            John"One day hero, one day I wil get a reaction from you!"
            hide kid_happy
            show kid_normal in Position(xpos = 0.7)
    John "Oh yeah here."
    Mc "Oh, you decided to pay."
    John "Yeah, nana gave me an earful when I came back yesterday and still had the money."
    John "I sweear it wasn't on purpose!"
<<<<<<< HEAD
=======



>>>>>>> main

    return

label kid_4:

    return
