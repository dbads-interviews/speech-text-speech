from google.cloud import speech

def transcribe_audio(file_path):
    client = speech.SpeechClient()

    with open(file_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US'
    )

    response = client.recognize(config=config, audio=audio)

    # Collect all transcriptions
    transcripts = []
    for result in response.results:
        transcripts.append(result.alternatives[0].transcript)

    # Join all transcripts into a single string
    full_transcript = ' '.join(transcripts)
    return full_transcript
