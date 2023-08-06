# Anki-Wiki

A simple tool that allows you to have a vim-wiki, and a custom syntax to search for anki cards

## Usage

To create importable anki cards, just run: `python3 generate_ankis.py`. No dependencies required :)

Which will return something like:
```bash
~/wiki$ python3 generate_ankis.py 

                 _    _    _____                           _             
     /\         | |  (_)  / ____|                         | |            
    /  \   _ __ | | ___  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
   / /\ \ | '_ \| |/ / | | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
  / ____ \| | | |   <| | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 /_/    \_\_| |_|_|\_\_|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
          


 -- Generating Anki cards from markdown files... -- 


Generated 2 cards from ./index.md, stored in ./index.txt
Generated 1 cards from ./english/The Gangster We Are All Looking For.md, stored in ./english/The Gangster We Are All Looking For.txt


 -- Aggregating all Anki cards... -- 


Generated 0 cards from science, stored in science/all.txt
Generated 0 cards from french, stored in french/all.txt
Generated 0 cards from history, stored in history/all.txt
Generated 0 cards from math, stored in math/all.txt
Generated 1 cards from english, stored in english/all.txt
Generated 3 cards from ., stored in ./all.txt


 -- Done! 3 cards in total. -- 


~/wiki$ 
```
