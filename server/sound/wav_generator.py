import wave
import os
import hashlib
from rtttl_parser import RtttlParser
from synthesizer import Synthesizer
from effects_processor import EffectsProcessor
from struct import pack

class WavGenerator(object):
    def __init__(self, song_id, organ_registry, rtttl, effects = []):
        self.song_id = song_id
        self.rtttl_parser = RtttlParser(rtttl)
        self.synthesizer = Synthesizer(self.rtttl_parser.interpret(), organ_registry)
        self.effects_processor = EffectsProcessor(self.synthesizer.synthesize(), effects)

    def md5(self, string):
        return hashlib.md5(str(string)).hexdigest()

    def save(self):
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '../storage/wave_files/' + self.md5(self.song_id) + '.wav'))
        wav = wave.open(filename, 'w')
        wav.setparams((1, 2, 44100, 0, 'NONE', 'not compressed'))

        data = self.effects_processor.process()

        wav_data = ''
        for v in data:
            wav_data += pack('h', v)

        wav.writeframes(wav_data)
        wav.close()

if __name__ == '__main__':
    wav_generator = WavGenerator(3, '888888888', 'Barbie girl:d=4,o=5,b=125:8g#,8e,8g#,8c#6,a,p,8f#,8d#,8f#,8b,g#,8f#,8e,p,8e,8c#,f#,c#,p,8f#,8e,g#,f#', ['echo', 'tremolo'])
    wav_generator.save()
