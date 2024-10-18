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
    
@route_post(BASE_URL + 'dislike', args={'id': int})
def add_dislike(args):
    if Song.objects.filter(id=args['id']).exists():
        add_dislike = Song.objects.get(id=args['id']) 
        add_dislike.increase_dislikes()
        return {'Recommendations' : add_dislike.json_response()}
    
@route_post(BASE_URL + 'change_description', args={'id': int,'new_description':str})
def description(args):
    if Song.objects.filter(id=args['id']).exists():
        new_description = Song.objects.get(id=args['id'])
        new_description.change_description(args['new_description'])
        return {'Recommendations' : new_description.json_response()}
    
 @route_post(BASE_URL + 'change_mood', args={'id': int,'Happy':bool, 'Sad':bool, 'Angry':bool, 'Love':bool, 'Calm':bool, 'Energetic':bool})
 def description(args):
     if Song.objects.filter(id=args['id']).exists():
        new_Happy = Song.objects.get(id=args['id'])
        new_Happy.change_mood(args['Happy'])
        new_Sad = Song.objects.get(id=args['id'])
        new_Sad.change_mood(args['Sad'])
        new_Angry = Song.objects.get(id=args['id'])
        new_Angry.change_mood(args['Angry'])
        new_Love = Song.objects.get(id=args['id'])
        new_Love.change_mood(args['Love'])
        new_Calm = Song.objects.get(id=args['id'])
        new_Calm.change_mood(args['Calm'])
        new_Energetic = Song.objects.get(id=args['id'])
        new_Energetic.change_mood(args['Energetic'])
        return {'Recommendations' : new_Happy.json_response()}