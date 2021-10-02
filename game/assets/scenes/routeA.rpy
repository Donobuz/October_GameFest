label routeA:
    "You look to Jesse and Camilla." with text_dissolve

    mc "I think Jesse's right on this one." with text_dissolve

    "Jesse beams." with text_dissolve

    show t_annoyed at right
    with moveinright

    t_right "Whatever. Don't be upset when we beat you guys there." with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "What do you mean \"beat us there\"?" with text_dissolve

    "Tanner scoffs." with text_dissolve

    t_right "We never specified that we had to all follow the path the majority picked." with text_dissolve

    j_left "I mean I guess?" with text_dissolve

    show t_annoyed at offscreenright
    show j_neutral at offscreenleft
    with dict_ease

    "Camilla interjects..." with text_dissolve

    show c_neutral at right
    with dict_moveinright

    c_right "B-But wouldn't it be better if we all stuck together?" with text_dissolve
    c_right "If all those scary movies you guys made me watch have taught me anything, it's that we should definitely be sticking together." with text_dissolve

    show s_neutral at left
    with dict_moveinleft

    s_left "I just want to get there as fast as possible so I can win this damn costume contest!" with text_dissolve
    s_left "I am coming for your ass Veronica Larenta!" with text_dissolve

    show c_neutral at offscreenright
    show s_neutral at offscreenleft
    with dict_emotion_change

    "You let out a loud sigh. Everyone has been on edge lately and you hate seeing your friends bicker so much." with text_dissolve

    menu:
        with dissolve
        "Come on guys. Why can't we work together? You guys have been at it all day.":
            "Your friends look at you sheepishly, refusing to make eye contact with each other." with text_dissolve
        
        "Everyone just shut up and stop bickering!":
            "Your friends look at you in shock for the sudden aggression. It's clear you're agitated." with text_dissolve

    "Tanner turns and starts heading down his chosen path." with text_dissolve

    show t_neutral at right
    with moveinright

    t_right "I am going this way." with text_dissolve

    show t_neutral at offscreenright
    with dict_emotion_change

    "Sequinn follows behind him as her feathered costume bounces with each step." with text_dissolve
    "Jesse simply shakes his head. Tanner pauses for a moment and turns around." with text_dissolve

    show t_angry at right
    with dict_moveinright

    t_right "HEY!" with hpunch

    show t_angry at offscreenright
    show t_happy at right
    with dict_emotion_change
    t_right "Last one there is Scrappie's next victim." with text_dissolve

    show c_scared at left
    with dict_emotion_change

    c_left "WHAT!?" with hpunch

    mc "Now, why the hell would you say that with Cami here!?" with text_dissolve

    show t_happy at offscreenright
    show c_scared at offscreenright
    with dict_emotion_change

    "Tanner walks away with a bounce; Sequinn trailing closely behind him, focusing on keeper her costume pristine." with text_dissolve

    show j_annoyed at left
    with moveinleft

    j_left "He is SOOOOO not kawaii." with text_dissolve

    show c_annoyed at right
    with moveinright

    c_right "He really does just do his own thing." with text_dissolve

    j_left "Well, whatever. I'm positive this is the right path." with text_dissolve

    "You nod in agreement." with text_dissolve

    mc "Tanner is a stubborn one but it's just part of his charm. I'm sure we'll beat them there." with text_dissolve

    show c_annoyed at offscreenright
    show j_neutral at left
    with dict_emotion_change
    hide j_annoyed

    j_left "We're def going to beat them. That'll show Tanner and his smug little IQ." with text_dissolve

    "Jesse pulls out a flashlight from his bag." with text_dissolve

    j_left "It's getting even darker than before. Let's go!" with text_dissolve

    show j_neutral at offscreenleft
    with dict_ease

    "Jesse takes the lead as you follow him onto the path. You see Camilla looking at the canopy of trees shrouding the forest in patches of darkness." with text_dissolve

    show c_scared at right 
    with moveinright

    c_right "A- Actually, do we even have to go to this party?" with text_dissolve
    c_right "There's always n-next year and who even knows if this is like, you know, the right path and there could be dangerous stuff in the woods..." with text_dissolve
    c_right "and it's getting darker a-a-and we should have just gone with Tanner and Sequinn so we all would be together and....!!!" with text_dissolve

    "You turn around to see that Camilla hasn't noticed that you had left yet." with text_dissolve

    mc "Camilla... I don't think standing there alone is the best idea you know!?" with text_dissolve

    c_right "EEEP!" with text_dissolve

    show c_scared at offscreenright
    with dict_emotion_change

    "She rushes to your side as you venture deeper into the woods, determined to get to the party first." with text_dissolve

    "You try to fill the eerie silence with some small talk, but it seems to do little to help ease Camilla's nerves." with text_dissolve

    mc "How's everyone holding up?" with text_dissolve

    show c_scared at right
    with dict_moveinright

    c_right "Why does this party have to be held in the woods? There are perfectly fine, well-lit establishments that the party could be at." with text_dissolve

    mc "It's probably the atmosphere. You know, dark and spooky for Halloween." with text_dissolve

    c_right "I know that but still... It's a little too dark and spooky for my liking. Plus, people died here, like come on!" with text_dissolve

    show c_scared at offscreenleft
    with dict_emotion_change

    "Camilla shudders and holds herself. It's hard to tell if it's from fear or the cold." with text_dissolve

    show c_scared at right
    with dict_emotion_change

    c_right "There could be lurking dangers hidden around every corner." with text_dissolve
    c_right "Coach needs me in tip top condition for when the season starts and I don't feel too tip top here!" with text_dissolve

    show j_neutral at left
    with dict_moveinleft

    j_left "Well then, good thing there's nothing dangerous in these woods!" with text_dissolve

    c_right "But how can you be so s-" with text_dissolve

    show j_annoyed at left
    with dict_emotion_change
    hide j_neutral

    j_left "Camilla please... It's not like you couldn't fight off everything and anything in these woods!" with text_dissolve
    j_left "You're stronger than half the campus." with text_dissolve

    "Camilla stops walking in shock and looks at you with pleading eyes." with text_dissolve

    mc "I mean, he's not wrong. You took down the entire wrestling team by yourself. I question if you're even human sometimes." with text_dissolve

    show c_scared at offscreenright
    show c_angry at right
    with dict_emotion_change

    c_right "That's not the point and they were asking for it!" with text_dissolve

    show c_angry at offscreenright
    show j_annoyed at offscreenleft
    with dict_emotion_change

    "You let out a small chuckle as you watch Camilla frantically speed walk to rejoin you and Jesse." with text_dissolve

    "As they continue bickering, you hear a slight rustle coming from your right side." with text_dissolve

    mc "Soooo... Not to freak you guys out but... did you hear-..." with text_dissolve

    play sound "../game/assets/music/Stampede.ogg" fadein 1.0 loop
    "All of a sudden a flury of movement charges in your direction." with text_dissolve


    stop sound fadeout 2.0
    

    show j_terrified at left
    with dict_moveinleft

    j_left "AAAAAAAAAAAAAAAAAHHHHHHHHHHHHHH!" with hpunch

    show j_terrified at offscreenleft
    with dict_emotion_change

    "Jesse screams and Camilla starts to panic." with text_dissolve
    "It’s dark and none of you can clearly see what is happening." with text_dissolve
    "You continuously feel the things brush past your legs and knocking into you." with text_dissolve

    menu:
        with dissolve
        "It's a stampede! Get over that ledge and get down!":

            $ stay_calm += 1
            hide text
            jump scene1A_calm

        "A stampede?! Oh... hell no! RUUUUUN!":

            $ freak_out += 1
            hide text
            jump scene1A_freakout


