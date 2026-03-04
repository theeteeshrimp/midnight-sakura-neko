define y = Character("Yuna", color="#ffd6f1")
define p = Character("Protagonist", color="#c8ffe5")
define n = Character(None)

default affinity = 0

label start:
    scene black
    with fade

    n "A city of sakura, neon, and midnight trains."
    n "You miss your stop—and meet an anime catgirl on a quiet platform."

    y "You're new here, huh?"
    p "Is it that obvious?"
    y "Only to me. I'm Yuna, a stray anime catgirl who knows every sakura alley in this city."

    menu:
        "How do you respond?"

        "Smile and introduce yourself":
            $ affinity += 1
            p "Then I'm lucky you found me first."
            y "Heh. Smooth."

        "Act cool and stay distant":
            $ affinity -= 1
            p "I'm fine on my own."
            y "Sure. If you say so."

    if affinity > 0:
        n "Petals drift between the station lights as she offers to show you the city."
        y "Come on. I'll show you my favorite sakura street."
    else:
        n "She turns, tail swaying, giving you one last look."
        y "If you get lost again, find the sakura clocktower."

    n "End of demo chapter."
    return
