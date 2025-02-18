from setuptools import setup, find_packages

setup(
    name="face_auth",
    version="1.1",
    packages=find_packages(),
    install_requires=["face_recognition", "numpy", "dlib"], 
    author="limFakson",
    description="""
    A simple python face authentication library, 
    designed to be used for face authentication in place of the traditional password authentication.
    """,
    author_email="fakeyejoshua2005@gmail.com",
    url="https://github.com/limFakson/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)