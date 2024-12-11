import itertools
from dataclasses import dataclass
import pandas as pd
import dearpygui as dpg

class DataWindow:
    
    def __init__(self):
        # parse through dataframe
        self.data: pd.DataFrame = None

    def create_data_window(self):
        with dpg.window(label="Data Window"):
            if self.data: 
                self.__create_data_table()
            else:
                dpg.add_text(default_value="No Data")

    def __create_data_table(self):
        num_rows = self.data.shape[0]
        num_cols = self.data.shape[1]

        with dpg.table(header_row=True, label="DataTable"):
            for i in range(num_cols):
                dpg.add_table_column()
            for row_col in itertools.product(range(num_rows), range(num_cols)):
                with dpg.table_row():
                    dpg.add_text(f"{row_col}")

        
    