import os
import socket
import asyncio
import dearpygui as dpg


def main():
    # Start dearpygui render loop
    dpg.create_context()
    dpg.create_viewport(title="Testing Suite", width=500, height=300)


    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()