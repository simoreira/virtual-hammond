from math import sin, pi

class Synthesizer(object):
	def __init__(self, interpreter_list, organ_registry):
		self.interpreter_list = interpreter_list
		self.durations = get_durations(interpreter_list)
		self.frequencies = get_frequencies(interpreter_list)
		self.organ_registry = get_organ_registry(organ_registry)

	def get_durations(self, interpreter_list):
		durations = []
		for i in range(0, len(interpreter_list)):
			durations.append(interpreter_list[i][0])	
		return durations

	def get_frequencies(self, interpreter_list):
		frequencies = []
		for i in range(0, len(interpreter_list)):
			frequencies.append(interpreter_list[i][1])	
		return frequencies

	def get_organ_registry(self, organ_registry):
		organ_registry_list = []
		for value in organ_registry:
			organ_registry_list.append(int(value))
		return organ_registry_list

	def synthesize(self, organ_registry_string):
		'''
		Method responsible for producing a sequence of samples
		that will represent the wave form of each note.
		'''

		output_samples = []
		output = []

		for i in range(0, len(interpreter_list)):
			output_samples.append(self.get_samples(organ_reg_int, self.durations[i], self.frequencies[i]))

		normalized_output_samples = self.normalize(output_samples)

		for i in range(0, len(interpreter_list)):
			output.append({'freq': frequencies[i], 'samples': normalized_output_samples[i]})

		return output

	def get_samples(self, org_reg_list, duration, frequency):
		'''
		Method responsible for producing the samples of a note
		taking into consideration the amplitude, duration
		and the frequency.

		Returns a list of the samples of a note.
		'''
		rate = 44100
		data = []
		mult_frequencies = self.get_mult_freq(frequency)

		for i in range(0, int(rate*duration)):
			data.append(self.get_one_sample(org_reg_list, mult_frequencies, rate, i))
		return data

	def get_one_sample(self, org_reg_list, mult_frequencies, rate, i):
		value = 0
		for j in range(0, len(org_reg_list)):
			value += org_reg_list[j]/8 * sin(2*pi*mult_frequencies[j]*i/rate)
		return value

	def get_mult_freq(self, freq):
		values = [1/2.0, 2/3.0 , 1, 2, 3, 4, 5, 6, 8]
		data = []
		for value in values:
			data.append(value*freq)
		data = map(int, data)
		return data

	def normalize(self, data):
		'''
		Method responsible for normalizing the samples.
		'''
		MAX_VALUE = 2 ** 15 - 1  #32767
		maximum = 0

		for k in data:
			for v in k:
				if abs(v) > maximum:
					maximum = abs(v)

		if not maximum == 0:
			normalize_factor = (float(MAX_VALUE)/ maximum)

		normalized_data = []
		tmp = []
		for i in data:
			tmp = []
			for values in i:
				tmp.append(values * normalize_factor)
			normalized_data.append(tmp)
		return normalized_data

if __name__ == "__main__":
	a = Synthesizer()
	b = [8,8,8,8,8,8,8,8,8]
	print(a.get_mult_freq(440))
	print(a.get_samples(b,1,440))