label scene1A_calm:
    "You spot a small ledge and jump under it with your friends." with text_dissolve
    "Covering your head, you close your eyes and try to endure the stampede." with text_dissolve
    "Hopefully you'll all make it." with text_dissolve
    "{i}Hopefully...{/i}" with text_dissolve
    "After what feels like a lifetime, the animals finally stop running at you." with text_dissolve
    "Jesse stands up first to try and figure out what just happened." with text_dissolve

    show j_scared at left
    with moveinleft

    j_left "What the hell was that?!?" with text_dissolve
    
    "You stand up and brush yourself off." with text_dissolve

    mc "Woodland creatures. Maybe should have been Snow White this year!" with text_dissolve

    show j_scared at offscreenleft
    with dict_ease

    hide j_scared

    show j_annoyed at left
    with dict_emotion_change

    j_left "Yeah thanks... that's totally what I was asking about [main_char]." with text_dissolve

    show j_annoyed at offscreenleft
    with dict_emotion_change

    "Camilla stands up last. A little shaken up, but overall okay." with text_dissolve

    show c_neutral at right
    with moveinright

    c_right "Okay yeah. Pack it up babes. It's definitely time to leave. Not cool, that was so super not cool." with text_dissolve

    mc "Hey, we made it through Camilla. Its alright!" with text_dissolve

    c_right "Is it too late to suggest going back to the van?" with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "Come on Cami, you got this. We gotta beat Tanner and Sequinn or they'll hold this over me for like... forever." with text_dissolve

    c_right "Ugh... fine! But Jesse, I'm just saying... van safe... woods spooky." with text_dissolve

    show c_neutral at offscreenright
    show j_neutral at offscreenleft
    with dict_emotion_change

    "You finish dusting yourselves off and gather your dropped belongings from the forest floor." with text_dissolve

    "Jesse walks up to you, whispering as to not worry Camilla." with text_dissolve

    show j_neutral at left
    with dict_emotion_change

    j_left "{i}[main_char], what do you think they were running away from?{/i}" with text_dissolve

    mc "{i}I have no clue... let's just keep going.{/i}" with text_dissolve

    show j_neutral at offscreenleft
    with dict_emotion_change

    "After the short set back, you all continue down the path towards what you hope is the party." with text_dissolve

    hide text
    jump scene2_routeA


