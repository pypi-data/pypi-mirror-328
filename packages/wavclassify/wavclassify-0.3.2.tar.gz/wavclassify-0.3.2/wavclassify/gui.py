import FreeSimpleGUI as sg

from .browser_tools import BrowserState
from .click_sound import make_click_sound
from .lib import WavList


def create_window() -> sg.Window:
    btn_size = (10, 4)
    btn_size_small = (10, 2)

    btn_updown = [
        [sg.Button("up  (8)", size=btn_size)],
        [sg.Button("down (2)", size=btn_size)],
    ]

    btn_unclear = [
        [sg.Button("invalid (0)", size=btn_size)],
        [sg.Button("delete (DEL)", size=btn_size)],
    ]

    btn_nav = [
        [
            sg.Button("<<", size=btn_size_small),
            sg.Button("Replay\n (space)", size=(7, 2)),
            sg.Button(">>", size=btn_size_small),
        ],
        [
            sg.Push(),
            sg.Button("Next\nunclassified", key="next_unclass", size=btn_size_small),
        ],
    ]

    layout = [
        [sg.Multiline(size=(80, 10), key="txt_box", font=('Courier', 12, "bold"), disabled=True, autoscroll=True)],
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


def refresh(win:sg.Window, s:BrowserState):
    txt = s.formated_info_text()
    win['txt_box'].update(value=txt, append=False)

def browse_subject(
    group: str, wav_list: WavList, filter_str: str = "", info_dict: dict | None = None
):
    s = BrowserState(
        group=group, wav_list=wav_list, filter_str=filter_str, info_dict=info_dict
    )
    click_sound = make_click_sound()

    win = create_window()
    win.finalize()
    # Display and interact with the Window using an Event Loop
    while True:
        refresh(win, s)
        event, values = win.read()
        print(event)
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == "Quit":
            break

        # new_line = values["-INPUT-"]
        # if new_line:  # Ensure input is not empty
        #        window["-TEXTBOX-"].update(value=new_line + "\n", append=True)

    # Finish up by removing from the screen
    win.close()


if __name__ == "__main__":
    browse_subject()
