label scene1:
    stop music fadeout 2.2
    pause (2)

    play music "assets/music/Tootsie-Pop-Blues.ogg" fadein 1.0 loop
    scene bedroom with dict_fade_4seconds

    "The sun shines through the window, causing you to squint as you sit up."

    no_name "Gross, sunlight. Looks like Alex is gone for the day… Having an early bird roommate is the worst sometimes."
    
    "You rub the sleep out of your eyes and look at the digital clock on the nightstand - 11:00 am."  with text_dissolve

    no_name "Eh, that’s an acceptable time to get up on a Saturday." with text_dissolve

    scene bathroom with dict_fade_1seconds

    "You head to the bathroom to do your morning routine."

    no_name "Done and done, back to bed I go." with text_dissolve

    "And like any good college student, you go right back to sleep on your day off."


    # EDIT THIS SECTION LATER

    scene bedroom with Fade(2.0, 0.0, 4.0)

    "You wake up for the second time today and look at the clock." with text_dissolve

    no_name "Hmm... 3:00pm, not bad for a 4 hour nap." with text_dissolve

    "You get up for the second time today and once again make your way to the bathroom." with text_dissolve

    "This time, however, you glance at the calendar on the wall." with text_dissolve

    scene calender
    with dict_dissolve_1seconds

    hide text
    pause 8

    "You notice a big red circle surrounding the current day." with text_dissolve

    no_name "Heh, it’s Halloween. That’s fun…" with text_dissolve

    "{i}Proccessing {b}{cps=0.80}....{/cps}{/b}{/i}{nw}" with text_dissolve

    no_name "WAIT IT’S HALLOWEEN!" with text_dissolve

    no_name "I’M SUPPOSED TO MEET UP WITH MY FRIENDS!" with text_dissolve

    "You glance at the clock again." with text_dissolve

    no_name "IN AN HOUR!" with text_dissolve

    "You quickly finish your post nap routine, rushing to pack for the party." with text_dissolve

    no_name "Good thing I prepared my costumed way early in advance." with text_dissolve

    "You grab your costume out of the closet and change." with text_dissolve

    "Before you head out, you do a quick once over in the mirror." with text_dissolve
    
    scene mirror_background with Fade(0.0,0.0,2.0)
    window hide
    jump costume_change

label scene1continue:

    scene bedroom
    "You grab your flashlight and wallet, placing the ID inside." with text_dissolve 

    menu:
        "I have everything I need!":
            window hide
            $beginning_choice = "everything I need"
            jump everything_I_need
            hide text

        "I think I'm forgetting something...":
            window hide
            $beginning_choice = "forgetting something"
            jump forget_something
            hide text

label everything_I_need:
    "You slip everything into your pockets, because obviously your costume has cool pockets." with text_dissolve 
    "We're not animals here." with text_dissolve 
    "You smile at yourself for being so efficient at getting ready in a pinch." with text_dissolve 
    "It’s time to get wasted and regret it tomorrow." with text_dissolve 
    "With one last look you head out the door to meet your friends with 5 minutes to spare... Nice." with text_dissolve 

    window hide
    jump scene2

label forget_something:
    "You look at your calendar again and notice a sticky note on it." with text_dissolve 
    "It’s a checklist for the party listing a flashlight, wallet and... " with text_dissolve
    "the party map!" with text_dissolve
    "Good thing you double checked! Hurriedly, you grab the map and put it into your wallet." with text_dissolve 
    "You slip everything into your pockets, because obviously your costume has cool pockets." with text_dissolve 
    "We're not animals here." with text_dissolve 
    "With one last look you head out the door to meet your friends with 5 minutes to spare... Nice." with text_dissolve

    window hide
    jump scene2
