import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that comes to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "http://www.youtube.com/watch?v=vwyZH85NQC4")


avatar = media.Movie("Avatar",
                     "The story of a marine on an alien planet.",
                     "http://www.movieposter.com/posters/archive/main/105/MPW-52799",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")
kung_fu_panda = media.Movie("Kung Fu Panda",
                            "An animated movie about a lazy panda who learns kung fu to save his clan.",
                            "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",
                            "https://www.youtube.com/watch?v=PXi3Mv6KMzY")
twilight = media.Movie("Twilight",
                       "Love story of a handsome guy who is a vampire in real life and his school mate",
                       "https://upload.wikimedia.org/wikipedia/en/b/b6/Twilight_%282008_film%29_poster.jpg",
                       "https://www.youtube.com/watch?v=fFLrRlPBg0A")
shawshank_redemption = media.Movie("Shawshank Redemption",
                                   "Story of a banker who is sentenced to life in Shawshank State Penitentiary for the murder of his wife , who manages to escape jail.",
                                   "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")
devil_wears_prada = media.Movie("Devil Wears Prada",
                                "Story about a regular journalist who starts working for a fashion magazine with a rude arrogant boss to handle ,and all topsy turvy in her life.",
                                "https://upload.wikimedia.org/wikipedia/en/e/e7/The_Devil_Wears_Prada_main_onesheet.jpg",
                                "https://www.youtube.com/watch?v=XTDSwAxlNhc")
                            

movies = [toy_story, avatar,kung_fu_panda, twilight, shawshank_redemption,devil_wears_prada]
fresh_tomatoes.open_movies_page(movies)
                             
