import os
import sys
from argparse import ArgumentParser
from pathlib import Path
from time import sleep
from typing import Callable

import readkeys
import sounddevice

from . import __version__
from .browser_tools import BrowserState, no_info_dict
from .click_sound import make_click_sound
from .lib import WavList

POSSIBLE_CLASSIFICATIONS = ("8", "2")

def clear_console():
    # for windows
    if os.name == "nt":
        os.system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        os.system("clear")


LEFT_ARROW = "\x1b[D"
RIGHT_ARROW = "\x1b[C"
UP_ARROW = "\x1b[A"
DOWN_ARROW = "\x1b[B"
DEL = "\x1b[3~"

NAV_BAR = f"""
(arrow keys) to navigate, (ENTER) next unclassified, (x or r) exit
(SPACE) replay, (p) toggle mode, (n) automatic next unclassified,

classification: {POSSIBLE_CLASSIFICATIONS}, ('0') invalid, (DEL) delete
"""


def _refresh_screen(s: BrowserState):
    clear_console()
    print(NAV_BAR + "\n")
    print(s.formated_info_text())


def browse_subject(
    subject_code: str, wav_folder: Path | str,
    filter_str:  str = "",
    info_dict_fnc: Callable | None = None
):
    wav_list = WavList(wav_folder)
    if info_dict_fnc is None:
        info_dict_fnc = no_info_dict
    s = BrowserState(
        subject_code=subject_code, wav_list=wav_list,
        filter_str=filter_str,
        info_dict=info_dict_fnc(subject_code)
    )
    click_sound = make_click_sound()

    while True:
        _refresh_screen(s)
        if not s.is_list_begin() and s.playme and not s.inhibit_next_play:
            s.curr_wav.play(wait=False)

        s.info = ""
        s.inhibit_next_play = False

        ### INPUT
        sys.stdout.write(">>> ")
        sys.stdout.flush()
        k = readkeys.getkey()
        s.cat = None
        if k in ("x", "q"):
            break
        elif k == LEFT_ARROW:
            s.previous()
        elif k == RIGHT_ARROW:
            s.next(omit_classified=False)
        elif k == "\r":
            s.next(omit_classified=True)
        elif k == "n":
            s.automatic_next_unclass = not s.automatic_next_unclass
            s.inhibit_next_play = True
        elif k == "p":
            s.playme = not s.playme
            s.inhibit_next_play = True
        elif k == " ":
            s.info = "replay"
        elif k in POSSIBLE_CLASSIFICATIONS:
            s.cat = int(k)
        elif k in DEL:
            s.cat = WavList.UNCAT
        elif k == "0":
            s.cat = WavList.INVALID
        else:
            s.info = f"{k}: unknown key"
            s.inhibit_next_play = True

        if s.cat is not None:  # item has been categorized
            if not s.playme:
                s.info = "ERROR: Classifications only possible in PLAY mode."
            elif s.is_list_begin():
                s.info = "ERROR: No file selected"
            else:
                s.curr_wav.cat = s.cat
                wav_list.changes = True
                sounddevice.play(click_sound[0], click_sound[1])

            _refresh_screen(s)
            if s.automatic_next_unclass:
                sleep(0.5)
                s.next(omit_classified=True)
            else:
                s.inhibit_next_play = True

    wav_list.save_classification(force_save=True)


def run_cli():
    parser = ArgumentParser(
        description="Classifying WAV files ",
        epilog="Version {0}, (c) O. Lindemann".format(__version__),
    )
    parser.add_argument("WAV_FOLDER", help="folder with wav files")
    parser.add_argument(
        "--id", nargs="?", type=int, default=0, help="process subject with the id"
    )
    args = vars(parser.parse_args())

    wav_lst = WavList(wav_folder=args["WAV_FOLDER"])
    feedback, lst = wav_lst.overview()
    if args["id"] > 0:
        browse_subject(lst[args["id"] - 1],
                       wav_folder=args["WAV_FOLDER"])
    else:
        print(feedback)
