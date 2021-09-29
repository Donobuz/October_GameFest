label scene4:
    scene forest_day with Fade(1.0,0.0,1.0)
    "Camilla peaks her head out of the window"
    show c_neutral at right
    with moveinright

    c_right "Are you sure this is the right place? Looks like no one is here..." with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "That's because we're supposed to walk the rest of the way there." with text_dissolve

    c_right "You're ABSOLUTELY sure this is the right place?" with text_dissolve

    "Jesse grabs a few things as he gets out of the van" with text_dissolve

    j_left "I'm like 99%% sure we're at the right place. Just gotta walk a little and we'll be there." with text_dissolve

    show j_neutral at offscreenleft
    show c_neutral at offscreenright
    with dict_ease

    "Everyone else gets out of the car, adjusting their costumes and stretching while breathing in that nice, fresh air." with text_dissolve

    show s_neutral at left
    with moveinleft

    s_left "If I would have known we would be driving for an hour, I never would have worn this costume in the car." with text_dissolve

    mc "Your costume still looks fine Sequinn! Don't worry so much." with text_dissolve

    show s_annoyed at left
    with dict_emotion_change

    hide s_neutral

    s_left "Fine? FINE? I did not spend 2 months putting hand dyed feathers one by one all over the ass of this thing for {i}fine{/i}." with text_dissolve

    mc "Okay. I take that back. It's {b}{i}SUPER{/i}{/b} fine." with text_dissolve

    s_left "I'm going to fight you." with text_dissolve

    show s_annoyed at offscreenleft
    with dict_ease

    hide s_annoyed

    show j_happy at left
    with dict_moveinleft

    j_left "OKAY!!! LET'S GO PARTY, YEAH?" with text_dissolve

    show c_neutral at right
    with moveinright

    c_right "Hey, does anyone have the map? We need it to find this year's party location." with text_dissolve

    show j_happy at offscreenleft
    with dict_ease

    hide j_happy

    show s_neutral at left
    with dict_moveinleft

    s_left "There was no room in my masterpiece for a grimey map." with text_dissolve

    show c_neutral at offscreenright
    with dict_ease

    hide c_neutral

    show t_neutral at right
    with dict_moveinright

    t_right "Hey man, no one told me to bring it so I didn't" with text_dissolve

    show t_neutral at offscreenright
    with dict_ease
    
    hide t_neutral

    show c_neutral at right
    with dict_moveinright

    c_right "Wait... didn't we agree that [main_char] would bring the map?" with text_dissolve

    show c_neutral at offscreenright
    show s_neutral at offscreenleft
    with dict_emotion_change

    "Everyone turns towards you, waiting for you to respond." with text_dissolve

    if beginning_choice == "everything I need":

        hide text
        jump scene4A
        

    elif beginning_choice == "forgetting something":
        hide text
        jump scene4B

label scene4A:

    "You may or may not have forgotten the map." with text_dissolve
    mc "uhhh... So I may or may not have forgotten the map" with text_dissolve

    show s_annoyed at left
    with moveinleft

    if main_char_pronoun_singular == "She":
        s_left "Oh... You cannot be serious. Is she serious!?" with text_dissolve
    elif main_char_pronoun_singular == "He":
        s_left "Oh... You cannot be serious. Is he serious!?" with text_dissolve
    else:
        s_left "Oh... You cannot be serious. Are they serious!?" with text_dissolve
    
    show t_annoyed at right
    with moveinright

    t_right "We're late, I'm down 5 bucks, and you... [main_char] forgot the map." with text_dissolve

    show s_annoyed at offscreenleft
    with dict_ease
    
    hide s_annoyed

    show c_neutral at left
    with dict_emotion_change

    c_left "Babe, I have your back always but what the hell?" with text_dissolve

    show t_annoyed at offscreenright
    with dict_ease

    hide t_annoyed

    show j_neutral at right
    with dict_emotion_change

    j_right "No worries! I have my map in the car! Follow me!" with text_dissolve

    
    show c_neutral at offscreenright
    show j_neutral at offscreenleft
    with dict_emotion_change


    "Everyone walks with Jesse back to his car for the party map." with text_dissolve
    "While Jesse is searching for the small slip of paper, Camilla teases Tanner about his height, holding his costume's prop over his head." with text_dissolve

    show c_happy at right
    with moveinright

    c_right "Are you like 4'11\"?" with text_dissolve

    show t_annoyed at left
    with moveinleft

    t_left "I'm 5'3\" Camilla De Leon and give back my Titarangs!" with text_dissolve

    show c_happy at offscreenright
    with dict_ease

    hide c_happy

    show s_annoyed at right
    with dict_moveinright

    s_right "I'm friends with literal children. I could be doing so much more with my life." with text_dissolve

    show s_annoyed at offscreenleft
    show t_annoyed at offscreenright
    with dict_emotion_change

    "Camilla laughs as Tanner struggles to reach the Titarang that she is dangling over his head." with text_dissolve
    
    "Tanner then starts to lunge towards Camilla and each time Camilla takes a step back." with text_dissolve

    "You notice that they are getting dangerously close to Jesse, who is still learning inside the car." with text_dissolve

    "They keep getting closer..." with text_dissolve

    "... and closer..."

    show s_annoyed at left
    with moveinleft

    s_left "Stop playing around before someone gets hurt!" with text_dissolve

    "Suddenly, you hear Jesse yell something out." with text_dissolve

    show j_happy at right
    with dict_moveinright

    j_right "I found the map! I found th-" with text_dissolve

    mc "Jesse look out!" with text_dissolve

    show s_annoyed at offscreenleft
    show j_happy at offscreenleft
    with dict_emotion_change

    "It's too late. Tanner lunges at Camilla once again, but this time she loses her footing and crashes into Jesse." with text_dissolve

    hide text
    jump scene4continue





