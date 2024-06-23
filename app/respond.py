from google.cloud import texttospeech
from google.cloud.texttospeech import SsmlVoiceGender, AudioEncoding
import os

def generate_response(text):
    return "This is a placeholder response to: " + text

def generate_speech_response(text):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=generate_response(text))
    voice = texttospeech.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=AudioEncoding.LINEAR16
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    response_audio_path = os.path.join(os.getcwd(), 'uploads', 'response.wav')
    with open(response_audio_path, 'wb') as out:
        out.write(response.audio_content)

    return response_audio_path
