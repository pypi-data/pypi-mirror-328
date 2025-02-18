from setuptools import setup, find_packages

setup(
    name="footap",
    version="1.6.1",
    author="Dims",
    description="Package d'analyse des touches de balle au football",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "mediapipe==0.10.7",
        "numpy==1.24.3",
        "ultralytics==8.3.69",
        "Pillow==10.1.0",
        "opencv-contrib-python==4.11.0.86",
        "opencv-contrib-python-headless==4.11.0.86",
        "opencv-python==4.11.0.86",
        "torch==2.1.1",
        "torchvision==0.16.1",
    ],
    entry_points={
        'console_scripts': [
            'footap=footap.main:main',
        ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Video :: Capture",
    ],
)
