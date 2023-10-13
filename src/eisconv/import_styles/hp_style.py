from pathlib import Path

import numpy as np
import numpy.typing as npt


class HPStyle:

    def __init__(self):
        self.delimiter = "\t"
        self.skiprows = 22

    def load_data(
        self,
        myfile: Path,
    ) -> tuple[
        npt.NDArray[np.float64],
        npt.NDArray[np.float64],
        npt.NDArray[np.float64],
    ]:
        """
        Load impedance data.

        """
        with open(myfile) as file:
            data = np.loadtxt(
                file,
                delimiter=self.delimiter,
                skiprows=self.skiprows,
            )

        if data[0, 1] < 1:
            magnitude_squared = data[:, 1]**2 + data[:, 3]**2
            data[:, 1] = data[:, 1]/magnitude_squared
            data[:, 3] = data[:, 3]/magnitude_squared

        return data[:, 5]*1e3, data[:, 1], -data[:, 3]

    def convert_to_ohm(
        self,
        Z_re: npt.NDArray[np.float64],
        Z_im: npt.NDArray[np.float64],
    ) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]:
        return Z_re, Z_im
