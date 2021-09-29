label scene2:
    
    scene cafe with Fade(2.0,0.0,4.0)
    mc "Ahhh the sweet smell of coffee and stale campus scones." with text_dissolve
    "In front of you is the campus coffee shop and your friends are in the distance at your usual table. You walk up the small set of steps to join them."
    
    scene cafe_table with dissolve
    show c_happy at right 
    with moveinright
    # with dissolve
    pause(0.15)

    c_right "Well well well... If it isn’t the guest of honor [main_char]. Thank you for taking time out of your busy schedule, babe, to grace us with your presence."
    mc "My bad, I kinda overslept a little bit..." with text_dissolve
    show j_neutral at left 
    with moveinleft
    # with dissolve
    pause(0.15)

    j_left "Did you oversleep or did you wake up and go back to sleep because you have zero sense of urgency?"

    show c_happy at offscreenright
    show j_neutral at offscreenleft
    with ease
    # with dissolve

    hide c_happy
    hide j_neutral
 
    show s_neutral at left with moveinleft

    s_left "Those two idiots were placing bets on how late you would be." with text_dissolve
    mc "Yeah that happens way too often, but this is the last time I swear!" with text_dissolve

    show j_neutral at right
    with moveinright
    # with dissolve

    j_right "Hey, I'm not even mad about it. I just made an easy 5 bucks!" with text_dissolve

    show j_happy at right
    with dissolve

    hide j_neutral

    j_right "Cough it up Tan Tan!" with text_dissolve

    show s_neutral at offscreenleft
    with dict_move
    # with dissolve

    show j_happy at left
    with move

    show t_annoyed at right
    with moveinright
    # with dissolve

    t_right "Call me Tan Tan again and there’s going to be problems worse than your costume." with text_dissolve

    show j_happy at offscreenleft
    show t_annoyed at offscreenright
    with ease

    hide j_happy
    hide t_annoyed

    mc "Speaking of costumes, what are you guys dressed as?" with text_dissolve
    "You take a look at the group before you. Everyone is dressed in both simple and elaborate, if not slightly unhinged, costumes." with text_dissolve

    show s_neutral at left
    with moveinleft
    # with dissolve

    s_left "Clearly I am the limited edition defective teal Furkey. The toys retail for $15 but this costume is worth a million. Hand sewn, I put every SINGLE FEATHER ON ONE AT A TIME AND I-" with text_dissolve

    show t_neutral at right
    with moveinright

    t_right "WELLLL ANYWAYS, I am a Bat Guy's trusty sidekick... the Somber Tit" with text_dissolve

    show s_neutral at offscreenleft
    with ease
    # with dissolve

    hide s_neutral

    show j_neutral at left
    with moveinleft

    j_left "Hey I’ve read every Bat Guy and Tit comic, including side stories, and there is no Somber Tit in any alternate universe" with text_dissolve

    show t_annoyed at right
    with dissolve

    t_right "It’s my OC you galactic nerd." with text_dissolve

    show t_annoyed at offscreenright
    show t_neutral at offscreenright
    with ease
    # with dissolve

    hide t_neutral
    hide t_annoyed

    show c_neutral at right
    with moveinright

    c_right "That was the cringiest thing I have ever listened to... I'm Tommy Hurrah. We're both super sexy" with text_dissolve

    show j_happy at left
    with dissolve

    j_left "And I am every single character from Let’s Go! Pretty Sailor Battle Girls!!! Even the unreleased character designs." with text_dissolve

    show c_neutral at offscreenright
    show j_happy at offscreenleft
    show j_neutral at offscreenleft
    with ease
    # with dissolve

    hide c_neutral
    hide j_neutral
    hide j_happy

    show s_neutral at left
    with moveinleft

    "Sequinn looks at you" with text_dissolve
    # "Sequinn looks to you"

    s_left "And what the hell are you supposed to be [main_char]?" with text_dissolve

    mc "I'm a [costume] obviously" with text_dissolve

    # python:
    #     if costume == "Sexy Panther":
    #         Jump("sexy_panther")
    #     elif costume == "90's Paper Cup":
    #         Jump("paper_cup")
    #     else:
    #         Jump("super_truper")

    if costume == "Sexy Panther":
        window hide
        jump sexy_panther
    elif costume == "90's Paper Cup":
        window hide
        jump paper_cup
    else:
        window hide
        jump super_truper

label sexy_panther:
    show t_neutral at right
    with moveinright

    t_right "That’s the Sexy Cat costume from the costume store down the street, not a panther. It still has the damn bell collar on it." with text_dissolve

    mc "I did not wake up from my second sleep to be attacked." with text_dissolve

    t_right "Ok well, are we going to sit around all day like a bunch of losers?" with text_dissolve

    window hide

    show s_neutral at offscreenleft
    show t_neutral at offscreenright
    with ease
    # with dissolve

    hide s_neutral
    hide t_neutral
    
    jump scene2continue


label paper_cup:
    s_left "You really came dressed up as a cup? Soooooo uninspired." with text_dissolve
    mc "I did not wake up from my second sleep to be attacked." with text_dissolve

    show t_neutral at right
    with moveinright

    t_right "Ok well, are we going to sit around all day like a bunch of losers?" with text_dissolve

    window hide

    show s_neutral at offscreenleft
    show t_neutral at offscreenright
    with ease
    # with dissolve

    hide s_neutral
    hide t_neutral

    jump scene2continue




