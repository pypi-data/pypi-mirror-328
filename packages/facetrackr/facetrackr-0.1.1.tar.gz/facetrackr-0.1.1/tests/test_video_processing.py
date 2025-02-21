import unittest
from unittest.mock import patch
from facetrackr.video_processing import VideoProcessor

class TestVideoProcessor(unittest.TestCase):

    @patch("face_recognition.video_processing.get_aws_client")
    def test_process_video(self, mock_get_client):
        mock_client = mock_get_client.return_value
        mock_client.search_faces_by_image.return_value = {
            'FaceMatches': [{'Face': {'ExternalImageId': 'test_face'}}]
        }

        video_processor = VideoProcessor()
        detections = video_processor.process_video("test.mp4", "test_face")

        self.assertIsInstance(detections, list)
        mock_client.search_faces_by_image.assert_called()

if __name__ == "__main__":
    unittest.main()
