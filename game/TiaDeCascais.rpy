label TiaDeCascais:

    if day == 1:
        call TiaDeCascais_1 from _call_TiaDeCascais_1
    elif dia == 2:
        if tia_points == 0:
            call TiaDeCascais_2_1 from _call_TiaDeCascais_2_1
        else:
            call TiaDeCascais_2_2 from _call_TiaDeCascais_2_2
    elif dia == 3:
        if tia_points == 0 or tia_points == 1:
            call TiaDeCascais_3_1 from _call_TiaDeCascais_3_1
        else:
            call TiaDeCascais_3_2 from _call_TiaDeCascais_3_2
    elif dia == 4:
        if tia_points == 0 or tia_points == 1:
            call TiaDeCascais_4_1 from _call_TiaDeCascais_4_1
        else:
            call TiaDeCascais_4_2 from _call_TiaDeCascais_4_2

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
            Tc "Say \"hi\" Cookie!"
            Co "..."
            Tc "Good job!"
            "{i}What in the world…"
            "{i}Well, I’ve always been a cat person."
            "{i}Maybe that’s why I don’t get it."

        "I must say I agree":
            Tc "Of course! Who wouldn’t?"
            Tc "All the leaves falling."
            Tc "Little Cookie throws herself into those piles of leaves."
            Tc "He ABSOLUTELY loves those."
            Mc "That’s very nice to hear ma’am."

        "...":
            "{i}This lady as so much energy"
            "{i}It’s actually hard to keep myself in the conversation"

    Mc "I’m glad you’re enjoying this time of the year."
    Mc "So, what can I get you?"
    Tc "I want something…. sweet."
    Tc "Something REALLY sweet."
    Tc "Like, REALLY REALLY sweet."
    Mc "Ok, ma’am, give me a second."
    "{i}God, this lady must have a constant sugar rush."
    "{i}What should I make her?"

    #call begin_minigame

    if coffee_right == 1:
        $ tia_points += 1

        Tc "Hmm!!"
        Tc "Yes! This is amazing!"
        Tc "It has just the right sweetness."
        Tc "Do you want to try Little Cookie?"
        Co "..."
        Tc "Yes, I don’t think you should drink it either."
        Mc "I’m glad you enjoy it."

    elif coffee_right == 0:

        Tc "Ahhhh!"
        Tc "This is too bitter!"
        Tc "I can’t drink this!"
        Tc "It’s absolutely unbearable!"
        Mc "I’m really sorry ma’am!"
        Mc "I thought it was sweet enough for you."
        Tc "I told you to make something REALLY sweet."
        Tc "But it’s fine… I guess."
        Tc "I’ll try to have some sips."

    Tc "How long has this been open?"
    Mc "Some weeks."
    Mc "I thought the park needed a quiet place from all the noise around the city."
    Tc "You don’t like noise, is that it?"
    Mc "No, that’s not necessarily it."
    Mc "I just think it’s nice to have a quiet place to rest after a hard day of working."
    Tc "What you need is a good party."
    Tc "Everyday ends well if you party a little."
    Mc "Ahah, I don’t think that’s for me ma’am."
    Tc "You just haven’t tried it yet."
    Tc "I think I’m leaving darling."
    Tc "Thank you for the coffee."

    if coffee_right == 0:
        Tc "Even though it wasn’t the way I wanted."

    Tc "Here’s the money."
    Mc "Thank you so much ma’am."

    if coffee_right == 0:
        Mc "Even though I messed up your coffee."

    Tc "Just get it the next time, please."
    Mc "Yes, of course."
    Mc "Can I get your name ma’am?"
    Tc "Susan."
    Mc "Thank you Susan. Enjoy the rest of your day."
    Tc "Goodbye darling!"

    return


