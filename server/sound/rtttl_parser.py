class RtttlParser(object):
    FREQUENCIES = {'a': 27.5, 'a1': 55.0, 'a2': 110.0, 'a3': 220.0, 'a4': 440.0, 'a5': 880.0,'a6': 1760.0, 'a7': 3520.0, 'a8': 7040.0, 
                   'a#': 29.14, 'a#1': 58.27, 'a#2': 116.54, 'a#3': 233.08, 'a#4': 466.16, 'a#5': 932.33, 'a#6': 1864.66,'a#7': 3729.31, 'a#8': 7458.62, 
                   'b': 30.87, 'b1': 61.74, 'b2': 123.47, 'b3': 246.94, 'b4': 493.88, 'b5': 987.77, 'b6': 1975.53, 'b7': 3951.07, 'b8': 7902.13, 
                   'c': 16.35, 'c1': 32.7, 'c2': 65.41, 'c3': 130.81, 'c4': 261.63, 'c5': 523.25, 'c6': 1046.5, 'c7': 2093.0, 'c8': 4186.01, 
                   'c#': 17.32, 'c#1': 34.65,'c#2': 69.3, 'c#3': 138.59, 'c#4': 277.18, 'c#5': 554.37, 'c#6': 1108.73, 'c#7': 2217.46, 'c#8': 4434.92, 
                   'd': 18.35, 'd1': 36.71, 'd2': 73.42, 'd3': 146.83, 'd4': 293.66, 'd5': 587.33, 'd6': 1174.66, 'd7': 2349.32, 'd8': 4698.64, 
                   'd#': 19.45, 'd#1': 38.89, 'd#2': 77.78, 'd#3': 155.56, 'd#4': 311.13, 'd#5': 622.25,'d#6': 1244.51, 'd#7': 2489.02, 'd#8': 4978.03, 
                   'e': 20.6, 'e1': 41.2, 'e2': 82.41, 'e3': 164.81, 'e4': 329.63, 'e5': 659.26, 'e6': 1318.51, 'e7': 2637.02, 'e8': 5274.04, 
                   'f': 21.83, 'f1': 43.65, 'f2': 87.31, 'f3': 174.61, 'f4': 349.23, 'f5': 698.46, 'f6': 1396.91, 'f7': 2793.83, 'f8': 5587.65, 
                   'f#': 23.12, 'f#1': 46.25, 'f#2': 92.5, 'f#3': 185.0, 'f#4': 369.99, 'f#5': 739.99, 'f#6': 1479.98, 'f#7': 2959.96, 'f#8': 5919.91, 
                   'g': 24.5, 'g1': 49.0, 'g2': 98.0, 'g3': 196.0, 'g4': 392.0, 'g5': 783.99, 'g6': 1567.98, 'g7': 3135.96, 'g8': 6271.93, 
                   'g#': 25.96, 'g#1': 51.91, 'g#2': 103.83,'g#3': 207.65, 'g#4': 415.3, 'g#5': 830.61, 'g#6': 1661.22, 'g#7': 3322.44, 'g#8': 6644.88, 
                   'h': 30.87, 'h1': 61.74, 'h2': 123.47, 'h3': 246.94, 'h4': 493.88, 'h5': 987.77, 'h6': 1975.53, 'h7': 3951.07, 'h8': 7902.13, 'p': 0}

    def __init__(self, rtttl):
        self.rtttl = rtttl

    def get_name(self):
        return self.rtttl.split(':')[0]

    def get_defaults(self):
        return self.rtttl.split(':')[1].split(',')

    def get_notes(self):
        return self.rtttl.split(':')[2].split(',')

    def parse(self):
        interpreted_notes = []
        
        name     = self.get_name()
        defaults = self.get_defaults()
        notes    = self.get_notes()

        time = 0

        for note in notes:
            if note[0].isdigit():
                time = int(note[0])

                if note[1].isdigit():
                    time = time*10 + int(note[1])

                duration = (60.0/int(defaults[2][2:]))*(4.0/time)
            else:
                time = int(defaults[0][2:])

                duration = (60.0/int(defaults[2][2:]))*(4.0/int(defaults[0][2:]))

                note = str(time) + note;

            if '.' in note:
                duration = duration*1.5

            note = note.replace('.', '')

            if time > 10:
                frequency = self.FREQUENCIES[note[2:]]
            else:
                frequency = self.FREQUENCIES[note[1:]]

            frequency = int(frequency)

            interpreted_notes.append((duration, frequency))

        return interpreted_notes


if __name__ == '__main__':
    simpsons = "The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6"

    parser = RtttlParser(simpsons)
    pairs = parser.parse()

    print pairs
