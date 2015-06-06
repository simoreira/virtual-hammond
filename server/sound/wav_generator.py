import wave
from rtttl_parser import RtttlParser
from synthesizer import Synthesizer
from effects_processor import EffectsProcessor
from struct import pack

class WavGenerator(object):
    def __init__(self, organ_registry, rtttl, effect_magnitude, effects = ['none']):
        self.expected_result = [
    (0.5625, 1046),
    (0.3750, 1318),
    (0.3750, 1479),
    (0.1875, 1760),
    (0.5625, 1567),
    (0.3750, 1318),
    (0.3750, 1046),
    (0.1875, 880),
    (0.1875, 739),
    (0.1875, 739),
    (0.1875, 739),
    (0.7500, 783),
    (0.1875, 0),
    (0.1875, 0),
    (0.1875, 523),
    (0.1875, 523),
    (0.1875, 739),
    (0.1875, 739),
    (0.1875, 739),
    (0.1875, 783),
    (0.5625, 932),
    (0.1875, 1046),
    (0.1875, 1046),
    (0.1875, 1046),
    (0.3750, 1046)
]
        self.rtttl_parser = RtttlParser(rtttl)
        self.synthesizer = Synthesizer(self.expected_result, organ_registry)
        self.effects_processor = EffectsProcessor(self.synthesizer.synthesize(), effect_magnitude, effects)

    def create(self, filename):
        wav = wave.open(filename, 'w')
        wav.setparams((1, 2, 44100, 0, 'NONE', 'not compressed'))

        data = self.effects_processor.process()

        wav_data = ''
        for v in data:
            wav_data += pack('h', v)

        wav.writeframes(wav_data)
        wav.close()


##__APAGAR
if __name__ == '__main__':
    gerador = WavGenerator('888888888','The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6', 3, ['distortion'])
    gerador.create("teste_simp_distortion.wav")