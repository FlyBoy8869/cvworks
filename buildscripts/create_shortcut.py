import os
import winshell

target = os.path.join(winshell.desktop(), "cvworks - Shortcut.lnk")

with winshell.shortcut(target) as shortcut:
    shortcut.path = r"C:\Users\charles\cvworks\cvworks.exe"
    shortcut.description = "Christina's Work Schedule"
    shortcut.working_directory = r"C:\Users\charles\cvworks"