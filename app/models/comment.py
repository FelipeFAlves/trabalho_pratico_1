from datetime import datetime

class Comment:
    def __init__(self,id, channelId, videoId, topLevelCommentId,
                 textDisplay, textOriginal, authorDisplayName,
                 authorProfileImageUrl, authorChannelUrl, canRate,
                 viewerRating, likeCount, publishedAt, updatedAt,
                 canReply, totalReplyCount, isPublic):
        self.id = id
        self.channelID = channelId
        self.videoId = videoId
        self.topLevelCommentId = topLevelCommentId
        self.textDisplay = textDisplay
        self.textOriginal = textOriginal
        self.authorDisplayName = authorDisplayName
        self.authorProfileImageUrl = authorProfileImageUrl
        self.authorChannelUrl = authorChannelUrl
        self.canRate = canRate
        self.viewerRating = viewerRating
        self.likeCount = likeCount
        self.publishedAt = publishedAt
        self.updatedAt = updatedAt
        self.canReply = canReply
        self.totalReplyCount = totalReplyCount
        self.isPublic = isPublic