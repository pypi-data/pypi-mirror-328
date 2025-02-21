from pathlib import Path

import numpy as np
import soundfile


def make_click_sound():
    data, smpl_rate = soundfile.read(Path(Path(__file__).parent, "click.wav"))
    data = data.astype(np.float32)
    data *= 0.1  # loudness
    return  (data, smpl_rate)