label TiaDeCascais_2_1:
    # points accepted: 1

    scene general_background

    Tc "Well, hello!"
    Mc "Hello Mrs. Susan."
    Mc "How is your day going?"
    Tc "It’s going very well, thank you darling."
    Tc "I’m still a little bit tired from yesterday’s party."
    Tc "But besides that, everything’s going well."

    menu:
        "How was the party?":
            Tc "The party was nice."
            Tc "I can’t say it was the highlight of this week"
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
    Tc "My body wasn’t feeling it last night."
    Tc "It left a bitter taste in my mouth…"
    Mc "Just like coffee…"
    Tc "What did you say?"
    Mc "Nothing. Nothing really."
    Tc "As I was saying, something was wrong."
    Tc "But I couldn’t quite get what."
    Mc "Sometimes the little things in our life are the ones who make the difference in the end."
    Tc "Hmm… I hope my party spirit gets back tonight."
    Tc "Well, time to have a drink."
    Mc "Of course ma’am."
    Mc "What can I get you?"
    Tc "I would like something very sweet."
    "{i}Who could have guessed."
    Tc "But.. not that sweet."
    "{i}I guess not me."
    Tc "Do you get what I’m saying?"
    Mc "So, less sweet than yesterday, but still sweet."
    Tc "Yes, but the sweet part is important."
    Mc "Ok, just a second."

    #call coffee_begin

    if coffee_right == 1:
        $ tia_points += 1

        Tc "Hmmm!"
        Tc "It’s perfect!"
        Tc "It’s sweet, but I can taste a little bitterness from the coffee."
        Mc "I’m glad you enjoy it."
        Mc "I didn’t make it very bitter because I know you prefer your coffee sweet."
        Tc "Yes. It's perfect. Thank you!"
        Tc "What do you think Little Cookie?"
        Co "..."
        Tc "Yes, I agree."
        Tc "Has the business been running nicely?"
        Mc "It has been good, overall."
        Tc "That’s good. You were right, this park really needed a place like this"
        Mc "Thank you, that means a lot."
        Tc "Business is hard. Keep your head up."
        Mc "Will do ma’am."
        Tc "Here’s the money."
        Mc "Thank you, let me just grab the change."
        Tc "No need darling."
        Mc "Thank you so much."
        Tc "Today I have more parties to attend."
        Tc "Goodbyeee darling."
        Mc "See you tomorrow Mrs. Susan."

    elif coffee_right == 0:

        Tc "This is far from the sweetness I asked for."
        Tc "Don’t you think Little Cookie?."
        Tc "You can smell it, can you?"
        Ck "..."
        Mc "I’m really sorry ma’am!"
        Mc "I thought it would be the right amount."
        Mc "I guess I was wrong."
        Mc "Can I offer you another coffee?"
        Tc "It’s fine, I also can’t be here much longer."
        Mc "Understandable."
        Mc "Again, I’m really sorry ma’am."
        Tc "Just try to pay more attention next time."
        Tc "Has the business been running nicely?"
        Mc "It has been good, overall."
        Tc "That’s good. You were right, this park really needed a place like this"
        Mc "Thank you, that means a lot."
        Tc "Business is hard. Keep your head up."
        Tc "You need to get these coffees right every time."
        Mc "I know. I’ve been trying. Thank you."
        Tc "I see, I see."
        Tc "Well, I have parties to attend, so I can’t be here much longer."
        Tc "Here’s your money."
        Tc "I’ll see you tomorrow."
        Mc "See you tomorrow Mrs. Susan."


    return


