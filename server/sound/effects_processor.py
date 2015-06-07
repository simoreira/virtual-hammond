from math import pi, sin

class EffectsProcessor(object):
	def __init__(self, synthesized_data, effects = []):
		self.data = synthesized_data
		self.effects = effects
		self.rate = 44100
		self.samples = self.get_samples(synthesized_data)
		self.frequencies = self.get_frequencies(synthesized_data)
		self.effects_mapping = {
			'percussion': self.percussion,
			'tremolo': self.tremolo,
			'echo': self.echo,
			'none': self.none,
			'distortion': self.distortion,
			'chorus': self.chorus,
			'envelop': self.envelop
		}

	def process(self):
		data_to_process = self.merge_samples(self.samples)
		data_to_return = []

		if self.effects == []:
			self.effects = ['none']

		for effect in self.effects:
			data_to_return = self.effects_mapping[effect](data_to_process)

		data_to_return = self.normalize(data_to_return)
		return data_to_return

	def get_samples(self, synthesized_data):
		samples = []
		for data in synthesized_data:
			samples.append(data['samples'])
		return samples

	def get_frequencies(self, synthesized_data):
		frequencies = []
		for data in synthesized_data:
			frequencies.append(data['freq'])
		return frequencies

	def silence(self, data):
		for value in data:
			if value != 0:
				return False
		return True

	def merge_samples(self, samples):
		output = []
		for sample in self.samples:
			output.extend(sample)
		return output

	def normalize(self, data):
		MAX_VALUE = 2 ** 15 - 1  #32767
		maximum_value = 0

		for value in data:
			if abs(value) > maximum_value:
				maximum_value = abs(value)

		if not maximum_value == 0:
			normalize_factor = (float(MAX_VALUE)/ maximum_value)

		normalized_data = []
		for value in data:
			normalized_data.append(value * normalize_factor)

		return normalized_data

	def none(self, data_to_process):
		return data_to_process

	def distortion(self, data_to_process):
		MAX_VALUE = 2**15 - 1 #32767
		MIN_VALUE = -MAX_VALUE - 1
		effect_magnitude = 3

		for i in range(0, len(data_to_process)):
			value = data_to_process[i]**effect_magnitude

			if value > MIN_VALUE and value < MAX_VALUE:
				data_to_process[i] = value
			elif value > MAX_VALUE:
				data_to_process[i] = MAX_VALUE
			elif value < MIN_VALUE:
				data_to_process[i] = MIN_VALUE

		return data_to_process

	def echo(self, data_to_process):
		delay_value = 0.3
		attenuation_factor = 0.5

		# Application of echo
		for i in range(0, len(data_to_process)):
			delay = int(i + delay_value*self.rate)

			if(delay < len(data_to_process)):
				data_to_process[delay] += attenuation_factor*data_to_process[i]


		return data_to_process

	def tremolo(self, data_to_process):
		effect_magnitude = 0.10
		frequency = 10

		size = len(data_to_process)

		for i in xrange(size):
			data_to_process[i] += effect_magnitude * sin(2*pi*frequency*i/self.rate) * data_to_process[i]

		return data_to_process

	def chorus(self, data_to_process):
		begin = end = 0
		effect_magnitude = 10
		freq_variation = [20, 50]

		for sample,frequency in zip(self.samples, self.frequencies):
			end = begin + len(sample)
			for i in xrange(begin, end):
				data_to_process[i] += effect_magnitude * sin(2*pi*(frequency + freq_variation[i%2])*i/self.rate)
			begin = end

		return data_to_process

	def percussion(self, data_to_process):
		begin = end = 0
		effect_magnitude = 100
		time = 1
		multiplier = 10
		was_pause= True;
		for sample,frequency in zip(self.samples, self.frequencies):
			end = begin + len(sample)

			if was_pause:
				x = 0
				for i in range(begin, end):
					if(x < time*self.rate):
						data_to_process[i] += effect_magnitude*(1-((1.0/(time*self.rate))*x))*sin(2*pi*multiplier*frequency*x/self.rate)
					x+=1

				if frequency:
					was_pause = False
				else:
					was_pause = True

			if not frequency:
				was_pause = True
			begin = end

		return data_to_process

	def envelop(self, effect_magnitude):
		pass
