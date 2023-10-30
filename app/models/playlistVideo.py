from datetime import datetime

class PlaylistVideo:
    def __init__(self,playlistId, videoId, position):
        self.playlistId = playlistId
        self.videoId = videoId
        self.position = position