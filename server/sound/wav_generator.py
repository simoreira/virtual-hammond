import wave
import os
import hashlib
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

    def md5(self, string):
        return hashlib.md5(string).hexdigest()

    def list_to_string(self, a):
        return ",".join(map(str, a))

    def save(self):
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '../storage/wave_files/' + self.md5(str(self.song_id) + self.registry + self.list_to_string(self.effects)) + '.wav'))
        wav = wave.open(filename, 'w')
        wav.setparams((1, 2, 44100, 0, 'NONE', 'not compressed'))

        data = self.effects_processor.process()

        wav_data = ''
        for v in data:
            wav_data += pack('h', v)

        wav.writeframes(wav_data)
        wav.close()

if __name__ == '__main__':
    wav_generator = WavGenerator(3, '888888888', 'Barbie girl:d=4,o=5,b=125:8g#,8e,8g#,8c#6,a,p,8f#,8d#,8f#,8b,g#,8f#,8e,p,8e,8c#,f#,c#,p,8f#,8e,g#,f#', ['chorus'])
    wav_generator.save()
