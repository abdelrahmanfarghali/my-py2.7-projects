import sometx
import fresh_tomatoes

mission_impossible = sometx.Movie("Mission: Impossible",
								"a mission that is impossible",
								"http://www.gstatic.com/tv/thumb/movies/168920/168920_aa.jpg",
								"https://www.youtube.com/watch?v=wb49-oV0F78")
x_men_the_new_mutants = sometx.Movie("X-MEN: THE NEW MUTANTS",
								"another story about the xmen",
								"http://t2.gstatic.com/images?q=tbn:ANd9GcR3OXGa2wVRnoOiqcnpcpNuQJ7ue5C38JlqOkqnnTZvWa2UVVRk",
								"https://www.youtube.com/watch?v=Qnb2ZdoxbbU")
incredibles_ii = sometx.Movie("Incredibles 2",
								"Incredibles super heroes",
								"http://t0.gstatic.com/images?q=tbn:ANd9GcTBSqU3FQGDEv76GgFdneuZpSQEh0tTupLhoWY8wnWzQoBhA45O",
								"https://www.youtube.com/watch?v=VW3ecQZVnjI")
#print sometx.Movie.__doc__
#print sometx.Movie.__name__
#print sometx.Movie.__module__
#print sometx.Movie.VALID_RATINGS
movies = [mission_impossible,
			x_men_the_new_mutants,
			incredibles_ii]
fresh_tomatoes.open_movies_page(movies)
