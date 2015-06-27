import wave
import os
from helpers import *
from rtttl_parser import RtttlParser
from synthesizer import Synthesizer
from effects_processor import EffectsProcessor
from struct import pack

class WavGenerator(object):
    def __init__(self, song_id, organ_registry, rtttl, effects = ['none']):
        self.song_id           = song_id
        self.registry          = organ_registry
        self.effects           = effects
        self.rtttl_parser      = RtttlParser(rtttl)
        self.synthesizer       = Synthesizer(self.rtttl_parser.interpret(), organ_registry)
        self.effects_processor = EffectsProcessor(self.synthesizer.synthesize(), effects)

    def save(self):
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '../storage/wave_files/' + md5(str(self.song_id) + self.registry + list_to_csv(self.effects)) + '.wav'))
        wav = wave.open(filename, 'w')
        wav.setparams((1, 2, 44100, 0, 'NONE', 'not compressed'))

        data = self.effects_processor.process()

        wav_data = ''
        for v in data:
            wav_data += pack('h', v)

        wav.writeframes(wav_data)
        wav.close()
