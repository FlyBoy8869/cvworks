"""All about the looks."""

import os
import platform
from _version import version

from cvworks_gui import IMAGES_BASE_FOLDER

# About Dialog Styling
ABOUT_INFO_ICON = os.path.join(IMAGES_BASE_FOLDER, "info.png")

ABOUT_INFO_DIALOG_HEADING_WEIGHT = 500
ABOUT_INFO_DIALOG_TEXT_SIZE = 10
ABOUT_INFO_DIALOG_TEXT_FONT_WEIGHT = 300

ABOUT_AUTHOR_HEADING = f"<p><span style='font-weight: {ABOUT_INFO_DIALOG_HEADING_WEIGHT};'>Written by:</span><br>"
ABOUT_AUTHOR_NAME = (
    f"<span style='font-weight: {ABOUT_INFO_DIALOG_TEXT_FONT_WEIGHT}; "
    f"font-size: {ABOUT_INFO_DIALOG_TEXT_SIZE}px;'>Charles Cognato</span><br>"
)
ABOUT_AUTHOR_EMAIL = (
    f"<span style='font-weight: {ABOUT_INFO_DIALOG_TEXT_FONT_WEIGHT}; "
    f"font-size: {ABOUT_INFO_DIALOG_TEXT_SIZE}px;'>charlescognato@gmail.com</span></p>"
)
ABOUT_VERSION_HEADING = f"<p><span style='font-weight: {ABOUT_INFO_DIALOG_HEADING_WEIGHT};'>Version:</span><br>"
ABOUT_OPERATING_SYSTEM = (
    f"<span style='font-weight: {ABOUT_INFO_DIALOG_TEXT_FONT_WEIGHT}; "
    f"font-size: {ABOUT_INFO_DIALOG_TEXT_SIZE}px;'>{platform.platform().split('-', 1)[0]}</span><br>"
)
ABOUT_PROGRAM_VERSION = (
    f"<span style='font-weight: {ABOUT_INFO_DIALOG_TEXT_FONT_WEIGHT}; "
    f"font-size: {ABOUT_INFO_DIALOG_TEXT_SIZE}px;'>{version}</span></p>"
)
