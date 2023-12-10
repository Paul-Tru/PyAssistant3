from pydub import AudioSegment
import sounddevice as sd
from scipy.io.wavfile import write


def convert_ogg_to_mp3(ogg_input_path):
    mp3_output_path = ogg_input_path.replace("ogg", "mp3")
    audio = AudioSegment.from_file(ogg_input_path, format="ogg")
    audio.export(mp3_output_path, format="mp3")


def record_audio():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)  # Save as WAV file
