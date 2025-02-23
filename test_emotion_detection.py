"""Tests for the service."""
import unittest
from emotion_detection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """Tests suite."""

    def test_emotion_detector_joy(self):
        """Tests joy emotion."""
        result = emotion_detector('I am glad this happened.')
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_emotion_detector_anger(self):
        """Tests anger emotion."""
        result = emotion_detector('I am really mad about this.')
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_emotion_detector_disgust(self):
        """Tests disgust emotion."""
        result = emotion_detector('I feel disgusted just hearing about this.')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_emotion_detector_sadness(self):
        """Tests sadness emotion."""
        result = emotion_detector('I am so sad about this.')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_emotion_detector_fear(self):
        """Tests fear emotion."""
        result = emotion_detector('I am really afraid that this will happen.')
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
