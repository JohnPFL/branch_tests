# pylint: disable=trailing-whitespace

"""This class will print artists, albums and songs!"""
class ArtistPrinter:
    """This class will print artists, albums and songs!"""
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def print_artist(artist_dict: dict):
        """This function will print artists in the dictionary!"""
        for artist in artist_dict.keys():
            print(artist)

    @staticmethod
    def print_album(artist_dict: dict):
        """This function will print albums in the dictionary!"""
        for artist in artist_dict.keys():
            for album in artist_dict[artist].keys():
                print(album)
    
    @staticmethod
    def print_songs(artist_dict: dict):
        """This function will print songs in the dictionary!"""
        for artist in artist_dict.keys():
            for album in artist_dict[artist].keys():
                for song in artist_dict[artist][album]:
                    print(song)


if __name__ == '__main__':
    # input variable
    artists = {'Aphex Twin': {'Selected works': ['Xtal', 'Tha', 'Pulsewidth', 'Ageispolis']
                      ,'Selected works II': ['1']}}
    ArtistPrinter().print_songs(artists)
