from sound.rtttl_parser import RtttlParser, FREQUENCIES
from image.waveform_image_renderer import WaveformImageRenderer

class TestWaveformImageRenderer:
    def test_frequencies(self):
        assert isinstance(FREQUENCIES, dict)

    def test_parse(self):
        for song in song:
            parser = RtttlParser(song)

            result = parser.interpret()

            expected_result = [
                (0.5625, 1046),
                (0.375, 1318),
                (0.375, 1479),
                (0.1875, 1760),
                (0.5625, 1567),
                (0.375, 1318),
                (0.375, 1046),
                (0.1875, 27),
                (0.1875, 23),
                (0.1875, 23),
                (0.1875, 23),
                (0.75, 24),
                (0.1875, 0),
                (0.1875, 0),
                (0.1875, 23),
                (0.1875, 23),
                (0.1875, 23),
                (0.1875, 24),
                (0.5625, 29),
                (0.1875, 1046),
                (0.1875, 1046),
                (0.1875, 1046),
                (0.375, 1046)
            ]

            assert result == expected_result

    def test_get_name(self):
        for song in songs:
            parser = RtttlParser(song)

            result = parser.get_name()

            expected_result = 'The Simpsons'

            assert result == expected_result

    def test_get_defaults(self):
        parser = RtttlParser(SONGS['simpsons'])

        result = parser.get_defaults()

        expected_result = ['d=4', 'o=5', 'b=160']

        assert result == expected_result

    def test_get_notes(self):
        parser = RtttlParser(SONGS['simpsons'])

        result = parser.get_notes()

        expected_result = ['c.6', 'e6', 'f#6', '8a6', 'g.6', 'e6', 'c6', '8a', '8f#', '8f#', '8f#', '2g', '8p', '8p', '8f#', '8f#', '8f#', '8g', 'a#.', '8c6', '8c6', '8c6', 'c6']

        assert result == expected_result