label TiaDeCascais_2_2:
    # points accepted: 0

    scene general_background

    Tc "Well, hello!"
    Mc "Hello Mrs. Susan."
    Mc "How is your day going?"
    Tc "I’m doing fine, thank you"
    Tc "Still a little bit nauseous from your coffee yesterday."
    Tc "And tired from yesterday’s party."
    Tc "But besides that, everything’s going well."
    Mc "Glad to hear that Mrs. Susan."

    menu:
        "How was the party?":
            Tc "The party was absolutely on spot."
            Tc "Everyone was having fun, it was a blast."
            Tc "Little Cookie played with the other pomeranians."
            Tc "Everyone loves Little Cookie."
            Mc "I’m sure they do."

        "Yes, you seem a little down today.":
            Tc "Do I look tired?"
            Tc "No, I can’t let that pass to the outside!"
            Tc "Please don’t tell anyone!"
            Mc "Of course not, don’t worry."
            Tc "Thank you darling, appreciate it."

    Mc "So, Mrs. Susan, What can I get you?"
    Tc "Well… you know the answer."
    Tc "Give me something sweeeeet!"
    Tc "I need some sugar to get myself ready for today’s party!"
    Mc "As you wish."

    # call coffee_begin

    if coffee_right == 1:
        $ tia_points += 1

        Tc "..."
        Tc "It’s perfect!"
        Tc "It has just the right sweetness."
        Mc "I’m glad you like it."
        "{i}Even though it’s almost pure sugar."
        Tc "Has the business been running nicely?"
        Mc "It has been good, overall."
        Tc "That’s good. You were right, this park really needed a place like this"
        Mc "Thank you, that means a lot."
        Tc "Business is hard. Keep your head up."
        Mc "Will do ma’am."
        Tc "Here’s the money."
        Mc "Thank you, let me just grab the change."
        Tc "No need darling."
        Mc "Thank you so much."
        Tc "Today I have more parties to attend."
        Tc "Goodbyeee darling."
        Mc "See you tomorrow Mrs. Susan."

    elif coffee_right == 0:

        Tc "..."
        Tc "What’s this?"
        Tc "This is undrinkable."
        Tc "It’s so bitter!"
        Mc "Oh no! I’m so so sorry Mrs. Susan!"
        Mc "I really thought I nailed it this time."
        Tc "O my god, it feels like my tongue will fall off."
        "{i}Ok, now she’s exaggerating…"
        Tc "Please, can you make a coffee or not?"
        Mc "I’ll do it better next time. I’m really sorry."
        Tc "Thank you. Sorry if I’m being rude, but my palette is kind of sensitive."
        Mc "It’s fine, it’s my fault."
        Tc "Here’s your money."
        Mc "Thank you."
        Tc "See you tomorrow darling."
        Mc "Have a nice party today."


    return


