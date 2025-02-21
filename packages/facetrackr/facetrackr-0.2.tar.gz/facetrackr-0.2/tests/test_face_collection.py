import unittest
from unittest.mock import patch
from facetrackr.face_collection import FaceCollection

class TestFaceCollection(unittest.TestCase):

    @patch("face_recognition.face_collection.get_aws_client")
    def test_add_face(self, mock_get_client):
        mock_client = mock_get_client.return_value
        mock_client.index_faces.return_value = {
            'FaceRecords': [{'Face': {'FaceId': '12345'}}]
        }

        face_collection = FaceCollection()
        face_id, external_image_id = face_collection.add_face("test.jpg")

        self.assertEqual(face_id, "12345")
        mock_client.index_faces.assert_called_once()

if __name__ == "__main__":
    unittest.main()
