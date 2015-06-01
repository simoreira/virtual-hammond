from math import sin, pi
import sys

class Synthesizer(object):
	def synthesize(self, organ_registry_string, interpreter_list):
		'''
		Method responsible for producing a sequence of samples
		that will represent the wave form of each note.
		'''
		organ_reg_int = []
		for i in range(0, len(organ_registry_string)):
			tmp = list(organ_registry_string)
			organ_reg_int.append(int(tmp[i]))

		duration = []
		frequencies = []
		output_samples = []
		output = []

		for i in range(0, len(interpreter_list)):
			duration.append(interpreter_list[i][0])
			frequencies.append(interpreter_list[i][1])

		for i in range(0, len(interpreter_list)):
			output_samples.append(get_samples(organ_reg_int, duration[i], frequencies[i]))

		normalized_output_samples = normalize(output_samples)

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
		mult_frequencies = get_mult_freq(frequency)

		for i in range(0, int(rate*duration)):
			data.append(
				(org_reg_list[0]/8 * sin(2*pi*mult_frequencies[0]*i/rate)) +
				(org_reg_list[1]/8 * sin(2*pi*mult_frequencies[1]*i/rate)) +
				(org_reg_list[2]/8 * sin(2*pi*mult_frequencies[2]*i/rate)) +
				(org_reg_list[3]/8 * sin(2*pi*mult_frequencies[3]*i/rate)) +
				(org_reg_list[4]/8 * sin(2*pi*mult_frequencies[4]*i/rate)) +
				(org_reg_list[5]/8 * sin(2*pi*mult_frequencies[5]*i/rate)) +
				(org_reg_list[6]/8 * sin(2*pi*mult_frequencies[6]*i/rate)) +
				(org_reg_list[7]/8 * sin(2*pi*mult_frequencies[7]*i/rate)) +
				(org_reg_list[8]/8 * sin(2*pi*mult_frequencies[8]*i/rate))
			)
		return data

	def get_mult_freq(self, freq):
		values = [1/2.0, 2/3.0 , 1, 2, 3, 4, 5, 6, 8]
		data = []
		for i in range(0, 9):
			data.append(freq*values[i])
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