label TiaDeCascais_3_1:
    # points accepted: 2

    scene general_background

    Tc "Hello Darling. How are you today?"
    Mc "I’m fine, thanks. What about you?"
    Tc "I’m ok."
    Tc "I’ve been walking Little Cookie around this afternoon."
    Tc "However, I still have a bitter taste in my mouth from last night."
    Tc "Yesterday’s party was weird again."
    Tc "I didn’t feel I quite belonged there."
    Tc "It was really strange."

    menu:
        "If you felt weird about it, you shouldn't go anymore.":
            Tc "But…"
            Tc "That’s part of who I am."
            Tc "I can’t let that go away."
            Mc "Why?"
            Tc "Because…"
            Tc "..."
            Tc "I don’t know…"
            Mc "You should give it some thought ma’am."
            Mc "If it doesn’t provide you any form of happiness, maybe it’s not worth it."
            Tc "Yes, I think you’re right."

        "Maybe you’ll feel better next time.":
            Tc "Will I?"
            Tc "I guess the only way to prove that is to go again tonight."

    Mc "What are those parties like?"
    Tc "You know…"
    Tc "Lots of drinks…"
    Tc "A pool…"
    Tc "And a dog food buffet!"
    Tc "If there’s no dog food buffet you can bet I’m not going to that party."
    Tc "Isn’t that right Little Cookie?"
    Ck "..."
    Tc "Ohh I know I know."
    Tc "Well, enough about parties."
    Tc "Today I want a good coffee with just a little bit of sugar."
    Tc "Something not absurdly sweet."
    Tc "And maybe I’ll try some milk."
    Mc "Sure. I’ll be right back."

    # call coffee_begin

    if coffee_right == 1:
        $ tia_points += 1

        Tc "..."
        Tc "Wow! This is very pleasant."
        Tc "Thank you!"
        Tc "I like this bitter taste, it’s very interesting"
        Mc "It’s the true flavor of coffee ma’am."
        Tc "Fascinating."
        Tc "How do you do it?"
        Mc "Do what?"
        Tc "The coffee darling. How is it made?"
        Mc "Oh, it’s kind of a long list."
        Mc "There are lots of ways to brew coffee."
        Mc "Here in the roulote I use an espresso machine."
        Mc "But you can have a V60 to pour over, a Chemex or a Kalista."
        Mc "You can also have it pressed with a French Press or an Aeropress."
        Tc "I like that Chemex one, the name has some charm to it."
        Mc "Each one has a different process and subtle differences to the flavor."
        Mc "After that you can do thousands of combinations with milk, toppings and many other things."
        Mc "Many coffee shops around the world use different things to make their coffee its own."
        Tc "That’s lovely."
        Tc "Thank you for the explanation"
        Tc "I think I’ll have another walk in the park today."
        Tc "You aren’t tired, are you Little Cookie?"
        Ck "..."
        Tc "Who’s adorable? Who’s adorable?"
        Tc "Yes, it’s you!"
        Tc "Here’s the payment."
        Tc "And here’s a little tip."
        Mc "Thank you so much Mrs. Susan."
        Tc "See you tomorrow darling."
        Mc "Have a nice day."

    elif coffee_right == 0:

        Tc "..."
        Tc "I don’t think this is quite what I was looking for."
        Tc "The sweetness is not exactly what I was hoping to get."
        Mc "Sorry, maybe I made it too sweet or too bitter?"
        Tc "It’s fine, don’t worry."
        Tc "I’ve been trying to try different types of coffee, so I don’t mind it that much."
        Tc "How do you do it?"
        Mc "Do what?"
        Tc "The coffee darling. How is it made?"
        Mc "Oh, it’s kind of a long list."
        Mc "There are lots of ways to brew coffee."
        Mc "Here in the roulote I use an espresso machine."
        Mc "But you can have a V60 to pour over, a Chemex or a Kalista."
        Mc "You can also have it pressed with a French Press or an Aeropress."
        Tc "I like that Chemex one, the name has some charm to it."
        Mc "Each one has a different process and subtle differences to the flavor."
        Mc "After that you can do thousands of combinations with milk, toppings and many other things."
        Mc "Many coffee shops around the world use different things to make their coffee its own."
        Tc "That’s lovely."
        Tc "Thank you for the explanation."
        Mc "You’re welcome."
        Tc "I think I’ll take another walk with Little cookie."
        Tc "Here’s your money."
        Mc "Thank you Mrs. Susan."
        Tc "I’ll see you tomorrow."
        Mc "Until tomorrow."


    return


