#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

parser = ArgumentParser(description = "Ein Programm um schnell und einafch Shebangs in Skripten zu ergaenzen")
parser.add_argument("file", metavar="Datei", type=str, help="Dateiname des Skripts")
parser.add_argument("interpreter", metavar="Interpreter", type=str, help="Name des Interpreters")
parser.add_argument("-e", "--executable", default = False, help="Option zum direkten Markieren als ausfuehrbare Datei Default: False")
args = parser.parse_args()

Interpreters = {
    "Python": "#!/usr/bin/env python3",
    "Bash": "#!/usr/bin/bash",
    "Zsh": "#!/usr/bin/zsh",
    "Shell": "#!/usr/bin/sh"
    }
    
Ip = args.interpreter
if Ip in Interpreters:
    try:
        with open(args.file, "r+") as script:
            content = script.read()
            script.seek(0,0)
            script.write(Interpreters[Ip]+ "\n"+ content)
    except FileNotFoundError:
        print("Die angegebene Datei existiert nicht.")