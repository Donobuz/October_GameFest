label scene_party:


    if stay_calm >= 3:
        jump winner

    elif freak_out >= 3:
        jump loser

label winner:
    "Camilla takes up the lead naturally, sprinting down the path." with text_dissolve

    "Impressive that she hasn't tripped on anything considering she doesn't have the flashlight." with text_dissolve

    "Jesse is in front of you illuminating the path as you guys make a run for it, the light bobbing violently with each step." with text_dissolve
    stop music fadeout 3.0

    "After a minute, you guys slow down to take a breather." with text_dissolve

    show j_scared at left
    with moveinleft



    play music "../game/assets/music/suspcious.ogg" fadein 3.0 loop

    j_left "That was the most uncool shit I've ever had to go through." with text_dissolve

    mc "I don't even want to know what that was." with text_dissolve

    show c_scared at right
    with moveinright

    c_right "I should have stayed home, and ate my dulces enchilados and minded my business." with text_dissolve

    show j_scared at offscreenleft
    show c_scared at offscreenright
    with dict_emotion_change

    "You look around, spotting a steady glow straight ahead." with text_dissolve

    "{i}Oh no... not again{/i}" with text_dissolve

    mc "Guys, there's more light." with text_dissolve

    show c_terrified at right
    with moveinright

    c_right "Ay! It came back for us! We're gonna die!" with text_dissolve

    show j_neutral at left
    with dict_moveinleft

    j_left "Wait, that looks like a light from a campfire!" with text_dissolve

    show c_happy at right
    with dict_emotion_change
    hide c_terrified

    c_right "Well, what are we waiting for? Vamos, nerds! Civilization here we come!" with text_dissolve

    show c_happy at offscreenright
    with dict_ease

    j_left "Camilla wait--" with text_dissolve

    "..." with text_dissolve

    j_left "... and she's gone." with text_dissolve

    "Jesse sighs then looks at you." with text_dissolve

    j_left "Shall we?" with text_dissolve

    mc "We shall." with text_dissolve

    show j_neutral at offscreenleft
    with dict_ease

    "You and Jesse start off on a small jog going in the direction of the light." with text_dissolve
    stop music fadeout 5.5
    "You come across a clearing at the end of the path, this time much bigger and brighter." with text_dissolve


    scene party with party_fade

    $ renpy.pause(3.0, hard=True)

    play music "../game/assets/music/Jumping-For-Fun.ogg" fadein 15.0 loop

    "And there are other people!" with text_dissolve

    mc "We finally made it!" with text_dissolve

    "Jesse rearranges himself, fixing his wig and straightening his skirt." with text_dissolve

    show j_happy at left
    with moveinleft

    j_left "Finally! It's time to make my grand entrance." with text_dissolve

    show j_happy at offscreenleft
    with dict_ease

    "You scan the area, looking for Camilla." with text_dissolve

    "When you spot her, she's already making her way towards you and Jesse, waving at some people." with text_dissolve

    show c_neutral at right
    with moveinright

    c_right "Guys, you will not believe what someone just told me." with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "Ohmigosh... What did someone just tell you?!" with text_dissolve

    c_right "Okay one, your sarcasm is not needed right now, two your wig is crooked..." with text_dissolve

    show j_scared at left
    with dict_emotion_change
    hide j_neutral

    j_left "Gasp!" with text_dissolve

    c_right "... and three, so you know how we came through there?" with text_dissolve

    show c_neutral at offscreenright
    show j_scared at offscreenleft
    with dict_emotion_change

    "She points in the direction you came from." with text_dissolve

    mc "The harrowing woods experience we just went through, yeah?" with text_dissolve

    show c_neutral at right
    with dict_emotion_change

    c_right "Well... Actually that was like a back route or something. The hunters like to set traps in the fall." with text_dissolve

    show j_annoyed at left
    with dict_emotion_change

    j_left "No fucking way. You're lying." with text_dissolve

    c_right "No, ya. {i}{b}That's{/b}{/i} the front entrance." with text_dissolve

    show j_annoyed at offscreenleft
    show c_neutral at offscreenright
    with dict_emotion_change

    "You walk in the direction she was pointing at." with text_dissolve

    "A parking lot..." with text_dissolve

    "... filled with cars." with text_dissolve

    "... right next to the road." with text_dissolve

    "{i}{b}Well Shit{/b}{/i}" with text_dissolve

    "Jesse walks up right next to you." with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "It's okay [main_char]. We don't ever have to talk about it." with text_dissolve

    show j_neutral at offscreenleft
    with dict_emotion_change

    "As you walk back with Jesse to meet back up with Camilla, you suddenly remember something rather important." with text_dissolve

    mc "Are Tanner and Sequinn here yet?" with text_dissolve

    "As soon as you ask, Tanner and Sequinn comes fumbling out of the woods, panting. They are close to where your group came out from." with text_dissolve

    "Sequinn looks a little ruffled while Tanner just looks pissed."

    "Well like how he usually looks."

    show t_angry at right
    with moveinright

    t_right "FINALLY!" with text_dissolve

    "Tanner dusts himself off." with text_dissolve

    t_right "That was single handedly one of the worst, most exhausting and unnecessary experiences of my life." with text_dissolve

    show s_annoyed at left
    with moveinleft

    s_left "My costume was almost destroyed!" with text_dissolve

    t_right "We almost died Sequinn!" with text_dissolve

    show t_angry at offscreenright
    show s_annoyed at offscreenleft
    with dict_emotion_change

    "Sequinn wobbles over to you." with text_dissolve

    show s_neutral at left
    with moveinleft

    s_left "[main_char]! Pal! Please tell me I didn't miss the costume contest." with text_dissolve

    show t_neutral at right
    with moveinright

    t_right "Is that really all you can think about right now?" with text_dissolve

    show s_neutral at offscreenleft
    show c_happy at left
    with dict_emotion_change

    c_left "My friends!" with text_dissolve

    "Camilla and Jesse walk over from the other side of the bonfire." with text_dissolve

    show t_annoyed at right
    with dict_emotion_change
    hide t_neutral
    "Tanner frown deepens." with text_dissolve
    show c_happy at offscreenleft
    show j_neutral at left
    with dict_emotion_change

    j_left "Glad to see you finally made it." with text_dissolve

    t_right "Shut it." with text_dissolve

    if routeA_scene3_choice == "both idiots":
        j_left "Look, can we please just talk?" with text_dissolve

        t_right "What is there to talk about bro? You ditch me for some pretty boy ever time we make plans." with text_dissolve

        j_left "You’re right, and I apologize. You’re my best friend and my first friend. I just want to talk." with text_dissolve

        "{b}IT’S TIME FOR THE ANNUAL COSTUME COMPETITION.{/b}" with text_dissolve

        "{b}WILL ALL  THE CONTESTANTS PLEASE GO TO THE STAGE BESIDE THE BONFIRE SO WE CAN GET THE SHOW STARTED!{/b}" with text_dissolve

        show t_happy at right
        with dict_emotion_change
        hide t_annoyed


        t_right "Let's support our eccentric friend first." with text_dissolve

        show j_happy at left
        with dict_emotion_change
        hide j_neutral

        j_left "You have a deal Tan Tan." with text_dissolve

        show t_happy at offscreenright
        show t_annoyed at right
        with dict_emotion_change

        t_right "Watch it..." with text_dissolve

        mc "Glad you guys could make up but we need to go. Sequin is freaking out and they could use some reassurance." with text_dissolve

        show j_happy at offscreenleft
        show t_annoyed at offscreenright
        with dict_emotion_change

    else:
        "Just as Jesse was about to speak, the host of the costume compeition started speaking..." with text_dissolve

        "{b}IT’S TIME FOR THE ANNUAL COSTUME COMPETITION.{/b}" with text_dissolve

        "{b}WILL ALL  THE CONTESTANTS PLEASE GO TO THE STAGE BESIDE THE BONFIRE SO WE CAN GET THE SHOW STARTED!{/b}" with text_dissolve

        t_right "We need to go to the stage now." with text_dissolve


        show t_annoyed at offscreenright
        show j_neutral at offscreenleft
        with dict_emotion_change

        "Tanner turns away from Jesse" with text_dissolve

    show s_happy at left
    with moveinleft

    s_left "That's my cue! This is {b}{i}my{/i}{/b} moment." with text_dissolve

    show s_happy at offscreenleft
    with dict_emotion_change

    "Sequinn starts to make their way forward to the stage, but hesitates." with text_dissolve

    "Suddenly Tanner walks over to you." with text_dissolve

    show t_neutral at right
    with moveinright

    t_right "What's the hold up, [main_char]?" with text_dissolve

    mc "I… I think they’re nervous? I’m not really sure. I’ve never seen this emotion come out of them..." with text_dissolve

    show t_neutral at offscreenright
    show t_annoyed at right
    with dict_emotion_change

    t_right "Hey! I need you and your weird Furkey ass to get on the stage. Or do you want Veronica to win again?" with text_dissolve

    show s_angry at left
    with moveinleft

    s_left "Veronica will not get her sexy fingers on this year's trophy!" with text_dissolve

    t_right "Uh... right..." with text_dissolve

    show t_annoyed at offscreenright
    show s_angry at offscreenleft
    with dict_emotion_change

    "Tanner guides the group towards the stage to support your friend." with text_dissolve

    show c_happy at right
    with dict_emotion_change

    c_right "You can do this Quinny!" with text_dissolve

    mc "We're rooting for you!" with text_dissolve

    show j_happy at left
    with moveinleft

    j_left "You look amazing up there!" with text_dissolve

    show c_happy at offscreenright
    show j_happy at offscreenleft
    with dict_emotion_change

    "Sequinn walks across the stage and powers on her costume. The lights and sound takes the crowd by surprise and they all cheer for them!" with text_dissolve

    "{b}AND THE WINNER IS SEQUINN SHEU AND THEIR FURKEY COSTUME!{/b}" with text_dissolve

    show s_happy at left
    with dict_emotion_change

    s_left "HELL YES!" with hpunch

    show s_happy at offscreenleft
    with dict_emotion_change

    "You and your friends run up to Sequinn for a well deserved congratulations." with text_dissolve

    "One of the organizers walks up to your group asking to take a picture of you all." with text_dissolve

    "You all pose for a spooky group picture, but right before the click…" with text_dissolve

    show j_happy at left
    with dict_emotion_change

    j_left "Winners who got here first jump on 3!" with text_dissolve

    "*CLICK*" with dissolve

    
    if costume == "Sexy Panther":
        scene winner_panther with flash


    elif costume == "90's Paper Cup":
        scene winner_cup with flash


    else:
        scene winner_truper with flash


    "You and your friends enjoy the rest of the night, feeling silly for being afraid in the first place." with text_dissolve

    "There was nothing to fear..." with text_dissolve

    scene scrappie_bg with dissolve

    stop music fadeout 5.0

    "Right?" with text_dissolve

    $renpy.pause(5.0, hard = True)


    return