label TiaDeCascais_3_2:
    # points accepted: 0, 1

    scene general_background

    Tc "Hello Darling. How are you today?"
    Mc "I’m fine, thanks. What about you?"
    Tc "I’m ok."
    Tc "I’ve been walking Little Cookie around this afternoon."
    Mc "That’s nice to hear."
    Mc "How was the party last night? "
    Tc "It was a strange one, I wasn’t really feeling it to be honest."
    Tc "I felt strange, I don’t know."

    menu:
        "If you felt weird about it, you should reconsider going or not.":
            Tc "I’ve always liked those parties."
            Tc "Why would I start disliking them now?"
            Mc "I don’t know."
            Tc "I don’t know either."
            Tc "But maybe you’re right, maybe I shouldn’t go to every party if I don’t feel like it."

        "Maybe you’ll feel better next time.":
            Tc "Will I?"
            Tc "I guess the only way to prove that is to go again tonight."

    Mc "What are those parties like?"
    Tc "You know…"
    Tc "Lots of drinks…"
    Tc "A pool…"
    Tc "And a dog food buffet!"
    Tc "If there’s no dog food buffet you can bet I’m not going to that party."
    Tc "Isn’t that right Little Cookie?"
    Ck "..."
    Tc "Ohh I know I know."
    Tc "Well, enough about parties."
    Tc "Today I’d like a good milky coffee with a good amount of sugar."
    Tc "I don’t want it that sweet, but still decently sweet."
    Mc "Sure. I’ll be right back."

    # call coffee_begin

    if coffee_right == 1:
        $ tia_points += 1

        Tc "..."
        Tc "Wow! This is very pleasant, you nailed it."
        Tc "Thank you!"
        Mc "I’m glad to hear that."
        Tc "How do you do it?"
        Mc "Do what?"
        Tc "The coffee darling. How is it made?"
        Mc "Oh, it’s kind of a long list."
        Mc "There are lots of ways to brew coffee."
        Mc "Here in the roulote I use an espresso machine."
        Mc "But you can have a V60 to pour over, a Chemex or a Kalista."
        Mc "You can also have it pressed with a French Press or an Aeropress."
        Tc "Hmm too many words for my own dictionary."
        Tc "However I do like the Chellex…. that Kemix one "
        Mc "The Chemex."
        Tc "Yes, that one, it sounds very french, I like it."
        Mc "Each one has a different process and subtle differences to the flavor."
        Mc "After that you can do thousands of combinations with milk, toppings and many other things."
        Mc "Many coffee shops around the world use different things to make their coffee its own."
        Tc "Thank you for the explanation my darling."
        Tc "I think I’ll have another walk in the park today."
        Tc "You aren’t tired, are you Little Cookie?"
        Ck "..."
        Tc "Who’s adorable? Who’s adorable?"
        Tc "Yes, it’s you!"
        Tc "Here’s the payment."
        Mc "Thank you so much."
        Tc "See you tomorrow."
        Mc "Goodbye Mrs. Susan."

    elif coffee_right == 0:

        Tc "..."
        Tc "Hmm I don’t think you nailed it."
        Tc "Something’s off, it’s not how I like it."
        Mc "Oh, sorry, can I take you another one?"
        Tc "No, it’s fine, I’ll try to drink it."
        Tc "Even though it’s not amazing, how do you do it?"
        Mc "Do what?"
        Tc "The coffee darling. How is it made?"
        Mc "There are lots of ways to brew coffee."
        Mc "Here in the roulote I use an espresso machine."
        Mc "But you can have a V60 to pour over, a Chemex or a Kalista."
        Mc "You can also have it pressed with a French Press or an Aeropress."
        Tc "Hmm too many words for my own dictionary."
        Tc "However I do like the Chellex…. that Kemix one "
        Mc "The Chemex."
        Tc "Yes, that one, it sounds very french, I like it."
        Mc "Each one has a different process and subtle differences to the flavor."
        Mc "After that you can do thousands of combinations with milk, toppings and many other things."
        Mc "Many coffee shops around the world use different things to make their coffee its own."
        Tc "Thank you for your explanation."
        Tc "I think I’ll have another walk in the park today."
        Tc "Before it’s time to party again!"
        Tc "You aren’t tired, are you Little Cookie?"
        Ck "..."
        Tc "Who’s adorable? Who’s adorable?"
        Tc "Yes, it’s you!"
        Tc "Here’s the payment."
        Mc "Thank you so much."
        Tc "See you tomorrow."
        Mc "Goodbye Mrs. Susan."


    return