label scene1A_freakout:
    "You decide to run from the stampede of animals." with text_dissolve

    "Maybe not the best idea but hey, that's instinct." with text_dissolve

    "As soon as you turn to start running, you see that Jesse did not have the same idea and you run straight into him." with text_dissolve

    show j_terrified at left
    with dict_moveinleft

    j_left "Aaack!" with hpunch

    show j_terrified at offscreenleft
    with dict_emotion_change

    "You both fall to the ground, just barely making it out of the way of the panicked animals." with text_dissolve

    "Camilla comes out of where she was hiding." with text_dissolve

    show c_scared at right
    with moveinright

    c_right "Oh my god... are you guys okay?!" with text_dissolve

    "Thanks for helping Camilla... you think to yourself." with text_dissolve

    "You start to stand up, lending a hand to Jesse." with text_dissolve

    mc "Sorry Jesse, totally didn't mean to run into you like that." with text_dissolve

    "Jesse takes the offered hand." with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "No biggie. That was so out of nowhere." with text_dissolve

    mc "I wonder what caused them to charge like that." with text_dissolve

    c_right "Hopefully, we'll never find out. I'm over this nature hike." with text_dissolve

    show c_scared at offscreenright
    show j_neutral at offscreenleft
    with dict_emotion_change

    "You gather yourself and start to walk, only to realize that you can't really see anything." with text_dissolve

    "You turn to Jesse who was supposed to be holding the flashlight." with text_dissolve

    show j_scared at left
    with moveinleft

    j_left "Guys, I don't know where the flashlight is." with text_dissolve

    show c_scared at right
    with moveinright

    c_right "What do you mean you don't know where the flashlight is." with text_dissolve

    show j_scared at offscreenleft
    show j_annoyed at left
    with dict_emotion_change

    j_left "Well, I dropped it when [main_char] ran into me and now I can't find it." with text_dissolve

    mc "Oh damn... my b." with text_dissolve

    show j_annoyed at offscreenleft
    show c_scared at offscreenright
    with dict_emotion_change

    "Camilla starts rummaging around the area." with text_dissolve

    show c_scared at right
    with moveinright

    c_right "Hey, get down here and help me!" with text_dissolve

    c_right "I am {b}{i}NOT{/i}{/b} going anywhere until we get our flashlight." with text_dissolve

    show c_scared at offscreenright
    with dict_emotion_change

    "You spend a solid 10 minutes ooking for the flashlight in the piles of branches and leaves left behding in the stampede's wake." with text_dissolve

    "Soon you faintly see Camilla emerge from a bush triumphantly, holding the flashlight." with text_dissolve

    "She hands it off to Jesse and you continue walking down the path." with text_dissolve

    hide text
    jump scene2_routeA


