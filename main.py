import os
from google.cloud import speech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"


def transcribe_audio(file_name):
    client = speech.SpeechClient()

    with open(file_name, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="pl-PL",
        enable_automatic_punctuation=True,
    )

    print(f"Przesyłam plik {file_name} do Google Cloud...")

    try:
        response = client.recognize(config=config, audio=audio)

        for result in response.results:
            print("-" * 20)
            print(f"Rozpoznany tekst: {result.alternatives[0].transcript}")
            print(f"Pewność (0-1): {result.alternatives[0].confidence:.2f}")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        print(
            "Wskazówka: Sprawdź czy sample_rate_hertz w kodzie zgadza się z plikiem audio."
        )


if __name__ == "__main__":
    transcribe_audio("nagranie.wav")
