from game_engine import * 
import cozyworld
import random
import time

cozy_room = Room("Your room", """
        You are in your cozily appointed room.
        Brightly patterned, hand-knit pillows are
        propped up in little piles against the
        gently curving walls.

        There's a little desk with a cozy lamp on it,
        and a smiling picture of a booper pinned
        up on the wall.
        """,
        "a cozy light glows",
        noop)

@Action("Put on scarf and coat", "p sc")
def put_on_scarf_and_coat(player, room):
    print("""
        You put on your favorite fuzzy scarf and your
        quilted coat""")
    increment_stat(player, "coziness", 3)
    increment_stat(player, "warmth", 10)

@Action("Take off scarf and coat", "p sc")
def take_off_scarf_and_coat(player, room):
    print("""
        You take off your scarf and coat and lay them
        gently on the ground.
        """)
    increment_stat(player, "coziness", -3)
    increment_stat(player, "warmth", -10)

scarf_and_coat = Thingy("scarf and coat", "sc",
        put_on_scarf_and_coat,
        take_off_scarf_and_coat,
        [],
        [])
register_action(cozy_room, scarf_and_coat.grab)

space_hallway = Room("The Hallway", """
        You find yourself in a grand hallway,
        richly appointed in warm-colored wood,
        and filled with stately oil portraits
        and landscapes in golden frames
        """,
        "rich hues gleam...",
        noop) 

PAINTINGS = [("THE COLONEL", "c", """
        A stern mustachioed colonol looking
        off into the middle distance, dressed
        in splendid military uniform with a
        tremendous feathered hat.

        His drooping mustache and somber eyes
        betray a melancholy. You wonder what
        war he fought in, and whether he thought
        it just.
        """),
        ("THE QUEEN", "q", """
        A queen, late in life. She holds a
        linden wand in one hand, a capuchin
        monkey cradled in the other. Her expression
        is serious, but the wrinkling around her eyes
        suggests she was quick to laughter
        """),
        ("THE SEA", "s", """
        The sea, churning, undulating, tossed by storm.
        You can barely make out the shape of
        a small boat, dwarfed by the rolling waves.
        """)]

def make_painting(name, code, description):
    @Action("Examine {}".format(name), "e {}".format(code))
    def examine_painting(player, room):
        print("You examine {}".format(name))
        print(description)
        increment_stat(player, "erudition", 1)
        delete_action(examine_painting)

    return examine_painting

for p in PAINTINGS:
    register_action(space_hallway, make_painting(p[0], p[1], p[2]))

#====== STAGE 1: the galley

KITCHEN_ROBOT_HELPED=False
def show_galley(player):
    print("""
        You are in a small ship's galley, stocked
        with compact and ingenious cooking
        devices, their copper and wooden sides
        gleaming gently in the light.
        
        Judging by the dishes, someone has made ganache here in
        the not so recent past. """)
    if not KITCHEN_ROBOT_HELPED:
        print("""
        A small, round robot is attempting to
        reach a small cookie jar shaped like
        a teddy bear placed on the tallest shelf""")
    else:
        print("""
        A robot is softly playing a happy little tune
        while holding onto a teddy bear-shaped cookie jar""")

galley = Room("The Galley", "", 
        "the smell of cookies lingers",
        show_galley)

@Action("Talk to robot", "t")
def talk_to_kitchen_robot_before_helping(player, room):
    print("""
        The robot boops plaintively, reaching up as
        high as it can.

        "Can't... reach!!!" """)
    deregister_action(galley, talk_to_kitchen_robot_before_helping)
    register_action(galley, help_kitchen_robot)

@Action("Help robot get jar", "h")
def help_kitchen_robot(player, room):
    print("""
        You reach up and grab the jar and hand it to the
        robot. It boops with joy!

        "Thank you, kindly hunam!!! I owe you much gratitude!!!
        Please, feel free to help yourself to some of these
        cookies!"

        Turning to you, it opens the jar,
        revealing it to be filled with usb drives. """)
    deregister_action(galley, help_kitchen_robot)
    register_action(galley, take_cookie)
    register_action(galley, ask_kitchen_robot_for_vote)
    global KITCHEN_ROBOT_HELPED
    KITCHEN_ROBOT_HELPED=True


