import platform
import sys

from PyQt6.QtWidgets import QApplication

import cvworks_gui.view

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if platform.system() == "Windows":
        import qdarktheme

        qdarktheme.setup_theme("auto")

    window = cvworks_gui.view.CalendarView()
    sys.exit(app.exec())
