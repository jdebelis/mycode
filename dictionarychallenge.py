#!/usr/bin/env python3

def main():
    """characters"""

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

char_name = input("which character do you want to know about? (Starlord, Mystique, Hulk)")

char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")



print(f"{char_name}'s {char_stat} is: {marvelchars}")
