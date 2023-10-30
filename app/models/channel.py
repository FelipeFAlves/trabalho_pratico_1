from datetime import datetime

class Channel:
    def __init__(self,id:str, title:str, description:str, customUrl:str, 
                publishedAt:datetime, viewCount:int, 
                subscriberCount:int, hiddenSubscriberCount:int,
                videoCount:int, brandingId:int, 
                bannerExternalUrl:str):
        self.id = id
        self.title = title
        self.description = description
        self.customUrl = customUrl
        self.publishedAt = publishedAt
        self.viewCount = viewCount
        self.subscriberCount = subscriberCount
        self.hiddenSubscriberCount = hiddenSubscriberCount
        self.videoCount = videoCount
        self.brandingId = brandingId
        self.bannerExternalUrl = bannerExternalUrl
