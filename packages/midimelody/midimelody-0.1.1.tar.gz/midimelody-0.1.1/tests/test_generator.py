import unittest
from unittest.mock import patch
import os
from midimelody.generator import (
    get_chord_progression,
    create_melodic_pattern,
    get_user_preferences,
    generate_midi
)

class TestMelodyGenerator(unittest.TestCase):
    def test_chord_progression_generation(self):
        # Test for each genre
        for genre in range(1, 9):
            key = 0  # C key
            progression, duration = get_chord_progression(genre, key)
            
            # Basic validation
            self.assertIsInstance(progression, list)
            self.assertIsInstance(duration, int)
            self.assertTrue(len(progression) > 0)
            
            # Check if notes are within MIDI range (0-127)
            for chord in progression:
                for note in chord:
                    self.assertTrue(0 <= note <= 127)

    def test_melodic_pattern_creation(self):
        # Test pattern creation for each genre
        chord_tones = [60, 64, 67]  # C major triad
        scale = [60, 62, 64, 65, 67, 69, 71, 72]  # C major scale
        
        for genre in range(1, 9):
            pattern = create_melodic_pattern(chord_tones, scale, genre)
            
            # Basic validation
            self.assertIsInstance(pattern, list)
            self.assertTrue(len(pattern) > 0)
            
            # Check if notes are within scale or chord tones
            for note in pattern:
                self.assertTrue(note in scale or note in chord_tones)

    @patch('builtins.input', side_effect=['1', '1'])  # Simulates user input: C key, Pop genre
    def test_user_preferences(self, mock_input):
        key_offset, genre = get_user_preferences()
        
        # Validate returned values
        self.assertEqual(key_offset, 0)  # C key (first option)
        self.assertEqual(genre, 1)  # Pop genre (first option)

    @patch('builtins.input', side_effect=['1', '1'])
    def test_midi_file_generation(self, mock_input):
        # Test full MIDI generation
        generate_midi()
        
        # Check if a MIDI file was created
        midi_files = [f for f in os.listdir('.') if f.endswith('.mid')]
        self.assertTrue(len(midi_files) > 0)
        
        # Clean up - remove generated MIDI file
        for midi_file in midi_files:
            os.remove(midi_file)

    def test_genre_specific_patterns(self):
        # Test specific characteristics for each genre
        chord_tones = [60, 64, 67]  # C major triad
        scale = [60, 62, 64, 65, 67, 69, 71, 72]  # C major scale
        
        # Pop/Rock (genre 1)
        pop_pattern = create_melodic_pattern(chord_tones, scale, 1)
        self.assertEqual(len(pop_pattern), 8)  # Check pattern length
        
        # Blues (genre 3)
        blues_pattern = create_melodic_pattern(chord_tones, scale, 3)
        self.assertEqual(len(blues_pattern), 12)  # Blues should have 12-bar pattern
        
        # Electronic (genre 6)
        electronic_pattern = create_melodic_pattern(chord_tones, scale, 6)
        self.assertEqual(len(electronic_pattern), 4)  # Electronic often has shorter patterns

if __name__ == '__main__':
    unittest.main()