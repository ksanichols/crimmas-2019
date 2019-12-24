import random
from game_engine import *

BOOKS = []

@Action("The Yellow Book of Riddles", "ybr")
def the_yellow_book_of_riddles(player, room):
    print("""

    THE YELLOW BOOK OF RIDDLES

    For earnest pleasure, and the strengthening of the mind, the author
    here collects all that he has learned of the art of riddling, by dint
    of diligent study, and through years of discourse with others of
    similar inclination.

    The posing and puzzling of riddles is a convention of polite
    aristocratic Western society. Nobles and social aspirants collect
    books of riddles and study them, hoping thereby to increase the
    chances of their appearing sly and witty in conversation.

    A metal neither black nor red As heavy as man's golden greed What you
    do to stay ahead With friend or arrow or steed 
    dael :rewsnA ehT

    A man says, "If you lie to me I will slay you with my sword. If you
    tell me the truth, I will slay you with a spell." What must you say to
    stay alive?  
    .drows a htiw em yals lliw uoY :rewsnA ehT

    A Bosmer, was slain. The Altmer claims the Dunmer is guilty. The
    Dunmer says the Khajiit did it. The Orc swears he didn't kill the
    Bosmer. The Khajiit says the Dunmer is lying. If only one of these
    speaks the truth, who killed the Bosmer?  
    crO ehT :rewsnA ehT

        """)
    increment_stat(player, "erudition", 5)
BOOKS.append(the_yellow_book_of_riddles)

@Action("Read six Wisemen came to Jhaampe-town", "swm")
def six_wisemen(player, room):
    print("""
        SIX WISEMEN CAME TO JHAAMPE-TOWN
        A traditional verse from the Kingdom of the Six Duchies

        Six Wisemen came to Jhaampe-town
        Climbed a hill, and never came down
        Found their flesh and lost their skins
        Flew away on stony wings.

        Five Wisemen came to Jhaampe-town
        Walked a road not up nor down
        Were torn to many and turned to one,
        In the end, left a task half-done

        Four Wisemen came to Jhaampe-town
        They spoke in words without a sound
        They begged their Queen to let them go
        And what became of them, no one can know.

        Three Wisemen came to Jhaampe-town
        They’d helped a king to keep his crown.
        But when they tried to climb the hill
        Down they came in a terrible spill.

        Two Wisemen came to Jhaampe-town
        Gentle women there they found.
        Forgot their quest and lived in love
        Perhaps were wiser than ones above.

        One Wiseman came to Jhaampe-town.
        He set aside both Queen and Crown
        Did his task and fell asleep
        Gave his bones to the stones to keep.

        No wise men go to Jhaampe-town,
        To climb the hill and never come down.
        ‘Tis wiser far and much more brave
        To stay at home and face the grave.

        """)
    increment_stat(player, "wistfulness", 1)
    increment_stat(player, "erudition", 1)
BOOKS.append(six_wisemen)

@Action("In the country of magic", "xx")
def in_the_country_of_magic(player, room):
    print(""" 
    IN THE COUNTRY OF MAGIC
    Henri Michaux

    For the construction of roads, they have a "paving paintbrush".  They
    also have a "paintbrush for building". For distant locations, they
    even have a building rifle. But you have to aim just right, yes, just
    right.  To say the reason is superfluous!  Who would like to get a
    roof to the head?

    ~ 

    Although they know perfectly well that the stars are more than just
    great lights in the sky, they cannot resist making illusory stars to
    please their kid, to please themselves- in part an exercise, in part
    magical spontaneity. I know a man who has but a small courtyard, but
    who created for it a roof of stars where the stars were as many as
    ants, the most beautiful thing I've ever seen. This impovershed
    courtyard, surrounded by walls exhausted to the point of seeming sad ,
    under this personal sky sparkling, nay, ~rumbling~ with stars...  what
    a sight!! I often have speculated, trying to calculate what the height
    of the stars is... But I have never succeeded, because, although some
    neighbors benefit, they are few in number, and the stars they do see
    are somewhat blurred. One thing I have noticed is that the stars never
    pass underneath a cloud... but, I have noticed that they takes great
    care to avoid the area nearest to the moon - out of fear, it seems
    certain, of having them pass in front of it in a moment of
    distraction...

    """)
    increment_stat(player, "erudition", 1)
BOOKS.append(in_the_country_of_magic)

