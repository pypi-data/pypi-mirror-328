import os
import logging
from facetrackr.config import get_aws_client

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FaceCollection:
    def __init__(self, collection_id="face-collection"):
        self.collection_id = collection_id
        self.client = get_aws_client("rekognition")

    def add_face(self, image_path):
        """
        Adds a face to the AWS Rekognition collection.
        """
        image_name = os.path.splitext(os.path.basename(image_path))[0]

        try:
            with open(image_path, 'rb') as image_file:
                image_bytes = image_file.read()

            response = self.client.index_faces(
                CollectionId=self.collection_id,
                Image={'Bytes': image_bytes},
                ExternalImageId=image_name,
                MaxFaces=1,
                DetectionAttributes=[]
            )

            if response['FaceRecords']:
                logger.info(f"Face added to collection with ExternalImageId: {image_name}")
                return response['FaceRecords'][0]['Face']['FaceId'], image_name
            else:
                logger.warning("No face detected in the provided image.")
                return None, None
        except Exception as e:
            logger.error(f"Error adding face: {e}")
            return None, None
