from pathlib import Path
from pymusicterm.api.ytmusic import SearchResult, YTMusic
from pymusicterm.api.player import MusicPlayer
from pymusicterm.api.downloader import Downloader
from pymusicterm.player.media_control import MediaControl
from pymusicterm.setting import SettingManager
from pymusicterm.api.local import fetch_lyrics_from_folder, fetch_songs_from_folder
from random import shuffle
from pymusicterm.api.lyrics import LyricsDownloader

    
    
class PyMusicTermPlayer:
    def __init__(self, setting: SettingManager, media_control: MediaControl) -> None:
        self.media_control = media_control
        self.setting = setting
        self.music_player = MusicPlayer(self.setting.volume)
        lyrics = LyricsDownloader(self.setting.lyrics_dir)
        self.ytm = YTMusic(lyrics)
        self.downloader = Downloader(self.setting.music_dir)
        self.list_of_downloaded_songs: list[str] = fetch_songs_from_folder(
            self.setting.music_dir
        )
        self.dict_of_lyrics: dict[str, str] = self.map_lyrics_to_song()
        self.dict_of_song_result: dict[str, SearchResult] = {}
        self.current_song_index = 0
    

    def query(self, query: str, filter: str) -> list[SearchResult]:
        """Query the YTMusic API for a song

        Args:
            query (str): the query to search for
            filter (str): the filter to use

        Returns:
            list[SearchSongResult | SearchVideoResult]: the list of the results found
        """
        result = self.ytm.search(query, filter)

        self.dict_of_song_result.clear()
        for song in result:
            self.dict_of_song_result[song.videoId] = song
        return result

    def play_from_ytb(self, video_id: str) -> None:
        """Play a song from the list of results

        Args:
            id (int): the index of the song to play
        """
        song = self.dict_of_song_result[video_id]
        path = self.downloader.download(song)
        self.ytm.get_lyrics(song)
        self.list_of_downloaded_songs = fetch_songs_from_folder(self.setting.music_dir)
        self.list_of_lyrics = self.map_lyrics_to_song()
        self.music_player.load_song(str(path))
        self.music_player.play_song()
        self.media_control.on_playback()

    def play_from_list(self, id: int) -> None:
        """Play a song from the list of downloaded songs

        Args:
            id (int): the index of the song to play
        """
        self.current_song_index = id
        self.list_of_downloaded_songs = fetch_songs_from_folder(self.setting.music_dir)
        self.list_of_lyrics = self.map_lyrics_to_song()
        self.music_player.load_song(self.list_of_downloaded_songs[id])
        self.music_player.play_song()
        self.media_control.on_playback()


    def previous(self) -> None:
        """Play the previous song"""
        if self.current_song_index == 0:
            self.current_song_index = len(self.list_of_downloaded_songs) - 1
        else:
            self.current_song_index -= 1
        self.music_player.load_song(self.list_of_downloaded_songs[self.current_song_index])
        self.music_player.play_song()
        self.media_control.on_playback()


    def next(self) -> None:
        """Play the next song"""
        if self.current_song_index == len(self.list_of_downloaded_songs) - 1:
            self.current_song_index = 0
        else:
            self.current_song_index += 1
        self.music_player.load_song(self.list_of_downloaded_songs[self.current_song_index])
        self.music_player.play_song()
        self.media_control.on_playback()

    def seek(self, time: float = 10) -> None:
        """Seek forward or backward

        Args:
            time (float, optional): The time to seek in seconds. Defaults to 10.
        """
        self.music_player.position += time

    def suffle(self) -> None:
        """Shuffle the list of downloaded songs"""
        shuffle(self.list_of_downloaded_songs)

    def loop_at_end(self) -> bool:
        """Loop at the end"""
        self.music_player.loop_at_end = not self.music_player.loop_at_end
        self.setting.loop = self.music_player.loop_at_end
        return self.music_player.loop_at_end

    def update(self) -> None:
        """Update the player"""
        if self.music_player.loop_at_end:
            return
        if self.music_player.position == 0 and not self.music_player.playing:
            self.next()

    def map_lyrics_to_song(self) -> None:
        """Map the lyrics to the songs"""
        list_of_lyrics: dict[str, str] = {}
        for song in fetch_songs_from_folder(self.setting.music_dir):
            lyric = self.setting.lyrics_dir + f"/{Path(song).stem.removesuffix('.mp3')}.md"
            list_of_lyrics[song] = Path(lyric)
        return list_of_lyrics

    def stop(self) -> None:
        self.music_player.unload_song()

    @property
    def song_length(self) -> float:
        """Get the song length"""
        return self.music_player.song_length

    @property
    def position(self) -> float:
        """Get the current position"""
        return self.music_player.position

    def volume(self, value: float) -> None:
        """Get the volume up"""
        self.music_player.volume += value
        self.media_control.on_volume()
        self.setting.volume = self.music_player.volume

    @property
    def playing(self) -> bool:
        """Get the playing status"""
        return self.music_player.playing

    def pause_song(self) -> None:
        """Pause the song"""
        self.music_player.pause_song()
        self.media_control.on_playpause()

    def resume_song(self) -> None:
        """Resume the song"""
        self.music_player.resume_song()
        self.media_control.on_playpause()