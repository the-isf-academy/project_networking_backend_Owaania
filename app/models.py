# models.py

from banjo.models import Model, StringField, IntegerField

class Song(Model):
    title = StringField()
    artist = StringField()
    # likes = IntegerField()
    # dislikes = IntegerField()
    # spotify_streams = IntegerField()
    # description = StringField()



    def json_response(self):
        
        return {
            'id': self.id,
            'title': self.title,
            'artist':self.artist
            # 'likes': self.likes,
            # 'dislikes': self.dislikes,
            # 'streams': self.spotify_streams, 
        }

    def increase_likes(self):
        self.likes += 1
        self.save()
           
    def increase_dislikes(self):
        self.dislikes += 1
        self.save()

 