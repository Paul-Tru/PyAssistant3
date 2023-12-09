from pydub import AudioSegment


def convert_ogg_to_mp3(ogg_input_path):
    mp3_output_path = ogg_input_path.replace("ogg", "mp3")
    audio = AudioSegment.from_file(ogg_input_path, format="ogg")
    audio.export(mp3_output_path, format="mp3")


def record_audio():
    pass
