QML_IMPORT_NAME = "FileSystemModule"
QML_IMPORT_MAJOR_VERSION = 1

@QmlNamedElement("Colors")
@QmlSingleton
class SchemeManager(QObject):
    schemeChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        with open(Path(__file__).parent / "schemes.json", 'r') as f:
            self.m_schemes = json.load(f)
        self.m_activeScheme = {}