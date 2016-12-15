#!/usr/bin/python

import sys
from providedcode.transitionparser import TransitionParser
from providedcode.dependencygraph import DependencyGraph

if __name__ == '__main__':
    # if you give  python parse.py english.model > englishfile.conll
    # the interpreter (python) is ignored, parse.py is [0] on the list returned by argv; english.model is [1]
    model = sys.argv[1]
    # .stdin is a bit like open(), but then without opening a file
    data = sys.stdin.readlines()
    for item in data:
        sentence = DependencyGraph.from_sentence(item)
        tp = TransitionParser.load(model)
        parsed = tp.parse([sentence])
        print parsed[0].to_conll(10).encode('utf-8')
        sys.stdout.flush()
