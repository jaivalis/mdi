from model.simpleModel import SimpleModel
from extapi.youtube import YoutubeApi
from util.globals import _youtube_API_key


def main():
    yt = YoutubeApi(_youtube_API_key)
    api_list = [yt]

    m = SimpleModel(db=None, api_list=api_list)
    m.update_counts_db()

if __name__ == '__main__':
    main()