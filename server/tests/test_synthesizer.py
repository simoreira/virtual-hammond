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

	def test_get_organ_reg(self):
		parser = Synthesizer()
		cases = [
			{'organ_registry': '888888888', 'results': [8,8,8,8,8,8,8,8,8]},
			{'organ_registry': '887451269', 'results': [8,8,7,4,5,1,2,6,9]},
			{'organ_registry': '215478456', 'results': [2,1,5,4,7,8,4,5,6]}
		]
		for case in cases:
			assert parser.get_organ_registry(case['organ_registry']) == case['results']

	def test_get_durations(self):
		parser = Synthesizer()
		cases = [
			{'rtttl_parser_data': [(0.5625, 1046), (0.3750, 1318), (0.3750, 1479)], 'results': [0.5625, 0.3750, 0.3750]},
			{'rtttl_parser_data': [(0.4121, 739), (0.0251, 783), (0.5625, 932)], 'results': [0.4121, 0.0251, 0.5625]},
			{'rtttl_parser_data': [(0.1875, 1046), (0.2125, 783), (0.7845, 932)], 'results': [0.1875, 0.2125, 0.7845]}
		]
		for case in cases:
			assert parser.get_durations(case['rtttl_parser_data']) == case['results']

	def test_get_frequencies(self):
		parser = Synthesizer()
		cases = [
			{'rtttl_parser_data': [(0.5625, 1046), (0.3750, 1318), (0.3750, 1479)], 'results': [1046, 1318, 1479]},
			{'rtttl_parser_data': [(0.4121, 739), (0.0251, 452), (0.5625, 932)], 'results': [739, 452, 932]},
			{'rtttl_parser_data': [(0.1875, 1046), (0.2125, 783), (0.7845, 932)], 'results': [1046, 783, 932]}
		]
		for case in cases:
			assert parser.get_frequencies(case['rtttl_parser_data']) == case['results']

	def test_get_samples(self):
		parser = Synthesizer()
		rtttl_parser_data = [(0.5625, 1046), (0.3750, 1318), (0.3750, 1479), (0.1875, 1760), (0.5625, 1567)]
		for value in rtttl_parser_data:
			to_test = parser.get_samples("888888888", value[0], value[1])
			assert len(to_test) == 44100*value[0]
			for x in to_test:
				assert isinstance(x, float)