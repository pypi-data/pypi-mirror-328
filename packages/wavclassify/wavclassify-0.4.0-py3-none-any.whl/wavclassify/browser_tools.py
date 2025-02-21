
from .lib import WavFile, WavList, stats

POSSIBLE_CLASSIFICATIONS = ("8", "2")

class BrowserState(object):
    _i = -1
    playme = True
    automatic_next_unclass = False
    inhibit_next_play = False
    info = ""
    cat: int | None = None

    def __init__(
        self,
        group: str,
        wav_list: WavList,
        filter_str: str = "",
        info_dict: dict | None = None,
    ) -> None:
        self.group = group
        self.filter_str = filter_str
        self.info_dict = info_dict

        dat = wav_list.wav_grouped[group]
        if len(filter_str):
            dat = list(filter(lambda x: x.name.find(filter_str) >= 0, dat))
        self.dat = dat

    @property
    def curr_wav(self) -> WavFile:
        return self.dat[self._i]

    def is_list_begin(self):
        return self._i < 0

    def next(self, omit_classified: bool):
        self._i += 1

        if self._i >= self.n_wavs:
            self._i = self.n_wavs - 1
            self.info = "LIST END --- LIST END --- LIST END"

        elif omit_classified and self.dat[self._i].cat != WavList.UNCAT:
            self.next(omit_classified=True)

    def previous(self):
        self._i -= 1
        if self._i < -1:
            self._i = -1  # before list

    @property
    def n_wavs(self):
        return len(self.dat)

    def formated_info_text(self) -> str:
        line = "-" * 70 + "\n"

        if self.playme:
            rtn = "Mode: PLAY"
            if self.automatic_next_unclass:
                rtn += " -- quick classifications\n"
        else:
            rtn = "Mode: BROWSE\n"

        n, n_un = stats(self.dat)
        rtn += f"\n{line}Group: {self.group}          n={n}, unclssified={n_un}\n"

        if not self.is_list_begin():
            if self.curr_wav.cat == WavList.UNCAT:
                cat_str = " "
            else:
                cat_str = str(self.curr_wav.cat)

            name = self.curr_wav.name
            rtn += f"\n{name}:            ** {cat_str} **\n"

            if isinstance(self.info_dict, dict) and name in self.info_dict:
                rtn += f"\nINFO: {self.info_dict[name]}\n"

        else:
            rtn += "\n"

        rtn += line
        rtn += f"{self.info}\n"

        return rtn
