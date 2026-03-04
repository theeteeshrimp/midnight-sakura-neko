define y = Character("Yuna", color="#ffd6f1")
define p = Character("Protagonist", color="#c8ffe5")
define a = Character("Akari", color="#ffe3b0")
define n = Character(None)

default affinity = 0
default honesty = 0
default courage = 0
default myth_clue = 0

default route_flag = "none"

default clue_clocktower_note = False
default clue_last_train_story = False

default chapter = 0

default journal = []

label add_journal(entry):
    $ journal.append(entry)
    return

label start:
    $ chapter = 0
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
            $ honesty += 1
            $ route_flag = "warm"
            p "Then guide me, O mysterious sakura spirit."
            y "Hehe, good answer. You learn fast."
            call add_journal("Met Yuna and matched her playful energy.")

        "Act cool and guarded":
            $ courage += 1
            $ route_flag = "cold"
            p "I can handle myself."
            y "Mm. Brave words for someone reading the map upside down."
            call add_journal("Met Yuna but kept emotional distance.")

    scene black
    with dissolve
    n "A breeze sweeps petals across the tracks. Somewhere, festival music echoes."

    jump chapter_1_clocktower

label chapter_1_clocktower:
    $ chapter = 1
    scene black
    with fade

    n "[Chapter 1: Sakura Clocktower]"

    n "Before dawn, Yuna leads you uphill through quiet lanes."
    n "The clocktower rises above old rooftops, ringed by sakura branches."

    y "People come here when they want answers."
    y "Or when they're scared to hear them."

    menu:
        "What do you ask Yuna?"

        "Ask directly about the Neko Hour":
            $ myth_clue += 1
            $ honesty += 1
            p "Everyone talks about the Neko Hour. Is it real?"
            y "Real enough to ruin bad excuses."
            y "Between last train and first light, the city gets honest."
            $ clue_last_train_story = True
            call add_journal("Asked Yuna directly about the Neko Hour myth.")

        "Ask why she helps strangers":
            $ affinity += 1
            $ honesty += 1
            p "Why help me at all?"
            y "Because lost people lie the least in their eyes."
            y "And because someone once did this for me."
            call add_journal("Asked Yuna personal questions instead of chasing rumor.")

        "Stay quiet and observe":
            $ courage += 1
            p "..."
            n "You notice old charms tied to the railing, each with a name."
            y "Silence counts as an answer too."
            call add_journal("Stayed quiet at the clocktower and observed details.")

    n "A station bell echoes from downhill. Akari, the morning attendant, appears with a thermos."

    a "So you're this season's midnight pair."
    p "This season's what?"
    a "Never mind. Tea?"

    menu:
        "How do you respond to Akari?"

        "Accept tea and ask about the clocktower":
            $ myth_clue += 1
            $ clue_clocktower_note = True
            a "Every bloom season, someone leaves a note up here at dawn."
            a "Same handwriting. Different names."
            p "What does it say?"
            a "'Don't be late to your own heart.'"
            call add_journal("Learned about the repeating clocktower note.")

        "Decline tea and focus on Yuna":
            $ affinity += 1
            $ courage += 1
            p "I'll pass. I just want one clear answer from Yuna."
            y "Dangerous. I like it."
            call add_journal("Ignored side info to focus on Yuna.")

        "Joke to deflect the tension":
            $ honesty -= 1
            p "If this is a cult, do I get a membership card?"
            a "Only if you stop pretending this is funny."
            call add_journal("Used humor to dodge uncomfortable questions.")

    if route_flag == "warm":
        n "Yuna walks beside you down the hill, close enough to brush your sleeve."
        y "Tonight, Sakura Alley. If you're serious."
    else:
        n "Yuna hops ahead, then glances back once."
        y "If you're brave, come to Sakura Alley tonight."

    jump chapter_1_end

label chapter_1_end:
    scene black
    with dissolve

    n "Chapter 1 Complete."

    if myth_clue >= 2:
        n "You now carry two pieces of the city's midnight rumor."
    elif affinity >= 2:
        n "You don't know the city's truth yet, but Yuna is opening up."
    else:
        n "You leave with more questions than answers."

    n "[Chapter 2 begins now.]"
    jump chapter_2_split

