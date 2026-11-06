class Movies:
    def __init__(self):
        self.movies = []
        return super().__init__()

    def add_movie(self, movie):
        self.movies.append(movie)  

class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Комедии: '{self.movies}'" 

class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: '{self.movies}'"

comedy_obj = Comedy()
print(comedy_obj.add_movie('Большой куш'))

drama_obj = Drama()
print(drama_obj.add_movie('Оружейный барон'))