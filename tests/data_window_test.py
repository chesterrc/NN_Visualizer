import pandas as pd
from src.gui.windows.data_window import DataWindow


def main():
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)

    dw = DataWindow()

if __name__ == "__main__":
    main()