# Write a function called make_album() that builds a dictionary describing a music album

def make_album(artist, album_name, tracks=""):
    """This will return a dictionary"""
    album= {'artist name': artist, 'album name': album_name}
    return album

dictionary = make_album('andrew bird', 'nonsense')
print(dictionary)

# i'll have to figure out