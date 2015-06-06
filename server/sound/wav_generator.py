import wave
from rtttl_parser import RtttlParser
from synthesizer import Synthesizer
from effects_processor import EffectsProcessor
from struct import pack

class WavGenerator(object):
    def __init__(self, organ_registry, rtttl, effects = []):
        self.rtttl_parser = RtttlParser(rtttl)
        self.synthesizer = Synthesizer(self.rtttl_parser.interpret(), organ_registry)
        self.effects_processor = EffectsProcessor(self.synthesizer.synthesize(), effects)

    def create(self, filename):
        wav = wave.open(filename, 'w')
        wav.setparams((1, 2, 44100, 0, 'NONE', 'not compressed'))

        data = self.effects_processor.process()


        wav_data = ''
        for v in data:
            for i in v:
                wav_data += pack('h', i)

        wav.writeframes(wav_data)
        wav.close()

if __name__ == '__main__':
    gerador = WavGenerator('888888888','The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6')
    gerador.create("teste_simp.wav")