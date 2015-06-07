import re

class RtttlParser(object):
    FREQUENCIES = {'a0': 27, 'a1': 55, 'a2': 110, 'a3': 220, 'a4': 440, 'a5': 880,'a6': 1760, 'a7': 3520, 'a8': 7040, 'a#0': 29, 'a#1': 58, 'a#2': 116, 'a#3': 233, 'a#4': 466, 'a#5': 932, 'a#6': 1864,'a#7': 3729, 'a#8': 7458, 'b0': 30, 'b1': 61, 'b2': 123, 'b3': 246, 'b4': 493, 'b5': 987, 'b6': 1975, 'b7': 3951, 'b8': 7902, 'c0': 16, 'c1': 32, 'c2': 65, 'c3': 130, 'c4': 261, 'c5': 523, 'c6': 1046, 'c7': 2093, 'c8': 4186, 'c#0': 17, 'c#1': 34,'c#2': 69, 'c#3': 138, 'c#4': 277, 'c#5': 554, 'c#6': 1108, 'c#7': 2217, 'c#8': 4434, 'd0': 18, 'd1': 36, 'd2': 73, 'd3': 146, 'd4': 293, 'd5': 587, 'd6': 1174, 'd7': 2349, 'd8': 4698, 'd#0': 19, 'd#1': 38, 'd#2': 77, 'd#3': 155, 'd#4': 311, 'd#5': 622,'d#6': 1244, 'd#7': 2489, 'd#8': 4978, 'e0': 20, 'e1': 41, 'e2': 82, 'e3': 164, 'e4': 329, 'e5': 659, 'e6': 1318, 'e7': 2637, 'e8': 5274, 'f0': 21, 'f1': 43, 'f2': 87, 'f3': 174, 'f4': 349, 'f5': 698, 'f6': 1396, 'f7': 2793, 'f8': 5587, 'f#0': 23, 'f#1': 46, 'f#2': 92, 'f#3': 185, 'f#4': 369, 'f#5': 739, 'f#6': 1479, 'f#7': 2959, 'f#8': 5919, 'g0': 24, 'g1': 49, 'g2': 98, 'g3': 196, 'g4': 392, 'g5': 783, 'g6': 1567, 'g7': 3135, 'g8': 6271, 'g#0': 25, 'g#1': 51, 'g#2': 103,'g#3': 207, 'g#4': 415, 'g#5': 830, 'g#6': 1661, 'g#7': 3322, 'g#8': 6644, 'h0': 30, 'h1': 61, 'h2': 123, 'h3': 246, 'h4': 493, 'h5': 987, 'h6': 1975, 'h7': 3951, 'h8': 7902, 'p0': 0, 'p1': 0, 'p2': 0, 'p3': 0, 'p4': 0, 'p5': 0, 'p6': 0, 'p7': 0, 'p8': 0}

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

    def remove_all_whitespace(self, string):
        return string.replace(" ", "")

    def get_rtttl_parts(self):
        rtttl_parts = self.rtttl.split(':')


        if (len(rtttl_parts) != 3) or (len(rtttl_parts[0]) == 0 or len(rtttl_parts[1]) == 0 or len(rtttl_parts[2]) == 0):
            raise Exception('Invalid RTTTL string.')
        else:
            rtttl_parts[1] = self.remove_all_whitespace(rtttl_parts[1])
            rtttl_parts[2] = self.remove_all_whitespace(rtttl_parts[2])
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

    def all_defaults(self, defaults):
        if len(defaults) < 3:
            if len(defaults) == 1 and defaults[0][0] == 'd':
                defaults.append('o=6')
                defaults.append('b=63')
                return defaults

            if len(defaults) == 1 and defaults[0][0] == 'o':
                defaults[:0] = 'd=4'
                defaults = self.defaults.append('b=63')
                return defaults

            if len(defaults) == 1 and defaults[0][0] == 'b':
               defaults[:0] = 'o=5'
               defaults[:0] = 'd=4'
               return defaults

            if len(defaults) == 2 and defaults[0][0] == 'd' and defaults[1][0] == 'o':
               defaults.append('b=63')
               return defaults

            if len(defaults) == 2 and defaults[0][0] == 'd' and defaults[1][0] == 'b':
               defaults.insert(1, 'o=5')
               return defaults

            if len(defaults) == 2 and defaults[0][0] == 'o' and defaults[1][0] == 'b':
               defaults[:0] = 'd=4'
               return defaults
        return defaults

    def is_valid_defaults(self, defaults):
        defaults = self.all_defaults(defaults)

        duration = defaults[0]
        octave   = defaults[1]
        bpm      = defaults[2]

        if not ((duration[0] == 'd') and (duration[1] == '=') and (duration[2:] in self.ALLOWED_DURATIONS)):
            print 'false duration'
            return False

        if not ((octave[0] == 'o') and (octave[1] == '=') and (octave[2:] in self.ALLOWED_OCTAVES)):
            print 'false octave'
            return False

        if not ((bpm[0] == 'b') and (bpm[1] == '=') and (bpm[2:] in self.ALLOWED_BPM)):
            print 'false bpm'
            return False

        return True

    def get_defaults_duration(self):
        return self.defaults[0][2:]

    def get_defaults_octave(self):
        return self.defaults[1][2]

    def get_defaults_bpm(self):
        return self.defaults[2][2:]

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

        if (duration in self.ALLOWED_DURATIONS) and (octave in self.ALLOWED_OCTAVES) and (pitch in self.ALLOWED_PITCHES):
            return True
        else:
            return False

    def interpret(self):
        name     = self.get_name()
        defaults = self.get_defaults()
        defaults = self.all_defaults(defaults)
        self.defaults = defaults
        notes    = self.get_notes()

        interpretation = []
        time = 0

        if self.is_valid_defaults(defaults):
            for note in notes:
                if self.is_valid_note(note):
                    time = float(self.get_note_duration(note))

                    duration = (60.0/int(defaults[2][2:]))*(4.0/time)

                    if '.' in note:
                        duration *= 1.5
                        note = note.replace('.', '')

                    duration  = round(float(duration), 4)
                    frequency = int(self.FREQUENCIES[str(self.get_note_pitch(note) + self.get_note_octave(note))])

                    interpretation.append((duration, frequency))
                else:
                    raise Exception('Invalid note.')
                    break
        else:
            raise Exception('Invalid defaults')

        return interpretation

if __name__ == '__main__':
    print RtttlParser('Dragon Ball GT:d=4,o=6,b=140:p,c,c,8a5,8a.5,8c,8d,c,a.5,a5,g5,a5,a5,8g5,8a5,8a.5,a5,g5,f5,e5,p,8d5,8d5,f5,d,f5,8g5,8a5,a.5,a5,g5,f5,g5,p,f5,e5,f5').interpret()
