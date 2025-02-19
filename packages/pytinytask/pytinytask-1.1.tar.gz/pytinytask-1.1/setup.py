from setuptools import setup, find_packages

setup(
    name="pytinytask",
    version="1.1",
    author="Smart Boy",
    description="A simple macro recording and replaying tool",
    packages=find_packages(),
    install_requires=[
        "keyboard",
        "mouse",
        "customtkinter"
    ],
    entry_points={
        'console_scripts': [
            'tiny_task = tinytask:main',
            'tinytask = tinytask:main',
            'tiny-task = tinytask:main',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
