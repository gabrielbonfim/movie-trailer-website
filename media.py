# This program is open source.  For license terms, see the LICENSE file.

class Movie():
    """Creates a Movie object with the possibility to define information about
    its title, poster URL and YouTube trailer.

    Attributes:
        title: The title of the movie.
        poster_image_url: URL to the poster of the movie.
        trailer_youtube_url: URL to the trailer in YouTube.
    """
    
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Initiates class Movie, reserving memory space"""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
