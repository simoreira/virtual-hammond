import wave
from sound.effects import Effects
from struct import pack
from math import sin, pi

class WavGenerator(object):
    def __init__(self, filename, tones, rate = 44100, effects = ['none']):
        self.tones    = tones
        self.rate     = rate
        self.effects  = effects

    def create(self, filename):
        wav = wave.open(filename, 'w')
        wav.setparams((1, 2, 44100, 0, 'NONE', 'not compressed'))

        data = []

        for tone in tones:
            if 'none' in effects:
                data = effect_none(data, tone['samples'])

        wav_data = ''
        for v in data:
            wav_data += pack('h', v)

        wav.writeframes(wav_data)
        wav.close()
