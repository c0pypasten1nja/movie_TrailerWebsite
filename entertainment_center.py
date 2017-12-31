import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://static.screenweek.it/2008/9/11/Toy-Story-3-Teaser-Poster-3.jpg",
                        "https://www.youtube.com/watch?v=hgzTFLAWlTE")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://goldbergblog.com/movies/posters/mini/avatar-poster.jpg",
                     "https://www.youtube.com/watch?time_continue=22&v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

transformers_the_last_knight = media.Movie("Transformers: The Last Knight",
                                           "Autobots and Decepticons are at war, with humans on the sidelines. Optimus Prime is gone. The key to saving our future lies buried in the secrets of the past, in the hidden history of Transformers on Earth.",
                                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk3OTI3MDk4N15BMl5BanBnXkFtZTgwNDg2ODIyMjI@._V1_UY268_CR0,0,182,268_AL_.jpg",
                                           "https://www.youtube.com/watch?time_continue=4&v=H0EMG2Z_Wyg")
#transformers_the_last_knight.show_trailer()

pirates_of_the_caribbean_salazar_revenge = media.Movie("Pirates of the Caribbean: Salazar's Revenge",
                                                       "Captain Jack Sparrow searches for the trident of Poseidon while being pursued by an undead sea captain and his crew.",
                                                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYyMTcxNzc5M15BMl5BanBnXkFtZTgwOTg2ODE2MTI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                                       "https://www.youtube.com/watch?time_continue=5&v=-6StS7p5TdQ")

star_wars_the_last_jedi = media.Movie("Star Wars: The Last Jedi",
                                      "Rey develops her newly discovered abilities with the guidance of Luke Skywalker, who is unsettled by the strength of her powers. Meanwhile, the Resistance prepares for battle with the First Order.",
                                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQ1MzcxNjg4N15BMl5BanBnXkFtZTgwNzgwMjY4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                      "https://www.youtube.com/watch?time_continue=1&v=Q0CbN8sfihY")

jumanji_welcome_to_the_jungle = media.Movie("Jumanji: Welcome to the Jungle",
                                            "Four teenagers discover an old video game console and are literally drawn into the game's jungle setting, becoming the adult avatars they choose.",
                                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkyNDQ1MDc5OV5BMl5BanBnXkFtZTgwOTcyNzI2MzI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                            "https://www.youtube.com/watch?v=2QKg5SZ_35I")

movies = [toy_story, avatar, transformers_the_last_knight, pirates_of_the_caribbean_salazar_revenge, star_wars_the_last_jedi, jumanji_welcome_to_the_jungle]
fresh_tomatoes.open_movies_page(movies)






