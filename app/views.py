# views.py

from banjo.urls import route_get, route_post
from settings import BASE_URL
from .models import Song

@route_post(BASE_URL + 'new', args={'title':str, 'artist': str, 'description':str, 'Happy':bool, 'Sad':bool, 'Angry':bool, 'Love':bool, 'Calm':bool, 'Energetic':bool})
def new_song(args):
    new_song = Song(
        title = args['title'],
        artist = args['artist'],
        likes = 0,
        dislikes = 0,
        Happy = args['Happy'],
        Sad = args['Sad'],
        Angry = args['Angry'],
        Love = args['Love'],
        Calm = args['Calm'],
        Energetic = args['Energetic'],
        description = args['description']
    )

    new_song.save()

    return {'Recommendations:': new_song.json_response()}

@route_get(BASE_URL + 'all')
def all_songs(args):
    song_list = []
    
    for song in Song.objects.all():
        song_list.append(song.json_response())

    return {'Recommendations:':song_list}

@route_post(BASE_URL + 'like', args={'id': int})
def add_like(args):
    if Song.objects.filter(id=args['id']).exists():
        add_likes = Song.objects.get(id=args['id']) 
        add_likes.increase_likes()
        return {'Recommendations' : add_likes.json_response()}
    
    else:
        return {'Error':'Song ID not found!'}
    
@route_post(BASE_URL + 'dislike', args={'id': int})
def add_dislike(args):
    if Song.objects.filter(id=args['id']).exists():
        add_dislike = Song.objects.get(id=args['id']) 
        add_dislike.increase_dislikes()
        return {'Recommendations' : add_dislike.json_response()}
    else:
        return {'Error':'Song ID not found!'}
    
@route_post(BASE_URL + 'change_description', args={'id': int,'new_description':str})
def description(args):
    if Song.objects.filter(id=args['id']).exists():
        new_description = Song.objects.get(id=args['id'])
        new_description.change_description(args['new_description'])
        return {'Recommendations' : new_description.json_response()}
    
    else:
        return {'Error':'Song ID not found!'}
    
@route_post(BASE_URL + 'change_mood', args={'id': int,'Happy':bool, 'Sad':bool, 'Angry':bool, 'Love':bool, 'Calm':bool, 'Energetic':bool})
def change_mood(args):
    if Song.objects.filter(id=args['id']).exists():
        new_mood = Song.objects.get(id=args['id'])
        new_mood.change_mood(args['Happy'],args['Sad'],args['Angry'],args['Love'],args['Calm'],args['Energetic'])
        return {'Recommendations' : new_mood.json_response()}
    
@route_get(BASE_URL + 'leaderboard')
def leaderboard(args):
    like_leaderboard = Song.objects.order_by('-likes')

    if like_leaderboard.exists():
        leaderboard_list = [song.leaderboard() for song in like_leaderboard]
        return {'Leaderboard': leaderboard_list}
    else:
        return {'Error': 'No songs with likes!'}
