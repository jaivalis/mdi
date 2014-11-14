"""
This script is used to collect hourly data from Youtube with which we will evaluate our scoring models
The implementation should go as follows:

if `videos` is empty (first run) :
    insert many video urls to the video table (from file probably)
update `history` table with new per video stats

$ python -m meecho.daemon.dataCollector

"""
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from ..db.orm import User, Video, get_history_length, insert_from_list, session
from ..extapi.youtube import YoutubeApi
import csv


def is_first_run():
    return get_history_length() == 0


def get_video_urls(urls_path=None):
    """ Reads a file containing video urls (the more the better)
    :return: a list of video urls
    """
    ret = []
    if urls_path is None:
        return ['5y4_Mi0fCz0']  # TODO debugging

    with open(urls_path, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            ret.append(row)
    return ret


def main():
    yt = YoutubeApi('IzaSyAkeqT270l7-YSWmDVscxo-A5POFmbb9ZU')
    if is_first_run():  # first run
        video_instances = []
        for url in get_video_urls():  # append video instance

            v = yt.get_video(url)
            video_instances.append(v)
            print '>>', v.__repr__()

        insert_from_list(video_instances)

    # testlist = session.query(User).all()
    # #
    # for user in testlist:
    #     print user
    #
    #     # Update history table

if __name__ == '__main__':
    main()
