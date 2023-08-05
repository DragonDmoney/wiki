import os

def generate_cards(path):
    with open(path, "r") as f:
        lines = f.readlines()
        cards = []
        for i, line in enumerate(lines):
            if line.startswith("***$"):
                tag = os.path.basename(path).split(".")[0]
                front = line[4:-4].strip()
                back = ""
                j = i + 1
                while j < len(lines) and lines[j].startswith(">"):
                    back += lines[j][1:].strip() + " "
                    j += 1

                tag = tag.replace(" ", "_")

                cards.append(f"{front};{back};{tag}")

    if len(cards) == 0:
        return

    txt_path = path[:-2] + "txt"

    with open(txt_path, "w") as f:
        f.write("\n".join(cards))
        print(
            "Generated {} cards from {}, stored in {}".format(
                len(cards), path, txt_path
            )
        )

    with open(path, "r+") as f:
        content = f.read()
        f.seek(0, 0)

        if content.startswith("cards are"):
            return

        f.write("cards are [here]({})\n".format(txt_path[1:]) + content)


def sum_ankis(path) -> int:
    all_cards = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt") and file != "all.txt":
                with open(os.path.join(root, file), "r") as f:
                    all_cards += f.readlines()

    with open(os.path.join(path, "all.txt"), "w") as f:
        f.write("\n".join(all_cards))
        print(
            "Generated {} cards from {}, stored in {}".format(
                len(all_cards), path, os.path.join(path, "all.txt")
            )
        )

    return len(all_cards)


def generate_ankis(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".md"):
                generate_cards(os.path.join(root, file))

if __name__ == "__main__":
    print("""
                 _    _    _____                           _             
     /\         | |  (_)  / ____|                         | |            
    /  \   _ __ | | ___  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
   / /\ \ | '_ \| |/ / | | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
  / ____ \| | | |   <| | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 /_/    \_\_| |_|_|\_\_|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
          """)

    print("\n\n -- Generating Anki cards from markdown files... -- \n\n")

    generate_ankis(".")

    print("\n\n -- Aggregating all Anki cards... -- \n\n")

    dirs = [d for d in os.listdir(".") if os.path.isdir(d)]
    for d in dirs:
        if d[0] != ".":
            sum_ankis(d)

    t = sum_ankis(".")
    print("\n\n -- Done! {} cards in total. -- \n\n".format(t))

