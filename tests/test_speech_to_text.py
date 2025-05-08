import unittest
from speech_to_text import transcribe_audio

class TestSpeechToText(unittest.TestCase):
    def test_transcribe_audio(self):
        result = transcribe_audio('examples/input_audio.wav')
        self.assertIsInstance(result, str)  # Verifica se a transcrição é uma string.

if __name__ == '__main__':
    unittest.main()

