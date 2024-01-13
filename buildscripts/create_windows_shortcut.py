"""Creates a desktop shortcut to cvworks.exe on Windows."""

import os
import winshell

target = os.path.join(winshell.desktop(), "cvworks - Shortcut.lnk")
user_profile = winshell.folder("profile")
path = os.path.join(user_profile, r"cvworks\cvworks.exe")
working_directory = os.path.join(user_profile, "cvworks")

with winshell.shortcut(target) as shortcut:
    shortcut.path = path
    shortcut.description = "Christina's Work Schedule"
    shortcut.working_directory = working_directory
