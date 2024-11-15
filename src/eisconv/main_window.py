from pathlib import Path

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFileDialog, QMainWindow, QMessageBox

from eisconv.eis_data import EisData
from eisconv.export_styles.enums import ExportStyles, ImportStyles
from eisconv.export_styles.excel_style import ExcelStyle
from eisconv.export_styles.zview_style import ZviewStyle
from eisconv.import_styles.hp_style import HPStyle
from eisconv.import_styles.nova_style import NovaStyle
from eisconv.ui.main_window_ui import Ui_MainWindow

STYLES = {
    "Nova": NovaStyle(),
    "HP": HPStyle(),
    "Zview": ZviewStyle(),
    "Excel": ExcelStyle()
}


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        # Set window
        self.set_icons()

        self.comboBoxImport.addItems(
            [ImportStyles.HP.value, ImportStyles.NOVA.value]
        )
        self.comboBoxImport.setCurrentIndex(0)

        self.comboBoxExport.addItems(
            [ExportStyles.EXCEL.value, ExportStyles.ZVIEW.value]
        )
        self.comboBoxExport.setCurrentIndex(0)

        # Set signals
        self.pushButtonImport.clicked.connect(self.import_data)
        self.pushButtonExport.clicked.connect(self.export_data)

    def set_icons(self):
        dir_icon = Path(Path(__file__).resolve().parents[1], "icons")
        self.setWindowIcon(QIcon(str(Path(dir_icon, "icon.svg"))))

    def import_data(self):
        self.import_style = STYLES[self.comboBoxImport.currentText()]

        self.myfiles = [
            Path(file) for file in QFileDialog.getOpenFileNames(
                parent=self,
                caption="Select a file",
                dir=str(Path.cwd()),
                filter="Text File (*.txt)",
            )[0]
        ]

        self.impedance_data = [EisData() for _ in range(len(self.myfiles))]
        for impedance, myfile in zip(self.impedance_data, self.myfiles):
            try:
                impedance.load_data(myfile, self.import_style)
                self.add_files_to_list_widget()
                self.data_imported = True
            except (ValueError, IndexError):
                msg = (
                    f'"{myfile.name}"\n'
                    + "Something went wrong when loading data.\n"
                    + "You may want to double check your file."
                )
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Warning!")
                dlg.setText(msg)
                dlg.setIcon(QMessageBox.Warning)
                dlg.exec()

    def export_data(self):
        self.export_style = STYLES[self.comboBoxExport.currentText()]
        for impedance in self.impedance_data:
            impedance.export_data(self.export_style)

    def add_files_to_list_widget(self):
        self.listWidget.addItems([str(item.name) for item in self.myfiles])