@Action("Ask kitchen robot for vote", "a")
def ask_kitchen_robot_for_vote(player, room):
    print("""
        You politely ask if the kitchen robot will
        vote for you for Cozy President this year.

        The robot beeps, "Of course!!! You are a real stand-up guy!" """)
    increment_stat(player, "votes", 1)
    deregister_action(galley, ask_kitchen_robot_for_vote)

@Action("Take cookie", "t c")
def take_cookie(player, room):
    print("""
        You take the usb stick. The woven cover around it
        feels comfortable under your fingers.  """)
    increment_stat(player, "has cookie", 1)

register_action(galley, talk_to_kitchen_robot_before_helping)

#====== STAGE 2: the poet


ENGINE_ROBOT_HELPED=False
def show_engine_room(player):
    if not ENGINE_ROBOT_HELPED:
        print("""
        A small square robot wearing an
        elaborate powdered wing is staring
        at a blank piece of paper with
        an unhappy expression""")
    else:
        print("""
        A small square robot wearing an
        elaborate powdered wing is happily
        scribbling away.
        
        You spy a snippet of a poem:
        
        "Shall I compare thee to a lisp program?" """)
engine_room = Room("Engine Room", """
        A stately engine-box hums contendedly,
        filling the room with a cozy warmth.""",
        "you hear a low hum...",
        show_engine_room)

@Action("Talk to robot", "t")
def talk_to_engine_room_robot_before_helping(player, room):
    erudition = get_stat(player, "erudition")
    if erudition < 3:
        print("""
        The robot look up briefly from its
        paper, before sniffing disdainfully.

        "I am a poet! I only speak with the most erudite boopers of culture!
        and you don't exactly look cultured to me..." """)
    elif erudition >= 4  and erudition < 5:
        print("""
        The robot look up briefly from its
        paper, before sniffing somewhat less disdainfully.

        "Somewhat better... But you still have something of an
        uncouth air about you!" """)
    else:
        print("""
        The robot look up briefly from its
        paper and then, seeing your air of obvious erudition
        and deep scholarship, sighs a sigh of profound relief.

        "Finally! Another artistic soul." """)
        deregister_action(engine_room, talk_to_engine_room_robot_before_helping)
        register_action(engine_room, ask_engine_room_robot_what_is_wrong)

@Action("Ask engine room robot what is wrong", "a")
def ask_engine_room_robot_what_is_wrong(player, room):
    print("""
        "It is a sad tale indeed... Such a sad circumstance,
        indeed, that is has stopped the very flow of sweet
        words from my quill." the robots sighs, looking at
        the blank piece of paper in its hands.

        "You see, kindly hunam... I... want a cookie..." the robot sniffs.
        "But... I do not have one..." """)
    deregister_action(engine_room, ask_engine_room_robot_what_is_wrong)
    register_action(engine_room, give_engine_room_robot_cookie)

@Action("Give engine room robot cookie", "c")
def give_engine_room_robot_cookie(player, room):
    if get_stat(player, "has cookie") < 1:
        print("""
        Alas, you cannot give the robot a cookie,
        for you do not have a cookie""")
    else:
        print("""
        You give the robot the usb stick.
        The robot's eyes light up, and it promptly
        plugs the cookie into its nose.

        "MMMMMMMMM!!!!" The robot does a little, joyful dance.

        "You've rekindled the poetic spirit inside me
        with that delightful cookie!! Please, have this star
        as a reward!"
        
        The robot reaches into its storage compartment
        and gives you a glass orb, suspended inside of which
        is a tiny, beautiful star, with planets orbiting around it.""")
        increment_stat(player, "has cookie", -1)
        increment_stat(player, "has star", 1)
        register_action(engine_room, ask_engine_room_robot_for_vote)
        deregister_action(engine_room, give_engine_room_robot_cookie)
    global ENGINE_ROBOT_HELPED
    ENGINE_ROBOT_HELPED=True

