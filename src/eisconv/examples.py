from pathlib import Path

from eisconv.eis_data import EisData
from eisconv.export_styles.excel_style import ExcelStyle
from eisconv.export_styles.zview_style import ZviewStyle
from eisconv.import_styles.hp_style import HPStyle
from eisconv.import_styles.nova_style import NovaStyle


def example_1():
    myfile = "hp_example_data.txt"
    myfile = Path(Path(__file__).resolve().parents[2], "./test_data/" + myfile)

    import_style = HPStyle()
    export_style = ZviewStyle()

    data_manager = EisData()
    data_manager.load_data(myfile, import_style)
    data_manager.export_data(export_style)


def example_2():
    myfile = "autolab_example_data.txt"
    myfile = Path(Path(__file__).resolve().parents[2], "./test_data/" + myfile)

    import_style = NovaStyle()
    export_style = ExcelStyle()

    data_manager = EisData()
    data_manager.load_data(myfile, import_style)
    data_manager.export_data(export_style)


def main():
    example_1()
    example_2()


if __name__ == "__main__":
    main()