# Freakout more than 3 times
label loser:
    "Camilla takes up the lead naturally, sprinting down the path." with text_dissolve

    "Impressive that she hasn't tripped on anything considering she doesn't have the flashlight." with text_dissolve

    "Jesse is in front of you illuminating the path as you guys make a run for it, the light bobbing violently with each step." with text_dissolve
    stop music fadeout 3.0

    "After a minute, you guys slow down to take a breather." with text_dissolve

    show j_scared at left
    with moveinleft



    play music "../game/assets/music/suspcious.ogg" fadein 3.0 loop

    j_left "That was the most uncool shit I've ever had to go through." with text_dissolve

    mc "I don't even want to know what that was." with text_dissolve

    show c_scared at right
    with moveinright

    c_right "I should have stayed home, and ate my dulces enchilados and minded my business." with text_dissolve

    show j_scared at offscreenleft
    show c_scared at offscreenright
    with dict_emotion_change

    "You look around, spotting a steady glow straight ahead." with text_dissolve

    "{i}Oh no... not again{/i}" with text_dissolve

    mc "Guys, there's more light." with text_dissolve

    show c_terrified at right
    with moveinright

    c_right "Ay! It came back for us! We're gonna die!" with text_dissolve

    show j_neutral at left
    with dict_moveinleft

    j_left "Wait, that looks like a light from a campfire!" with text_dissolve

    show c_happy at right
    with dict_emotion_change
    hide c_terrified

    c_right "Well, what are we waiting for? Vamos, nerds! Civilization here we come!" with text_dissolve

    show c_happy at offscreenright
    with dict_ease

    j_left "Camilla wait--" with text_dissolve

    "..." with text_dissolve

    j_left "... and she's gone." with text_dissolve

    "Jesse sighs then looks at you." with text_dissolve

    j_left "Shall we?" with text_dissolve

    mc "We shall." with text_dissolve

    show j_neutral at offscreenleft
    with dict_ease

    "You and Jesse start off on a small jog going in the direction of the light." with text_dissolve
    stop music fadeout 5.5
    "You come across a clearing at the end of the path, this time much bigger and brighter." with text_dissolve


    scene party with party_fade

    $ renpy.pause(3.0, hard=True)

    play music "../game/assets/music/Jumping-For-Fun.ogg" fadein 15.0 loop

    "And there are other people!" with text_dissolve

    mc "We finally made it!" with text_dissolve

    "Jesse rearranges himself, fixing his wig and straightening his skirt." with text_dissolve

    show j_happy at left
    with moveinleft

    j_left "Finally! It's time to make my grand entrance." with text_dissolve

    show j_happy at offscreenleft
    with dict_ease

    "You scan the area, looking for Camilla." with text_dissolve

    "When you spot her, she's doubled over next to Tanner and Sequinn." with text_dissolve

    show j_annoyed at left
    with moveinleft

    j_left "No way! They made it first... ugh. I'm not ready to hear it." with text_dissolve

    show j_annoyed at offscreenleft
    with dict_emotion_change

    "You and Jesse make your way over to them." with text_dissolve

    show t_happy at right
    with moveinright

    t_right "Heh... the Dude Scouts would be very dissapointed." with text_dissolve

    show s_happy at left
    with moveinleft

    s_left "Glad to see you finally made it. We were going to send a search party after you soon." with text_dissolve

    show t_happy at offscreenright
    show j_annoyed at right
    with dict_emotion_change

    j_right "You two are real cute..." with text_dissolve

    mc "Well I for one, am happy to know you two made it out just fine." with text_dissolve

    s_left "Just fine is an understatement." with text_dissolve

    show s_happy at offscreenleft
    show t_happy at left
    with dict_emotion_change

    t_left "Hey, Jesse." with text_dissolve

    j_right "What do you want, Tanner?" with text_dissolve

    show t_happy at offscreenright
    show j_annoyed at offscreenleft
    with dict_emotion_change

    "Sequinn points in the direction you came from." with text_dissolve

    show s_neutral at left
    with dict_emotion_change

    s_left "Uh huh, so you know how we came through there?" with text_dissolve

    mc "Yeah, I'd rather not think about that... Thanks." with text_dissolve

    show t_neutral at right
    with moveinright

    t_right "That was a back route." with text_dissolve

    show t_neutral at offscreenright
    show c_angry at right
    with dict_emotion_change

    c_right "A back route?!" with text_dissolve

    s_left "Yeah, where naturists and hunters go through for nature... and shit." with text_dissolve

    show s_neutral at offscreenleft
    show c_angry at offscreenright
    with dict_emotion_change

    "Tanner points in the opposite direction." with text_dissolve

    show t_neutral at right
    with dict_emotion_change
    t_right "{b}{i}That's{/i}{/b} the fucking front entrance." with text_dissolve

    show j_annoyed at left
    with dict_emotion_change

    j_left "No fucking way. You're lying." with text_dissolve

    show j_annoyed at offscreenleft
    show t_neutral at offscreenright
    with dict_emotion_change

    "You’re already heading to where he was pointing, ready for the disappointment to hit you." with text_dissolve

    "A parking lot..." with text_dissolve

    "... filled with cars." with text_dissolve

    "... right next to the road." with text_dissolve

    "{i}{b}Well Shit{/b}{/i}" with text_dissolve

    "Jesse walks up right next to you." with text_dissolve

    show j_angry at left
    with moveinleft

    j_left "First we make it here last, and then we went through the BACK ENTRANCE??"

    show j_neutral at left
    with dict_emotion_change

    hide j_angry

    "Jesse takes a deep breath." with text_dissolve

    j_left "I don't even want to think about it anymore." with text_dissolve

    mc "I am here for you in these harrowing times." with text_dissolve

    show j_neutral at offscreenleft
    with dict_emotion_change

    "You put an arm around Jesse as the two of you head back to the group." with text_dissolve
    "Tanner’s usual frown deepens after seeing the two of you." with text_dissolve

    "You didn’t know it was possible to make a frown…frownier." with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "Tanner..." with text_dissolve

    show t_annoyed at right
    with moveinright

    t_right "Even Henry has a better sense of direction than you." with text_dissolve

    if routeA_scene3_choice == "both idiots":
        j_left "Look, can we please just talk?" with text_dissolve

        t_right "What is there to talk about bro? You ditch me for some pretty boy ever time we make plans." with text_dissolve

        j_left "You’re right, and I apologize. You’re my best friend and my first friend. I just want to talk." with text_dissolve

        "{b}IT’S TIME FOR THE ANNUAL COSTUME COMPETITION.{/b}" with text_dissolve

        "{b}WILL ALL  THE CONTESTANTS PLEASE GO TO THE STAGE BESIDE THE BONFIRE SO WE CAN GET THE SHOW STARTED!{/b}" with text_dissolve

        show t_happy at right
        with dict_emotion_change
        hide t_annoyed


        t_right "Let's support our eccentric friend first." with text_dissolve

        show j_happy at left
        with dict_emotion_change
        hide j_neutral

        j_left "You have a deal Tan Tan." with text_dissolve

        show t_happy at offscreenright
        show t_annoyed at right
        with dict_emotion_change

        t_right "Watch it..." with text_dissolve

        mc "Glad you guys could make up but we need to go. Sequin is freaking out and they could use some reassurance." with text_dissolve

        show j_happy at offscreenleft
        show t_annoyed at offscreenright
        with dict_emotion_change
    else:
        "Just as Jesse was about to speak, the host of the costume compeition started speaking..." with text_dissolve

        "{b}IT’S TIME FOR THE ANNUAL COSTUME COMPETITION.{/b}" with text_dissolve

        "{b}WILL ALL  THE CONTESTANTS PLEASE GO TO THE STAGE BESIDE THE BONFIRE SO WE CAN GET THE SHOW STARTED!{/b}" with text_dissolve

        t_right "We need to go to the stage now." with text_dissolve

        show t_annoyed at offscreenright
        show j_neutral at offscreenleft
        with dict_emotion_change

        "Tanner turns away from Jesse." with text_dissolve
    
    show s_happy at left
    with moveinleft

    s_left "That's my cue! This is {b}{i}my{/i}{/b} moment." with text_dissolve

    show s_happy at offscreenleft
    with dict_emotion_change

    "Sequinn starts to make their way forward to the stage, but hesitates." with text_dissolve

    "Suddenly Tanner walks over to you." with text_dissolve

    show t_neutral at right
    with moveinright

    t_right "What's the hold up, [main_char]?" with text_dissolve

    mc "I… I think they’re nervous? I’m not really sure. I’ve never seen this emotion come out of them..." with text_dissolve

    show t_neutral at offscreenright
    show t_annoyed at right
    with dict_emotion_change

    t_right "Hey! I need you and your weird Furkey ass to get on the stage. Or do you want Veronica to win again?" with text_dissolve

    show s_angry at left
    with moveinleft

    s_left "Veronica will not get her sexy fingers on this year's trophy!" with text_dissolve

    t_right "Uh... right..." with text_dissolve

    show t_annoyed at offscreenright
    show s_angry at offscreenleft
    with dict_emotion_change

    "Tanner guides the group towards the stage to support your friend." with text_dissolve

    show c_happy at right
    with dict_emotion_change

    c_right "You can do this Quinny!" with text_dissolve

    mc "We're rooting for you!" with text_dissolve

    show j_happy at left
    with moveinleft

    j_left "You look amazing up there!" with text_dissolve

    show c_happy at offscreenright
    show j_happy at offscreenleft
    with dict_emotion_change

    "Sequinn walks across the stage and powers on her costume. The lights and sound takes the crowd by surprise and they all cheer for them!" with text_dissolve

    "{b}AND THE WINNER IS SEQUINN SHEU AND THEIR FURKEY COSTUME!{/b}" with text_dissolve

    show s_happy at left
    with dict_emotion_change

    s_left "HELL YES!" with hpunch

    show s_happy at offscreenleft
    with dict_emotion_change

    "You and your friends run up to Sequinn for a well deserved congratulations." with text_dissolve

    "One of the organizers walks up to your group asking to take a picture of you all." with text_dissolve

    "You pose with all your friends which now includes Sequinn's trophy." with text_dissolve

    "*CLICK*" with flash

    "You and your friends enjoy the rest of the night, feeling silly for being afraid in the first place." with text_dissolve

    "There was nothing to fear..." with text_dissolve

    scene scrappie_bg with dissolve

    stop music fadeout 5.0

    "Right?" with text_dissolve

    $renpy.pause(5.0, hard = True)


    return