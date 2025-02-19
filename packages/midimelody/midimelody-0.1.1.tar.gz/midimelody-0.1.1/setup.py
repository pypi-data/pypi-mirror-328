from setuptools import setup, find_packages

setup(
    name="midimelody",
    version="0.1.1",
    description="A MIDI melody generator supporting multiple musical genres",
    provides=['music.fun'],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="JD Curry",
    author_email="jdcurry@gmail.com",
    url="https://github.com/JDCurry/midi-melody-generator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "mido>=1.2.10",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Multimedia :: Sound/Audio :: MIDI",
        "Topic :: Artistic Software"
    ],
    keywords="midi, music, generator, melody, composition",
    project_urls={
        "Homepage": "https://github.com/JDCurry/midi-melody-generator",
        "Repository": "https://github.com/JDCurry/midi-melody-generator.git",
    },
)