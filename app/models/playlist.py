from datetime import datetime

class Playlist:
    def __init__(self,id, publishedAt, channelId, title, description, channelTitle, defaultLanguage):
        self.id = id
        self.publishedAt = publishedAt
        self.channelId = channelId
        self.title = title
        self.description = description
        self.channelTitle = channelTitle
        self.defaultLanguage = defaultLanguage
