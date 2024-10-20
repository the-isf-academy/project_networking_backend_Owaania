# Project Networking


> **Don't forget to edit this `README.md` file**
>
> If you're interested in how to format markdown, click [here](https://www.markdownguide.org/basic-syntax/#images-1)

## API Overview
*My API is about songs and music, and it's goal is to be able to provide users with song recommendations for different purposes. 

In the API, users can add their own song recommendations, "like" other users songs, and do much more, to find or help users discover more songs. *

### Model


| Model Name  | What it does  |
|---|---|
| json response  |  This model give the default json response of a song, containing the songs title, author, description, and much more. |
| increase likes  | This model allows users to increase/add likes to songs in the list.  |
| increase dislikes  | This model allows users to increase/add dislikes to songs in the list.  |
| change description  |  This model allows users to change the description of a song, to add extra information or correct any false information about the song. |
| change mood  | This model allows users to change the represented mood of the song, to change any incorrect information about the mood, or to add a mood that is relavent to the song.   |
### Endpoints
| Endpoint Name  |  What it does |  How to use |
|---|---|---|
| new  | This endpoint allows users to add new song recommendations, with the description of the song, and the mood of the song.  |  /new (post route) |
|  all |  This endpoint allows users to see all of the song recommendations, their likes, dislikes, and much more. | /all (get)  |
| like  | This endpoint allows users to add likes to another users song recommendation  | /like (post)  |
| dislike  | This endpoint allows users to add dislikes to another users song recommendation  | /dislike (post)  |
| change_description  | This endpoint allows to change the description of a song recommendation in the list | /change_description (post)  |
| change_mood  | This endpoint allows users to change the mood of a song recommendation  | /change_mood (post)  |

---

## Setup

### Contents

Here's what is included:
- `\app`
    - `models.py` - `Fortune` model
    - `views.py` - endpoints
- `database.sqlite`  
- `README.md` 

**To start a Banjo server:** `banjo` 
- [Banjo Documentation](https://the-isf-academy.github.io/banjo_docs/)



