from image.waveform_image_renderer import WaveformImageRenderer

class TestWaveformImageRenderer(object):
    INTERPRETATION = [(0.5625, 1046), (0.375, 1318), (0.375, 1479), (0.1875, 1760), (0.5625, 1567), (0.375, 1318), (0.375, 1046), (0.1875, 880), (0.1875, 739), (0.1875, 739), (0.1875, 739), (0.75, 783), (0.1875, 0), (0.1875, 0), (0.1875, 739), (0.1875, 739), (0.1875, 739), (0.1875, 783), (0.5625, 932), (0.1875, 1046), (0.1875, 1046), (0.1875, 1046), (0.375, 1046)]

    def test_get_durations(self):
        renderer = WaveformImageRenderer(self.INTERPRETATION)

        result = renderer.get_durations(self.INTERPRETATION)

        expected_result = [0.5625, 0.375, 0.375, 0.1875, 0.5625, 0.375, 0.375, 0.1875, 0.1875, 0.1875, 0.1875, 0.75, 0.1875, 0.1875, 0.1875, 0.1875, 0.1875, 0.1875, 0.5625, 0.1875, 0.1875, 0.1875, 0.375]

        assert result == expected_result

    def test_get_frequencies(self):
        renderer = WaveformImageRenderer(self.INTERPRETATION)

        result = renderer.get_frequencies(self.INTERPRETATION)

        expected_result = [1046, 1318, 1479, 1760, 1567, 1318, 1046, 880, 739, 739, 739, 783, 0, 0, 739, 739, 739, 783, 932, 1046, 1046, 1046, 1046]

        assert result == expected_result