label TiaDeCascais_4_1:
    # points acepted: 2, 3

    scene general_background

    Tc "Hello! How are you today?"
    Tc "Is everything fine?"
    Mc "Hello Mrs. Susan."
    Mc "I’m fine, thank you very much"
    Mc "What about you?"
    Mc "You look very happy today."
    Tc "You think so?"
    Tc "Well, I suppose you’re right."
    Tc "The day has been amazing!"
    Tc "I’ve been walking Little Cookie around the park for a while."
    Tc "She’s been loving it!"
    Ck "..."
    Mc "I’m very glad to hear that."
    Mc "So, how was the party yesterday?"
    Tc "Oh, about that."
    Tc "I didn’t even enter."
    Tc "I was at the door for a few minutes."
    Tc "And I started to think I didn’t really want to go drinking and partying in the pool."
    Tc "All I craved was a nice cup of coffee by the fireplace."
    Tc "And that’s what I ended up doing that evening."
    Tc "I went to the attic and got some old coffee utensils from my father."
    Tc "And I made a nice coffee with them"
    Tc "It wasn’t very good to be honest."
    Tc "But the mood was more than enough."
    Mc "I’m glad you ended up having a relaxing evening."
    "{i}This lady is a different person from the one I met days ago."
    "{i}She was… bitter."
    "{i}Now she’s sweet."
    "{i}And her coffee has been getting more bitter, stronger."
    "{i}I guess this is one of those coincidences the universe throws at us once in a while."
    Mc "So, Susan, what can I get you today?"
    Tc "I’d like something simple. No sugar please."
    Mc "No sugar?"
    Tc "Yes. I want to feel the coffee fragrance at its fullest."
    Mc "That means a lot to a coffee brewer."
    Mc "Even though there’s no right or wrong way to drink your coffee."
    Mc "Give me a second."

    # call coffee_begin

    if coffee_right == 1:
        $ tia_points += 1

        Tc "..."
        Tc "It’s amazing."
        Tc "Such a simple drink, yet so many different nuances in the taste."
        Tc "Thank you so much."
        Mc "You’re welcome.."
        Mc "If Little Cookie could drink coffee, I bet she would love it."
        Tc "Ahahaha. Yes, I do agree with that."
        Tc "Tell me something, do you sell coffee beans here?"
        Mc "Yes, we do sell coffee beans from farmers all around the world."
        Tc "Amazing. I’d like to buy one package."
        Tc "What do you recommend?"
        Mc "Hmm… I’d say this one from the Equator is always a safe pick."
        Tc "I’ll trust your judgment."
        Tc "How much is it?"
        Mc "The coffee beans are 15$, plus the usual price of the coffee."
        Tc "There you go."
        Mc "now you can start making your own specialty coffee at home."
        Mc "But please, come visit the roulote once in a while ahaha."
        Tc "Ahaha, of course, don’t worry."
        Tc "Well, I think I should go."
        Mc "See you tomorrow Susan."
        Tc "Goodbye."
        "{i}I'm glad this lady found something comforting in this roulote."
        "{i}The breeze from the afternoon hits like anything else around here."
        "{i}May these red and yellow days last until the season’s end"
        "{i}And the autumn leaves fall from the trees around the park."

    elif coffee_right == 0:

        Tc "..."
        Tc "I think this is a bit too sweet."
        Tc "I like it, don’t worry."
        Tc "I was just hoping it could be a little bitter."
        Mc "I’m sorry. Can I get you another one?"
        Mc "It’s on the house."
        Tc "That’s very sweet of you. I’ll accept it."
        Mc "I’ll be right back."

        # call coffee_begin

        if coffee_right == 0:
            $ tia_points += 1

            Tc "..."
            Tc "It’s amazing."
            Tc "Such a simple drink, yet so many different nuances in the taste."
            Tc "Thank you so much."
            Mc "You’re welcome.."
            Mc "If Little Cookie could drink coffee, I bet she would love it."
            Tc "Ahahaha. Yes, I do agree with that."
            Tc "Tell me something, do you sell coffee beans here?"
            Mc "Yes, we do sell coffee beans from farmers all around the world."
            Tc "Amazing. I’d like to buy one package."
            Tc "What do you recommend?"
            Mc "Hmm… I’d say this one from the Equator is always a safe pick."
            Tc "I’ll trust your judgment."
            Tc "How much is it?"
            Mc "The coffee beans are 15$, plus the usual price of the coffee."
            Tc "There you go."
            Mc "now you can start making your own specialty coffee at home."
            Mc "But please, come visit the roulote once in a while ahaha."
            Tc "Ahaha, of course, don’t worry."
            Tc "Well, I think I should go."
            Mc "See you tomorrow Susan."
            Tc "Goodbye."
            "{i}I'm glad this lady found something comforting in this roulote."
            "{i}The breeze from the afternoon hits like anything else around here."
            "{i}May these red and yellow days last until the season’s end"
            "{i}And the autumn leaves fall from the trees around the park."

        elif coffee_right == 0:

            Tc "..."
            Tc "I’m sorry, maybe it’s my palette? I don’t know."
            Tc "It’s still a bit sweet."
            Mc "Oh, I’m so sorry again!"
            Tc "Don’t worry, it’s fine."
            Tc "Everyone has bad days, even coffee brewers."
            Tc "I still like it, so there’s no problem."
            Mc "Thank you Susan."
            "{i}God, how did I fail that coffee…"
            Tc "Tell me something, do you sell coffee beans here?"
            Mc "Yes, we do sell coffee beans from farmers all around the world."
            Tc "Amazing. I’d like to buy one package."
            Tc "What do you recommend?"
            Mc "Hmm… I’d say this one from the Equator is always a safe pick."
            Tc "I’ll trust your judgment."
            Tc "How much is it?"
            Mc "The coffee beans are 15$, plus the usual price of the coffee."
            Tc "There you go."
            Mc "now you can start making your own specialty coffee at home."
            Mc "But please, come visit the roulote once in a while ahaha."
            Tc "Ahaha, of course, don’t worry."
            Tc "Well, I think I should go."
            Mc "See you tomorrow Susan."
            "{i}I'm glad this lady found something comforting in this roulote."
            "{i}The breeze from the afternoon hits like anything else around here."
            "{i}May these red and yellow days last until the season’s end"
            "{i}And the autumn leaves fall from the trees around the park."


    return


