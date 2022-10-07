# import data.movie as movie
# => movie.Movie
# import data.movie as mv
# => mv.Movie
from data.movie import Movie
# => Movie
import sys

# to execute this program
# python main.py
# python -m main

def run(argv):
    m = Movie('Prey', 2022)
    print(m)
    print("args:", argv)

if __name__ == '__main__':
    run(sys.argv)


