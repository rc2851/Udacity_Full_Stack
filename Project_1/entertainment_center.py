import fresh_tomatoes
import media

#Create movie objects
zero_dark_thirty = media.Movie("Zero Dark Thirty",
                        "For a decade, an elite team of intelligence and military operatives, working in secret across the globe, devoted themselves to a single goal: to find and eliminate Osama bin Laden.",
                        "http://upload.wikimedia.org/wikipedia/en/7/77/ZeroDarkThirty2012Poster.jpg",
                        "https://www.youtube.com/watch?v=EYFhFYoDAo4")

its_a_wonderful_life= media.Movie("It's A Wonderful Life",
                        "On Christmas Eve, George Bailey is deeply troubled and suicidal. Prayers for his well-being from friends and family reach Heaven. Clarence Odbody, Angel 2nd Class, is assigned to save George. In order to prepare Clarence for his trip to Earth, his superior Joseph shows flashbacks of George's life.",
                        "http://upload.wikimedia.org/wikipedia/en/9/95/Its_A_Wonderful_Life_Movie_Poster.jpg",
                        "https://www.youtube.com/watch?v=LJfZaT8ncYk")

shawshank_redemption = media.Movie("Shawshank Redemption",
                        "A banker Andy Dufresne is wrongfully convicted of murdering his wife and her lover and sentenced to two consecutive life sentences at the fictional Shawshank State Penitentiary in rural Maine.",
                        "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")


schindlers_list = media.Movie("Schindler's List",
                        "Oskar Schindler is a vain, glorious and greedy German businessman who becomes unlikely humanitarian amid the barbaric Nazi reign when he feels compelled to turn his factory into a refuge for Jews.",
                        "http://upload.wikimedia.org/wikipedia/en/3/38/Schindler%27s_List_movie.jpg",
                        "https://www.youtube.com/watch?v=dwfIf1WMhgc")

airplane = media.Movie("Airplane",
                        "Ex-fighter pilot and taxi driver Ted Striker (Robert Hays) became traumatized during an unnamed war, leading to a pathological fear of flying. As a result, he is unable to hold a responsible job. His wartime girlfriend, Elaine Dickinson (Julie Hagerty), now a flight attendant, leaves him. Striker nervously boards a Boeing 707 (Trans American Flight 209) from Los Angeles to Chicago on which she is serving, hoping to win her back, but she rebuffs him.",
                        "http://upload.wikimedia.org/wikipedia/en/f/f5/Airplane%21.jpg",
                        "https://www.youtube.com/watch?v=qaXvFT_UyI8")

inglorious_bastards = media.Movie("Inglorious Bastards",
                     "In the spring of 1944, 1st Special Service Force Lieutenant Aldo Raine recruits eight Jewish-American soldiers for a mission behind enemy lines, telling them they each owe him 100 Nazi scalps and will take no prisoners. Their number swells to nine when they learn of Staff Sergeant Hugo Stiglitz, a German soldier who was imprisoned awaiting transfer to Berlin for murdering thirteen Gestapo officers. The Basterds learn the location of the jail he's being held in, kill all the guards and invite Stiglitz to join the Basterds, which he accepts.",
                     "http://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg",
                     "https://www.youtube.com/watch?v=Krithhm1150")

#Put movie objects in an array called movies 
movies = [zero_dark_thirty, shawshank_redemption, schindlers_list, inglorious_bastards, its_a_wonderful_life, airplane]

#Create and open the movies html webpage
fresh_tomatoes.open_movies_page(movies)
