import webbrowser  # for opening window

class Movie():
    """A class for creating movie objects"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # constructor function
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # launch youtube_trailer function
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
