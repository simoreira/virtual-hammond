import re

class RtttlParser(object):
    FREQUENCIES = {'a0': 27, 'a1': 55, 'a2': 110, 'a3': 220, 'a4': 440, 'a5': 880,'a6': 1760, 'a7': 3520, 'a8': 7040, 'a#0': 29, 'a#1': 58, 'a#2': 116, 'a#3': 233, 'a#4': 466, 'a#5': 932, 'a#6': 1864,'a#7': 3729, 'a#8': 7458, 'b0': 30, 'b1': 61, 'b2': 123, 'b3': 246, 'b4': 493, 'b5': 987, 'b6': 1975, 'b7': 3951, 'b8': 7902, 'c0': 16, 'c1': 32, 'c2': 65, 'c3': 130, 'c4': 261, 'c5': 523, 'c6': 1046, 'c7': 2093, 'c8': 4186, 'c#0': 17, 'c#1': 34,'c#2': 69, 'c#3': 138, 'c#4': 277, 'c#5': 554, 'c#6': 1108.73, 'c#7': 2217.46, 'c#8': 4434.92, 'd0': 18.35, 'd1': 36.71, 'd2': 73.42, 'd3': 146.83, 'd4': 293.66, 'd5': 587.33, 'd6': 1174.66, 'd7': 2349.32, 'd8': 4698.64, 'd#0': 19.45, 'd#1': 38.89, 'd#2': 77.78, 'd#3': 155.56, 'd#4': 311.13, 'd#5': 622.25,'d#6': 1244.51, 'd#7': 2489.02, 'd#8': 4978.03, 'e0': 20.60, 'e1': 41.20, 'e2': 82.41, 'e3': 164.81, 'e4': 329.63, 'e5': 659.26, 'e6': 1318.51, 'e7': 2637.02, 'e8': 5274.04, 'f0': 21.83, 'f1': 43.65, 'f2': 87.31, 'f3': 174.61, 'f4': 349.23, 'f5': 698.46, 'f6': 1396.91, 'f7': 2793.83, 'f8': 5587.65, 'f#0': 23.12, 'f#1': 46.25, 'f#2': 92.50, 'f#3': 185.00, 'f#4': 369.99, 'f#5': 739.99, 'f#6': 1479.98, 'f#7': 2959.96, 'f#8': 5919.91, 'g0': 24.50, 'g1': 49.00, 'g2': 98.00, 'g3': 196.00, 'g4': 392.00, 'g5': 783.99, 'g6': 1567.98, 'g7': 3135.96, 'g8': 6271.93, 'g#0': 25.96, 'g#1': 51.91, 'g#2': 103.83,'g#3': 207.65, 'g#4': 415.30, 'g#5': 830.61, 'g#6': 1661.22, 'g#7': 3322.44, 'g#8': 6644.88, 'h0': 30.87, 'h1': 61.74, 'h2': 123.47, 'h3': 246.94, 'h4': 493.88, 'h5': 987.77, 'h6': 1975.53, 'h7': 3951.07, 'h8': 7902.13, 'p0': 0, 'p1': 0, 'p2': 0, 'p3': 0, 'p4': 0, 'p5': 0, 'p6': 0, 'p7': 0, 'p8': 0}

    ALLOWED_DURATIONS = ['', '1', '2', '4', '8', '16', '32']
    ALLOWED_OCTAVES   = ['', '0', '1', '2', '3', '4', '5', '6', '7', '8']
    ALLOWED_BPM       = ['25', '28', '31', '35', '40', '45', '50', '56', '63', '70', '80', '90', '100', '112', '125', '140', '160', '180', '200', '225', '250','285', '320', '355', '400', '450', '500', '565', '635', '715', '800', '900']
    ALLOWED_PITCHES   = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b', 'h', 'p']

    def __init__(self, rtttl):
        self.rtttl       = rtttl
        self.rtttl_parts = self.get_rtttl_parts()
        self.name        = self.get_name()
        self.defaults    = self.get_defaults()
        self.notes       = self.get_notes()

    def get_rtttl_parts(self):
        rtttl_parts = self.rtttl.split(':')

        if (len(rtttl_parts) != 3) or (len(rtttl_parts[0]) == 0 or len(rtttl_parts[1]) == 0 or len(rtttl_parts[2]) == 0):
            raise Exception('Invalid RTTTL string.')
        else:
            return rtttl_parts

    def get_name(self):
        return self.rtttl_parts[0]

    def get_defaults(self):
        return self.rtttl_parts[1].split(',')

    def get_notes(self):
        return self.rtttl_parts[2].split(',')

    def is_valid_name(self, name):
        if ':' in name:
            return False
        else:
            return True

    def is_valid_defaults(self, defaults):
        duration = defaults[0]
        octave   = defaults[1]
        bpm      = defaults[2]

        if not ((duration[0] == 'd') and (duration[1] == '=') and (duration[2:] in self.ALLOWED_DURATIONS)):
            print 'false duration'
            return False

        if not ((octave[0] == 'o') and (octave[1] == '=') and (octave[2] in self.ALLOWED_OCTAVES)):
            print 'false octave'
            return False

        if not ((bpm[0] == 'b') and (bpm[1] == '=') and (bpm[2:] in self.ALLOWED_BPM)):
            print 'false bpm'
            return False

        return True

    def get_defaults_duration(self):
        return self.get_defaults()[0][2:]

    def get_defaults_octave(self):
        return self.get_defaults()[1][2]

    def get_defaults_bpm(self):
        return self.get_defaults()[2][2:]

    def get_note_elements(self, note):
        return re.findall(r'^(\d{0,2})([pbeh]|[cdfga]#?)(\.?)(\d?)$', note)[0]

    def get_note_duration(self, note):
        return self.get_note_elements(note)[0] or self.get_defaults_duration()

    def get_note_pitch(self, note):
        return self.get_note_elements(note.replace('.', ''))[1]

    def get_note_octave(self, note):
        return self.get_note_elements(note.replace('.', ''))[3] or self.get_defaults_octave()

    def is_valid_note(self, note):
        duration = self.get_note_duration(note)
        octave   = self.get_note_octave(note)
        pitch    = self.get_note_pitch(note)

        if not ((duration in self.ALLOWED_DURATIONS) or (octave in self.ALLOWED_OCTAVES) or (pitch in self.ALLOWED_PITCHES)):
            return False
        else:
            return True

    def interpret(self):
        name     = self.get_name()
        defaults = self.get_defaults()
        notes    = self.get_notes()

        interpretation = []
        time = 0

        for note in notes:
            if self.is_valid_note(note):
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
                    duration *= 1.5

                note = note.replace('.', '')

                frequency = self.FREQUENCIES[self.get_note_pitch(note)+self.get_note_octave(note)]

                duration  = float(duration)
                frequency = int(frequency)

                interpretation.append((duration, frequency))
            else:
                raise Exception('Invalid note.')
                break

        return interpretation

if __name__ == '__main__':
    song = 'The Simpsons:d=4213,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6'

    parser = RtttlParser(song)

    print parser.interpret()
