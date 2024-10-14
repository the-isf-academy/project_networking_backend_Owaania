# views.py

from banjo.urls import route_get, route_post
from settings import BASE_URL
from .models import Song

@route_post(BASE_URL + 'new', args={'title':str, 'artist': str})
def new_song(args):
    new_song = Song(
        title = args['title'],
        artist = args['artist'],
        # likes = 0,
        # archive = False,
    )

    new_song.save()

    return {'fortune': new_song.json_response()}

@route_get(BASE_URL + 'all')
def all_fortunes(args):
    song_list = []

    for fortune in Fortune.objects.all():
        fortunes_list.append(fortune.json_response())

    return {'fortunes':fortunes_list}