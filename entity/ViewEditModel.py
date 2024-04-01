class ViewEditType:
    id = None
    id_list = None
    MaterialCode = None
    DrawingCode = None
    Name = None
    ProductSize = None
    Material = None
    Color = None
    Quantity = None
    Unit = None
    MaterialCategory = None
    Note = None

    def __init__(self, MaterialCode, DrawingCode, Name, ProductSize, Material, Color, Quantity, Unit, MaterialCategory, Note):
        self.MaterialCode = MaterialCode
        self.DrawingCode = DrawingCode
        self.Name = Name
        self.ProductSize = ProductSize
        self.Material = Material
        self.Color = Color
        self.Quantity = Quantity
        self.Unit = Unit
        self.MaterialCategory = MaterialCategory
        self.Note = Note
