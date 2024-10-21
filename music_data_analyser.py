#print options
def print_options():
    print(f"""
    ******Welcome to our spotify analyzer!*****
    
    
    """)

#calculate distance average person could walk while listening ot album
def calculate_walk_distance(album_duration):
    album_seconds = album_duration * 1 #multiply to get seconds
    average_speed = 1.4 #m/s
    distance = album_seconds * average_speed

    return distance




