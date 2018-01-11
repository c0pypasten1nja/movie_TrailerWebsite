import webbrowser


class Movie():
    """This class provides a way to store movie related information such as
    movie title, storyline, poster image, and link to trailer
    This class can be initialised by passing the arguments:
    movie title, storyline, poster image, and link to trailer.

    This class comes with a function to execute the link to trailer by
    calling the open function of the webbrowser library"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
    	         trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
