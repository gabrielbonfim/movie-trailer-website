# This program is open source.  For license terms, see the LICENSE file.
#
# We use entertainment_center.py to to create a list of movie objects by
# calling media.Movie() to instantiate those movie objects. The movie objects
# then will be placed in a list that will be used to feed open_movies_page()
# function that will produce the HTML that will be displayed in the webpage

# Import module media to have access to the class Movie
import media

# Import module fresh_tomatoes to access open_movies_page that will generate
# the HTML based on the list of movie objects received
import fresh_tomatoes

# Instantiation of the movie "Alien" with the arguments movie title, poster
# and trailer
alien = media.Movie("Alien",
                    "https://goo.gl/ugvYsU",
                    "https://www.youtube.com/watch?v=LjLamj-b0I8")

# Instantiation of the movie "Aliens" with the arguments movie title, poster
# and trailer
aliens = media.Movie("Aliens",
                     "https://goo.gl/riN8VW",
                     "https://www.youtube.com/watch?v=W857ys3BlRI")

# Instantiation of the movie "Alien 3" with the arguments movie title, poster
# and trailer
alien_3 = media.Movie("Alien 3",
                      "https://goo.gl/VcVyrs",
                      "https://www.youtube.com/watch?v=Ipv1y-Phi7A")

# Instantiation of the movie "Alien: Resurrection" with the arguments movie
# title, poster and trailer
alien_resurrection = media.Movie("Alien: Resurrection",
                                 "https://goo.gl/QpRkqB",
                                 "https://www.youtube.com/watch?v=-qJjiq72WOo")

# Instantiation of the movie "Predator" with the arguments movie title, poster
# and trailer
predator = media.Movie("Predator",
                       "https://goo.gl/okz8Zg",
                       "https://www.youtube.com/watch?v=Y1txEAywdiw")

# Instantiation of the movie "Predator 2" with the arguments movie title,
# poster and trailer
predator_2 = media.Movie("Predator 2",
                         "https://goo.gl/Auf619",
                         "https://www.youtube.com/watch?v=UPlSNCoUNXE")

# Instantiation of the movie "AVP: Alien vs. Predator" with the arguments movie
# title, posterand trailer
avp_1 = media.Movie("AVP: Alien vs. Predator",
                    "https://goo.gl/f9JtQE",
                    "https://www.youtube.com/watch?v=jC1ngKr6QA8")

# Instantiation of the movie "Aliens vs. Predator: Requiem" with the arguments
# movie title, poster and trailer
avp_2 = media.Movie("Aliens vs. Predator: Requiem",
                    "https://goo.gl/WLCveu",
                    "https://www.youtube.com/watch?v=YrTXTb03Ixc")

# Instantiation of the movie "Star Wars: Episode I - The Phantom Menace" with
# the arguments movie title, poster and trailer
star_wars_1 = media.Movie("Star Wars: Episode I - The Phantom Menace",
                          "https://goo.gl/QNfZUv",
                          "https://www.youtube.com/watch?v=bD7bpG-zDJQ")

# Instantiation of the movie "Star Wars: Episode II - Attack of the Clones"
# with the arguments movie title, poster and trailer
star_wars_2 = media.Movie("Star Wars: Episode II - Attack of the Clones",
                          "https://goo.gl/6M4BDh",
                          "https://www.youtube.com/watch?v=gYbW1F_c9eM")

# Instantiation of the movie "Star Wars: Episode III - Revenge of the Sith"
# with the arguments movie title, poster and trailer
star_wars_3 = media.Movie("Star Wars: Episode III - Revenge of the Sith",
                          "https://goo.gl/cnHwEp",
                          "https://www.youtube.com/watch?v=5UnjrG_N8hU")

# Instantiation of the movie "Star Wars: Episode IV - A New Hope" with the
# arguments movie title, poster and trailer
star_wars_4 = media.Movie("Star Wars: Episode IV - A New Hope",
                          "https://goo.gl/BCSBUv",
                          "https://www.youtube.com/watch?v=vZ734NWnAHA")

# Instantiation of the movie "Star Wars: Episode V - The Empire Strikes Back"
# with the arguments movie title, poster and trailer
star_wars_5 = media.Movie("Star Wars: Episode V - The Empire Strikes Back",
                          "https://goo.gl/8ne1L5",
                          "https://www.youtube.com/watch?v=JNwNXF9Y6kY")

# Instantiation of the movie "Star Wars: Episode VI - Return of the Jedi" with
# the arguments movie title, poster and trailer
star_wars_6 = media.Movie("Star Wars: Episode VI - Return of the Jedi",
                          "https://goo.gl/L1bxob",
                          "https://www.youtube.com/watch?v=7L8p7_SLzvU")

# Instantiation of the movie "Star Wars: The Force Awakens" with the arguments
# movie title, poster and trailer
star_wars_7 = media.Movie("Star Wars: The Force Awakens",
                          "https://goo.gl/gkJgE9",
                          "https://www.youtube.com/watch?v=sGbxmsDFVnE")

# Instantiation of the movie "Star Wars: The Last Jedi" with the arguments
# movie title, poster and trailer
star_wars_8 = media.Movie("Star Wars: The Last Jedi",
                          "https://goo.gl/tKoVfe",
                          "https://www.youtube.com/watch?v=Q0CbN8sfihY")

# Instantiation of the movie "Rogue One: A Star Wars Story" with the arguments
# movie title, poster and trailer
star_wars_r1 = media.Movie("Rogue One: A Star Wars Story",
                           "https://goo.gl/3jLKbt",
                           "https://www.youtube.com/watch?v=frdj1zb9sMY")

# Instantiation of the movie "Solo: A Star Wars Story" with the arguments movie
# title, poster and trailer
star_wars_s = media.Movie("Solo: A Star Wars Story",
                          "https://goo.gl/618maF",
                          "https://www.youtube.com/watch?v=K9PkToULL1c")

# List of the movie objects created
movies = [alien, aliens, alien_3, alien_resurrection, predator, predator_2,
          avp_1, avp_2, star_wars_1, star_wars_2, star_wars_3, star_wars_4,
          star_wars_5, star_wars_6, star_wars_7, star_wars_8, star_wars_r1,
          star_wars_s]

# Call of the open_movies_page function of the fresh_tomatoes module, with the
# argument 'movies' that is our movie list. The function open_movies_page will
# generate the HTML based in this list
fresh_tomatoes.open_movies_page(movies)
