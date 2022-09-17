label TiaDeCascais:

    if tia_points == 1:
        call TiaDeCascais_1 from _call_TiaDeCascais_1
    elif tia_points == 2:
        call TiaDeCascais_2 from _call_TiaDeCascais_2
    elif tia_points == 3:
        call TiaDeCascais_3 from _call_TiaDeCascais_3
    elif tia_points == 4:
        call TiaDeCascais_4 from _call_TiaDeCascais_4


    return

label TiaDeCascais_1:

    scene general_background

    Tc "Hello, Darling!"
    Mc "Hello Ma’am. How are you today?"
    Tc "Wonderful! I love these autumn days!"
    Tc "And the summer ones, and the spring."
    Tc "And don’t get me started on winter clothes!"
    Tc "But autumn takes the cake."
    Tc "Little Cookie loves to run around the park in times like these."

    menu:
        "Little Cookie?":
            Tc "Yes, Little Cookie!"
            Tc "This beautiful ball of fur!"
            Tc "Say “hi” Cookie!"
            Lk "..."
            Tc "Good job!"
            "What in the world…"
            "Well, I’ve always been a cat person."
            "Maybe that’s why I don’t get it."

        "I must say I agree ma’am.":
            Tc "Of course! Who wouldn’t?"
            Tc "All the leaves falling."
            Tc "Little Cookie throws herself into those piles of leaves."
            Tc "He ABSOLUTELY loves those."
            Mc "That’s very nice to hear ma’am."

        "...":
            "This lady as so much energy."
            "It's actually hard to keep myself in the conversation."


    Mc "I’m glad you’re enjoying this time of the year."
    Mc "So, what can I get you?"
    Tc "I want something..."
    Tc "Something sweet."
    Tc "Something REALLY sweet."
    Tc "Like, REALLY REALLY sweet."
    Mc "Ok, ma’am, give me a second."
    "God, this lady must have a constant sugar rush."
    "What should I make her?"

    # DECIDE COFFEE RIGHT VARIABLE


    return

label TiaDeCascais_2:

    scene general_background

    Tc "Well, hello!"
    Mc "Hello ma’am."
    Mc "How is your day going?"
    Tc "It’s going very well, thank you."
    Tc "I’m still a little bit tired from yesterday’s party."
    Tc "But besides that, everything’s going well."

    menu:
        "How was the party?":
            Tc "The party was nice."
            Tc "I can’t say it was the highlight of this week."
            Tc "But it was a nice event."

        "I’m not really a party type of person.":
            Tc "Yes, I can tell by just talking with you."
            Tc "You seem very calm."
            Tc "Too calm for a socialite’s party."
            Mc "I guess you could say that."
            Tc "It’s right in your face."

        "Yes, you seem a little down today.":
            Tc "Are you serious?!"
            Tc "Can you really tell by just looking?"
            Mc "Don’t worry, it’s barely noticeable."
            Tc "I need to keep my image alive."
            Tc "It’s very important!"
            Mc "Yes, I understand ma’am."

    Tc "However, I must say I really do feel weird."
    Tc "I didn’t feel like I was part of that party yesterday."
    Tc "It left a bitter taste in my mouth…"
    Mc "Just like coffee..."
    Tc "What did you say?"
    Mc "Nothing. Nothing really."
    Tc "Well, let’s get to business."
    Tc "I would like something sweet today."
    Tc "But.. not that sweet."
    Tc "Do you get what I’m saying?"
    Mc "Of course. Just a second."

    # DECIDE COFFEE RIGHT VARIABLE


    return

label TiaDeCascais_3:

    scene general_background

    Tc "Hello Darling. How are you today?"
    Mc "I’m fine, thanks. What about you?"
    Tc "I’m ok."
    Tc "The party was weird again."
    Tc "I didn’t feel I quite belonged there."
    Tc "It was really strange."

    menu:
        "If you feel weird about it, you shouldn't go anymore.":
            Tc "But…"
            Tc "That’s part of who I am."
            Tc "I can’t let that go away."
            Mc "Why?"
            Tc "Because..."
            Tc "..."
            Tc "I don’t know..."
            Mc "You should give it some thought ma'am."
            Tc "Yes, I think you’re right."

        "Maybe you’ll feel better next time.":
            Tc "Will I?"
            Tc "I guess the only way to prove that is to go again tonight."


    Mc "What are those parties like?"
    Tc "You know..."
    Tc "Lots of drinks…"
    Tc "A pool..."
    Tc "And a dog food buffet!"
    Tc "If there’s no dog food buffet you can bet I’m not going to that party."
    Tc "Isn’t that right Little Cookie?"
    Lk "..."
    Tc "Ohh I know I know."
    Tc "Well, enough about parties."
    Tc "Today I want a good coffee with just a little bit of sugar."
    Tc "Something not absurdly sweet."
    Mc "Sure. I’ll be right back."

    # DECIDE RIGHT COFFEE VARIABLE




    return

label TiaDeCascais_4:

    scene general_background

    Tc "Hello! How are you today?"
    Tc "Is everything fine?"
    Mc "Hello ma’am."
    Mc "I’m fine, thank you very much."
    Mc "What about you ma’am?"
    Mc "You look very happy today."
    Tc "You think so?"
    Tc "Well, I think your right."
    Tc "The day has been amazing!"
    Tc "I’ve been walking Little Cookie around the park for a while."
    Tc "She’s been loving it!"
    Ck "..."
    Mc "I’m very glad to hear that."
    Mc "So, how was the party yesterday?"
    Tc "I didn’t even enter."
    Tc "I was at the door for a few minutes."
    Tc "And I noticed I didn’t really want to go drink and party in the pool."
    Tc "All I craved was a nice cup of coffee by the fireplace."
    Tc "And that’s what I ended up doing that evening."
    Tc "It was a pleasant one, no doubt."
    Mc "I’m glad you ended up having a relaxing evening ma’am."
    Tc "Please, call me Susan."
    "This lady is a different person from the one I met days ago."
    "She was… bitter."
    "Now she’s sweet."
    "And her coffee has been getting bitter."
    "I guess this is one of those coincidences the universe throws at us once in a while."
    Mc "So, Susan, what can I get you today?"
    Tc "I’d like something simple. No sugar please."
    Mc "No sugar?"
    Tc "Yes. I want to feel the coffee fragrance at its fullest."
    Mc "That means a lot to a coffee brewer."
    Mc "Give me a second."

    # DECIDE RIGHT COFFEE VARIABLE


    return
