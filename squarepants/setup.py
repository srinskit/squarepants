from setuptools import setup

try:
    import cv2
finally:
    print("Do install opencv for python")

setup(
    name='squarepants',
    packages=['squarepants'],
    entry_points={
        'console_scripts': [
            'squarepants = squarepants.main:main',
        ]
    },
    install_requires=[]
)