label chapter_2_split:
    $ chapter = 2
    scene black
    with fade

    n "Night falls again. Lantern light blooms across Hanamichi City."
    y "So? Follow your heart or your curiosity?"

    menu:
        "Choose tonight's route"

        "Go with Yuna to Sakura Alley (Romance Route)":
            $ route_flag = "romance"
            jump chapter_2_sakura_alley

        "Investigate Lantern District rumors (Mystery Route)":
            $ route_flag = "mystery"
            jump chapter_2_lantern_district

label chapter_2_sakura_alley:
    scene black
    with dissolve

    n "You follow Yuna through narrow lanes covered in petals and paper lights."
    y "No masks tonight, okay?"

    menu:
        "How honest are you with Yuna?"

        "Tell her you're scared of getting attached":
            $ honesty += 2
            $ affinity += 1
            p "I keep pretending I'm fine alone. I'm not."
            y "...good. Keep talking like that."
            call add_journal("In Sakura Alley, I admitted my fear of attachment.")

        "Flirt and keep things light":
            $ affinity += 1
            p "Maybe I'm only here because you look unfairly cute under lanterns."
            y "Heh. Acceptable answer."
            call add_journal("In Sakura Alley, I kept things playful with Yuna.")

        "Deflect and joke":
            $ honesty -= 1
            p "I'm just collecting midnight side quests."
            y "That's not what I asked."
            call add_journal("In Sakura Alley, I dodged emotional honesty.")

    n "Yuna stops near an old torii wrapped in blossoms."
    y "If we meet here next week, make sure it's not by accident."

    if honesty >= 2:
        $ courage += 1
        p "Then I'll choose it on purpose."
        y "...okay."
        call add_journal("I promised intention instead of coincidence.")

    jump chapter_2_merge

label chapter_2_lantern_district:
    scene black
    with dissolve

    n "You head to Lantern District, where old shop signs sway in the wind."
    n "Akari waits near a shuttered tea shop, like she expected you."

    a "Looking for ghost stories, or your own reflection?"
    p "Both, maybe."

    menu:
        "What lead do you chase?"

        "The station archives about last-train sightings":
            $ myth_clue += 2
            $ courage += 1
            n "You find repeated reports: same time, same sakura wind, same cat-eared witness."
            call add_journal("Investigated station logs tied to Neko Hour sightings.")

        "Interview stall owners about the clocktower note":
            $ myth_clue += 1
            $ honesty += 1
            n "Three vendors confirm the same phrase appears every bloom season."
            call add_journal("Cross-checked local stories about the clocktower note.")

        "Follow Yuna from a distance":
            $ myth_clue += 1
            $ affinity -= 1
            n "You lose her twice and feel worse when you finally spot her alone on a bridge."
            call add_journal("Chose suspicion over trust while tracking Yuna.")

    if myth_clue >= 3:
        n "A pattern emerges: the Neko Hour appears around unresolved promises."
        call add_journal("Connected Neko Hour events to unresolved promises.")

    jump chapter_2_merge

label chapter_2_merge:
    scene black
    with fade

    n "Chapter 2 Complete."

    if route_flag == "romance":
        n "Route lock-in trend: Heart-first path."
    elif route_flag == "mystery":
        n "Route lock-in trend: Truth-first path."

    n "[Next: Chapter 3 — Missed Meeting / Trust Fracture]"
    jump codex_preview

label codex_preview:
    n "Route Summary:"
    n "Affinity: [affinity] | Honesty: [honesty] | Courage: [courage] | Myth Clue: [myth_clue]"

    if clue_clocktower_note:
        n "Clue unlocked: Repeating Clocktower Note"
    if clue_last_train_story:
        n "Clue unlocked: Last Train Story"

    if route_flag == "romance":
        n "Current route mood: Sakura Alley (Romance)"
    elif route_flag == "mystery":
        n "Current route mood: Lantern District (Mystery)"

    n "Journal recap:"
    python:
        for i, entry in enumerate(journal, 1):
            renpy.say(n, f"{i}. {entry}")

    return
