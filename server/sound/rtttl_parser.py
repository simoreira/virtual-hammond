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
        self.rtttl    = rtttl
        self.name     = self.get_name()
        self.defaults = self.get_defaults()
        self.notes    = self.get_notes()

    def get_name(self):
        return self.rtttl.split(':')[0]

    def get_defaults(self):
        return self.rtttl.split(':')[1].split(',')

    def get_notes(self):
        return self.rtttl.split(':')[2].split(',')

    def valid_name(self, name):
        if ':' in name:
            return False
        else:
            return True

    def valid_defaults(self, defaults):
        possible_duration = ['1','2','4','8','16','32']
        possible_octaves = ['1','2','3','4','5','6','7','8']
        possible_bpm = ['25',  '28',  '31',  '35',  '40',  '45',  '50', '56',  '63',  '70',  '80',  '90',  '100', '112', '125', '140', '160', '180', '200', '225', '250','285', '320', '355', '400', '450', '500', '565', '635', '715', '800', '900']

        if defaults[0][0] == 'd' and defaults[0][1] == '=':
            for d in possible_duration:
                if d in defaults[0][2:]:
                    return True  
        else:
            return False 
        
        if defaults[1][0] == 'o' and defaults[1][1] == '=':
            for o in possible_octaves:
                if o in defaults[1][2:]:
                    return True
        else:
            return False
        
        if defaults[2][0] == 'b' and defaults[2][1] == '=':
            for b in possible_bpm:
                if b in defaults[2][2:]:
                    return True
        else:
            return False

    def valid_note(self, note):
        possible_duration = ['1','2','4','8','16','32']
        possible_notes = ['a', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a#', 'a#1', 'a#2', 'a#3', 'a#4', 'a#5', 'a#6', 'a#7', 'a#8', 'b', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c#', 'c#1', 'c#2', 'c#3', 'c#4', 'c#5', 'c#6', 'c#7', 'c#8', 'd', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd#', 'd#1', 'd#2', 'd#3', 'd#4', 'd#5', 'd#6', 'd#7', 'd#8', 'e', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f#', 'f#1', 'f#2', 'f#3', 'f#4', 'f#5', 'f#6', 'f#7', 'f#8', 'g', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g#', 'g#1', 'g#2', 'g#3', 'g#4', 'g#5', 'g#6', 'g#7', 'g#8', 'h', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'p']

        if note[0].isdigit() and not note[1].isdigit():
            if note[0] in possible_duration:
                if note[1:] in possible_notes:
                    return True
            else:
                return False

        if(note[0].isdigit() and note[1].isdigit()): 
            if note[:1] in possible_duration:
                if note[2:] in possible_notes:
                    return True
            else:
                return False
        if note in possible_notes:
            return True
        else:
            return False

    def interpret(self):
        allowed_characters = []
        interpreted_notes = []
        
        name     = self.get_name()
        defaults = self.get_defaults()
        notes    = self.get_notes()

        time = 0

        for note in notes:
            if self.valid_note(note):
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
            else:
                print note
                interpreted_notes = []
                break

        return interpreted_notes

if __name__ == '__main__':
    gt = 'Dragon Ball GT:d=4,o=6,b=140:p,c,c,8a5,8a5,8c,8d,c,a5,a5,g5,a5,a5,8g5,8a5,8a5,a5,g5,f5,e5,p,8d5,8d5,f5,d,f5,8g5,8a5,a5,a5,g5,f5,g5,p,f5,e5,f5'

    parser = RtttlParser(gt)

    print parser.interpret()