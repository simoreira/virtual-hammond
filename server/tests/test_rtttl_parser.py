from sound.rtttl_parser import RtttlParser

class TestRtttlParser(object):
    SONG = {
        'rtttl': 'The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6',
        'name': 'The Simpsons',
        'defaults': ['d=4', 'o=5', 'b=160'],
        'notes': ['c.6', 'e6', 'f#6', '8a6', 'g.6', 'e6', 'c6', '8a', '8f#', '8f#', '8f#', '2g', '8p', '8p', '8f#', '8f#', '8f#', '8g', 'a#.', '8c6', '8c6', '8c6', 'c6'],
        'interpretation': [(0.5625, 1046), (0.375, 1318), (0.375, 1479), (0.1875, 1760), (0.5625, 1567), (0.375, 1318), (0.375, 1046), (0.1875, 880), (0.1875, 739), (0.1875, 739), (0.1875, 739), (0.75, 783), (0.1875, 0), (0.1875, 0), (0.1875, 739), (0.1875, 739), (0.1875, 739), (0.1875, 783), (0.5625, 932), (0.1875, 1046), (0.1875, 1046), (0.1875, 1046), (0.375, 1046)]
    }

    def test_frequencies(self):
        assert isinstance(RtttlParser(self.SONG['rtttl']).FREQUENCIES, dict)

    def test_interpret(self):
        parser = RtttlParser(self.SONG['rtttl'])

        result = parser.interpret()

        expected_result = self.SONG['interpretation']

        assert result == expected_result

    def test_get_name(self):
        parser = RtttlParser(self.SONG['rtttl'])

        result = parser.get_name()

        expected_result = self.SONG['name']

        assert result == expected_result

    def test_get_defaults(self):
        parser = RtttlParser(self.SONG['rtttl'])

        result = parser.get_defaults()

        expected_result = self.SONG['defaults']

        assert result == expected_result

    def test_get_notes(self):
        parser = RtttlParser(self.SONG['rtttl'])

        result = parser.get_notes()

        expected_result = self.SONG['notes']

        assert result == expected_result

    def test_get_note_elements(self):
        parser = RtttlParser(self.SONG['rtttl'])

        result = parser.get_note_elements('4c#.7')

        expected_result = ('4', 'c#', '.', '7')

        assert result == expected_result

    def test_get_note_pitch(self):
        parser = RtttlParser(self.SONG['rtttl'])

        result = parser.get_note_pitch('4c#.7')

        expected_result = 'c#'

        assert result == expected_result

    def test_get_note_octave(self):
        parser = RtttlParser(self.SONG['rtttl'])

        result = parser.get_note_octave('4c#.7')

        expected_result = '7'

        assert result == expected_result
