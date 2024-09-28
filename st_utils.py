import streamlit as st
import st_audiorec

import speech_recognition as sr

from espeakng import ESpeakNG


def read_input(label, use_stt=False, value="", key=None):
    if(use_stt):
        st.write(label)
        wav_data = st_audiorec.st_audiorec(key=key)
        while(wav_data is None):
            pass
        r = sr.Recognizer()
        if(wav_data is not None):
            open("audio.wav",'wb').write(wav_data)
            with sr.AudioFile("audio.wav") as source:
                audio_data = r.record(source)
                result = r.recognize_whisper_api(audio_data)
                print(result)
                del wav_data
                return result
    else:
        return st.text_input(label, value=value, key=key)


def output_text(text, use_tts=False, key=None):
    if(use_tts):
        engine = ESpeakNG()
        engine.voice='en-us'
        wavs = engine.synth_wav(text)
        
        open("response.wav",'wb').write(wavs)
        st.audio("response.wav", autoplay=True)
#        engine.runandwait()
    else:
        st.write(text, key=key)