@Action("A Word for Winter", "ww")
def a_word_for_winter(player, room):
    print("""
    A WORD FOR AUTUMN
    A. A. Milne

    Last night the waiter put the celery on with the cheese, and I knew
    that summer was indeed dead. Other signs of autumn there may be—the
    reddening leaf, the chill in the early-morning air, the misty
    evenings—but none of these comes home to me so truly. There may be
    cool mornings in July; in a year of drought the leaves may change
    before their time; it is only with the first celery that summer is
    over.

    I knew all along that it would not last. Even in April I was saying
    that winter would soon be here. Yet somehow it had begun to seem
    possible lately that a miracle might happen, that summer might drift
    on and on through the months—a final upheaval to crown a wonderful
    year. The celery settled that. Last night with the celery autumn came
    into its own.

    There is a crispness about celery that is of the essence of
    October. It is as fresh and clean as a rainy day after a spell of
    heat. It crackles pleasantly in the mouth. Moreover it is excellent, I
    am told, for the complexion. One is always hearing of things which are
    good for the complexion, but there is no doubt that celery stands high
    on the list. After the burns and freckles of summer one is in need of
    something. How good that celery should be there at one’s elbow.

    A week ago—(“A little more cheese, waiter”)—a week ago I grieved for
    the dying summer. I wondered how I could possibly bear the waiting—the
    eight long months till May. In vain to comfort myself with the thought
    that I could get through more work in the winter undistracted by
    thoughts of cricket grounds and country houses. In vain, equally, to
    tell myself that I could stay in bed later in the mornings. Even the
    thought of after-breakfast pipes in front of the fire left me
    cold. But now, suddenly, I am reconciled to autumn. I see quite
    clearly that all good things must come to an end. The summer has been
    splendid, but it has lasted long enough. This morning I welcomed the
    chill in the air; this morning I viewed the falling leaves with
    cheerfulness; and this morning I said to myself, “Why, of course, I’ll
    have celery for lunch.” (“More bread, waiter.”)

    “Season of mists and mellow fruitfulness,” said Keats, not actually
    picking out celery in so many words, but plainly including it in the
    general blessings of the autumn. Yet what an opportunity he missed by
    not concentrating on that precious root. Apples, grapes, nuts, and
    vegetable marrows he mentions specially—and how poor a selection! For
    apples and grapes are not typical of any month, so ubiquitous are
    they, vegetable marrows are vegetables pour rire and have no place in
    any serious consideration of the seasons, while as for nuts, have we
    not a national song which asserts distinctly, “Here we go gathering
    nuts in May”? Season of mists and mellow celery, then let it be. A pat
    of butter underneath the bough, a wedge of cheese, a loaf of bread
    and—Thou.

    How delicate are the tender shoots unfolded layer by layer. Of what a
    whiteness is the last baby one of all, of what a sweetness his
    flavor. It is well that this should be the last rite of the meal—finis
    coronat opus—so that we may go straight on to the business of the
    pipe. Celery demands a pipe rather than a cigar, and it can be eaten
    better in an inn or a London tavern than in the home. Yes, and it
    should be eaten alone, for it is the only food which one really wants
    to hear oneself eat. Besides, in company one may have to consider the
    wants of others. Celery is not a thing to share with any man. Alone in
    your country inn you may call for the celery; but if you are wise you
    will see that no other traveler wanders into the room, Take warning
    from one who has learnt a lesson. One day I lunched alone at an inn,
    finishing with cheese and celery. Another traveler came in and lunched
    too. We did not speak—I was busy with my celery. From the other end of
    the table he reached across for the cheese. That was all right! it was
    the public cheese. But he also reached across for the celery—my
    private celery for which I owed. Foolishly—you know how one does—had
    left the sweetest and crispest shoots till the last, tantalizing
    myself pleasantly with the thought of them. Horror! to see them
    snatched from me by a stranger. He realized later what he had done and
    apologized, but of what good is an apology in such circumstances? Yet
    at least the tragedy was not without its value. Now one remembers to
    lock the door.

    Yet, I can face the winter with calm. I suppose I had forgotten what
    it was really like. I had been thinking of the winter as a horrid wet,
    dreary time fit only for professional football. Now I can see other
    things—crisp and sparkling days, long pleasant evenings, cheery
    fires. Good work shall be done this winter. Life shall be lived
    well. The end of the summer is not the end of the world. Here’s to
    October—and, waiter, some more celery.

    """)
    increment_stat(player, "erudition", 1)
BOOKS.append(a_word_for_winter)
    

# From Jonathan Strange & Mr. Norrell
@Action("Carpets", "em")
def carpets(player, room):
    print("""

    You find a page torn from a book tucked between the shelves...

    MUSINGS

    "It is possible, of course,” he said, “to imprison someone within the
    pattern of a carpet for a thousand years or so. That is a particularly
    horrible fate which I always reserve for people who have offended me
    deeply – as have these magicians! The endless repetition of colour and
    pattern – not to mention the irritation of the dust and the
    humiliation of stains – never fails to render the prisoner completely
    mad! The prisoner always emerges from the carpet determined to wreak
    revenge upon all the world and then the magicians and heroes of that
    Age must join together to kill him or, more usually, imprison him a
    second time for yet more thousands of years in some even more ghastly
    prison. And so he goes on growing in madness and evil as the millennia
    pass. Yes, carpets! Perhaps …"
    
    """)
    increment_stat(player, "erudition", 1)