label scene2_routeA:

    show c_neutral at right
    with moveinright

    c_right "Hey guys, you remember the story that Tanner told us about earlier right?" with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "You mean the story about The Scrappie Killer?" with text_dissolve

    c_right "Uhhh, yeah that one" with text_dissolve

    show c_scared at right
    with dict_emotion_change

    hide c_neutral
    c_right "Like, what if the killer was still here. Like, what if he's here and following us." with text_dissolve

    j_left "Come on Cami, Tanner was just messing with us. You’re way too easy to scare and like, he’s called the Scrappie Killer, how scary could he possibly be?" with text_dissolve

    mc "The media gives them the names, not the killer himself." with text_dissolve

    c_right "Any killer is a scary killer regardless of the name." with text_dissolve

    mc "That's a good point. Killers are scary." with text_dissolve

    j_left "Whatever, just don't think about Tanner's dumb story." with text_dissolve

    show c_scared at offscreenright
    show j_neutral at offscreenleft
    with dict_emotion_change

    "You walk in silence until Jesse stops abruptly, making you and Camilla bump into him." with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "Alright, don't freak out. That means you Cami." with text_dissolve

    show c_annoyed at right
    with moveinright

    c_right "You little... what is it?" with text_dissolve

    j_left "Do you see that handing from the tree?" with text_dissolve

    show j_neutral at offscreenleft
    show c_annoyed at offscreenright
    with dict_emotion_change

    "Jesse moves the light in the direction he was referring to. The light illuminates the tree." with text_dissolve

    "You spot a little piece of... something stuck in one of the branches." with text_dissolve

    mc "Hmmm, what is that? There's definitely something up in that branch." with text_dissolve

    show c_scared at right
    with dict_moveinright

    c_right "I-is it something scary?" with text_dissolve

    show j_neutral at left
    with dict_moveinleft

    j_left "Uhhhh, no clue. But heh, Cami... you should get it for us." with text_dissolve

    show c_scared at offscreenright
    show c_terrified at right
    with dict_emotion_change

    c_right "HUH?! Por qué yo? Why do I have to go?" with text_dissolve

    j_left "Uhhhh, cause you're the tallest and like the only athletic one here." with text_dissolve

    "Camilla grumbles, and looks up at the tree again, with fear and worry in her eyes." with text_dissolve

    c_right "No way! Send [main_char] up there! Or you go!" with text_dissolve

    mc "If Jesse goes it’ll be a disaster. Do you really expect him to just climb a tree? He couldn’t even climb the jungle gym." with text_dissolve

    show c_terrified at offscreenright
    show c_annoyed at right
    with dict_emotion_change

    c_right "ALRIGHT! Alright... but if anything happens..." with text_dissolve

    j_left "We won't let anything happen to you. just get it and run back." with text_dissolve

    show c_annoyed at offscreenright
    show j_neutral at offscreenleft
    with dict_emotion_change

    "Camilla gingerly walks over to the tree and proceeds to climb. Partway up she stops and grabs whatever it is hanging in the branches." with text_dissolve

    "You and Jesse walk over to the tree as well, and wait expectantly as Camilla climbs down as graceful as ever." with text_dissolve

    show c_happy at right
    with moveinright

    c_right "Heh, piece of cake." with text_dissolve

    "She holds up the item for us to see." with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "It looks like a piece of fabric?" with text_dissolve

    show c_happy at offscreenright
    show c_neutral at right
    with dict_emotion_change

    mc "Why would a piece of fabric be stuck to a tree branch so high up... in the middle of the woods?" with text_dissolve

    j_left "It probably tore from someone's costume. We're on the right path then!" with text_dissolve

    show c_neutral at offscreenright
    show c_scared at right
    with dict_emotion_change

    c_right "No... Jesse look! It's perfectly cut. That doesn't come from a torn costume. Oh no, Oh nooooo..." with text_dissolve

    menu:
        with dissolve

        "You look to Camilla for an explanation":

            $ freak_out += 1
            show j_neutral at offscreenleft
            with dict_emotion_change
            hide text
            jump scene2A_freakout
    
        "You look to Jesse for an explanation":

            $ stay_calm += 1
            show c_scared at offscreenright
            with dict_emotion_change
            hide text
            jump scene2A_calm


label scene2A_calm:
    j_left "You know what... you're right." with text_dissolve
    j_left "Wait! This is a crazy coincidence!" with text_dissolve

    show j_neutral at offscreenleft
    show j_happy at left
    with dict_emotion_change

    j_left "This is just like this scene of an anime I'm watching right now." with text_dissolve
    j_left "It's called Deserk and it's this fighty anime because you know... I eat that shit up for breakfast, lunch, and dinner." with text_dissolve

    show j_happy at offscreenleft
    with dict_emotion_change

    "Jesse proceeds to ferociously explain in great detail the plot of the anime." with text_dissolve

    "No one asked for this and yet, here we are." with text_dissolve

    "You and Camilla share a knowing look and continue to walk, dragging Jesse along while he explains how Griffin could be better if only the writers gave him the chance." with text_dissolve

    "The ominous scrap of cloth is forgotten about." with text_dissolve

    "Nothing to worry about here..." with text_dissolve

    "Nope..." with text_dissolve

    "Hey! Stop searching! There's nothing here!" with text_dissolve

    hide text
    jump scene3_routeA

