import matplotlib.pyplot as plot

class WaveformImageRenderer(object):
    def __init__(self, interpretations):
        self.durations   = self.get_durations(interpretations)
        self.frequencies = self.get_frequencies(interpretations)

    def get_durations(self, interpretations):
        durations = []

        for interpretation in interpretations:
            durations.append(interpretation[0])

        return durations

    def get_frequencies(self, interpretations):
        frequencies = []

        for interpretation in interpretations:
            frequencies.append(interpretation[1])

        return frequencies

    def draw(self):
        plot.plot(self.durations, self.frequencies, 'ro')

    def save(self, filename):
        plot.savefig(filename)
