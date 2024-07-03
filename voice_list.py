import pyttsx3 as tts


def list_voices():
    engine = tts.init()
    voices = engine.getProperty('voices')
    for idx, voice in enumerate(voices):
        print(f"Voice {idx}: {voice.name} - {voice.id}")

list_voices()
