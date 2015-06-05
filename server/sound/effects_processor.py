from math import pi, sin

class EffectsProcessor(object):
    def __init__(self, synthesized_data, effects = []):
        self.data = synthesized_data
        self.effects = effects
        self.effects_mapping = {'percussion': self.percussion,
                                'tremolo': self.tremolo,
                                'echo': self.echo,
                                'distortion': self.distortion,
                                'chorus': self.chorus,
                                'envelop': self.envelop
                                }
    
    def process(self):
        data_to_return = []
        for effect in self.effects:
            data_to_return = effects_mapping[effect]()

    def tremolo(self, data, samples):
        effect_magnitude    = 5
        effect_frequency    = 10
        samples_per_seconds = 44100

        for i in samples:
            data.append(effect_magnitude * sin(2*pi*effect_frequency*(i/samples_per_seconds)) * samples[i])

        return data

    def distortion(self, data, samples):
        MAX_VALUE = 2**15 - 1 #32767
        MIN_VALUE = -MAX_VALUE - 1
        effect_magnitude = 5

        for i in samples:
            value = samples[i]**effect_magnitude)
            if value > MIN_VALUE and value < MAX_VALUE:
                data.append(value)
            elif value > MAX_VALUE:
                data.append(MAX_VALUE)
            elif value < MIN_VALUE:
                data.append(MIN_VALUE)

        return data

    def echo(self, data, samples):
        delay_value = 0.1
        attenuation_factor = 0.9

        for i in samples:
            data.append(samples[i]+samples[i]*attenuation_factor)

        return data

    def chorus(self, data, samples):
        example_freq = 15000
        rate = 44100
        for i in samples:
            data.append(samples[i]+sin(2*pi*example_freq*i/rate))

        return data
