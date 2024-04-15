class ComponentUpdateConditionType:
    ProductCode = None
    dandaoDiameter = None
    dandaoLength = None
    drainageMethod = None
    dandaoHeadStyle = None
    dandaoConfigurationCode = None
    yinliuDiameter = None
    yinliuLength = None
    yinliuLockStyle = None
    yinliuHeadStyle = None
    yinliuConfigurationCode = None

    def __init__(self, ProductCode, dandaoDiameter, dandaoLength, drainageMethod, dandaoHeadStyle, dandaoConfigurationCode, yinliuDiameter, yinliuLength, yinliuLockStyle, yinliuHeadStyle, yinliuConfigurationCode):
        self.ProductCode = ProductCode
        self.dandaoDiameter = dandaoDiameter
        self.dandaoLength = dandaoLength
        self.drainageMethod = drainageMethod
        self.dandaoHeadStyle = dandaoHeadStyle
        self.dandaoConfigurationCode = dandaoConfigurationCode
        self.yinliuDiameter = yinliuDiameter
        self.yinliuLength = yinliuLength
        self.yinliuLockStyle = yinliuLockStyle
        self.yinliuHeadStyle = yinliuHeadStyle
        self.yinliuConfigurationCode = yinliuConfigurationCode