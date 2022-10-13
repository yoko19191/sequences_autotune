# coding=utf-8
import json
import os, sys, time
import random
from pyautogui import press, typewrite, hotkey, confirm
import utilities


def main():
    #
    msg = confirm(text='Do you want start auto keyboard?', title="Confirm", buttons=['OK', 'Cancel'])
    print(msg)
    if msg == 'Cancel':
        sys.exit(0)

    time.sleep(5)

    #
    mapping = utilities.load_json('audio/mapping.json')

    #
    with open('FASTA/smallet_genome_goose_circovirus/Goose circovirus, complete genome.fasta', 'r') as seq_file:
        first_line, items = utilities.seq_split(seq_file)

    typewrite(first_line, interval=random.uniform(0.1, 1))

    for item in items:
        # print(item, mapping[item])
        interval = random.uniform(0.1, 0.5)
        press(mapping[item], interval=interval)

        # add chord
        press("space", interval=0.5)
        if interval > 0.2:
            press("enter")
        else:
            press("backspace")




if __name__ == "__main__":
    main()
