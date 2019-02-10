import sys
from twython import Twython
import time
import json
import os
import re
import numpy as np
import sounddevice as sd



sd.default.samplerate = 44100
sd.default.channels = 2
sd.default.device = 1
fs = 44100
duration = 10
# time = 5
# frequency = 420
#
# # Generate time of samples between 0 and two seconds
# samples = np.arange(44100 * time) / 44100.0
# # Recall that a sinusoidal wave of frequency f has formula w(t) = A*sin(2*pi*f*t)
# wave = 10000 * np.sin(2 * np.pi * frequency * samples)
# # Convert it to wav format (16 bits)
# wav_wave = np.array(wave, dtype=np.int16)
#
# sd.play(wav_wave, blocking=False)
# out_wav = np.array(wave)
#
# my_recording = sd.rec(int(time * samples), samplerate=samples, channels=2)
# sd.stop()

myrecording = sd.rec(int(duration * fs))
