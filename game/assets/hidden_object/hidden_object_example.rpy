# Define some point and click objects
default traps_groundsnare = pnco(
    "Ground Snare",
    "assets/hidden_object/traps/ground_snare.png",
    (0, 0),
    items = ["Ground Snare"]
    )
default traps_deadfall = pnco(
    "Deadfall Trap",
    "assets/hidden_object/traps/deadfall_trap.png",
    (0, 0),
    items = ["Deadfall Trap"]
    )
default traps_netdrop = pnco(
    "Net Drop",
    "assets/hidden_object/traps/net_drop.png",
    (0, 0),
    items = ["Net Drop"]
    )
default traps_rockdrop = pnco(
    "Rock Drop",
    "assets/hidden_object/traps/rock_drop.png",
    (0, 0),
    items = ["Rock Drop"]
    )
default traps_springsnare = pnco(
    "Sprin Snare",
    "assets/hidden_object/traps/spring_snare.png",
    (0, 0),
    items = ["Spring Snare"]
    )
default traps_springtrap = pnco(
    "Spring Trap",
    "assets/hidden_object/traps/spring_trap.png",
    (0, 0),
    items = ["Spring Trap"]
    )
default traps_nettrap = pnco(
    "Net Trap",
    "assets/hidden_object/traps/net_trap.png",
    (0, 0),
    items = ["Net Trap"]
    )

# Define a point and click location
default hidden_object = pncs(
    "Traps",
    [
        traps_groundsnare,
        traps_deadfall,
        traps_netdrop,
        traps_rockdrop,
        traps_springsnare,
        traps_springtrap,
        traps_nettrap,
    ],
    darkness = "../game/assets/images/flashlight_minigame/darkness.webp"

)


label minigame:
    show forest_fog with dict_dissolve_1seconds
    call screen pnc(p = None, g=hidden_object)
    if _return:
        "I can't believe I found all those traps..."
        "I'm glad I did though... Someone could have gotten hurt!"
        $stay_calm += 1

        jump flashlight_minigame_calm

    else:
        "I don't see anything else."
        "We should be fine to move forward."
        $freak_out += 1
        jump flashlight_minigame_freakout
