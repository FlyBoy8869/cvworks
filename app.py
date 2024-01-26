import sys
import cvworks_gui.view
import platform
from PyQt6.QtWidgets import QApplication

QApplication.setOrganizationName("Charles Industries")
QApplication.setOrganizationDomain("charlesindustries.com")
QApplication.setApplicationName("cvworks")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if platform.system() == "Windows":
        import qdarktheme

        qdarktheme.setup_theme("auto")

    window = cvworks_gui.view.CalendarView()
    sys.exit(app.exec())
