

from openai import OpenAI
from pathlib import Path
from playsound import playsound

client = OpenAI(
    api_key="sk-proj-MJUGIJaug79bm61yBTNQT3BlbkFJaTJNmtVw6sPp69qjUNoY"
)

audio_file= open("myrecording.wav", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
)
print(transcription.text)


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are my servant, your name is Jarvis and my name is Master Curtis"},
        {"role": "user", "content": transcription.text}
    ]
)

print(completion.choices[0].message.content)

audioinput = completion.choices[0].message.content

with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        input=audioinput,
) as response:
    response.stream_to_file("speech.mp3")

playsound('speech.mp3')