label scene2A_freakout:
    c_right "Oh my god it's him..." with text_dissolve

    mc "It's who?" with text_dissolve

    show c_terrified at right
    with dict_emotion_change
    hide c_scared
    c_right "Don't you remember the story?! He leaves scraps of fabric! That's his calling card!" with text_dissolve

    show c_terrified at offscreenright
    with dict_emotion_change

    "She starts pacing back and forth, her mind going a mile a minute." with text_dissolve
    "The panic starts to set in and nothing either of you say is working to ease her nerves." with text_dissolve

    show c_terrified at right
    with dict_moveinright

    c_right "I won't let him get me!" with text_dissolve

    show c_terrified at offscreenright
    with dict_emotion_change

    show j_neutral at left
    with dict_moveinleft

    j_left "CAMI! WAIT!" with text_dissolve

    show j_neutral at offscreenleft
    with dict_emotion_change

    "You and Jesse go after her, barely keeping up between her incredible speed fueled by fear and the uneven terrain." with text_dissolve

    "It takes a while but she finally runs out of gas and begins to slow down enough for you and Jesse to catch up to her." with text_dissolve

    mc "Hey... it's alright. We won't let anything get you okay?" with text_dissolve

    "After some more reassurance, you are able to get Camilla back on the path to the party." with text_dissolve

    "The whole fiasco definitely ate up some of your time." with text_dissolve

    hide text
    jump scene3_routeA



label scene3_routeA:

    scene forest_fog with Dissolve(3.0)
    "As you continue along the path, everyone is starting to feel restless." with text_dissolve

    show c_neutral at right
    with moveinright

    c_right "Ya llegamos?" with text_dissolve

    "Jesse sighs and rolls his shoulders, completely ignoring her question." with text_dissolve

    mc "That sounded like a hard no." with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "Not there yet, but we're totally beating Tanner and Sequinn right now." with text_dissolve

    mc "How can you be so sure of that?" with text_dissolve

    j_left "I can just sense it." with text_dissolve

    c_right "Well, see if you sense the fastest way there." with text_dissolve

    show j_annoyed at left
    with dict_emotion_change
    hide j_neutral

    j_left "Oh, you're right. Let me just activate my Dude Scout powers and sing a song to the stampede to get us out like a Sidney Princess." with text_dissolve

    mc "Hey what’s been going on lately? You’ve been especially snarky, sir. Everyone has been fighting all night, what gives? Did I miss something?" with text_dissolve

    show c_scared at right
    with dict_emotion_change
    hide c_neutral

    c_right "It's just really scary out here..." with text_dissolve

    j_left "No... Tanner and I got into it a few days ago over something stupid." with text_dissolve

    show j_angry at left
    show j_annoyed at offscreenleft
    with dict_emotion_change

    j_left "He doesn't know how to let things go! And that's exactly why he is going the wrong way." with text_dissolve

    j_left "He just always has to be right!" with text_dissolve

    show c_neutral at right
    with dict_emotion_change
    hide c_scared

    c_right "You two have been friends longer than any of us. You shouldn’t fight like that." with text_dissolve

    j_left "He’s just jealous. I’ve been spending so much time with Henry and he wants to hang out with me all the time. But I have a life too!" with text_dissolve

    menu:
        with dissolve

        "You’re both being idiots about it. We’re adults! Act like it and talk it out.":
            $ routeA_scene3_choice = "both idiots"
            mc "You've been friends damn near since birth. If you can't talk about things now, you have no business being friends." with text_dissolve

            c_right "[main_char] is right. Stop acting like children and just talk to your bestie." with text_dissolve

            show j_neutral at left
            show j_angry at offscreenleft
            with dict_emotion_change


            j_left "Maybe you're right... I'll talk to him when we get out of these woods." with text_dissolve

            show c_scared at right
            with dict_emotion_change
            hide c_neutral

            c_right "{i}If we get out of these woods{/i}." with text_dissolve

            j_left "Cami, no." with text_dissolve

            show c_scared at offscreenright
            show j_neutral at offscreenleft
            with dict_emotion_change

            hide text
            jump scene3_routeA_continued
        
        "You’re right. Tanner needs to get over himself.":

            $routeA_scene3_choice = "not both idiots"
            mc "Maybe he needs to find someone so he doesn't depend on you all the time." with text_dissolve

            c_right "Oh! I know some absolutely adorable goth girls who are all for his... uhhh... vibe?" with text_dissolve

            show j_angry at offscreenleft
            show j_neutral at left
            with dict_emotion_change

            j_left "Last time you played matchmaker, [main_char] ended up getting robbed and locked in a meat locker." with text_dissolve

            c_right "I have apologized a billion times. How was I supposed to know they were born with crazy in their DNA?" with text_dissolve

            mc "I did leave with some prime cuts so it wasn’t all bad." with text_dissolve

            j_left "Yeah, well maybe Tanner needs some roast beef..." with text_dissolve

            c_right "Ain't no way..." with text_dissolve

            show j_neutral at offscreenleft
            show c_neutral at offscreenright
            with dict_emotion_change

            hide text
            jump scene3_routeA_continued

        "You have been spending a lot of time with Henry though.":
            $routeA_scene3_choice = "not both idiots"

            mc "You barely spend time with us too." with text_dissolve

            c_right "Yeah we hardly see you anymore. But new love is always like that I suppose." with text_dissolve

            j_left "Not you two getting on my case too! My world doesn’t revolve around you!" with text_dissolve

            mc "We know that Jesse, we just don't want you to put all your eggs in one basket you know?" with text_dissolve

            c_right "You’re always so responsible until it comes to love. We’re here for you too." with text_dissolve

            j_left "Let's just keep walking." with text_dissolve

            show c_neutral at offscreenright
            show j_angry at offscreenleft
            with dict_emotion_change

            hide text

            jump scene3_routeA_continued

