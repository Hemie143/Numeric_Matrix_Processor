class Painting:

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def __str__(self):
        return f'"{self.title}" by {self.artist} ({self.year}) hangs in the Louvre.'


new_title = input()
new_artist = input()
new_year = input()
painting = Painting(new_title, new_artist, new_year)
print(painting)
