from apiclient.discovery import build


class YoutubeAPI:  # TODO extends API_abstract

    def __init__(self, key):
        # authenticate

        # This OAuth 2.0 access scope allows for full read/write access to the
        # authenticated user's account.
        YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
        YOUTUBE_API_SERVICE_NAME = "youtube"
        YOUTUBE_API_VERSION = "v3"
        self.youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=key)


        # search_response = self.youtube.search().list(
        #     q=options.q,
        #     part="id,snippet",
        #     maxResults=options.max_results
        # ).execute()

