from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import contains_eager, joinedload
from sqlalchemy.orm import relationship

from random import random

base = declarative_base()
engine = create_engine("mysql://root:fifty50@localhost:3306/mdi", echo=True)
metadata = MetaData(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


class Bet(base):
    global metadata
    __table__ = Table('bets', metadata, autoload=True)

    def __init__(self,
                 _id,
                 user_id,
                 video_id,
                 current_views_count,
                 current_subscribers_count,
                 created_at,
                 updated_at):
        self.id = _id
        self.user_id = user_id
        self.video_id = video_id
        self.current_views_count = current_views_count
        self.current_subscribers_count = current_subscribers_count
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return "<Bet('{}','{}', '{}', '{}', '{}', '{}', '{}', '{}')>". \
            format(self.id, self.user_id, self.video_id, self.current_views_count,
                   self.current_subscribers_count, self.created_at, self.updated_at)


class Channel(base):
    global metadata
    __table__ = Table('channels', metadata, autoload=True)
    videos = relationship("Video", backref="channel")
    history_entries = relationship("HistoryEntry", backref="channel")

    def __init__(self,
                 _id,
                 youtube_channel_id,
                 subscribers_count,
                 videos_count,
                 total_upload_count,
                 created_at,
                 updated_at):
        self.id = _id
        self.youtube_channel_id = youtube_channel_id
        self.subscribers_count = subscribers_count
        self.videos_count = videos_count
        self.total_upload_count = total_upload_count
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return "<Channel('{}','{}', '{}', '{}', '{}', '{}', '{}', '{}')>". \
            format(self.id, self.user_id, self.video_id, self.current_views_count,
                   self.current_subscribers_count, self.created_at, self.updated_at)


class User(base):
    global metadata
    __table__ = Table('users', metadata, autoload=True)
    bets = relationship("Bet", backref="user")

    def __init__(self, _id, username, email, password, remember_token, points, created_at, updated_at):
        self.id = _id
        self.username = username
        self.email = email
        self.password = password
        self.remember_token = remember_token
        self.points = points
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return "<User('{}','{}', '{}', '{}', '{}', '{}', '{}', '{}')>".\
            format(self.id, self.username, self.email, self.password, self.remember_token,
                   self.points, self.created_at, self.updated_at)


class HistoryEntry(base):
    global metadata
    __table__ = Table('video_history', metadata, autoload=True)

    def __init__(self, channels_id, videos_id, subscribers_count, created_at):
        self.channels_id = channels_id
        self.videos_id = videos_id
        self.subscribers_count = subscribers_count
        self.created_at = created_at

    def __repr__(self):
        return "<HistoryEntry('%d','%d', '%d', '%d', '%d')>"\
            .format(self.id, self.channels_id, self.videos_id, self.subscribers_count, self.created_at)


class Video(base):
    global metadata
    __table__ = Table('videos', metadata, autoload=True)
    bets = relationship("Bet", backref="bet_video")
    history = relationship("HistoryEntry", backref="ref_video")

    def __init__(self, _id, channels_id, videos_id, views, favorite_count, published_at, created_at):
        self.id = _id
        self.channels_id = channels_id
        self.videos_id = videos_id
        self.views = views
        self.favorite_count = favorite_count
        self.published_at = published_at
        self.created_at = created_at
        self.updated_at = created_at

    def __repr__(self):
        return "<Video({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7})>" \
            .format(self.id,
                    self.channels_id,
                    self.videos_id,
                    self.views,
                    self.favorite_count,
                    self.published_at,
                    self.created_at,
                    self.updated_at)

    def __str__(self):
        return self.__repr__()


def insert_from_list(s):
    """ Inserts into the db contained in set s
    :param s: Set containing data
    """
    assert isinstance(s, list)
    print '+++', s
    session.add_all(s)
    session.commit()


def generate_random_bet():
    query = session.query(Video)
    row_count = int(query.count())
    random_video = query.offset(int(row_count * random())).first()

    bet = Bet()
    insert_from_list([bet])


def update_videos(l):
    # for e in l:
    #     update(Video.__table__).where(users.c.id == 5).values(name='user #5')
    pass


def get_history_length():
    """ Returns the count of the `History` table """
    return session.query(func.count('*')).select_from(HistoryEntry).scalar()


# if __name__ == '__main__':
#     testlist = session.query(User).all()
#     #
#     for user in testlist:
#         print user

# insert test
#     st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    # d_user = User(None, 'Ed Jones', 'a@b.c', 'pass', 1, 0, datetime.now(), datetime.now())
    # session.add(d_user)
    # session.commit()
