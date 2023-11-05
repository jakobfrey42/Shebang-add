#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import json

with open("config.json") as conFile:
    data = json.load(conFile)

Config = data[0]
Interpreters = data[1]
Languages = data[2]

outputLanguage = Config["defaultLanguage"]
sentences = Languages[outputLanguage]
print(sentences)

parser = ArgumentParser(description = sentences[0])
parser.add_argument("file", metavar=sentences[1], type=str, help=sentences[2])
parser.add_argument("interpreter", metavar="Interpreter", type=str, help=sentences[3])
parser.add_argument("-e", "--executable", default = Config["executable"], help=sentences[4])
parser.add_argument("-v", "--version", action="version", version="0.91", help=sentences[5])
args = parser.parse_args()
    
Ip = args.interpreter
if Ip in Interpreters:
    Shebang = Interpreters[Ip]
else:
    Shebang = ''.join(["#!", Ip])

try:
    with open(args.file, "r+") as script:
        content = script.readlines()
        script.seek(0,0)
        firstLineLst = list(content[0])
        if firstLineLst[0] == "#" and firstLineLst[1] == "!":
            del(content[0])
        script.write(Shebang+ "\n"+ "".join(content))
except FileNotFoundError:
    print(sentences[6])

if args.executable == "True":
    from os import system
    system("chmod +x "+ args.file)