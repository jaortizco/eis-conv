from pathlib import Path

import numpy as np
import numpy.typing as npt


class NovaStyle:

    def __init__(self):
        self.delimiter = ";"
        self.skiprows = 1

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

        return data[:, 1], data[:, 2], -data[:, 3]
