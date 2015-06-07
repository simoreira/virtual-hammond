from image.waveform_image_renderer import WaveformImageRenderer

class TestWaveformImageRenderer(object):
    RTTTL = 'The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6'

    def test_get_durations(self):
        renderer = WaveformImageRenderer(self.RTTTL)

        result = renderer.get_durations()

        expected_result = [0.5625, 0.375, 0.375, 0.1875, 0.5625, 0.375, 0.375, 0.1875, 0.1875, 0.1875, 0.1875, 0.75, 0.1875, 0.1875, 0.1875, 0.1875, 0.1875, 0.1875, 0.5625, 0.1875, 0.1875, 0.1875, 0.375]

        assert result == expected_result

    def test_get_frequencies(self):
        renderer = WaveformImageRenderer(self.RTTTL)

        result = renderer.get_frequencies()

        expected_result = [1046, 1318, 1479, 1760, 1567, 1318, 1046, 880, 739, 739, 739, 783, 0, 0, 739, 739, 739, 783, 932, 1046, 1046, 1046, 1046]

        assert result == expected_result
