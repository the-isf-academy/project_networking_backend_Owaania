# models.py

from banjo.models import Model, StringField, IntegerField, BooleanField
#These are the models of a song
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


#This is the standard json response of a song
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
        }

#this is the model of the leaderboard
    def leaderboard(self):

        return {
            'id': self.id,
            'title': self.title,
            'artist':self.artist,
            'likes':self.likes,
            'dislikes': self.dislikes,
            'description':self.description
        }

#this is the model that allows users to increase the amount of likes
    def increase_likes(self):
        self.likes += 1
        self.save()
#this is the model that allows users to increase the amount of dislikes 
    def increase_dislikes(self):
        self.dislikes += 1
        self.save()
#This model allows users to change the description of a song
    def change_description(self, new_description):
        self.description = new_description
        self.save()
#this is the model that allows users to change the mood of a song
    def change_mood(self, new_Happy, new_Sad, new_Angry, new_Love, new_Calm, new_Energetic):

        self.Happy = new_Happy
        self.Sad = new_Sad
        self.Angry = new_Angry
        self.Love = new_Love
        self.Calm = new_Calm
        self.Energetic = new_Energetic
        
        self.save()

 