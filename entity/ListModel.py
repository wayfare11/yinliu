class ListType:
    id = None
    Name = None
    FileCode = None
    VersionCode = None
    ProductSize = None
    ProductCode = None
    DandaoSize = None
    DandaoStyle = None
    DandaoCode = None
    YinliuSize = None
    YinliuLock = None
    YinliuStyle = None
    YinliuCode = None
    MaterialCode = None

    def __init__(self, Name, FileCode, VersionCode, ProductSize, ProductCode, DandaoSize, DandaoStyle, DandaoCode, YinliuSize, YinliuLock, YinliuStyle, YinliuCode, MaterialCode):
        self.Name = Name
        self.FileCode = FileCode
        self.VersionCode = VersionCode
        self.ProductSize = ProductSize
        self.ProductCode = ProductCode
        self.DandaoSize = DandaoSize
        self.DandaoStyle = DandaoStyle
        self.DandaoCode = DandaoCode
        self.YinliuSize = YinliuSize
        self.YinliuLock = YinliuLock
        self.YinliuStyle = YinliuStyle
        self.YinliuCode = YinliuCode
        self.MaterialCode = MaterialCode
