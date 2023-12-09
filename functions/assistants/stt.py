import whisper


def whisper_speech_rc(path):
    options = {"language": "de"}
    model = whisper.load_model("small")
    res = model.transcribe(path, **options)

    return res["text"]
