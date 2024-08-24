define b = Character("Benny",color="97F998")
define e = Character("Edelweiss",color="77F998")
define l = Character("Landlord",color="6F95BB")
define m = Character("Melphys",color="E42E06")
define mcn = Character("[mcname]",color="C8FFC8")
define mcs = Character("[mcsurname]",color="C8FFC8")


label splashscreen:
    scene black
    with Pause(1)

    show text "Niminie Presents..." with moveouttop
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    return

label start:

        stop music

        $ mcname = renpy.input("What is your name human?", length=12)
        if mcname == "":
            $mcname = "Yuki"

        $ mcsurname = renpy.input("And your surname?", length=12)
        if mcsurname == "":
            $mcsurname = "Tsunoda"

        scene bg appartn
        with dissolve
        play music "audio/clearair.mp3"

        "YOUR APARTMENT - LATE EVENING"

        mcn "..."
        "Being an adult sucks."
        "I litteraly just came back from work and-"
        show landlord mad at center with fade:
            zoom 0.5
        l "[mcname]."
        l "You remember what day it is today RIGHT?"
        mcn "Well...yeah, I know but please can't you give me more time to-"
        l "Not this time young one, I may be generous but NOW this is too much."
        mcn "I swear I'll pay everything back to you so please don't kick me out toda-!"
        l "THIS PLACE is not your appartment, not anymore since you just can't seem afford it any longer."
        l "Besides, someone has gotten interested by getting a room appartement here and trust me, their proposal is greater than anything I could expect from you."
        "...What?"
        mcn "But I'll have nowhere else to go and I still haven't been paid yet...Please !"
        l "That's what you always say, and as result : no paid rent."
        "I start to flinch, looking at him with a despaired look."
        "he sighs, his eyebrows furrowing even more."
        l "Okay, three days. That's it. No more excuses."
        hide landlord angry
        with dissolve
        "With that said, the landlord furiously got out of my appartment, his steps echoing inside the whole building."
        "I sigh, exhausted by the weight of these hard news."
        mcn "So... 3 days uh?"
        mcn "It's gonna be though to earn more money, especially since I work in..."

        menu:
            "A modest coffee shop":
                "It's actually a good first experience for me and the coffee owner was and still is really nice with me."
                "However, due to the lack of customers these months, I got paid less and less."
                "Everytime he gives me my salary, he apologizes constantly."
                "Unfortunatly, kindness doesn't pay the bills."
            "The local bookstore":
                "Apparently it was constructed on the top of an ancient cimetery. "
                "Yeah, how charming."
                "It's the kind of place where you instantly feel the silence deafening you, with shelves packed full of old crackeled books."
                "The aged woman in charge of it often looks absent or is in her own little world, but she actually is adorable."
                "Unfortunatly, because of the lack of customers these months, I got paid less and less by her."
        mcn "Even if I already work full time it won't be enough to repay my debt."
        mcn "But honestly... is that even possible to find another job that fast?"
        mcn "Maybe I should try to sell my lung to the black market now that I fell so low...Ouch."
        "I look at my huge collection of horror mangas and comics, paranormal films and miniature statues representing various fantasy creatures all over my room"
        "I've always been a huge fan of basically anything that was related to the unreal."
        "And I was kinda renied for that among my pairs but...Well, now it doesn't matter that much I'll never see their faces again."
        "Years of dedictation were mobilized in order to expose all of these precious treasures proudly into my room."
        mcn "But now that i'm too short on money...I'll have to ..."
        "No..."
        "I NEED to sell them."
        "..."
        mcn"Yeah...being an adult TRULY sucks."

        show bg appartj
        with fade

        "YOUR APARTMENT - NEXT MORNING"
        mcn"My eyes hurt."
        "I spent all the night looking for a sustainable job, but in the end I didn't have the right to be picky. "
        mcn"Ugh..."
        "At this point I just automatically sent my resume to whatever seemed like a job application, while often refreshing my mailbox, praying for a miracle to happen after hours of spamming."
        "And then..."
        with hpunch
        "{i} TING~ {/i}"
        mcn"?!"
        "I clicked fastly onto my mailbox page at the sudden sound of a notification."

        stop music

        return
