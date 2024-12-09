import os
import tkinter as tk
import dearpygui as dpg


def main(argv):
    #TODO: Parse through files 

    #TODO: Format ech file with pandas

    #TODO: start up gui 

    raise NotImplementedError
    

if __name__ == "__main__":
    try: 
        files = tk.filedialog.askopenfilenames(
            title="Select File(s)",
            initialdir="/",
            filetypes=(".txt", ".xlsx", ".xls", ".csv")
        )
    except ValueError as e: 
        raise ValueError("Not a valid file")
    
    main(files)