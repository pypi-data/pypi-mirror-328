from pathlib import Path
from time import sleep
from typing import Callable

import FreeSimpleGUI as sg
import sounddevice

from .browser_tools import BrowserState, no_info_dict
from .click_sound import make_click_sound
from .lib import WavList

SAVE_INTERVALL = 10

def _create_window() -> sg.Window:
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


def _refresh(win: sg.Window, s: BrowserState):
    s.automatic_next_unclass = win["auto_next"].get() # type: ignore
    s.playme = win["sound"].get() # type: ignore
    txt = s.formated_info_text()
    win["txt_box"].update(value=txt, append=False) # type: ignore


def browse_subject(
    wav_folder: Path | str,
    reference_utterances: str = "", info_dict_fnc:Callable | None = None
):
    save_cnt = 0
    wav_list = WavList(wav_folder)
    click_sound = make_click_sound()
    win = _create_window()
    win.finalize()

    subjects = wav_list.subject_code_list(with_unclassified_cnt=True)
    if info_dict_fnc is None:
        info_dict_fnc = no_info_dict

    if win["references"].get():
        filter_str = reference_utterances
    else:
        filter_str = ""

    first_subject = subjects[0].split(" ")[0] # remove potential counter
    s = BrowserState(
        subject_code=first_subject,
        wav_list=wav_list, filter_str=filter_str,
        info_dict=info_dict_fnc(first_subject))

    win["subjects"].update(values=subjects, value=subjects[0])

    # Display and interact with the Window using an Event Loop
    while True:

        _refresh(win, s)

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
            new_subject = new_subject.split(" ")[0] # remove counter
            if win["references"].get():
                filter_str = reference_utterances
            else:
                filter_str = ""
            s = BrowserState(
                subject_code=new_subject, wav_list=wav_list, filter_str=filter_str,
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
                save_cnt += 1
                sounddevice.play(click_sound[0], click_sound[1])

            _refresh(win, s)
            if s.automatic_next_unclass:
                sleep(0.25)
                s.next(omit_classified=True)
            else:
                s.inhibit_next_play = True

            if save_cnt > SAVE_INTERVALL:
                wav_list.save_classification()
                save_cnt = 0
                print("Save")

    # Finish up by removing from the screen
    wav_list.save_classification(force_save=True)
    win.close()

