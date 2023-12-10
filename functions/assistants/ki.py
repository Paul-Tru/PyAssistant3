import whisper
from gpt4all import GPT4All


def whisper_speech_rc(path):
    options = {"language": "de"}
    model = whisper.load_model("small")
    res = model.transcribe(path, **options)

    return res["text"]


def chat_gpt(question):
    model = GPT4All("wizardlm-13b-v1.2.Q4_0.gguf")  # device='amd', device='intel'
    output = model.generate(question)
    return output