label super_truper:
    show s_neutral at offscreenleft
    with ease
    # with dissolve

    hide s_neutral

    show j_neutral at left
    with moveinleft

    j_left "While I appreciate the attempt, your Super TruperZ helmet has too many stripes and there is no Purple Truper." with text_dissolve

    mc "I did not wake up from my second sleep to be attacked." with text_dissolve

    show t_neutral at right
    with moveinright

    t_right "Ok well, are we going to sit around all day like a bunch of losers?" with text_dissolve

    window hide

    show t_neutral at offscreenright
    show j_neutral at offscreenleft
    with ease
    # with dissolve

    hide t_neutral
    hide j_neutral

    jump scene2continue

label scene2continue:

    show c_annoyed at right
    with moveinright

    c_right "Tanner, don't be a jerk" with text_dissolve

    show c_happy at right
    with dict_dissolve_1seconds

    "She turns to you with a warm smile"

    c_right  "Let me get you a coffee then we can hit the road!" with text_dissolve

    show c_annoyed at offscreenright
    show c_happy at offscreenright
    with dict_ease
    # with dissolve



    "Camilla walks into the coffee shop." with text_dissolve

    "With the plastic wig on top of her already tall frame, she has to duck to get through the door" with text_dissolve

    hide c_happy
    hide c_annoyed

    show s_happy at left
    with moveinleft

    s_left "I don’t care what you have to say, I'm definitely going to win this year! I put every ounce of my skills into this costume. And some of Jayce’s too." with text_dissolve

    show s_happy at right
    with dict_move
    # with dissolve

    show j_neutral at left
    with moveinleft

    j_left  "He programmed those lights for you?" with text_dissolve  

    s_right "Of course he did. He's in love with me. He even made it possible for the costume to talk. Listen to This!" with text_dissolve

    "Sequinn proudly presses down on the top beak of her Furkey costume. After a few seconds of silence, you and Jessie start shifting nervously." with text_dissolve
    hide s_happy
    show s_neutral at right
    with dict_dissolve_1seconds



    s_right "Just give it a-"


    show j_neutral at offscreenleft
    with moveinleft

    show t_annoyed at left
    with dict_emotion_change

    t_left "Get over yourself! Nothing is going to happ-" with text_dissolve
    hide t_annoyed

    show t_annoyed at left
    with dict_hpunch
    "Turkey Noise!!!!!!!!!!!!" #Edit this later
    
    "The loud noise causes everyone to jump and cover their ears" with text_dissolve
    
    mc "Well, that definitely caught everyone off guard" with text_dissolve

    show s_happy at right
    with dict_emotion_change

    s_right "Ha! That’ll teach you to keep cutting people off. I’m winning this year for sure." with text_dissolve

    hide t_annoyed
    show t_neutral at left
    with dissolve


    t_left "You say that every year but it hasn't happened yet" with text_dissolve

    show s_neutral at offscreenright
    show s_happy at offscreenright
    with ease
    # with dissolve

    hide s_neutral
    hide s_happy

    show j_happy at right
    with moveinright

    j_right "I believe in you Sequinn!" with text_dissolve

    t_left "You say that every year too..." with text_dissolve

    show j_happy at offscreenright
    with dict_emotion_change
    # with dissolve

    show s_happy at right
    with moveinright

    s_right "Well this year for sure! There's no way I'll lose this time!" with text_dissolve


    show t_annoyed at left
    with dissolve
    hide t_neutral

    t_left "You try too damn hard! Every year you do some crazy costume and every year you lose to a Sexy Devil." with text_dissolve

    mc "Or a Sexy Cowgirl..."

    show t_annoyed at offscreenleft
    show t_neutral at offscreenleft
    with dict_emotion_change

    show c_neutral at left
    with moveinleft

    c_left "Or the Sexy Pickle that one time."

    show s_annoyed at right
    with dict_emotion_change
    hide s_happy

    s_right "You will all burn, I'll make sure of it."

    show c_happy at left
    with dict_emotion_change
    hide c_neutral

    c_left "We're just teasing you babe"

    show c_happy at offscreenright
    with dict_emotion_change
    # with dissolve


    show t_happy at left
    with moveinleft

    t_left "I'm not. You're a certified loser." with text_dissolve

    show t_annoyed at left
    with dict_emotion_change
    hide t_happy
    "You hear a loud smack." with hpunch

    "Jesse smacked the back of Tanner's head." with text_dissolve

    show s_annoyed at offscreenleft
    show s_neutral at offscreenleft
    show s_happy at offscreenleft
    with dict_emotion_change
    # with dissolve

    show j_annoyed at right
    with moveinright

    j_right "That’s enough out of you!" with text_dissolve

    show t_annoyed at offscreenleft
    show j_annoyed at offscreenright
    with ease
    # with dissolve
 
    "As the drama continues in the background, you look at Camilla who quickly looks down at her watch" with text_dissolve

    show c_happy at right
    with moveinright

    c_right "Well, it's about time to get going so let's head out!" with text_dissolve
    
    "You all gather your belongings and head to the car so you can make your way to the party of the century… or at least of the month." with text_dissolve

    

    window hide
    jump scene3