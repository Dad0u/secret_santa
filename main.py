from random import choice
from collections import Counter

LIST_FILE = "list.txt"
COLOR = True


def read_entries(target: str):
    """Reads all the entries in a file, puts them in a list

    Checks unicity"""
    with open(target, 'r') as f:
        entries = f.readlines()

    entries = [name.strip() for name in entries]

    duplicates = [i for i, count in Counter(entries).items() if count > 1]
    if duplicates:
        raise RuntimeError(f"Duplicate entries: {duplicates}")
    return entries


def pick_names(name_list: list):
    """Picks a random name for every one, cannot be yourself"""
    while True:
        names = set(name_list)
        target = {}
        for name in name_list:
            pool = names - {name}
            if not pool:
                print("No luck, restarting...")
                continue
            # I know this is not efficient but who cares ?
            target[name] = choice(tuple(pool))
            names.remove(target[name])
        break
    return target


def green(message: str):
    if COLOR:
        return "\x1b[32m" + message + "\x1b[0m"
    return message


def red(message: str):
    if COLOR:
        return "\x1b[31m" + message + "\x1b[0m"
    return message


def secret_print(target: dict):
    """Will call each person individually and print them their pick"""
    for k, v in target.items():
        input(f"Please ask {green(k)} to come and press enter")
        print("You will have to find a gift for the following person:")
        print("IMPORTANT: Press enter again once you memorized the name !")
        print(red(v), end='', flush=True)
        input("")
        print("\x1b[2K\x1b[1A\x1b[2K")


if __name__ == '__main__':
    target = pick_names(read_entries(LIST_FILE))
    secret_print(target)

