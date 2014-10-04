from extapi.Youtube import YoutubeAPI
from util.globals import _youtube_API_key


def main():
    yt = YoutubeAPI(_youtube_API_key)


if __name__ == '__main__':
    main()