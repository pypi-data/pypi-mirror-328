import cv2
import logging
from facetrackr.config import get_aws_client
from botocore.exceptions import ClientError

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VideoProcessor:
    def __init__(self, collection_id="face-collection"):
        self.collection_id = collection_id
        self.client = get_aws_client("rekognition")

    def process_video(self, video_path, external_image_id):
        """
        Extracts exactly one frame per second from the video and searches for matching faces.
        """
        logger.info(f"Processing video: {video_path}")

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            logger.error("Could not open video file.")
            return {"error": "Could not open video file."}

        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = int(total_frames / fps)  # Duration in seconds
        detected_faces = []

        for second in range(duration):
            # Calculate exact frame number for this second
            frame_number = int(second * fps)
            
            # Set position to exact frame
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            ret, frame = cap.read()
            
            if not ret:
                break

            # Convert frame to bytes
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            _, img_encoded = cv2.imencode('.jpg', frame_rgb)
            img_bytes = img_encoded.tobytes()

            try:
                search_response = self.client.search_faces_by_image(
                    CollectionId=self.collection_id,
                    Image={'Bytes': img_bytes},
                    MaxFaces=1
                )

                if search_response.get("FaceMatches"):
                    matched_face = search_response["FaceMatches"][0]["Face"]
                    detected_external_id = matched_face.get("ExternalImageId", "Unknown")

                    if detected_external_id == external_image_id:
                        detected_faces.append({
                            "timestamp": second,
                            "external_image_id": detected_external_id
                        })
                        logger.info(f"Match found at {second}s")

            except ClientError as e:
                if e.response['Error']['Code'] == 'InvalidParameterException' and 'no faces' in str(e):
                    # Silently skip frames with no faces
                    continue
                else:
                    logger.error(f"AWS error at {second}s: {e}")
            except Exception as e:
                logger.error(f"Unexpected error at {second}s: {e}")

        cap.release()
        logger.info("Video processing completed.")
        return detected_faces