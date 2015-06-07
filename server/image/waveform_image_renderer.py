import os
import hashlib
import matplotlib.pyplot as plot
from sound.rtttl_parser import RtttlParser

class WaveformImageRenderer(object):
    def __init__(self, rtttl):
        self.rtttl          = rtttl
        self.interpretation = RtttlParser(rtttl).interpret()
        self.durations      = self.get_durations()
        self.frequencies    = self.get_frequencies()

    def md5(self, string):
        return hashlib.md5(string).hexdigest()

    def get_durations(self):
        durations = []

        for element in self.interpretation:
            durations.append(element[0])

        return durations

    def get_frequencies(self):
        frequencies = []

        for element in self.interpretation:
            frequencies.append(element[1])

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

    def md5(self, string):
        return hashlib.md5(string).hexdigest()

    def save(self):
        self.draw()

        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '../storage/wave_form_files/' + self.md5(self.rtttl) + '.png'))
        plot.savefig(filename, bbox_inches = 'tight')
