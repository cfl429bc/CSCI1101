import sys

movies = {
    "ANH": "A New Hope",
    "ESB": "The Empire Strikes Back",
    "RotJ": "Return of the Jedi"
    }
filename = "Qzzz_files/q4p6movies.txt"
try:
    with open(filename,"w") as movie_file:
        for init,full in movies.items():
            print(full, end=",")
            print(init, end=",", file=movie_file)
except OSError:
    print(f"Error opening {filename}!")
    sys.exit()