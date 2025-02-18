import face_recognition
import numpy as np

def face_locations(image):
    return face_recognition.face_locations(image)

def encode_face(image_location: str, model: str = "hog")->list:
    """
    Encode the face in the image
    
    Returns the face encodings of the face in the image
    
    Returns:
        list: list of face encodings numpy arrays

    Args:
        image_location (str): url to the location of the image
        model (str, optional): model Defaults to "hog".
    """
    loaded_image = face_recognition.load_image_file(image_location)
    
    face_locations = face_recognition.face_locations(loaded_image, model=model)
    
    face_encoding = face_recognition.face_encodings(loaded_image, face_locations)
    
    return face_encoding

def compare_faces(known_encodings, unknown_encoding)->bool:
    """
    Compare the face encodings of the known faces with the unknown face encoding

    Args:
        known_encodings (numpy array type): _description_
        unknown_encoding (List): _description_

    Returns:
        boolean: returns True if the face is recognized
    """
    min_distance = float("inf")
    # numpy_val = face_recognition.compare_faces(known_encodings, unknown_encoding)
    
    distance = np.linalg.norm(known_encodings - unknown_encoding)

    if distance < min_distance and distance < 0.6:
        min_distance = distance
        return True 
    
    return False
