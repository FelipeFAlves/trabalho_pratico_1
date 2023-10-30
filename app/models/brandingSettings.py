from datetime import datetime

class brandingSettings:
    def __init__(self,id:str, title:str, description:str, keywords:str, unsubscribedTrailer:str):
        self.id = id
        self.title = title
        self.description = description
        self.keywords = keywords
        self.unsubscriberTrailer = unsubscribedTrailer