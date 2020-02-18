#!/usr/bin/env python3

import os

current_dir = os.path.dirname(os.path.realpath(__file__))

for d in os.listdir(current_dir):
    if os.path.isdir(os.path.join(current_dir, d)):
        infopath = os.path.join(current_dir, d, "info.dat")
        if os.path.isfile(infopath):
            with open(infopath, "r") as f:
                line = f.readline()
                lines = []
                while line:
                    lines.append(line)
                    line = f.readline()
            
            if len(lines) == 1:
                lines = lines[0].split(",")
            songname, author, levelcreator = "","",""
            for line in lines:
                try:
                    content = line.split(":")[1].split("\"")[1].replace(" ","_").replace("/","")
                except:
                    continue
                if "_songName" in line:
                    songname = content
                if "_songAuthorName" in line:
                    author = content
                if "_levelAuthorName" in line:
                    levelcreator = content
               
            if author == "":
                newname = f"{levelcreator}-{songname}"
            else:
                newname = f"{author}-{songname}-({levelcreator})"
            if newname not in os.listdir(current_dir):
                print(f"renaming {d} to {newname}")
                old = os.path.join(current_dir, d)
                new = os.path.join(current_dir, newname)
                os.rename(old, new)
            else:
                if d != newname:
                    print(f"{newname} duplicate")