label scene3_routeA_continued:
    "Your group moves along the path. As you continue along, you notice the path splits into two different locations." with text_dissolve

    show j_happy at left
    with moveinleft

    j_left "Oh! I remember the fork being here on the map!" with text_dissolve

    show c_happy at right
    with moveinright

    c_right "That's amazing!! Do you remember which way to go?" with text_dissolve

    show j_happy at offscreenleft
    show c_happy at offscreenright
    with dict_emotion_change

    "A moment of hesitation comes over Jesse. It would appear that he does not." with text_dissolve

    show j_neutral at left
    with dict_moveinleft

    j_left "Uhhhhh..." with text_dissolve

    mc "Another hard no it seems." with text_dissolve

    show c_neutral at right
    with dict_moveinright

    c_right "Time's up J, where do we go?" with text_dissolve

    "The three of you proceed to look at the paths before you, trying to come up with a decision together." with text_dissolve

    c_right "So... yeah. This one looks absolutely terrifying. We should go down the other path." with text_dissolve

    j_left "Wait... I think we should take the spooky path." with text_dissolve

    c_right "You... You think a group of college kids lost in the woods at night, {b}{i}Halloween Night{/i}{/b} to be exact, should take the spooky path?" with text_dissolve

    c_right "That's the thought you decided to think?" with text_dissolve

    mc "I mean it {i}does{/i} kind of sound like a horror movie plot waiting to happen. We already split into 2 groups." with text_dissolve

    j_left " I totally think that I like, kind of remember seeing that we should take this way on the map." with text_dissolve

    c_right "Uh huh, no thanks. I'd rather take the one that looks less menacing." with text_dissolve

    show c_neutral at offscreenright
    show j_neutral at offscreenleft
    with dict_emotion_change

    "Jesse and Camilla look at you expectantly." with text_dissolve

    mc "Why do I have to always make the decision?" with text_dissolve

    "You try to recall what you saw on the map. Hopefully you looked at more than just those blobs." with text_dissolve

    menu:
        with dissolve

        "You point to the less spooky path":
            $ freak_out += 1

            hide text
            jump scene3A_freakout

        "You point to the spooky path":
            $ stay_calm += 1

            hide text
            jump scene3A_calm

    
label scene3A_freakout:

    show j_neutral at left
    with moveinleft

    j_left "Awwww, come on. Don't you all trust me?" with text_dissolve

    mc "Sorry Jesse. I’m with Cami on this one. Don’t want to risk anything happening." with text_dissolve

    j_left "I guess..." with text_dissolve

    show c_neutral at right
    with moveinright

    c_right "We’re alone in these woods, if we get lost we don’t know how to get back." with text_dissolve

    j_left "Alright, that makes sense." with text_dissolve

    show c_happy at right
    with dict_emotion_change

    hide c_neutral

    c_right "Yay! Do the math, take the safe path! Woooo!" with text_dissolve

    show c_happy at offscreenright
    show j_neutral at offscreenleft
    with dict_emotion_change

    "You proceed to take the less spooky path. You seem to be walking forever, hardly making your way out of this dense patch of forest." with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "We've been walking for a while now. I don't know if this was the right direction." with text_dissolve

    show c_neutral at right
    with moveinright

    c_right "No look! There's an opening up ahead!" with text_dissolve

    hide text

    jump scene4_routeA

