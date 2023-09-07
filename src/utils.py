import os
import re

import music_tag
import torch
import torchaudio
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_voice

PATH_TO_RVC = "Mangio-RVC-Fork/"


def clean_text(text: str, target_len: int = 200, max_len: int = 300) -> list[str]:
    # remove double new line, redundant whitespace, convert non-ascii quotes to ascii quotes
    text = re.sub(r"\n\n+", r"\n", text)
    text = re.sub(r"\s+", r" ", text)
    text = re.sub(r"[“”]", '"', text)

    # split text into sentences, keep quotes together
    sentences = re.split(r'(?<=[.!?])\s+(?=(?:[^"]*"[^"]*")*[^"]*$)', text)

    # recombine sentences into chunks of desired length
    chunks = []
    chunk = ""
    for sentence in sentences:
        if len(chunk) + len(sentence) > target_len:
            chunks.append(chunk)
            chunk = ""
        chunk += sentence + " "
        if len(chunk) > max_len:
            chunks.append(chunk)
            chunk = ""
    if chunk:
        chunks.append(chunk)

    # clean up chunks, remove leading/trailing whitespace, remove empty/unless chunks
    chunks = [s.strip() for s in chunks]
    chunks = [s for s in chunks if s and not re.match(r"^[\s\.,;:!?]*$", s)]

    return chunks


def process_textfile(file_path: str) -> list[str]:
    with open(file_path, "r", encoding="utf-8") as f:
        text = " ".join([l for l in f.readlines()])
    text = clean_text(text)
    return text


def tts(paper_name: str):
    # load tts model
    tts = TextToSpeech(
        autoregressive_model_path="./ai-voice-cloning/training/GlaDOS/finetune/models/5304_gpt.pth"
    )
    voice = "GlaDOS"
    voice_samples, conditioning_latents = load_voice(
        voice, extra_voice_dirs="./ai-voice-cloning/voices"
    )

    # process text file
    texts = process_textfile(f"./llm/scripts/{paper_name}.txt")

    # generate audio for each chunk of text
    all_audio_chunks = []
    for i, text in enumerate(texts):
        gen = tts.tts(
            text=text,
            voice=voice,
            voice_samples=voice_samples,
            conditioning_latents=conditioning_latents,
        )
        torchaudio.save(f"./audio/raw/{i}.wav", gen.squeeze(0).cpu(), 24000)

        all_audio_chunks.append(gen)

    # concatenate all audio chunks
    full_audio = torch.cat(all_audio_chunks, dim=-1)
    torchaudio.save(f"./audio/raw/{paper_name}.wav", full_audio, 24000)


def process_metadata(file_path: str, book_title: str, chapter_no: int, author: str):
    audio = music_tag.load_file(file_path)

    audio["album"] = book_title
    audio["tracknumber"] = chapter_no
    audio["artist"] = author
    audio["title"] = file_path[:-4]

    audio.save()
