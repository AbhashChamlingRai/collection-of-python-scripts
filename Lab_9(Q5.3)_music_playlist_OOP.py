"""
5.3 
Briefly describe a possible collection of classes that can be used to represent a music collection
(for example, inside a music player), focusing on how they would be related using aggregation
only or combination between aggregation and weak association. You should include classes for
songs, artists and playlists. Hint: write down the three class names, draw a line between each pair
of classes which youthink should have a relationship, and decide what kind of relationship would
be the most appropriate.
For simplicity, you can assume that any song has a single “artist”, and the “playlists” can contain
multiple songs. Before you start your coding, you need to identify the attributes and methods
needed for each class. For example, the song class will need to store information about the artist
name, song title and time duration of the song. The Playlist class should contain a method that
prints the song titles of all songs it contains. Once you defined the necessary classes, you need to
initialise the necessary objects to test the functionalities of your code.
"""

class Artist:
    def __init__(self, artist_name):
        self.__artist_name = artist_name

    def get_artist_name(self):
        return self.__artist_name
    def set_artist_name(self, new_artist_name):
        self.__artist_name = new_artist_name


class Song:
    def __init__(self, artist_object, song_title, time_duration):
        self.__artist_object = artist_object
        self.__song_title = song_title
        self.__time_duration = time_duration
    
    def get_song_artist_name(self):
        return self.__artist_object.get_artist_name()
    def set_song_artist_name(self, new_name):
        self.__artist_object.set_artist_name(new_name)
        
    def get_song_title(self):
        return self.__song_title
    def set_song_title(self, new_song_title):
        self.__song_title = new_song_title

    def get_time_duration(self):
        return self.__time_duration
    def set_time_duration(self, new_time_duration):
        self.__time_duration = new_time_duration


class Playlist:
    def __init__(self, playlist_name):
        self.__playlist_name = playlist_name
        self.__all_songs_objects = []
        print(f"\n'{self.__playlist_name}' playlist created.")

    def print_songs(self):
        print("\nPrinting playlist information:")
        for count, song in enumerate(self.__all_songs_objects):
            print(f"\n{count+1}.\nArtist Name: {song.get_song_artist_name()}\nSong title: {song.get_song_title()}\nSong duration: {song.get_time_duration()}")
    
    def add_song(self, song_object):
        self.__all_songs_objects.append(song_object)
        print(f"\n'{song_object.get_song_title()}' added to the playlist '{self.__playlist_name}'.")



def main():

    artist1 = Artist("Adele")
    song1 = Song(artist1, "Hello", 4.55)

    artist2 = Artist("Ed Sheeran")
    song2 = Song(artist2, "Shape of you", 4.2)

    playlist = Playlist("My Favourite songs")

    playlist.add_song(song1)
    playlist.print_songs()

    playlist.add_song(song2)
    playlist.print_songs()


if __name__ == "__main__":
    main()