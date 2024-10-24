# Project Networking


> **Don't forget to edit this `README.md` file**
>
> If you're interested in how to format markdown, click [here](https://www.markdownguide.org/basic-syntax/#images-1)

## API Overview
*My API is about songs and music, and it's goal is to be able to provide users with song recommendations for different purposes. 

In the API, users can add their own song recommendations, "like" other users songs, and do much more, to find or help users discover more songs. 

I hope my API successfully provides you with the songs that you are searching for. Feel free to add your own song recommendations to my API!*

> To access my api, you must use the HTTPie App, and enter in the api URL: http://127.0.0.1:5000/Songs/


### Model


| **`Model Name`**  | **`What it does`**  |
|---|---|
| `json response`  |  This model give the default json response of a song, containing the songs title, author, description, and much more. |
| `increase likes`  | This model allows users to increase/add likes to songs in the list.  |
| `increase dislikes`  | This model allows users to increase/add dislikes to songs in the list.  |
| `change description`  |  This model allows users to change the description of a song, to add extra information or correct any false information about the song. |
| `change mood`  | This model allows users to change the represented mood of the song, to change any incorrect information about the mood, or to add a mood that is relavent to the song.   |
| `leaderboard`  | This model gives the json response for the leaderboard endpoint (Standard json response, but with no moods)   |
### Endpoints
| **`Endpoint Name`**  |  **`What it does`** |  **`Endpoint name & Method type`** | **`Arguments Needed`** |
|---|---|---|---|
| `new`  | This endpoint allows users to add new song recommendations, with the description of the song, and the mood of the song.  |  /new (post) | Title(string), Artist(string), Description(string), Happy(boolean), Sad(boolean), Angry(boolean), Love(boolean), Calm(boolean), Energetic(boolean) |
|  `all` |  This endpoint allows users to see all of the song recommendations, their likes, dislikes, and much more. | /all (get)  | N/A  |
| `like`  | This endpoint allows users to add likes to another users song recommendation  | /like (post)  | id(integer) |
| `dislike`  | This endpoint allows users to add dislikes to another users song recommendation  | /dislike (post)  | id(integer)  |
| `change_description`  | This endpoint allows to change the description of a song recommendation in the list | /change_description (post)  | id(integer), new_description(string)  |
| `change_mood`  | This endpoint allows users to change the mood of a song recommendation  | /change_mood (post)  | id(integer), Happy(boolean), Sad(boolean), Angry(boolean), Love(boolean), Calm(boolean), Energetic(boolean)  |
| `leaderboard`  | This endpoint allows users to see the song recommendation leaderboard, sorted by likes  | /leaderboard (get)  | N/A |

---

### Contents
- `\app`
    - `models.py` - `Song` model
    - `views.py` - endpoints
- `database.sqlite`  
- `README.md` 

**To start a Banjo server:** `banjo --debug` 




