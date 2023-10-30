from datetime import datetime

class thumbnail:
    def __init__(self,id, urlDefault, widthDefault, heightDefault,
                urlMedium, widthMedium, heightMedium, urlHigh,
                widthHigh, heightHigh, urlStandard, widthStandard,
                heightStandard, urlMaxRes, widthMaxRes, 
                heightMaxRes):
        self.id = id
        self.urlDefault = urlDefault
        self.widthDefault = widthDefault
        self.heightDefault = heightDefault
        self.urlMedium = urlMedium
        self.widthMedium = widthMedium
        self.heightMedium = heightMedium
        self.urlHigh = urlHigh
        self.widthHigh = widthHigh
        self.heightHigh = heightHigh
        self.urlStandard = urlStandard
        self.widthStandard = widthStandard
        self.heightStandard = heightStandard
        self.urlMaxRes = urlMaxRes
        self.widthMaxRes = widthMaxRes
        self.heightMaxRes = heightMaxRes
