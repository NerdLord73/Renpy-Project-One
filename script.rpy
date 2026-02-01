define one = Character("The Mind", color = "#CFA2FD" )
define two = Character("The Man", color = "#1F7DE8")
define three = Character("You", color = "#31D457")
define four = Character("Serpent", color = "#FF1A00")


label start:

    scene bg renintro
    one "Awaken."
    "You come to with very little memory, everything seems a blur."
    "You lay in a canopy, facing a beautiful night sky."
    "Nothing moves; the owls are silent, and the usual rattling of the leaves on the wind has ceased."
    "Somehow, you know that this world is utterly abandoned."
    two "Something is wrong."
    one "You should get moving."

label choices0:
    "What should you do?"
menu:
    "Get up.":
        jump choice00
    "Continue laying down.":
        jump choice01

label choice00:
    scene bg truck
    jump sc2

label choice01:
    one "Shameful."
    two "We're really not going to investigate?"

menu:
    "Nope.":
        jump choice010
    "FINE.":
        jump choice00

label choice010:
    "Time passes on without fail, as it always has. You grow hungry, weak, and weary, and just like your memories, eventually give way to nothingness."
    "Good ending achieved."

return

label sc2:
    
    two "Lights! Maybe it's a truck? see if you can grab some supplies."
    one "Maybe see if you can find the road it was on. After all, don't want to start your new life a criminal."

label choices1:
    "What will you do?"
menu:
    "See if you can find a road.":
        jump choice10
    "Go steal.":
        jump choice11

label choice10:
    scene bg light
    "Where moments ago you thought you saw headlights, a lamppost emerges from the forested darkness."
    one "There! In the distance, I see some sort of opening!"
    two "No supplies though..."
    jump choiceext0

label choice11:
    scene bg light
    "Where moments ago you thought you saw headlights, a lamppost emerges from the forested darkness."
    two "DAMNIT!"
    one "Calm yourself. Look, there's an opening in the trees that way!"
    jump choiceext0

label choiceext0:
    scene bg church
    "You come upon an open field."
    "Disguised by the hill is an old church, bathed in sickly moonlight."
    "Eerily, the grass doesn't sway one bit."
    "Then you hear it, a rustling."
    "It's the first thing you've heard since waking up."
    two "Thank goodness, something's moving for once, you should go in and see what it is."
    one "A house of the lord, surely it should be your sanctuary."

label choices2:
menu:
    "Enter the church?":
        jump choice20

label choice20:
    scene bg churchin
    "The front door is barricaded, forcing you to enter through the side window. You hope you haven't upset the building's residents."
    "For the first time, somewhere feels alive; a breeze blows past your head as you turn to face the nighttime sky out the window."
    jump choiceext1

label choiceext1:
    scene bg dark
    four "Hello new neighbor."
    show serpent zero
    four "What brings you to my humble inhabitance?"
    "You're glad that this thing is buried in darkness because you wince to look at it."
    "A snake's body, covered in spiny hairs, leads up to a slimy, deformed head, goat-like in nature. Its breath smells of decay, and crusted blood lines its sickening maw"
    one "Run, hide, fight, get away from him."
    two "He'll kill us on the spot if we do that, say something smart."
    four "No need to run, I can already smell the worry on your coat..."

label choices30:
menu:
    "Run like hell.":
        jump choice30
    "Fight like hell.":
        jump choice30
    "Hide like a baby.":
        jump choice30
    "Steel your nerves, speak to the thing.":
        jump choice31

label choice31:
    three "Sorry, I didn't mean to intrude. It's just, I'm lost and this was the first building I could find."
    show serpent one
    four "Ah, you're one of them."
menu:
    "What?":
        jump choiceext2

label choiceext2:
    four "No matter, let's start with introductions, my name is Satan. Welcome to Hell"
menu:
    "WHAT?":
        jump choiceext3

label choiceext3:
    four "Be not alarmed, you have been sent here a... Savior of sorts, to purge sin, not wallow in it."
    four "You'll need to gather the most deadly of that slithering kind, and bring them here to the church as your predecessor did to me..."
    "He gazes down at the floor in apparent resentment, though you feel he's holding back."
menu:
    "No offense, but why would the devil rebuke sin?":
        jump choiceext4

label choiceext4:
    four "I am caged here in this monolith to the one who spurns me, unable to escape."
    four "I wish no longer to suffer, but I have hope that rapture which you might bring will return me to the father's embrace."
    one "Don't listen, everything about him says he's lying."
    two "You have to listen, if you can do what he says, you might escape too."

menu:
    "Sympathy for the devil.":
        jump choiceext5
    "Indifference.":
        jump choice30

label choiceext5:
    "Worst ending achieved."

return

label choice30:
    four "He catches you with lightning speed, constricting you tightly in his tail."
    four "Yet another coward..."
    four "Empty, stupid, without redemption; yet God's mission marks you the favorite child."
    show serpent one
    four "You would do anything but confront your sin..."
    "He bites directly into your head; you have a feeling you won't be coming back from this one..."
    "Bad ending achieved."


    return
