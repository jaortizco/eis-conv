from pathlib import Path
from typing import Protocol

import numpy as np
import numpy.typing as npt
import eisconv


class ImportStyle(Protocol):

    def load_data(
        self,
        myfile: Path,
    ) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64],
               npt.NDArray[np.float64]]:
        ...


class ExportStyle(Protocol):

    def export_data(
        self,
        myfile: Path,
        freq: npt.NDArray[np.float64],
        Z_re: npt.NDArray[np.float64],
        Z_im: npt.NDArray[np.float64],
        Z: npt.NDArray[np.float64],
        phase: npt.NDArray[np.float64],
        info: str,
    ) -> None:
        ...


class EisData:

    def __init__(self):
        self.info = (f"{eisconv.__name__} v{eisconv.__version__}\n" + "\n\n\n")

    def load_data(self, myfile: Path, style: ImportStyle) -> None:
        self.myfile = myfile
        self.freq, self.Z_re, self.Z_im = style.load_data(self.myfile)

        self.Z = np.sqrt(self.Z_re**2 + self.Z_im**2)
        self.phase = np.arctan(self.Z_im/self.Z_re)*180/np.pi

    def export_data(self, export_style: ExportStyle) -> None:

        export_style.export_data(
            self.myfile, self.freq, self.Z_re, self.Z_im, self.Z, self.phase,
            self.info
        )
