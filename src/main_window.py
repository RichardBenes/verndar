from PySide6.QtWidgets import QMainWindow, QPushButton

class MainWindow(QMainWindow):



    def __init__(self):
        super().__init__()
        
        btn = QPushButton("Verndar here")
        money = "euros"        
        btn.clicked.connect(lambda _, a=money: print(f"verndar is working hard {a=}"))

        self.setCentralWidget(btn)