import wave
from rtttl_parser import RtttlParser
from synthesizer import Synthesizer
from effects_processor import EffectsProcessor
from struct import pack

class WavGenerator(object):
    def __init__(self, organ_registry, rtttl, effect_magnitude, effects = ['none']):
        self.rtttl_parser = RtttlParser(rtttl)
        self.synthesizer = Synthesizer(self.rtttl_parser.interpret(), organ_registry)
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
    gerador = WavGenerator('888888888','Barbie girl:d=4,o=5,b=125:8g#,8e,8g#,8c#6,a,p,8f#,8d#,8f#,8b,g#,8f#,8e,p,8e,8c#,f#,c#,p,8f#,8e,g#,f#', 3)
    gerador.create("teste_barbie.wav")