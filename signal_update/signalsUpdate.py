from PyQt6.QtCore import QObject, pyqtSignal

class GlobalSignals(QObject):
    updateTable = pyqtSignal()
    
global_signals = GlobalSignals()