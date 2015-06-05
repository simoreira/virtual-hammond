import wave
from sound.rtttl_parser import RtttlParser
from sound.synthesizer import Synthesizer
from sound.effects_processor import EffectsProcessor
from struct import pack

class WavGenerator(object):
    def __init__(self, rtttl, effects = []):
        self.rtttl_parser = RtttlParser(rtttl)
        self.synthesizer = Synthesizer(rtttl_parser.interpret())
        self.effects_processor = EffectsProcessor(synthesizer.synthesize(), effects)

    def create(self, filename):
        wav = wave.open(filename, 'w')
        wav.setparams((1, 2, 44100, 0, 'NONE', 'not compressed'))

        data = effects_processor.process()

        wav_data = ''
        for v in data:
            wav_data += pack('h', v)

        wav.writeframes(wav_data)
        wav.close()

if __name__ == '__main__':
    gerador = WavGenerator('Dragon Ball GT:d=4,o=6,b=140:p,c,c,8a5,8a5,8c,8d,c,a5,a5,g5,a5,a5,8g5,8a5,8a5,a5,g5,f5,e5,p,8d5,8d5,f5,d,f5,8g5,8a5,a5,a5,g5,f5,g5,p,f5,e5,f5')
    gerador.create("teste.wav")