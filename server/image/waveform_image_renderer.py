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
        tmp = 0.0
        point = 0.05

        for duration, frequency in zip(self.durations, self.frequencies):
            end = tmp + duration
            plot.hlines(frequency, tmp, end - point, 'k', linewidth = 4)
            plot.hlines(frequency, end - point, end, 'r', linewidth = 4)
            tmp = end - point

        plot.axis('off')

    def save(self, filename):
        plot.savefig(filename, bbox_inches = 'tight')

if __name__ == '__main__':
    interpretation = [
        (0.5625, 1046),
        (0.3750, 1318),
        (0.3750, 1479),
        (0.1875, 1760),
        (0.5625, 1567),
        (0.3750, 1318),
        (0.3750, 1046),
        (0.1875, 880),
        (0.1875, 739),
        (0.1875, 739),
        (0.1875, 739),
        (0.7500, 783),
        (0.1875, 0),
        (0.1875, 0),
        (0.1875, 523),
        (0.1875, 523),
        (0.1875, 739),
        (0.1875, 739),
        (0.1875, 739),
        (0.1875, 783),
        (0.5625, 932),
        (0.1875, 1046),
        (0.1875, 1046),
        (0.1875, 1046),
        (0.3750, 1046)
    ]

    renderer = WaveformImageRenderer(interpretation)
    renderer.draw()
    renderer.save('test.png')
