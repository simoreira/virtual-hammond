from sound.synthesizer import Synthesizer

class Synthesizer(object):
	def test_get_mult_freq(self):
		parser = Synthesizer()
		cases = [
			{'frequency': 440, 'results': [220, 293, 440, 880, 1320, 1760, 2200, 2640, 3520]},
			{'frequency': 127, 'results': [63, 84, 127, 254, 381, 508, 635, 762, 1016]},
			{'frequency': 541, 'results': [270, 360, 541, 1082, 1623, 2164, 2705, 3246, 4328]}
		]
		for case in cases:
			assert parser.get_mult_freq(case['frequency']) == case['results']

	def test_get_samples(self):
		