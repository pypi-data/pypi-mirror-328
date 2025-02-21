from pathlib import Path
from time import sleep
from typing import Any, Callable

import FreeSimpleGUI as sg
import sounddevice

from .browser_tools import BrowserState
from .click_sound import make_click_sound
from .lib import WavList


def create_window() -> sg.Window:
    btn_size = (10, 4)
    btn_size_small = (10, 2)

    btn_updown = [
        [sg.Button("up  (8)", key="up", size=btn_size)],
        [sg.Button("down (2)", key="down", size=btn_size)],
    ]

    btn_unclear = [
        [sg.Button("invalid (0)", key="invalid", size=btn_size)],
        [sg.Button("delete (DEL)", key="delete", size=btn_size)],
    ]

    btn_nav = [
        [
            sg.Button("<<", size=btn_size_small),
            sg.Button("Replay\n (space)", key="replay", size=(7, 2)),
            sg.Button(">>", size=btn_size_small),
        ],
        [
            sg.Push(),
            sg.Button("Next\nunclassified", key="next_unclass", size=btn_size_small),
        ],
    ]

    layout = [
        [
            sg.Text("Choose subject:"),
            sg.Combo(
                ["Option 1", "Option 2", "Option 3"],
                enable_events=True,
                key="subjects",
                readonly=True,
            ),
            sg.Checkbox("Reference utterances only", True,
                        enable_events=True, key="references"),

        ],
        [],
        [
            sg.Multiline(
                size=(80, 10),
                key="txt_box",
                font=("Courier", 12, "bold"),
                disabled=True,
                autoscroll=True,
            )
        ],
        [
            sg.Checkbox("Play sounds", True, enable_events=False, key="sound"),
            sg.Checkbox(
                "Automatic next unclassified", enable_events=False, key="auto_next"
            ),
        ],
        [
            sg.Column(btn_updown, background_color="yellow"),
            sg.Column(btn_unclear, background_color=""),
            sg.Column(btn_nav, background_color=""),
        ],
        [
            sg.Push(),
            sg.Button("Quit", size=(10, 2)),
        ],
    ]

    # Create the window
    return sg.Window("Window Title", layout, return_keyboard_events=True)


def refresh(win: sg.Window, s: BrowserState):
    s.automatic_next_unclass = win["auto_next"].get()
    s.playme = win["sound"].get()
    txt = s.formated_info_text()
    win["txt_box"].update(value=txt, append=False)

def _no_info_dict(sid) -> None:
    # helper func returns None
    return None

def browse_subject(
    wav_folder: Path | str, filter_str: str = "", info_dict_fnc:Callable | None = None
):

    wav_list = WavList(wav_folder)
    click_sound = make_click_sound()
    win = create_window()
    win.finalize()

    _, subjects = wav_list.overview()
    if info_dict_fnc is None:
        info_dict_fnc = _no_info_dict

    if win["references"].get():
        filter_str = "Block"
    else:
        filter_str = ""
    s = BrowserState(
        group=subjects[0], wav_list=wav_list, filter_str=filter_str,
        info_dict=info_dict_fnc(subjects[0]))

    win["subjects"].update(values=subjects, value=subjects[0])
    # Display and interact with the Window using an Event Loop
    while True:
        refresh(win, s)
        if not s.is_list_begin() and s.playme and not s.inhibit_next_play:
            s.curr_wav.play(wait=False)
        s.info = ""
        s.inhibit_next_play = False

        event, _ = win.read()
        s.cat = None

        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == "Quit":
            break
        elif event == "subjects" or event == "references":
            new_subject = win["subjects"].get()
            if win["references"].get():
                filter_str = "BLOCK"
            else:
                filter_str = ""
            s = BrowserState(
                group=new_subject, wav_list=wav_list, filter_str=filter_str,
                info_dict=info_dict_fnc(new_subject))

        elif event == "<<":
            s.previous()
        elif event == ">>":
            s.next(omit_classified=False)
        elif event == "next_unclass":
            s.next(omit_classified=True)
        elif event == "replay":
            s.info = "replay"
        elif event == "up":
            s.cat = 8
        elif event == "down":
            s.cat = 2
        elif event in "delete":
            s.cat = WavList.UNCAT
        elif event == "invalid":
            s.cat = WavList.INVALID
        else:
            s.info = f"{event}: unknown key"
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

            refresh(win, s)
            if s.automatic_next_unclass:
                sleep(0.25)
                s.next(omit_classified=True)
            else:
                s.inhibit_next_play = True

    # Finish up by removing from the screen
    wav_list.save_classification(force_save=True)
    win.close()


if __name__ == "__main__":
    browse_subject()
