from image_caption import imageCaption
from speech_to_text import speech_to_text
from ask_llm import query_groq_llm
import os
from dotenv import load_dotenv

load_dotenv()

image_path = input("이미지 파일 경로를 입력하세요 (예: image.png): ")
audio_path = input("오디오 파일 경로를 입력하세요 (예: audio.wav): ")

caption = generate_image_caption(image_path)
speech = speech_to_text(audio_path)

response = query_groq_llm(caption, speech)

print("AI 응답:")
print(response)