import fresh_tomatoes  # helper file for creating webpage
import media  # import Movie class

"""Top 20 U.S. Movies of all Time According to The American Film Institute"""

# List of movie instances constructed from media file
# movie title, poster image, youtube trailer url
citizen_kane = media.Movie("Citizen Kane",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/c/ce/Citizenkane.jpg/220px-Citizenkane.jpg",
                           "https://www.youtube.com/watch?v=zyv19bg0scg")

casablanca = media.Movie("Casablanca",
                         "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/CasablancaPoster-Gold.jpg/220px-CasablancaPoster-Gold.jpg",
                         "https://www.youtube.com/watch?v=BkL9l7qovsE")

the_godfather = media.Movie("The Godfather",
                            "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                            "https://www.youtube.com/watch?v=sY1S34973zA")

gone_with_the_wind = media.Movie("Gone With the Wind",
                                 "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Poster_-_Gone_With_the_Wind_01.jpg/220px-Poster_-_Gone_With_the_Wind_01.jpg",
                                 "https://www.youtube.com/watch?v=8mM8iNarcRc")

lawrence_of_arabia = media.Movie("Lawrence of Arabia",
                                 "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Lawrence_of_arabia_ver3_xxlg.jpg/220px-Lawrence_of_arabia_ver3_xxlg.jpg",
                                 "https://www.youtube.com/watch?v=zmr1iSG3RTA")

the_wizard_of_oz = media.Movie("The Wizard of Oz",
                               "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/WIZARD_OF_OZ_ORIGINAL_POSTER_1939.jpg/212px-WIZARD_OF_OZ_ORIGINAL_POSTER_1939.jpg",
                               "https://www.youtube.com/watch?v=H_3T4DGw10U")

the_graduate = media.Movie("The Graduate",
                           "https://upload.wikimedia.org/wikipedia/en/8/8b/Graduateposter67.jpg",
                           "https://www.youtube.com/watch?v=hsdvhJTqLak")

on_the_waterfront = media.Movie("On the Waterfront",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/9/93/On_the_Waterfront_original_poster.jpg/220px-On_the_Waterfront_original_poster.jpg",
                                "https://www.youtube.com/watch?v=QOLHbQjtSFs")

schindlers_list = media.Movie("Schindler's List",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/3/38/Schindler%27s_List_movie.jpg/220px-Schindler%27s_List_movie.jpg",
                              "https://www.youtube.com/watch?v=JdRGC-w9syA")

singin_in_the_rain = media.Movie("Singin in the Rain",
                                 "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/Singing_in_the_rain_poster.jpg/220px-Singing_in_the_rain_poster.jpg",
                                 "https://www.youtube.com/watch?v=36QiuRc_3I8")

its_a_wonderful_life = media.Movie("It's a Wonderful Life",
                                   "https://upload.wikimedia.org/wikipedia/en/thumb/9/95/Its_A_Wonderful_Life_Movie_Poster.jpg/220px-Its_A_Wonderful_Life_Movie_Poster.jpg",
                                   "https://www.youtube.com/watch?v=ewe4lg8zTYA")

sunset_blvd = media.Movie("Sunset Blvd",
                          "https://upload.wikimedia.org/wikipedia/en/0/0a/SunsetBoulevardfilmposter.jpg",
                          "https://www.youtube.com/watch?v=Y3P0Zpe-2og")

the_bridge_on_the_river_kwai = media.Movie("The Bridge on the River Kwai",
                                           "https://upload.wikimedia.org/wikipedia/en/f/f2/The_Bridge_on_the_River_Kwai_poster.jpg",
                                           "https://www.youtube.com/watch?v=RlC7XBayj0s")

some_like_it_hot = media.Movie("Some Like it Hot",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/b/b4/Some_Like_It_Hot_poster.jpg/220px-Some_Like_It_Hot_poster.jpg",
                               "https://www.youtube.com/watch?v=rI_lUHOCcbc")

star_wars = media.Movie("Star Wars",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/8/87/StarWarsMoviePoster1977.jpg/220px-StarWarsMoviePoster1977.jpg",
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k")

all_about_eve = media.Movie("All About Eve",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/2/22/AllAboutEve.jpeg/220px-AllAboutEve.jpeg",
                            "https://www.youtube.com/watch?v=LSntQerk8cQ")

the_african_queen = media.Movie("The African Queen",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/The-african-queen-1-.jpeg/250px-The-african-queen-1-.jpeg",
                                "https://www.youtube.com/watch?v=88jytHOsDos")

psycho = media.Movie("Psycho",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b9/Psycho_%281960%29.jpg/220px-Psycho_%281960%29.jpg",
                     "https://www.youtube.com/watch?v=NG3-GlvKPcg")

chinatown = media.Movie("Chinatown",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/3/38/Chinatownposter1.jpg/220px-Chinatownposter1.jpg",
                        "https://www.youtube.com/watch?v=T37QkBc4IGY")

one_flew_over_the_cuckoos_nest = media.Movie("One Flew Over the Cuckoos Nest",
                                             "https://upload.wikimedia.org/wikipedia/en/thumb/2/26/One_Flew_Over_the_Cuckoo%27s_Nest_poster.jpg/220px-One_Flew_Over_the_Cuckoo%27s_Nest_poster.jpg",
                                             "https://www.youtube.com/watch?v=2WSyJgydTsA")

# array of movie objects
movies = [
    citizen_kane, casablanca, the_godfather, gone_with_the_wind,
    lawrence_of_arabia, the_wizard_of_oz,the_graduate, on_the_waterfront,
    schindlers_list, singin_in_the_rain, its_a_wonderful_life, sunset_blvd,
    the_bridge_on_the_river_kwai, some_like_it_hot, star_wars, all_about_eve,
    the_african_queen, psycho, chinatown, one_flew_over_the_cuckoos_nest
]

# launch webpage
fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)
