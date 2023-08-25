from pathlib import Path

import numpy as np
import numpy.typing as npt


class ZviewStyle:

    def __init__(self):
        pass

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
        """
        Export impedance data for use with Zview software.

        """
        data = np.column_stack((freq, Z_re, Z_im, Z, phase))

        labels = [
            "freq (Hz)", "Z' (Ohm)", "Z'' (Ohm)", "Z (ohm)", "Phase (degree)"
        ]

        header = (
            "Data formatted for importing into Zview software\n" + info
            + ",".join(labels)
        )

        newfile = Path(myfile.parent, myfile.stem + "_zview.csv")
        np.savetxt(newfile, data, fmt="%.5g", delimiter=",", header=header)
