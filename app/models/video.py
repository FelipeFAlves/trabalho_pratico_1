from datetime import datetime

class Video:
    def __init__(self,id, publishedAt, channelId, title,
                description, thumbnailId, duration, dimension,
                definition, caption, licensedContent, projection,
                viewCount, likeCount, favoriteCount, commentCount):
        self.id = id
        self.publushedAt = publishedAt
        self.channelId = channelId
        self.title = title
        self.description = description
        self.thumbnailId = thumbnailId
        self.duration = duration
        self.dimension = dimension
        self.definition = definition
        self.caption = caption
        self.lincensedContent = licensedContent
        self.projection = projection
        self.viewCount = viewCount
        self.likeCount = likeCount
        self.favoriteCount = favoriteCount
        self.commentCount = commentCount