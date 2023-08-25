from pathlib import Path

import numpy as np
import numpy.typing as npt
import xlwings as xw
from xlwings.constants import HAlign, VAlign


class ExcelStyle:
    HLEFT = HAlign.xlHAlignLeft
    HCENTER = HAlign.xlHAlignCenter
    HRIGHT = HAlign.xlHAlignRight
    VTOP = VAlign.xlVAlignTop
    VCENTER = VAlign.xlVAlignCenter
    VBOTTOM = VAlign.xlVAlignBottom

    def __init__(self):
        self.load_settings = {
            "delimiter": "\t",
            "skiprows": 22,
            "usecols": (1, 3, 5)
        }

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
        info = "Data formatted for Excel\n" + info
        header = [
            "Frequency (Hz)", "Z' (ohm)", "-Z'' (ohm)", "Z (ohm)",
            "-Phase (degree)"
        ]

        excel_data = self._create_formatted_data(
            header, freq, Z_re, Z_im, Z, phase
        )

        newfile = Path(myfile.parent, myfile.stem + ".xlsx")
        self._export_to_excel(newfile, excel_data, info)

    def _create_formatted_data(
        self,
        header: list[str],
        freq: npt.NDArray[np.float64],
        Z_re: npt.NDArray[np.float64],
        Z_im: npt.NDArray[np.float64],
        Z: npt.NDArray[np.float64],
        phase: npt.NDArray[np.float64],
    ) -> list[list[str]]:
        data = [header]

        for row in np.column_stack((freq, Z_re, -Z_im, Z, -phase)).tolist():
            data.append(row)

        return data

    def _export_to_excel(
        self,
        myfile,
        data: list[list[str]],
        info: str,
    ) -> None:
        with xw.App(visible=False) as app:
            wb = xw.Book()

            wb.sheets[0].name = "Data"
            xl_range = wb.sheets["Data"][(0, 0)]
            xl_range.value = data
            xl_range.expand().number_format = "0.000"
            xl_range.expand().api.HorizontalAlignment = self.HCENTER
            xl_range.expand().api.VerticalAlignment = self.VCENTER
            wb.sheets[0].autofit(axis="columns")

            wb.sheets.add("Info", after="Data")
            # Information should be split across different rows in Excel
            info_list = info.splitlines()
            wb.sheets["Info"][(0, 0)].value = [[line] for line in info_list]

            wb.sheets["Data"].select()
            wb.save(myfile)
            wb.close()

            app.quit()
