import movie
import sys

# to execute this program
# python main.py
# python -m main

def run(argv):
    m = movie.Movie('Prey', 2022)
    print(m)
    print("args:", argv)

if __name__ == '__main__':
    run(sys.argv)


