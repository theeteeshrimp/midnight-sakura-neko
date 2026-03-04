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
default festival_outcome = "none"

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
    jump chapter_3_trust_fracture

label chapter_3_trust_fracture:
    $ chapter = 3
    scene black
    with fade

    n "Rain starts early. Your phone lights up with one message from Yuna:"
    n "'Clocktower. 11:40. Don't be late.'"

    if route_flag == "romance":
        n "After Sakura Alley, this feels less like an invitation and more like a promise."
    elif route_flag == "mystery":
        n "After Lantern District, this feels like a test."

    menu:
        "How do you handle the meeting?"

        "Go immediately, no excuses":
            $ affinity += 2
            $ courage += 1
            p "On my way."
            call add_journal("I prioritized Yuna and went to the meeting immediately.")
            jump chapter_3_on_time

        "Finish one task first, then go":
            $ honesty += 1
            $ courage += 1
            p "Give me twenty minutes. I'll still come."
            call add_journal("I delayed honestly, hoping not to be too late.")
            jump chapter_3_late

        "Ignore the message":
            $ affinity -= 2
            $ honesty -= 1
            p "..."
            call add_journal("I ignored Yuna's message and avoided the meeting.")
            jump chapter_3_missed

label chapter_3_on_time:
    scene black
    with dissolve

    n "You arrive before the bell chimes. Yuna is already there, tail flicking in the rain."
    y "Whoa. You actually came first."

    if myth_clue >= 3:
        y "Then hear this: the Neko Hour appears when people stand where they once ran."
        $ myth_clue += 1
        call add_journal("Yuna revealed a key Neko Hour condition: choosing to stay.")

    menu:
        "How do you answer her?"

        "I don't want to keep running":
            $ honesty += 2
            $ affinity += 1
            p "I keep pretending timing decides everything. It doesn't. I do."
            y "...good."
            call add_journal("I admitted my pattern of running from closeness.")

        "I came for answers":
            $ myth_clue += 1
            p "Tell me what you are to this city."
            y "Maybe ask who you are to yourself first."
            call add_journal("I pushed the myth question even in a vulnerable moment.")

    jump chapter_3_resolve

label chapter_3_late:
    scene black
    with dissolve

    n "You arrive as the clock hits 12:03. The bench is empty."
    n "A paper charm waits in her place."

    if route_flag == "romance":
        n "The charm reads: 'I wanted to trust tonight.'"
        $ affinity -= 1
    else:
        n "The charm reads: 'Truth waits for no one.'"
        $ myth_clue += 1

    menu:
        "What now?"

        "Call Yuna and apologize directly":
            $ honesty += 2
            $ courage += 1
            p "I messed up. Not because of work—because I hesitated."
            call add_journal("I apologized directly after arriving late.")

        "Rationalize the delay":
            $ honesty -= 1
            p "Any reasonable person would understand."
            call add_journal("I defended myself instead of taking accountability.")

    jump chapter_3_resolve

label chapter_3_missed:
    scene black
    with dissolve

    n "You don't go."
    n "At 2:11 AM, Akari sends one line: 'She waited anyway.'"

    $ courage -= 1
    $ affinity -= 1

    menu:
        "How do you respond to the guilt?"

        "Admit the truth in your journal":
            $ honesty += 1
            p "I wasn't busy. I was afraid of being seen."
            call add_journal("I admitted fear was the real reason I missed the meeting.")

        "Blame circumstances":
            $ honesty -= 1
            p "Timing was impossible tonight."
            call add_journal("I blamed timing instead of my own avoidance.")

    jump chapter_3_resolve

label chapter_3_resolve:
    scene black
    with fade

    n "Chapter 3 Complete."

    if affinity >= 4 and honesty >= 3:
        n "Trust remains fragile, but alive."
    elif myth_clue >= 4:
        n "You are closer to the city's truth than to your own."
    else:
        n "Distance is now a habit, not an accident."

    n "[Next: Chapter 4 — Festival Night Decision]"
    jump chapter_4_festival

label chapter_4_festival:
    $ chapter = 4
    scene black
    with fade

    n "Sakura Festival night. Lanterns ripple in the wind like breathing stars."
    n "Crowds laugh, drums pulse, and every path in Hanamichi seems to lead to one person."

    if route_flag == "romance":
        n "Yuna waits near the torii where you promised not to be accidental."
    else:
        n "Yuna stands by the clocktower stairs, as if deciding whether to trust your questions."

    y "Tonight matters. So don't give me a half-answer."

    menu:
        "Festival Night Decision"

        "Choose Yuna openly (Heart path)":
            $ affinity += 2
            $ honesty += 1
            $ courage += 1
            $ festival_outcome = "heart"
            p "No more drifting. I choose you, on purpose."
            y "...then stay when it's difficult, not just when it's pretty."
            call add_journal("Festival choice: chose Yuna openly and directly.")

        "Choose the truth first (Mind path)":
            $ myth_clue += 2
            $ courage += 1
            $ festival_outcome = "mind"
            p "I need the full truth about the Neko Hour, even if it hurts."
            y "Then hear it without hiding behind analysis."
            call add_journal("Festival choice: prioritized unraveling the city's truth.")

        "Hesitate and postpone":
            $ affinity -= 2
            $ honesty -= 1
            $ courage -= 1
            $ festival_outcome = "drift"
            p "Can we... do this another night?"
            y "You said that last time."
            call add_journal("Festival choice: hesitated and postponed again.")

    # trajectory setup scene
    if festival_outcome == "heart":
        n "Yuna takes your hand and leads you through the lantern gate."
        n "For the first time, the city feels less like a puzzle and more like a place to live."
    elif festival_outcome == "mind":
        n "Akari appears with an old envelope stamped with the clocktower seal."
        a "If you want answers, open this at dawn."
        $ myth_clue += 1
    else:
        n "You watch the festival from the edge, present in body, absent in decision."

    jump chapter_4_resolve

label chapter_4_resolve:
    scene black
    with dissolve

    n "Chapter 4 Complete."

    if festival_outcome == "heart" and affinity >= 5:
        n "Ending trajectory unlocked: Soft Dawn (Romance-forward)."
    elif festival_outcome == "mind" and myth_clue >= 5:
        n "Ending trajectory unlocked: Clocktower Truth (Mystery-forward)."
    else:
        n "Ending trajectory unlocked: Moonlit Distance (Drift risk)."

    n "[Next: Chapter 5 — Dawn Resolution]"
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

    if festival_outcome != "none":
        n "Festival trajectory: [festival_outcome]"

    n "Journal recap:"
    python:
        for i, entry in enumerate(journal, 1):
            renpy.say(n, f"{i}. {entry}")

    return
