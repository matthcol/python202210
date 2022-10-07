# import reflix.data.movie as movie
# => movie.Movie
# import reflix.data.movie as mv
# => mv.Movie
from .data.movie import Movie
# => Movie
import sys

# to execute this program
# python -m reflix.main

def run(argv):
    m = Movie('Prey', 2022)
    print(m)
    print("args:", argv)

if __name__ == '__main__':
    run(sys.argv)


