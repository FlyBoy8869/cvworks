import platform
import sys

import darkdetect
import qtmodern.styles
import qtmodern.windows

from PySide6.QtWidgets import QApplication

import cvworks_gui.view

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = cvworks_gui.view.CalendarView()

    if darkdetect.isDark():
        qtmodern.styles.dark(app)
    else:
        qtmodern.styles.light(app)

    modern_window = qtmodern.windows.ModernWindow(window)

    # because qtmodern wraps the "window" widget,
    # this must be called before the window is shown
    # and all reference to "window" must now reference
    # qtmodern's window
    window.set_qtmodern_window_reference(modern_window)

    # not sure if qtmodern is causing the problem,
    # but this is needed on MS Windows in order for
    # keyReleaseEvent to work without having to
    # click in the CalendarWidget first
    window.calendarWidget.setFocus()

    modern_window.show()

    sys.exit(app.exec())
