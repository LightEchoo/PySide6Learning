from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from random import choice
window_titles = [ # A list of window titles we’ll select from using random.choice()
  'My App',
  'My App',
  'Still My App',
  'Still My App',
  'What on earth',
  'What on earth',
  'This is surprising',
  'This is surprising',
  'Something went wrong'
]
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        # Hook up our custom slot method the_window_title_changed to the windows .windowTitleChanged signal
        self.windowTitleChanged.connect(self.the_window_title_changed)
        # The signal of .windowTitleChanged only fires if the new title is changed from the previous one.
        # If you set the same title multiple times, the signal will only be fired the first time.
        # It is important to double-check the conditions under which signals fire, to avoid being surprised
        # when using them in your app.


        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)
    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)
        if window_title == 'Something went wrong':
            self.button.setDisabled(True)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
