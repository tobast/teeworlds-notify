#!/usr/bin/env python3

import sys
import re


def onLeave(line, match):
    return "TEEWORLDS — Départ de {} :(".format(match.group(2))


def onJoin(line, match):
    return "TEEWORLDS — Arrivée de {} \o/".format(match.group(3))

ACTIONS = [
    (re.compile("leave player='([0-9]+):([^']+)'"), onLeave),
    (re.compile("team_join (. )*player='([0-9]+):([^']+)'"), onJoin),
    ]

if __name__ == '__main__':
    for line in sys.stdin:
        for (regexp, action) in ACTIONS:
            match = regexp.search(line)
            if match:
                print(action(line, match))
                sys.stdout.flush()
                break