@Action("Ask engine room robot for vote", "a")
def ask_engine_room_robot_for_vote(player, room):
    print("""
        You politely ask if the engine room robot will
        vote for you for Cozy President this year.

        The robot beeps, "Of course!!! You have the soul of a poet!" """)
    increment_stat(player, "votes", 1)
    deregister_action(engine_room, ask_engine_room_robot_for_vote)

register_action(engine_room, talk_to_engine_room_robot_before_helping)

piano_room = Room("Piano Room", """
        A room paneled in honey-colored wood stretches in
        front of you. Off to one side, a grand piano
        gleams in the light. Soft cushions are
        strewn about, for comfortable lounging.""",
        "an echo of music drifts",
        noop)

TUNES=["boogie woogie", "sweet, soft chopin", "captivating Swedish polskas"]
@Action("Play piano", "p")
def play_piano(player, room):
    random.shuffle(TUNES)
    print("""
        You play some {}.""".format(TUNES[0]))
    increment_stat(player, "erudition", 1)

register_action(piano_room, play_piano)

# ===== PART THREE

STORAGE_ROOM_ROBOT_HELPED=False

def show_storage_room(player):
    if not STORAGE_ROOM_ROBOT_HELPED:
        print("""
        A small triangular robot is looking
        at the tree with concern, sighing dejectedly. """)
    else:
        print("""
        A small triangular robot is dancing
        around the tree, pointing at its
        beautiful star hat""")

@Action("Talk to robot", "t")
def talk_to_storage_room_robot_before_helping(player, room):
    print("""
        "I wish," you can hear the robot sighing, "there was... a star!!!" """)

storage_room = Room("Storage Room", """
        The biggest room in the ship stretches up
        in front of you. Although it is piled high with potatoes,
        books, musical instruments, clothes, and
        various wooden boxes and cabinets, the most
        notable feature currently is a huge, beautiful
        christmas tree, planted in an automatic-watering
        hydroponic unit, with grow-light christmas lights
        twinkling merrily in its branches.

        Countless ornaments are hanging from the tree-
        you spy a little wooden crocodile, a little penguin,
        and many blown-glass potatoes.""",
        "the smell of pine wafts",
        show_storage_room)

@Action("Ask storage room robot for vote", "a")
def ask_storage_room_robot_for_vote(player, room):
    print("""
        You politely ask if the storage room robot will
        vote for you for Cozy President this year.

        The robot beeps, "Of course!!! You are as shiney as a star!" """)
    increment_stat(player, "votes", 1)
    deregister_action(storage_room, ask_storage_room_robot_for_vote)

@Action("Help storage room robot", "h")
def help_storage_room_robot(player, room):
    if get_stat(player, "has star") < 1:
        print("""
        You aren't quite sure how to help the storage room robot...""")
    else:
        print("""
        You give the robot the star.
        The robot's eyes light up, and it promptly
        puts the star on its head.

        "THANK YOU, kindly hunam! With the beautiful hat
        on my head, the tree looks so beautiful!!!!" """)
        increment_stat(player, "has star", -1)
        global STORAGE_ROOM_ROBOT_HELPED
        STORAGE_ROOM_ROBOT_HELPED=True
        register_action(storage_room,   ask_storage_room_robot_for_vote)
        deregister_action(storage_room, help_storage_room_robot)
        deregister_action(storage_room, talk_to_storage_room_robot_before_helping)

register_action(storage_room, help_storage_room_robot)
register_action(storage_room, talk_to_storage_room_robot_before_helping)

# ===== FINAL STAGE
# ===== REWARD ROOMS

