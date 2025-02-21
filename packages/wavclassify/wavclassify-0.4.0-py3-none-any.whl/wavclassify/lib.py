from operator import attrgetter
from pathlib import Path
from typing import Iterable, List, Optional, Tuple

import sounddevice
import soundfile


class WavFile(object):
    """Filename structure

    EXP - SUBJECT_ID - .. - BLOCK_LABEL - TRIAL

    """
    def __init__(self, path: str | Path, cat: int) -> None:
        self.cat = cat
        self.path = Path(path)
        self.name = self.path.stem
        self.data = None
        self.samplerate = None
        x = self.name.split("-")
        try:
            self.exp = x[0]
        except IndexError:
            self.exp = ""
        try:
            self.subject = int(x[1])
        except (ValueError, IndexError):
            self.subject = -99
        try:
            self.trial = int(x[-1])
        except (ValueError, IndexError):
            self.trial = -99
        try:
            self.level = x[-2]
        except IndexError:
            self.level = ""

    def exp_subject(self) -> str:
        return f"{self.exp}-{self.subject}"

    def load(self):
        self.data, self.samplerate = soundfile.read(self.path)

    def play(self, wait:bool=True):
        if self.data is None:
            self.load()
        sounddevice.play(self.data, self.samplerate)
        if wait:
            sounddevice.wait()

class WavList(object):
    A: int = 1
    B: int = 2
    INVALID: int = 0
    UNCAT: int = -1

    def __init__(self, wav_folder: str | Path, classify_file:str = "classification.csv",
                 recursive: bool = True, wav_file_extension: str = "wav") -> None:
        self.ext = wav_file_extension
        self.wav_fld = Path(wav_folder)
        self._classify_file = Path(classify_file)
        self.wavs: List[WavFile] = []
        self.changes = False

        if not self.wav_fld.is_dir():
            raise RuntimeError(f"{wav_folder} is not an existing folder")

        classify_list = {}
        if self._classify_file.is_file():
            # read dict
            with open(self._classify_file, "r", encoding="utf-8") as f:
                heading = True
                for ln in f.readlines():
                    if heading:
                        heading = False
                    else:
                        name, cat = ln.split(",")
                        classify_list[name] = int(cat)

        # existing wavs
        if recursive:
            all_wav_files = self.wav_fld.rglob(f"*.{self.ext}")
        else:
            all_wav_files = self.wav_fld.glob(f"*.{self.ext}")

        #build wav list
        file_list_changed = False
        for wav_file in all_wav_files:
            if wav_file.stem not in classify_list: # stem: name
                self.wavs.append(WavFile(wav_file, self.UNCAT))
                file_list_changed = True
            else:
                self.wavs.append(WavFile(wav_file, cat=classify_list[wav_file.stem]))

        if file_list_changed:
            self.save_classification(force_save=True)

        # wav dict organized by subjects
        self.wav_grouped = {}
        for x in self.wavs:
            es = x.exp_subject()
            if es in self.wav_grouped:
                self.wav_grouped[es].append(x)
            else:
                self.wav_grouped[es] = [x]

    def save_classification(self, force_save: bool = False):
        if force_save or self.changes:
            with open(self._classify_file, "w", encoding="utf-8") as f:
                f.write("file,category\n")
                arr = sorted(self.wavs, key=attrgetter("name"))
                for wfl in arr:
                    f.write(f"{wfl.name},{wfl.cat}\n")

    def get_unclassified(self, exp_subject: str) -> Iterable:
        return self.get_classify(exp_subject=exp_subject, cat=WavList.UNCAT)

    def get_classify(self, exp_subject: str, cat: int) -> Iterable:
        return filter(lambda x: x.cat == cat, self.wav_grouped[exp_subject])

    def all_stats(self) -> dict:
        es = []
        n = []
        n_un = []
        for k, lst in self.wav_grouped.items():
            es.append(k)
            s = stats(lst)
            n.append(s[0])
            n_un.append(s[1])
        return {"exp_subject": es, "n": n, "n_unclass": n_un}

    def overview(self, only_unclassified: bool = False) -> Tuple[str, List]:
        """returns info_txt, list of names"""
        s = self.all_stats()
        cnt = 1
        lst = []
        rtn = ""
        rtn += tab_str("id", "name", "wavs", "unclassified")
        rtn += tab_str("--", "----", "----", "------------")
        if not only_unclassified:
            for es, n, n_un in zip(s["exp_subject"], s["n"], s["n_unclass"]):
                if n_un == 0:
                    rtn += tab_str(str(cnt), es, str(n), "-")
                    cnt += 1
                    lst.append(es)

        for es, n, n_un in zip(s["exp_subject"], s["n"], s["n_unclass"]):
            if n_un > 0:
                rtn += tab_str(str(cnt), es, str(n), str(n_un))
                cnt += 1
                lst.append(es)
        return rtn, lst

    def filter(
        self,
        subject: Optional[int] = None,
        level: Optional[str] = None,
        trial: Optional[int] = None,
        cat: Optional[int] = None,
    ):
        if subject is None:
            rtn = self.wavs
        else:
            rtn = filter(lambda x: x.subject == subject, self.wavs)

        if level is not None:
            rtn = filter(lambda x: x.level == level, rtn)

        if trial is not None:
            rtn = filter(lambda x: x.trial == trial, rtn)

        if cat is not None:
            rtn = filter(lambda x: x.cat == cat, rtn)

        return rtn


def stats(wavs: List[WavFile]) -> tuple:
    uncat = 0
    for w in wavs:
        if w.cat == WavList.UNCAT:
            uncat += 1
    return (len(wavs), uncat)

def tab_str(a:str, b:str, c:str, d:str) -> str:
    x = " "
    na = 5 - len(a)
    nb = 25 - len(b)
    nc = 10 - len(c)
    return f"{a}{x*na}{b}{x*nb}{c}{x*nc}{d}\n"
