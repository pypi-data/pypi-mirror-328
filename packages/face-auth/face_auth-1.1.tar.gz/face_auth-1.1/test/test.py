import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from face_auth.detector import encode_face, compare_faces

def test_encode_face():
    """
    Test the encode_face function
    """
    face_encoding = encode_face("assets/training/elon_musk/161881.jpg")
    
    sign_in_face(face_encoding[0], encode_face("assets/training/elon_musk/161879.jpg"))
    
    
def sign_in_face(registered_face, unknown_face):
    """
    Sign in the face
    """
    if compare_faces(registered_face, unknown_face):
        print("Face recognized")
    
test_encode_face()