from setuptools import setup, find_packages

setup(
    name="pytinytask",
    version="1.5",
    author="Smart Boy",
    description="A simple macro recording and replaying tool",
    long_description=open('README.md').read(),  # Or .rst if you're using reStructuredText
    long_description_content_type='text/markdown',  # Set to 'text/rst' if you're using reStructuredText
    packages=find_packages(),
    install_requires=[
        "keyboard",
        "mouse",
        "customtkinter"
    ],
    entry_points={
        'console_scripts': [
            'tiny_task = main',
            'tinytask = main',
            'tiny-task = main',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
