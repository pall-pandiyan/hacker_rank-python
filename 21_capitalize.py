# Complete the solve function below.
def solve(s):
    for word in s.split():
        s = s.replace(word, word.capitalize())
    return s
