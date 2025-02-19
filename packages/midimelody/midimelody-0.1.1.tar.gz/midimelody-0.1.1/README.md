# Musical MIDI Generator

A Python-based MIDI melody generator that creates musical compositions across different genres with sophisticated chord progressions, melodic patterns, and basslines.

## Features

- Multiple genre support including:
  - Pop/Rock
  - Jazz
  - Blues
  - Latin
  - Folk/Acoustic
  - Electronic
  - Epic/Film Score
  - R&B/Soul
- Intelligent chord progression generation based on genre
- Dynamic melody creation with genre-specific patterns
- Accompanying bassline generation
- Support for different musical keys
- Multi-track MIDI output (melody, chords, and bass)
- Genre-appropriate rhythmic patterns
- Verse and chorus section generation

## Installation

You can install this package in two ways:

### 1. Using pip (Recommended)
```bash
pip install --index-url https://maven.pkg.github.com/JDCurry/midi-melody-generator/ midimelody
```

### 2. From source
```bash
git clone https://github.com/JDCurry/midi-melody-generator.git
cd midi-melody-generator
pip install -e .
```

## Usage

### As a Python Package
```python
from midimelody import generate_midi

# Generate a new MIDI composition
generate_midi()
```

### From Command Line
If installed from source, you can run directly:
```bash
python melody_generator.py
```

Follow the interactive prompts to:
1. Select a musical key (C, C#/Db, D, etc.)
2. Choose a genre
3. The program will generate a MIDI file with a unique name in your current directory

## How It Works

The generator creates music in three layers:

1. **Chord Progression**: Genre-specific chord progressions that form the harmonic foundation
2. **Melody**: Intelligent melody generation that follows chord tones and scale degrees
3. **Bassline**: Complementary bass patterns that match the genre and harmony

Each genre has its own characteristics:
- Pop/Rock: Standard chord progressions with catchy melodic patterns
- Jazz: Sophisticated harmony with extended chords
- Blues: Traditional 12-bar patterns with blue notes
- Latin: Syncopated rhythms and specific harmonic movements
- Folk: Simple, traditional progressions
- Electronic: Modern, repetitive patterns
- Epic/Film Score: Dramatic progressions and wide melodic ranges
- R&B/Soul: Soulful progressions with rhythmic emphasis

## Development

### Setting up for development

1. Clone the repository:
```bash
git clone https://github.com/JDCurry/midi-melody-generator.git
cd midi-melody-generator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -e ".[dev]"
```

### Running Tests
```bash
python -m unittest tests/test_generator.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Areas for Improvement

- Additional genres and sub-genres
- More sophisticated rhythm generation
- User interface improvements
- Additional instrument tracks
- Custom tempo support
- Scale mode options (minor, dorian, etc.)
- MIDI file naming conventions
- Export options for different file formats

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built using the [Mido](https://mido.readthedocs.io/) library for MIDI file handling
- Inspired by music theory and common chord progressions across different genres

---

# LICENSE

MIT License

Copyright (c) 2025 JD Curry

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

# .gitignore

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Generated MIDI files
*.mid

# Virtual Environment
venv/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
