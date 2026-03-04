define y = Character("Yuna", color="#ffd6f1")
define p = Character("Protagonist", color="#c8ffe5")
define n = Character(None)

default affinity = 0

default route_flag = "none"

label start:
    scene black
    with fade

    n "Sakura petals drift through neon light like pink snow."
    n "The final train sighs into Shiun Station... and you step out at the wrong stop."

    p "Wait—this isn't my district."

    n "A soft bell chimes. A girl with cat ears lands on the platform rail like it's nothing."

    y "Nyaa~ Lost traveler detected."
    p "Uh... did you just jump from up there?"
    y "Maybe. I'm Yuna—resident anime catgirl, midnight guide, part-time troublemaker."

    menu:
        "How do you respond?"

        "Play along with her energy":
            $ affinity += 1
            $ route_flag = "warm"
            p "Then guide me, O mysterious sakura spirit."
            y "Hehe, good answer. You learn fast."

        "Act cool and guarded":
            $ affinity -= 1
            $ route_flag = "cold"
            p "I can handle myself."
            y "Mm. Brave words for someone reading the map upside down."

    scene black
    with dissolve
    n "A breeze sweeps petals across the tracks. Somewhere, festival music echoes."

    if route_flag == "warm":
        jump scene_sakura_walk
    else:
        jump scene_clocktower_hint

label scene_sakura_walk:
    n "Yuna grabs your sleeve and pulls you toward a hidden side street glowing with paper lanterns."
    y "Rule one of this city: never rush past sakura at night."
    p "Why?"
    y "Because some meetings only happen once."

    menu:
        "Your next move"

        "Ask about her":
            $ affinity += 1
            p "So who are you really?"
            y "A girl who knows every shortcut—and pretends she doesn't get lonely."

        "Ask about the city":
            p "This place feels unreal."
            y "It's real. Just... softer after midnight."

    jump ending_demo

label scene_clocktower_hint:
    n "Yuna hops down, tail swaying, eyes bright under station lights."
    y "Fine. Do it your way."
    y "But if this city swallows you, find the sakura clocktower at dawn."
    p "Why dawn?"
    y "Because that's when masks get tired."

    jump ending_demo

label ending_demo:
    if affinity >= 1:
        n "As you walk, Yuna hums a tune you somehow already know."
        n "A new route has opened in your heart."
    else:
        n "You leave alone, but the scent of sakura follows you home."
        n "Some stories begin with distance."

    n "END OF PROLOGUE DEMO"
    n "(Chapter 1: Sakura Clocktower, coming next.)"
    return
