import cv2
from deepface import DeepFace

def analyze_image_emotion(image_path):
    # Analyze the emotion in the image using DeepFace
    try:
        # DeepFace can directly analyze an image for emotion
        analysis = DeepFace.analyze(image_path, actions=['emotion'])
        
        # Extract the emotion with the highest confidence
        dominant_emotion = analysis[0]['dominant_emotion']
        confidence = analysis[0]['emotion'][dominant_emotion]
        
        # Output the dominant emotion and its confidence level
        print(f"Dominant Emotion: {dominant_emotion}")
        print(f"Confidence: {confidence:.2f}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    # Provide the path to your image file
    image_path = input("Enter the path to the image: ")
    analyze_image_emotion(image_path)
