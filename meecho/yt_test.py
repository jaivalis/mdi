from extapi.youtube import YoutubeApi
from util.globals import _youtube_API_key


def main():
    yt = YoutubeApi(_youtube_API_key)


if __name__ == '__main__':
    main()