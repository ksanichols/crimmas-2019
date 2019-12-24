from get_holiday_color import *
from twiddle import twiddle
import random
import sys
import time

verbs = ["Importing", "Calibrating", "Compiling", "Parsing", "Starting"]

nouns = ["mistletoed", "figgypuddingd", "stocking manager",
         "christmas tree", "milk and cookies",
         "fireplace", "powder snow", "yule log",
         "snowman", "treats and snoozin", "wrapping paper",
         "tinsel", "ribbons and bows", "3 wise men",
         "reindeer", "christmas specials", "ho ho ho"]

adjectives = [" OK "]

if __name__ == "__main__":
    for noun in nouns:
        verb = random.choice(verbs)
        sys.stdout.write("{:40}".format(verb + " " + noun))
        sys.stdout.flush()
        twiddle(random.choice([0, 0.1, 0.4]))
        result = random.choice(adjectives)
        color = GREEN
        sys.stdout.write("[{}{}{}]\n".format(color, result, DEFAULT_COLOR))
        sys.stdout.flush()
    print("I AM READY")
    print("""
      *                                                            
     /.\                                                           
    /  &\    Welcome to {}C{}r{}i{}m{}m{}i{}s{} OS v2.0.1 (GENERIC)
   % o   \                                                         
  ._#_ _%_.                                                        
  E m' ' [+]                                                       
   [+] [] """.format(RED, GREEN, RED, GREEN, RED, GREEN, RED, DEFAULT_COLOR))


