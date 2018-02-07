# This program is open source.  For license terms, see the LICENSE file.
#
# We use entertainment_center.py to to create a list of movie objects by calling
# media.Movie() to instantiate those movie objects. The movie objects then will
# be placed in a list that will be used to feed open_movies_page() function that
# will produce the HTML that will be displayed in the webpage

import media
import fresh_tomatoes

alien = media.Movie("Alien",
                    "https://goo.gl/ugvYsU",
                    "https://www.youtube.com/watch?v=LjLamj-b0I8")

aliens = media.Movie("Aliens",
                     "https://goo.gl/riN8VW",
                     "https://www.youtube.com/watch?v=W857ys3BlRI")

alien_3 = media.Movie("Alien 3",
                      "https://goo.gl/VcVyrs",
                      "https://www.youtube.com/watch?v=Ipv1y-Phi7A")

alien_resurrection = media.Movie("Alien: Resurrection",
                                 "https://goo.gl/QpRkqB",
                                 "https://www.youtube.com/watch?v=-qJjiq72WOo")

predator = media.Movie("Predator",
                       "https://goo.gl/okz8Zg",
                       "https://www.youtube.com/watch?v=Y1txEAywdiw")

predator_2 = media.Movie("Predator 2",
                         "https://goo.gl/Auf619",
                         "https://www.youtube.com/watch?v=UPlSNCoUNXE")

avp_1 = media.Movie("AVP: Alien vs. Predator",
                    "https://goo.gl/f9JtQE",
                    "https://www.youtube.com/watch?v=jC1ngKr6QA8")

avp_2 = media.Movie("Aliens vs. Predator: Requiem",
                    "https://goo.gl/WLCveu",
                    "https://www.youtube.com/watch?v=YrTXTb03Ixc")

star_wars_1 = media.Movie("Star Wars: Episode I - The Phantom Menace",
                          "https://goo.gl/QNfZUv",
                          "https://www.youtube.com/watch?v=bD7bpG-zDJQ")

star_wars_2 = media.Movie("Star Wars: Episode II - Attack of the Clones",
                          "https://goo.gl/6M4BDh",
                          "https://www.youtube.com/watch?v=gYbW1F_c9eM")

star_wars_3 = media.Movie("Star Wars: Episode III - Revenge of the Sith",
                          "https://goo.gl/cnHwEp",
                          "https://www.youtube.com/watch?v=5UnjrG_N8hU")

star_wars_4 = media.Movie("Star Wars: Episode IV - A New Hope",
                          "https://goo.gl/BCSBUv",
                          "https://www.youtube.com/watch?v=vZ734NWnAHA")

star_wars_5 = media.Movie("Star Wars: Episode V - The Empire Strikes Back",
                          "https://goo.gl/8ne1L5",
                          "https://www.youtube.com/watch?v=JNwNXF9Y6kY")

star_wars_6 = media.Movie("Star Wars: Episode VI - Return of the Jedi",
                          "https://goo.gl/L1bxob",
                          "https://www.youtube.com/watch?v=7L8p7_SLzvU")

star_wars_7 = media.Movie("Star Wars: The Force Awakens",
                          "https://goo.gl/gkJgE9",
                          "https://www.youtube.com/watch?v=sGbxmsDFVnE")

star_wars_8 = media.Movie("Star Wars: The Last Jedi",
                          "https://goo.gl/tKoVfe",
                          "https://www.youtube.com/watch?v=Q0CbN8sfihY")

star_wars_r1 = media.Movie("Rogue One: A Star Wars Story",
                           "https://goo.gl/3jLKbt",
                           "https://www.youtube.com/watch?v=frdj1zb9sMY")

star_wars_s = media.Movie("Solo: A Star Wars Story",
                          "https://goo.gl/618maF",
                          "https://www.youtube.com/watch?v=K9PkToULL1c")

movies = [alien, aliens, alien_3, alien_resurrection, predator, predator_2,
          avp_1, avp_2, star_wars_1, star_wars_2, star_wars_3, star_wars_4,
          star_wars_5, star_wars_6, star_wars_7, star_wars_8, star_wars_r1,
          star_wars_s]

fresh_tomatoes.open_movies_page(movies)
