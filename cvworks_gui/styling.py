"""All about the looks."""

import os
import platform
from version import VERSION

BASEDIR = os.path.dirname(__file__)

WORKS = {True: "WORKING", False: "OFF"}

WORKS_STYLESHEET = (
    "background-color: red; color: yellow; "
    "border: 2px solid yellow; border-radius: 6px; font-weight: bold;"
)
OFF_STYLESHEET = (
    "background-color: green; color: white; "
    "border: 2px solid white; border-radius: 6px; font-weight: bold;"
)
STYLESHEET = {True: WORKS_STYLESHEET, False: OFF_STYLESHEET}

# About Dialog
INFO_ICON = os.path.join(BASEDIR, "info.png")

INFO_DIALOG_HEADING_WEIGHT = 500
INFO_DIALOG_TEXT_SIZE = 10
INFO_DIALOG_TEXT_FONT_WEIGHT = 300

AUTHOR_HEADING = f"<p><span style='font-weight: {INFO_DIALOG_HEADING_WEIGHT};'>Written by:</span><br>"
AUTHOR_NAME = (
    f"<span style='font-weight: {INFO_DIALOG_TEXT_FONT_WEIGHT}; "
    f"font-size: {INFO_DIALOG_TEXT_SIZE}px;'>Charles Cognato</span><br>"
)
AUTHOR_EMAIL = (
    f"<span style='font-weight: {INFO_DIALOG_TEXT_FONT_WEIGHT}; "
    f"font-size: {INFO_DIALOG_TEXT_SIZE}px;'>charlescognato@gmail.com</span></p>"
)
VERSION_HEADING = (
    f"<p><span style='font-weight: {INFO_DIALOG_HEADING_WEIGHT};'>Version:</span><br>"
)
OPERATING_SYSTEM = (
    f"<span style='font-weight: {INFO_DIALOG_TEXT_FONT_WEIGHT}; "
    f"font-size: {INFO_DIALOG_TEXT_SIZE}px;'>{platform.platform().split('-', 1)[0]}</span><br>"
)
PROGRAM_VERSION = (
    f"<span style='font-weight: {INFO_DIALOG_TEXT_FONT_WEIGHT}; "
    f"font-size: {INFO_DIALOG_TEXT_SIZE}px;'>{VERSION}</span></p>"
)