label scene4B:
    "You're a responsible adult... barely. Of course you have the map!" with text_dissolve

    mc "And once again [main_char] to the rescue." with text_dissolve

    show t_neutral at right
    with moveinright

    t_right "I guess we can excuse you for being late. This time..." with text_dissolve

    show s_happy at left
    with moveinleft

    s_left "Heh, way to go [main_char]" with text_dissolve

    show t_neutral at offscreenright
    show s_happy at offscreenleft
    with dict_emotion_change

    "You hand the map over for Jesse to look at." with text_dissolve
    "While Jesse tries to pinpoint the locations, Tanner and Camilla antagonize each other." with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "I'm going to grab a marker so we can stay on track. It's a bit of a walk." with text_dissolve

    mc "Can you bring me my coffee too? It's chilly out here." with text_dissolve

    j_left "Of course! I'll be right back." with text_dissolve

    show j_neutral at offscreenleft
    with dict_ease

    "Jesse leaves on his quest for a marker." with text_dissolve
    "With Jesse walking away, your attention goes back to your bickering friends" with text_dissolve

    "Tanner found a fake spider and is chasing Camilla with it." with text_dissolve

    "In her panic, she loses her usual athletic composure and trips over herself." with text_dissolve

    mc "Tanner stop! She's going to fall!" with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "I have your coffee [main_char]!" with text_dissolve

    show s_neutral at right
    with dict_emotion_change

    s_right "Wait, Jesse look out!" with text_dissolve

    show j_neutral at offscreenleft
    show s_neutral at offscreenleft
    with dict_emotion_change

    "Suddenly you see Camilla run into Jesse." with text_dissolve


    hide text
    jump scene4continue



