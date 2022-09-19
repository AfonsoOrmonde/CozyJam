define e = Character("Eileen")



label start:
    $acucar = 0
    $cafe = 0
    $chantili = 0
    $leite = 0
    $marshmallow = 0
    $chocolate = 0
    $cinnamon = 0
    #call begin_minigame


    #------------------------------- ARC POINTS --------------------------------
    $ tia_points = 1
    $ kid_points = 1
    $ girl_points = 1

    $ day = 1

    # ----------------------------- CHARACTERS ---------------------------------
    define Mc = Character("Barista", who_color="#cc9741")
    define Tc = Character("Socialite", who_color="#cc9741")
    define Kid = Character("Kid", who_color="#cc9741")
    define Phy = Character("Girl", who_color="#cc9741")
    define Lc = Character("Little Cookie", who_color="#cc9741")

    #--------------------------- BACKGROUND IMAGES -----------------------------
    image general_background = "general_background.png"

    #---------------------------- CHARACTER IMAGES -----------------------------
    image tia_happy = "tia_happy.png"
    image tia_sad = "tia_sad.png"
    image kid_happy = "kid_happy.png"
    image kid_sad = "kid_sad.png"
    image girl_happy = "girl_happy.png"
    image girl_sad = "girl_sad.png"

    #--------------------------- INGREDIENTS IMAGES ----------------------------
    # TO DO

    #----------------------------- DAY MANAGMENT -------------------------------
    # DAY 1
    call TiaDeCascais from _call_TiaDeCascais

    # DAY 2

    # DAY 3

    # DAY 4



    return
