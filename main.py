from spotiplex import (
connect_plex,
connect_spotify, 
getlidarrlists, 
extract_playlist_id, 
get_playlist_name,
get_spotify_playlist_tracks,
create_list,
check_tracks_in_plex
)

from decouple import config

def main():
    
    # Assuming you have this in your environment variables or settings
    plex = connect_plex()
    sp = connect_spotify()

    try:
        lidarr_playlists = getlidarrlists()

        for playlist in lidarr_playlists:
            try:
                playlist_id = extract_playlist_id(playlist)
                spotify_tracks = get_spotify_playlist_tracks(sp, playlist_id)
                plex_tracks, _ = check_tracks_in_plex(plex, spotify_tracks)
                playlist_name = get_playlist_name(sp, playlist_id)

                create_list(plex, plex_tracks, playlist_name)

                print(f"Processed playlist '{playlist_name}'.")

            except Exception as e:
                print(f"An error occurred processing playlist {playlist}:", e)
                continue  # continue will ensure that the loop proceeds to the next playlist even if an error occurs
    except Exception as playlistfailed:
        print("Grabbing all playlists failed")
        print(playlistfailed)
        


if __name__ == "__main__":
    main()