label scene4continue:
    #play sound here

    "SPLAT!" with hpunch
    "You and Sequinn run over to your friends toppled over on the ground." with text_dissolve

    show s_neutral at left
    with moveinleft

    s_left "Please don't tell me the coffee spilled on the map." with text_dissolve

    mc "I won't tell you that." with text_dissolve

    show s_neutral at offscreenleft
    with dict_ease

    "You pick the now delicious smelling paper off the ground, holding the dropping map for everyone to see." with text_dissolve

    show map_image at map_transform
    with dict_dissolve_1seconds

    mc "But I will show you" with text_dissolve

    hide map_image

    "You squeeze the coffee out of the paper, hoping to salvage whatever is left." with text_dissolve
    
    show c_scared at right
    with moveinright

    c_right "I'm so sorry! I couldn't catch myself!" with text_dissolve

    show t_neutral at left
    with dict_dissolve_1seconds

    t_left "Is the map okay?" with text_dissolve

    show c_scared at offscreenright
    with dict_ease

    hide c_scared

    show s_annoyed at right
    with dict_moveinright

    s_right "iS tHe MaP oKaY?" with text_dissolve


    show s_neutral at right
    hide s_annoyed
    with dict_emotion_change


    s_right "Jesse, are {i}YOU{/i} okay?" with text_dissolve

    show t_neutral at offscreenright
    with dict_ease

    hide t_neutral

    show j_neutral at left
    with dict_moveinleft

    j_left "Hey! I am fine!" with text_dissolve
    j_left "It's not the end of the world! I saw the map so I remember some parts." with text_dissolve
    j_left "May I?" with text_dissolve

    show s_neutral at offscreenleft
    show j_neutral at offscreenleft
    with dict_emotion_change

    "Jesse holds out his hand for the damp map in your hand." with text_dissolve
    "You give it to him and he quickly looks at the map." with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "See some parts of the map are still okay! Let's go. We're late enough as it is. It's going to get dark soon." with text_dissolve

    show j_neutral at offscreenleft
    with dict_ease

    hide j_neutral

    show t_annoyed at left
    with dict_emotion_change

    t_left "I hate walking." with text_dissolve

    "You roll your eyes" with text_dissolve

    mc "You hate everything Tanner" with text_dissolve

    "Tanner just shrugs nonchalantly." with text_dissolve

    show t_annoyed at offscreenleft
    with dict_ease

    "The group start off on their trek through the woods." with text_dissolve
    "Jesse takes point with Camilla following close behind him looking a little wary." with text_dissolve
    "You take up the center of the group." with text_dissolve
    "Sequinn and Tanner are in the back. Sequinn tries to show Tanner the cool feature of their costume but he is very uninterested." with text_dissolve

    scene forest_dark with dark_forest_transition
    "The cold and encroaching darkness has started to take effect on your group." with text_dissolve
    $ renpy.pause(2.0, hard=True)

    "After walking a bit, the party encounters a fork on the trail." with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "Look! There's the huge tree that was on the map! We're on the right track. We just have to go this way." with text_dissolve

    show t_neutral at right
    with moveinright

    t_right "No... it was that small boulder over there, not a tree." with text_dissolve

    show j_annoyed at left
    with dict_emotion_change
    hide j_neutral

    j_left "I know how to read a map, Tanner. I was a Dude Scout after all. Best in Troop 069." with text_dissolve

    show t_annoyed at right
    with dict_emotion_change

    show t_neutral at offscreenleft
    with dict_emotion_change

    hide t_neutral

    t_right "Yeah... I know and because of you I had to join too." with text_dissolve

    show j_happy at left
    with dict_emotion_change
    hide j_annoyed

    j_left "And you looked adorable in your khakis." with text_dissolve

    show j_happy at offscreenleft
    show t_annoyed at offscreenleft
    with dict_emotion_change

    hide j_happy
    hide t_annoyed

    show s_annoyed at left
    with dict_moveinleft

    s_left "Hey, can you two Dude Dorks shut up and tells us where to go?" with text_dissolve

    show s_annoyed at offscreenleft
    with dict_emotion_change
    show t_neutral at left
    show j_neutral at right
    with dict_emotion_change
    hide s_annoyed

    t_and_j "We go this way!" with text_dissolve

    show t_neutral at offscreenright
    show j_neutral at offscreenleft
    show t_annoyed at left
    show j_annoyed at right
    with dict_emotion_change

    hide t_neutral
    hide j_neutral
    "Tanner and Jesse glare at each other at the realization that they had pointed at different paths." with text_dissolve

    show t_annoyed at offscreenright
    show j_annoyed at offscreenleft
    with dict_emotion_change
    "Bickering ensues..." with text_dissolve

    show c_scared at right
    with moveinright

    c_right "Please... please don't tell me we're lost." with text_dissolve

    mc "I don't think so. Let me check the map." with text_dissolve

    "You grab the map from the still arguing Jesse and unravel the map." with text_dissolve

    mc "Huh, the map is smudged here. It just looks like a blob now." with text_dissolve
    mc "It could have been a boulder or a tree." with text_dissolve
    mc "What do we do?" with text_dissolve

    c_right "WE'RE LOST!" with hpunch

    show s_neutral at left
    with moveinleft

    s_left "Wait... are we going to make it to the party? I didn't spend all my free time making this costume for something." with text_dissolve

    show s_neutral at offscreenleft
    show c_scared at offscreenright
    with dict_ease

    hide c_scared
    hide s_neutral
    "Jesse walks over to the tree and points to the path on the left." with text_dissolve

    show j_annoyed at left
    with dict_moveinleft

    j_left "I remember most of the map before it was smudged. We go this way." with text_dissolve

    "Tanner immediately speaks up." with text_dissolve

    show t_annoyed at right
    with dict_moveinright

    t_right "I’m the one with a high IQ here, who’s to say that you didn't forget which path is correct?" with text_dissolve

    "Jesse looks at Tanner, very annoyed." with text_dissolve

    show j_angry at left
    with dict_emotion_change
    hide j_annoyed

    j_left "I’m not the one who was goofing off and causing accidents. I'm pretty sure it's this path." with text_dissolve

    t_right "Tch. Pretty sure isn't good enough for me. I think it's the other way" with text_dissolve

    show j_angry at offscreenleft
    show t_annoyed at offscreenright
    with dict_emotion_change
    hide j_angry
    hide t_annoyed

    "Tanner points to the path on the right by the boudler." with text_dissolve

    "Camilla stands next to Jesse." with text_dissolve

    show c_neutral at right
    with dict_moveinright

    c_right "Jesse has a really good sense of direction. Plus, he did look at the map the longest..." with text_dissolve

    "Sequinn looks to Tanner." with text_dissolve

    show s_neutral at left
    with dict_moveinleft

    s_left "This is stupid. Tanner has a 170 IQ and he's usually right about this kind of stuff so I'm going where he goes." with text_dissolve

    show c_neutral at offscreenright
    show s_neutral at offscreenleft
    with dict_ease
    hide c_neutral
    hide s_neutral    

    "Tanner and Sequinn walk to the boulder. You friends have split into two groups and are looking at you expectantly." with text_dissolve
    
    show j_annoyed at left
    with dict_moveinleft

    "Well [main_char], who do you think is right?" with text_dissolve




