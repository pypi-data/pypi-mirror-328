# 🎭 Face Recognition with AWS Rekognition

## 📌 Overview
This package enables face detection in videos using **AWS Rekognition**. It allows you to:
- ✅ **Add a face** to an AWS Rekognition Face Collection.
- 🎥 **Analyze a video** and detect occurrences of the face.
- 🕒 **Get timestamps** where the face is detected.

Built using **AWS Rekognition, OpenCV, and Python** for seamless facial recognition.

---

## 🚀 Features
✔️ **AWS Rekognition Integration** – Secure and scalable cloud-based face recognition.  
✔️ **Automated Video Processing** – Extracts frames and detects faces in real-time.  
✔️ **Timestamp-based Reporting** – Returns exact timestamps where a face appears.  
✔️ **Error Handling & Logging** – Structured error management and logging.  

---

## 🔑 AWS Configuration

### **1️⃣ Set Up AWS Credentials**
Make sure your AWS credentials are configured in the environment:
```sh
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_REGION="us-east-2"
```
Or, configure them using AWS CLI:
```sh
aws configure
```

### **2️⃣ Create a Face Collection in AWS Rekognition**
If you haven't created a face collection, run:
```sh
aws rekognition create-collection --collection-id "face-collection" --region us-east-2
```

---

## 📖 Usage

### **Run the Face Recognition Pipeline**
Execute the main script:
```sh
python main.py
```

You'll be prompted to enter:
1️⃣ **Path to the face image**  
2️⃣ **Path to the video file**

The script will:
- Upload the face to AWS Rekognition.
- Process the video and detect the face.
- Return timestamps where the face is found.

---

## 🖥️ Example Usage in Python

```python
from face_recognition.face_collection import FaceCollection
from face_recognition.video_processing import VideoProcessor

# Initialize Face Collection
face_collection = FaceCollection()

# Add a face to AWS Rekognition
face_id, external_image_id = face_collection.add_face("face.jpg")

if face_id:
    print("Face added successfully!")

    # Initialize Video Processor
    video_processor = VideoProcessor()

    # Process video and detect face
    results = video_processor.process_video("video.mp4", external_image_id)
    
    print("Face detected at timestamps:", results)
else:
    print("No face detected in the image.")
```

---

## 🧪 Running Tests
Run unit tests with:
```sh
pytest tests/
```

---

## 🔄 File Structure
```
face_recognition_package/
│── facetrackr/
│   │── __init__.py
│   │── config.py
│   │── face_collection.py
│   │── video_processing.py
│── tests/
│   │── test_face_collection.py
│   │── test_video_processing.py
│── setup.py
│── requirements.txt
│── README.md
│── main.py
```

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🤝 Contributing
Want to improve this project? Fork it and submit a pull request! 🚀  

📩 **Contact**: harsh.langaliya@holbox.ai  
💡 **Author**: Harsh Langaliya