label scene3A_calm:
    
    show c_scared at right
    with moveinright

    c_right "WHAT!?" with text_dissolve

    mc "I gotta go with Jesse on this one. I remember seeing this path marked on the map." with text_dissolve

    show j_happy at left
    with moveinleft

    j_left "See! The great and wise [main_char] has spoken!" with text_dissolve

    c_right "...Do we have to?" with text_dissolve

    show j_neutral at left
    with dict_emotion_change
    hide j_happy

    j_left "Sorry Cami. The right path may be spooky, but nothing worth having ever comes easy." with text_dissolve

    c_right "Oh stuff it you uninspirational quack." with text_dissolve

    show j_neutral at offscreenleft
    show c_scared at offscreenright
    with dict_emotion_change

    "Camilla hesitates for another moment, seeming to consider options." with text_dissolve

    show c_annoyed at right
    with moveinright

    c_right "If [main_char] says so then I guess I can't argue. I'll trust your judgement on this since you also looked at the map." with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "See... I knew I was right." with text_dissolve

    c_right "We have nothing right now." with text_dissolve

    "Jesse does an anime pose." with text_dissolve

    j_left "Just trust me! Nyan~" with text_dissolve

    show c_annoyed at offscreenright
    show j_neutral at offscreenleft
    with dict_emotion_change

    "You and your friends walk through this darker part of the woods. Though much more ominous, the woods seem to be treating you well." with text_dissolve

    hide text
    
    jump scene4_routeA

label scene4_routeA:
    "You come out into a clearing." with text_dissolve
    "Looking back, both paths ended up leading to the same location." with text_dissolve
    show c_neutral at right
    with moveinright

    c_right "Huh, guess it didn't really matter which one we took then." with text_dissolve

    show j_neutral at left
    with moveinleft

    j_left "It seems like it." with text_dissolve

    mc "Who knows, one of them may have been a shorter path." with text_dissolve

    j_left "You could be right." with text_dissolve

    j_left "Let's go. If that was the longer path, we gotta keep moving forward so we can beat Tanner and Sequinn." with text_dissolve

    c_right "I don't care about winning or losing. I just want to get out of these scary woods before I end up attacked by spiders next!" with text_dissolve

    mc "You’ll be lucky if a spider even wants to be near you with you freaking out every 10 seconds." with text_dissolve
    
    show c_neutral at offscreenright
    show c_annoyed at right
    with dict_emotion_change

    c_right "Hey fun fact... Shut up." with text_dissolve

    show j_neutral at offscreenleft
    show c_annoyed at offscreenright
    with dict_emotion_change

    "You and your friends laugh and talk as you make your way through the woods. Though dark and foggy, you’re enjoying your walk, joking around with Camilla and Jesse." with text_dissolve
    "As you all let your guards down, you notice something glint in the moonlight." with text_dissolve

    mc "The hell is that?" with text_dissolve

    jump flashlight_minigame


