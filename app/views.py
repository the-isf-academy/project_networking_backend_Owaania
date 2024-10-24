# views.py

from banjo.urls import route_get, route_post
from settings import BASE_URL
from .models import Song

#This endpoint allows users to add a new song to the list
@route_post(BASE_URL + 'new', args={'title':str, 'artist': str, 'description':str, 'Happy':bool, 'Sad':bool, 'Angry':bool, 'Love':bool, 'Calm':bool, 'Energetic':bool})
def new_song(args):
    #This line makes it so if another user adds a new song with a title that already exists, it will return an error, preventing a duplicate song.
    if Song.objects.filter(title=args['title']).exists():
        return {'Error': 'Song with this title already exists!'}
    #This is the new songs arguments
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

    #saves the new song into the song list
    new_song.save()
    #returns the new song's response
    return {'Recommendations:': new_song.json_response()}

#This endpoint allows users to see all the songs in the recommendations list, sorted by ID
@route_get(BASE_URL + 'all')
def all_songs(args):
    song_list = []
    
    #adds a json response to every song in the list
    for song in Song.objects.all():
        song_list.append(song.json_response())
    #returns the whole song list
    return {'Recommendations:':song_list}

#This endpoint allows users to add likes to a song in the list
@route_post(BASE_URL + 'like', args={'id': int})
def add_like(args):

    #filters the song id, and increases the like count by 1
    if Song.objects.filter(id=args['id']).exists():
        add_likes = Song.objects.get(id=args['id']) 
        add_likes.increase_likes()
        #returns the song with the new like count
        return {'Recommendations' : add_likes.json_response()}
    else:
        return {'Error':'Song ID not found!'}

 #This endpoint allows users to add dislikes to a song in the list   
@route_post(BASE_URL + 'dislike', args={'id': int})
def add_dislike(args):

    #filters the song id, and increases the dislike count by 1
    if Song.objects.filter(id=args['id']).exists():
        add_dislike = Song.objects.get(id=args['id']) 
        add_dislike.increase_dislikes()
        #returns the song with the new dislike count
        return {'Recommendations' : add_dislike.json_response()}
    else:
        return {'Error':'Song ID not found!'}
    
#This endpoint allows users to change the description of a song in the list
@route_post(BASE_URL + 'change_description', args={'id': int,'new_description':str})
def description(args):

    #filters the song id, and changes the old description to the new description
    if Song.objects.filter(id=args['id']).exists():
        new_description = Song.objects.get(id=args['id'])
        new_description.change_description(args['new_description'])
        #returns the song with the new description
        return {'Recommendations' : new_description.json_response()} 
    else:
        return {'Error':'Song ID not found!'}

#This endpoint allows users to change the moods of a song in the list
@route_post(BASE_URL + 'change_mood', args={'id': int,'Happy':bool, 'Sad':bool, 'Angry':bool, 'Love':bool, 'Calm':bool, 'Energetic':bool})
def change_mood(args):

    #filters the song id, and then changes the old moods to the new moods
    if Song.objects.filter(id=args['id']).exists():
        new_mood = Song.objects.get(id=args['id'])
        new_mood.change_mood(args['Happy'],args['Sad'],args['Angry'],args['Love'],args['Calm'],args['Energetic'])
        #returns the song with the new moods
        return {'Recommendations' : new_mood.json_response()}
    else:
        return {'Error':'Song ID not found!'}

#This endpoint allows users to see the leaderboard of songs with the most likes
@route_get(BASE_URL + 'leaderboard')
def leaderboard(args):

    #orders the songs in the list by likes
    like_leaderboard = Song.objects.order_by('-likes')
    if like_leaderboard.exists():
        leaderboard_list = [song.leaderboard() for song in like_leaderboard]
        return {'Leaderboard': leaderboard_list}
    else:
        return {'Error': 'No songs with likes!'}
