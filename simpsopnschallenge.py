#!/usr/bin/env python3

def main():

    #challenge 1: Pull out eyes, goggles, nothing
    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

    a = challenge[2][1]
    b = challenge[2][0]
    c = challenge[3]

    print(f"My {a}! The {b} do {c}!")
