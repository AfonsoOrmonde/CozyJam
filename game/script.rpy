define e = Character("Eileen")


label start:


    #------------------------------- ARC POINTS --------------------------------
    $ tia_points = 0
    $ kid_points = 0
    $ girl_points = 0

    $ day = 1

    # ----------------------------- CHARACTERS ---------------------------------
    define Mc = Character("Barista", who_color="#cc9741")
    define Uk = Character("?", who_color="#cc9741")
    define Tc = Character("Susan", who_color="#cc9741")
    define Kid = Character("Kid", who_color="#cc9741")
    define John = Character("John", who_color="#cc9741")
    define Brit = Character("Girl", who_color="#cc9741")
    define Co = Character("Little Cookie", who_color="#cc9741")


    #--------------------------- BACKGROUND IMAGES -----------------------------
    image general_background = "general_background.png"
    image general_background_kid = "general_background_kid.png"
    image general_background_tia = "general_background_tia.png"
    image general_background_girl = "general_background_girl.png"

    #---------------------------- CHARACTER IMAGES -----------------------------
    image tia_happy = "tia_happy.png"
    image tia_sad = "tia_sad.png"
    image tia_angry = "tia_angry.png"
    image tia_pat = "tia_pat.png"
    image tia_drinking = "tia_drinking.png"
    image tia_sassy = "tia_sassy.png"

    image kid_happy = "kid_happy.png"
    image kid_sad = "kid_sad.png"
    image kid_disgusted = "kid_disgusted.png"
    image kid_normal = "kid_normal.png"
    image kif_drinking = "kid_drinking.png"

    image girl_happy = im.FactorScale("girl_happy.png", 0.45)
    image girl_sad = im.FactorScale("girl_sad.png", 0.45)
    image girl_traumatized = im.FactorScale("girl_traumatized.png", 0.45)
    image girl_normal = im.FactorScale("girl_normal.png", 0.45)
    image girl_drinking = im.FactorScale("girl_drinking.png", 0.45)
    #----------------------------- DAY MANAGMENT -------------------------------
    # DAY 1
    #call girl
    call TiaDeCascais
    #call kid
    $ day += 1

    # DAY 2
    call TiaDeCascais
    #call kid
    $ day += 1

    # DAY 3
    call TiaDeCascais
    $ day += 1

    # DAY 4
    call TiaDeCascais


    return
