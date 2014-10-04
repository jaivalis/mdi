from apiclient.discovery import build
import httplib2
import json


class YoutubeApi:  # TODO extends API_abstract
    """
    documentation: https://google-api-python-client.googlecode.com/hg/docs/epy/module-tree.html
    """
    YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    # TODO chache the response of this func to extract other values (such as 'totalUploadViews', 'favoriteCount')
    def _get_json_response(self, url):
        """ Return a JSON object containing the response for a given url
        :param url: URL to request
        :return: JSON object.
        :raises: HttpLib2ErrorWithResponse Probable cause is the quota
        """
        resp, content = httplib2.Http().request(url)
        if resp['status'] != '200':  # quota limit reached
            raise httplib2.HttpLib2ErrorWithResponse

        return json.loads(content)

    def get_channel_id(self, vid_id):
        return vid_id

    def get_channel_subscription_count(self, channel_id):
        url = 'http://gdata.youtube.com/feeds/api/users/{0}?alt=json'.format(channel_id)
        obj = None
        try:
            obj = self._get_json_response(url)
        except httplib2.HttpLib2ErrorWithResponse:
            print 'Http exception'

        return int(obj['entry']['yt$statistics']['subscriberCount'])

    def get_view_count(self, vid_id, channel_id=None):
        if channel_id is None:  # refer to this: https://code.google.com/p/gdata-issues/issues/detail?id=1745
            channel_id = self.get_channel_id(vid_id)
        url = "http://gdata.youtube.com/feeds/api/users/{0}/uploads/{1}?alt=json".format(channel_id, vid_id)

        obj = None
        try:
            obj = self._get_json_response(url)
        except httplib2.HttpLib2ErrorWithResponse:
            print 'Http exception'

        return int(obj['entry']['yt$statistics']['viewCount'])

    def __init__(self, key):
        # authenticate

        # This OAuth 2.0 access scope allows for full read/write access to the
        # authenticated user's account.
        self.yt = build(self.YOUTUBE_API_SERVICE_NAME,
                        self.YOUTUBE_API_VERSION,
                        developerKey=key)

        # http = httplib2.Http()
        # self.service = build("plus", "v1", http=http)
        # self.service.activities().list(userId="me")

        c = self.get_view_count('0pqzNJYzh7I', 'citizentube')
        s = self.get_channel_subscription_count('Tollywood')
        print c
        print s

        # search_response = self.youtube.search().list(
        #     q=options.q,
        #     part="id,snippet",
        #     maxResults=options.max_results
        # ).execute()

