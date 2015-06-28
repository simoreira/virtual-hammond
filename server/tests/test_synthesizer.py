from sound.synthesizer import Synthesizer

class TestSynthesizer(object):
    DATA = {
        'rtttl_output' : [(0.5625, 440), (0.375, 541), (0.375, 1479), (0.1875, 1760), (0.5625, 1567)],
        'organ_registry': ['888888888', '887451269', '215478456'],
        'frequencies': [440, 541, 1479, 1760, 1567],
        'durations': [0.5625, 0.375, 0.375, 0.1875, 0.5625],
        'organ_reg_parsed': [[8,8,8,8,8,8,8,8,8], [8,8,7,4,5,1,2,6,9], [2,1,5,4,7,8,4,5,6]],
        'mult_frequencies': [[220, 293, 440, 880, 1320, 1760, 2200, 2640, 3520], [270, 360, 541, 1082, 1623, 2164, 2705, 3246, 4328], [739, 986, 1479, 2958, 4437, 5916, 7395, 8874, 11832], [880, 1173, 1760, 3520, 5280, 7040, 8800, 10560, 14080], [783, 1044, 1567, 3134, 4701, 6268, 7835, 9402, 12536]]
    }

    def test_get_durations(self):
        parser = Synthesizer(self.DATA['rtttl_output'], self.DATA['organ_registry'][0])

        results = parser.get_durations(self.DATA['rtttl_output'])

        assert results == self.DATA['durations']

    def test_get_frequencies(self):
        parser = Synthesizer(self.DATA['rtttl_output'], self.DATA['organ_registry'][0])

        results = parser.get_frequencies(self.DATA['rtttl_output'])

        assert results == self.DATA['frequencies']

    def test_get_organ_reg(self):
        parser = Synthesizer(self.DATA['rtttl_output'], self.DATA['organ_registry'][0])

        results = [parser.get_organ_registry(self.DATA['organ_registry'][0]), parser.get_organ_registry(self.DATA['organ_registry'][1]), parser.get_organ_registry(self.DATA['organ_registry'][2])]

        for i in range(0, len(results)):
            assert results[i] == self.DATA['organ_reg_parsed'][i]

    def test_get_mult_freq(self):
        parser = Synthesizer(self.DATA['rtttl_output'], self.DATA['organ_registry'][0])

        results = []
        for frequency in self.DATA['frequencies']:
            results.append(parser.get_mult_freq(frequency))

        for i in range(0, len(results)):
            assert results[i] == self.DATA['mult_frequencies'][i]

    def test_get_samples(self):
        parser = Synthesizer(self.DATA['rtttl_output'], self.DATA['organ_registry'][0])

        results = parser.synthesize()

        assert len(results) == len(self.DATA['rtttl_output'])

        for value in self.DATA['rtttl_output']:
            results = parser.get_samples(self.DATA['organ_reg_parsed'][0], value[0], value[1])
            assert len(results) == int(44100*value[0])
            for x in results:
                assert isinstance(x, float)