@Action("Under a big locked oak door, starlight winkles...", "helm")
def go_to_helm_before_president(player, room):
    if get_stat(player, "is president") < 1:
        print("""
        When you try to open the door, a cool robot
        wearing sunglasses jumps in your way.

        "I'm sorry, hunam!" the robot beeps, apologetically.
        "But only the president is allowed in there!" """)
    else:
        print("""
        Seeing your presidential aura, the robot salutes,
        opening the big oak door for you.

        "After you, Cozy President!""")
        deregister_action(space_hallway, go_to_helm_before_president)
        player.room = helm
        link_rooms(helm, space_hallway, "Through an open oak door", ("hallway", "helm"),
                   "The guard robot smartly salutes as you walk by...")

register_action(space_hallway, go_to_helm_before_president)

helm = Room("The Helm", """
        The room is dominated by a beautiful window,
        opening out onto the vastness of space.
        A shimmering, sparkling vastness of stars
        twinkles, more than the eye can see.

        A worn wood control console is arrayed in front
        of the window, and two big, comfy arm chairs are
        placed within arm's reach of the controls.

        Kai is settled in to one of the cozy armchairs,
        sipping on a hot chocolate and looking out at
        the vastness of space.""",
        "starlight twinkles",
        noop)

@Action("Talk to Kai", "t")
def talk_to_kai(player, room):
    print("""
        Kai takes a sip from the hot chocolate and looks up.
        
        "Isn't it pretty???" """)

register_action(helm, talk_to_kai)

computer_room = Room("Computer Room", """
        A little wooden desk cluttered with unicornettes
        supports a lovingly crafted wooden computer - an early
        model, with the monitor casing carved in
        the shape of a medieval house, complete
        with happy villagers peering out through
        the windows.
        """,
        "an electronic light glows",
        noop)

link_rooms(helm, computer_room, "Through a cool arch", ("computer room", "helm"),
           "You walk through the arch...")

# ===== LINK ROOMS
        
link_rooms(cozy_room, space_hallway, "Through a little round door", ("hallway", "room"),
           "You amble through the door...")

link_rooms(space_hallway, storage_room, "Through a steel archway", ("storage room", "hallway"),
           "You slip through the kitchen door...")
link_rooms(space_hallway, engine_room, "Through a steel archway", ("engine room", "hallway"),
           "You slip through the kitchen door...")
link_rooms(space_hallway, galley, "Through the kitchen door", ("kitchen", "hallway"),
           "You slip through the kitchen door...")
link_rooms(space_hallway, piano_room, "From a spiral staircase", ("music room", "hallway"),
           "You enter the staircase...")

link_rooms(computer_room, cozyworld.foyer, "A computer terminal happily blinks... Through a glowing screen",
           ("p", "p"),
           "The computer boops.")

# ===== WIN CONDITION

class OneTimeConditionalAction(object):
    def __init__(self, action, condition):
        self.action = action
        self.condition = condition
    @onetime 
    def register(self, obj):
        register_action(obj, self.action)
    def check(self, player):
        if self.condition(player):
            self.register(player)

@Action("Win Election", "ap")
def win_election_action(player, room):
    print("""
        You have finally achieved enough votes
        that you become THE COZY PRESIDENT

        A golden light wreathes you, and your vision blurs.
        You feel a tremendous energy coursing through you-
        the power of COZINESS!!!
        """)
    increment_stat(player, "coziness", 998832419875)
    increment_stat(player, "is president", 1)
    delete_action(win_election_action)
def win_election_check(player):
    return get_stat(player, "votes") >= 3
win_election = OneTimeConditionalAction(win_election_action, win_election_check)

#========== THE WORLD

def world():
    conditions = [win_election, cozyworld.apotheosis]
    def world_action(player):
        nonlocal conditions
        for condition in conditions:
            condition.check(player)

    return World(cozy_room, world_action)

def player():
    player = Player();
    set_stat(player, "coziness", 5)
    return player
