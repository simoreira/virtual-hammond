from math import pi, sin

class EffectsProcessor(object):
	def __init__(self, synthesized_data, effect_magnitude, effects = ['none']):
		self.data = synthesized_data
		self.effect_magnitude = effect_magnitude
		self.effects = effects
		self.rate = 44100
		self.effects_mapping = {'percussion': self.percussion,
								'tremolo': self.tremolo,
								'echo': self.echo,
								'none': self.none,
								'distortion': self.distortion,
								'chorus': self.chorus,
								'envelop': self.envelop
								}
		self.samples = self.get_samples(synthesized_data)
		self.frequencies = self.get_frequencies(synthesized_data)
	####################_MAIN FUNCTION_#################
	def process(self):
		data_to_return = []
		for effect in self.effects:
			if effect == 'none':
				data_to_return = self.merge_samples(self.samples)
			else:
				data_to_return = self.effects_mapping[effect](self.effect_magnitude)
		return data_to_return
	####################################################

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

	#####################_EFFECTS_######################
	def none(self):
		output = self.merge_samples(self.samples)
		return output

	#values passed in?!
	def distortion(self):
		output = self.merge_samples(self.samples)

		MAX_VALUE = 2**15 - 1 #32767
		MIN_VALUE = -MAX_VALUE - 1
		effect_magnitude = 3

		for i in range(0, len(output)):
			value = output[i]**effect_magnitude

			if value > MIN_VALUE and value < MAX_VALUE:
				output[i] = value
			elif value > MAX_VALUE:
				output[i] = MAX_VALUE
			elif value < MIN_VALUE:
				output[i] = MIN_VALUE

		return output

	#values passed in?!
	def echo(self):
		output = self.merge_samples(self.samples)

		delay_value = 0.4
		attenuation_factor = 0.8

		#aplicacao do eco
		for i in range(0, len(output)):
			delay = int(i + delay_value*self.rate)

			if(delay < len(output)):
				output[delay] += attenuation_factor*output[i]


		return output

	#values passed in?!
	def tremolo(self):
		output = self.merge_samples(self.samples)

		effect_magnitude = 0.05
		begin = end = 0

		for sample,frequency in zip(self.samples, self.frequencies):

			begin = end + len(sample)
			x = 0
			for i in range(begin, end):
				output[i] += effect_magnitude * sin(2*pi*frequency*x/self.rate) * output[i]
				x += 1

			end = begin
		return output

	#values passed in?!      
	def chorus(self):
		output = self.merge_samples(self.samples)

		begin = end = 0
		effect_magnitude = 10
		freq_variation = [20, 50]

		for sample,frequency in zip(self.samples, self.frequencies):

			begin = end + len(sample)
			freq_to_apply = 1 - ((freq_variation[1]-freq_variation[0])/len(output))

			x=0
			for i in range(0, len(self.samples)):
				output[i] += effect_magnitude * sin(2*pi*freq_to_apply*x/self.rate)
				x+=1

			end = begin

		return output

	def percussion(self):
		output = self.merge_samples(self.samples)

		begin = end = 0
		effect_magnitude = 50
		time = 1
		multiplier = 5

		for sample,frequency in zip(self.samples, self.frequencies):

			begin = end + len(sample)

			if self.silence(sample) or self.samples.index(sample) == 0:
				x = 0
				for i in range(begin, end):
					if(x < time*self.rate):
						output[i] += effect_magnitude*(1-((1.0/(time*self.rate))*x))*sin(2*pi*multiplier*frequency*w/rate)

					x+=1

			end = begin

		return output

	def envelop(self, effect_magnitude):
		pass