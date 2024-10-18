# models.py

from banjo.models import Model, StringField, IntegerField, BooleanField

class Song(Model):
    title = StringField()
    artist = StringField()
    likes = IntegerField()
    dislikes = IntegerField()
    description = StringField()
    Happy = BooleanField(default=False)
    Sad = BooleanField(default=False)
    Angry = BooleanField(default=False)
    Love = BooleanField(default=False)
    Calm = BooleanField(default=False)
    Energetic = BooleanField(default=False)

    # spotify_streams = IntegerField()
    # description = StringField()


    def json_response(self):
        
        return {
            'id': self.id,
            'title': self.title,
            'artist':self.artist,
            'likes':self.likes,
            'dislikes': self.dislikes,
            'description':self.description,
            'Happy':self.Happy,
            'Sad':self.Sad,
            'Angry':self.Angry,
            'Love':self.Love,
            'Calm':self.Calm,
            'Energetic':self.Energetic
            # 'streams': self.spotify_streams, 
        }

    def increase_likes(self):
        self.likes += 1
        self.save()
           
    def increase_dislikes(self):
        self.dislikes += 1
        self.save()

    def change_description(self, new_description):
        self.description = new_description
        self.save()

    def change_mood(self, new_Happy, new_Sad, new_Angry, new_Love, new_Calm, new_Energetic):
        self.Happy = new_Happy
        self.Sad = new_Sad
        self.Angry = new_Angry
        self.Love = new_Love
        self.Calm = new_Calm
        self.Energetic = new_Energetic
        self.save()

 