BOOKS.append(carpets)

@Action("Selections", "yk")
def selections(player, room):
    print("""
    SELECTIONS
    Yoshida Keno, “Selections.” 
    Quotidiana. Ed. Patrick Madden. 8 Feb 2007.

    Travel

    It wakes one up to go away from home for a time, no matter
    where. Exploring and rambling about the countryside you come upon a
    host of unusual sights in rustic spots and mountain hamlets. You get a
    messenger to take letters to the capital, and you write and say “Do
    not forget to send me so-and-so at the next opportunity.” All this is
    in its way amusing. Of course you have a thousand things to think of
    in such a place.

    Pleasant also to slip away and go into retreat in some mountain
    temple.

    Friendship

    It is a joyful thing indeed to hold intimate converse with a man after
    one’s own heart, chatting without reserve about things of interest or
    the fleeting topics of the world; but such, alas, are few and far
    between. Not that one desires a companion who will sit opposite and
    never utter a word in contradiction—one might as well be alone. Far
    better in hours of loneliness the company of one who, while he will
    listen with respect to your views, will disagree a little, and argue,
    saying “Yes, that is so, but…,” or “For this reason such and such is
    the case.” And yet, with those who are not of the same way of thinking
    or are contentious, a man can discuss only things of passing interest,
    for the truth is there must not be any wide gulf between bosom
    friends.

    Though the breeze blow not, the flower of the heart of man will change
    its hue. Now looking back on months and years of intimacy, to feel
    that your friend, while you still remember the moving words you
    exchanged, is yet growing distant and living in a world apart—all this
    is sadder far than partings brought by death.

    Although some will say, “After all this time, why stand on ceremony?”
    I myself feel that it is a sign of genuine and proper feeling when
    even the most inseparable friends treat one another, if the occasion
    demands, with due reserve and decorum. On the other hand, it is
    sometimes well for people who are not intimate to speak freely.

    Dwellings

    A house should be built with the summer in view. In winter one can
    live anywhere, but a poor dwelling in summer is unbearable. Deep water
    does not give a cool sensation. Far cooler is a shallow running
    stream. A room with sliding doors is lighter than one with doors on
    hinges. When the ceiling is high the room is cold in winter and
    difficult to light. As for construction, people agree in admiring a
    place with plenty of spare room, as being pleasing to the eye and at
    the same time useful for all sorts of purposes.

    There is a charm about a neat and proper dwelling house, although this
    world, it is true, is but a temporary abode. Even the moonshine, when
    it strikes into the house where a good man lives in peaceful ease,
    seems to gain in friendly brilliancy.

    The man is to be envied who lives in a house, not of the modern,
    garish kind, but set among venerable trees, with a garden where plants
    grow wild and yet seem to have been disposed with care, verandas and
    fences tastefully arranged, and all its furnishings simple but
    antique.

    A house which multitudes of workmen have devoted all their ingenuity
    to decorate, where rare and strange things from home and abroad are
    set out in array, and where even the trees and shrubs are trained
    unnaturally—such is an unpleasant sight, depressing to look at, to say
    nothing of spending one’s days in there. Nor, gazing on it, can one
    but reflect how easily it might vanish in a moment of time.

    The appearance of a house is in some sort an index to the character of
    its occupant.

    Once in the month of September I passed over the plain of Kurusu and
    sought out a certain village among the hills beyond, when, threading
    my way far down a narrow moss-grown path, I came upon a lonely
    hut. There was never a sound to greet me, save the dripping of water
    from a pipe buried in fallen leaves, but I knew that someone lived
    there, for sprays of chrysanthemum and maple leaves bestrewed the
    shelf before the shrine, and “Ah!” thought I, “In such a place a man
    can spend his days.” But as I stood and gazed in wonder, I perceived
    in the garden beyond a great orange tree, its branches weighted down
    with fruit. It was strongly closed in on all sides by a fence. This
    broke the spell, and I thought to myself, “If only that tree had not
    been there!”

    """)
    increment_stat(player, "erudition", 1)
    increment_stat(player, "coziness", 1)
BOOKS.append(selections)

@Action("No books left...", ":(")
def no_books(player, room):
    print("""
        You have sadly read all the books...""")

def get_random():
    if len(BOOKS) == 0:
        return no_books
    else:
        random.shuffle(BOOKS)
        return BOOKS.pop()