label TiaDeCascais_4_2:
    # points accepted: 0, 1

    scene general_background

    Tc "Hello! How are you today?"
    Mc "I’m fine, thanks. What about you?"
    Tc "I’m having a wonderful day."
    Mc "You look very happy today."
    Tc "You think so?"
    Tc "Well, I suppose you’re right."
    Tc "Little Cookie has been such a good girl today."
    Tc "Who is the best girl?"
    Tc "It’s you!"
    Ck "..."
    Mc "How did you feel about yesterday’s party?"
    Tc "Kinda bad."
    Tc "I didn’t want to party yesterday."
    Tc "But I still went. It was a dumb decision."
    Tc "Uff, whatever, it’s done"
    Tc "Also last night I found some old coffee tools my father used to use."
    Mc "Oh really? how was it like?"
    Tc "It was a smaller version of the one you have but older and dustier"
    Tc "My hair got all dirty in that attic!"
    Mc "So, it was an espresso machine."
    Tc "I guess… I don’t know"
    Mc "It was probably it."
    Mc "So, what can I get you today?"
    Tc "Hmm, I want something a little bit sweet, just a little."
    Mc "Ok, a second."

    # call coffee_begin

    if coffee_right == 1:
        $ tia_points += 1

        Tc "..."
        Tc "It’s amazing."
        Tc "Such a simple drink, yet so many different nuances in the taste."
        Tc "Thank you so much."
        Mc "You’re welcome.."
        Mc "If Little Cookie could drink coffee, I bet she would love it."
        Tc "Ahahaha. Yes, I do agree with that."
        Tc "You sell coffee here, right?"
        Mc "Yes, we do."
        Mc "We have coffee beans from different producers around the world."
        Mc "From Colombia, Vietnam, Ethiopia and Nicaragua."
        Tc "That’s so far away."
        Tc "Little Cookie would be scared of a flight like that."
        Tc "But that’s impressive."
        Mc "It’s my job knowing about these things."
        Tc "Thank you for the coffee, here’s the money."
        Tc "You can keep the change."
        Mc "Thank you so much Mrs. Susan."
        Mc "I hope I’ll see you around soon."
        Tc "Goodbye darling."

    elif coffee_wrong == 0:

        Tc "..."
        Tc "Ok, this is definitely not what I was looking for."
        Tc "It was almost right, but still not the right sweetness"
        Mc "Ahh, I failed again."
        Tc "Everyone has bad days darling."
        Tc "Even I have those sometimes."
        Mc "I appreciate your words Mrs. Susan."
        Tc "You sell coffee here, right?"
        Mc "Yes, we do."
        Mc "We have coffee beans from different producers around the world."
        Mc "From Colombia, Vietnam, Ethiopia and Nicaragua."
        Tc "That’s so far away."
        Tc "Little Cookie would be scared of a flight like that."
        Tc "But that’s impressive."
        Mc "It’s my job knowing about these things."
        Tc "Thank you for the coffee, here’s the money."
        Mc "Thank you. Have a great day."
        Tc "Goodbye."


    return