label scene5_routeA:
    show j_neutral at left
    with moveinleft

    j_left "Okay, so after that small clearing, there should be an even bigger clearing up ahead and that's where the party should be!" with text_dissolve

    show c_neutral at right
    with moveinright

    c_right "God, I hope so... It's so hard to see. It's so dense in this part of the forest." with text_dissolve

    mc "I don't see Tanner or Sequinn anywhere. I hope they're okay." with text_dissolve

    show j_annoyed at left
    with dict_emotion_change
    hide j_neutral

    j_left "Hmph... They should have came with us but Tanner is so stubborn and Sequinn was just... being Sequinn." with text_dissolve

    mc "Jesse, don't you start." with text_dissolve

    show c_neutral at offscreenright
    with dict_ease
    hide c_neutral

    show c_scared at right
    with dict_emotion_change

    c_right "Oh... What if they got caught in some traps too?! Who knows what crazy cannibal family is living here hunting people for dinner!" with text_dissolve

    mc "Cami, don't {b}{i}you{/i}{/b} start." with text_dissolve

    show j_happy at left
    with dict_emotion_change
    hide j_neutral

    j_left "OoOoOoO... they'll go for your thighs first." with text_dissolve

    show c_scared at offscreenright
    show c_terrified at right
    with dict_emotion_change

    c_right "How?! Why?!?" with text_dissolve

    j_left "Hahaha! That's what I would do." with text_dissolve

    c_right "Come on. Let's go! I will not become a 5-Star meal." with text_dissolve

    show j_happy at offscreenleft
    show c_terrified at offscreenright
    show j_annoyed at offscreenleft
    with dict_emotion_change

    "You shake your head, partly amused at how easy it is to get someone so confident worked up. As you push past the shrubs and brush, you hear a whisper from Camilla." with text_dissolve

    show c_neutral at right
    with dict_moveinright

    c_right "Hey guys, do you see that?" with text_dissolve

    show j_neutral at left
    with dict_moveinleft

    j_left "See what Cami?" with text_dissolve

    show c_scared at right
    with dict_emotion_change

    hide c_neutral

    c_right "Shhhhhhh! Keep it down!" with text_dissolve

    "She pushes both you and Jesse to a crouching position. You crane your head to the direction she's pointing to." with text_dissolve

    c_right "O-o-over there... a light... floating?" with text_dissolve

    "Jesse leans into you to get a closer look." with text_dissolve

    j_left "Oh yeah yeah... I can see it." with text_dissolve

    mc "It's probably the light from the party." with text_dissolve

    c_right "Pero, it's too small and the wrong color for a bonfire. That's a red light, not an orange glow." with text_dissolve

    mc "Oh, come on Cami. Eventually you will need to get over all this fear. It's nothing!" with text_dissolve

    play sound "assets/music/ghost_scream.ogg" volume 0.75

    $ renpy.pause (1.5, hard = True)

    stop sound fadeout 2.0

    show j_terrified at left
    show c_terrified at right
    with dict_emotion_change
    hide j_neutral
    hide c_scared

    j_left "OHHHH! But that was something!" with text_dissolve

    show c_terrified at right
    with dict_emotion_change
    hide c_scared

    c_right "Fuck this! Give me that!" with text_dissolve

    "Camilla reaches into the pockets in Jesse’s costume and pulls out his (totally, 100%% legally acquired) smoke bombs." with text_dissolve

    j_left "Hey! What are you doing with my smoke bombs!" with text_dissolve

    c_right "I won't go down without a fight!" with text_dissolve

    show c_terrified at offscreenright
    show j_terrified at offscreenleft
    with dict_emotion_change

    "She chucks the smoke bomb and rocks in the direction of the horrible light and sound. All of the sudden the light starts to flicker rapidly..." with text_dissolve

    show j_terrified at left
    with moveinleft

    play sound "assets/music/digitalscream.ogg"
    stop music fadeout 3.0
    
    j_left "You pissed it off!" with text_dissolve


    play music "../game/assets/music/Fright-Fest.ogg" fadein 3.0 loop

    show c_terrified at right
    with moveinright

    c_right "This is what I get for being brave?!? Death?!" with text_dissolve

    show c_terrified at offscreenright
    show j_terrified at offscreenleft
    with dict_emotion_change

    menu:  
        with dissolve

        "No, We are getting the hell out of here!":
            $stay_calm += 1
            hide text
            jump scene5A_calm

        "W-We have to hide!":
            $freak_out += 1
            hide text
            jump scene5A_freakout

label scene5A_calm:
    "You and your friends book it down the path, rushing past the evil red light." with text_dissolve

    show c_terrified at right
    with moveinright

    c_right "Fantasma demonio! That was definitely a demon ghost! You can’t run from demon ghosts!" with text_dissolve

    show j_terrified at left
    with moveinleft
    
    j_left "My wig is going to be a mess after all this!" with text_dissolve

    mc "Just shuddup and keep running!" with text_dissolve

    c_right "Si salgo de esto viva, te lo juro que voy a sacar la basura y nunca me voy a agachar de una chancla. Y le voy a llamar a mi abuela!" with text_dissolve

    j_left "Why is she breaking out the Spanish!?" with text_dissolve

    mc "Less talky, more runny!" with text_dissolve

    show c_terrified at offscreenright
    show j_terrified at offscreenleft
    with dict_emotion_change

    hide text

    jump scene_party

label scene5A_freakout:
    "You and your friends duck behind some foliage, hoping that the danger would pass." with text_dissolve

    $ renpy.pause (3.0, hard = True)

    show c_terrified at right
    with moveinright

    c_right "Do y-you think it's g-gone far enough now?" with text_dissolve

    show j_terrified at left
    with moveinleft
    
    j_left "I don't know where the heck it is but stay down." with text_dissolve

    show c_terrified at offscreenright
    show j_terrified at offscreenleft
    with dict_emotion_change

    "After some time, the noise fades away." with text_dissolve

    mc "We should be good now. I don't hear anything anymore." with text_dissolve

    "Eventually you and your friends feel comfortable enough to leave the safety of your hiding spot." with text_dissolve

    "All three of you book it down the path, putting as much distance between yourselves and the mysterious entity as you can." with text_dissolve

    hide text

    jump scene_party


