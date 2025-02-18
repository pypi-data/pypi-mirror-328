"""Test character-based text generation functionality."""
import pytest
from adpa.training.data_generation import DataGenerator, GenerationConfig
from adpa.training.character_style.profile_extractor import ProfileExtractor
from adpa.training.character_style.advanced_analysis import CharacterAnalyzer
import json
import numpy as np
from pathlib import Path

# Test character profile
SHERLOCK_PROFILE = {
    "name": "Sherlock Holmes",
    "personality": {
        "analytical": 0.9,
        "emotional": 0.3,
        "formal": 0.8,
        "creative": 0.7,
        "assertive": 0.9
    },
    "vocabulary_level": "academic",
    "speech_patterns": [
        "elementary, my dear {name}",
        "the game is afoot",
        "when you eliminate the impossible"
    ],
    "tone": "formal_academic",
    "background": "Consulting detective with exceptional deductive abilities"
}

# Test text samples
SHERLOCK_TEXTS = [
    """
    "My name is Sherlock Holmes. It is my business to know what other people don't know."
    Holmes examined the paper carefully with his double-powered lens.
    "The deduction is elementary, my dear Watson. Notice the peculiar chemical composition
    of the ink, combined with the distinctive watermark of the paper manufacturer."
    """,
    """
    "You know my methods, Watson. There was not one of them which I did not apply to the inquiry.
    Three separate times did I make the circuit of the house, and examined the paths leading
    to the road. The ground was dry and hard, but still I gathered evidence of footprints."
    """
]

@pytest.fixture
def generator():
    """Create data generator instance."""
    return DataGenerator(model_name="gpt2-medium", use_gpu=False)

@pytest.fixture
def profile_extractor():
    """Create profile extractor instance."""
    return ProfileExtractor()

@pytest.fixture
def character_analyzer():
    """Create character analyzer instance."""
    return CharacterAnalyzer()

class TestCharacterGeneration:
    """Test character-based text generation."""

    def test_basic_generation(self, generator):
        """Test basic text generation."""
        config = GenerationConfig(num_samples=5)
        samples = generator.generate_character_samples(
            SHERLOCK_PROFILE,
            config
        )
        
        assert len(samples) == 5
        for sample in samples:
            assert len(sample["text"]) > 0
            assert "prompt_type" in sample
            assert "style_attributes" in sample

    def test_style_consistency(self, generator, character_analyzer):
        """Test consistency of generated text with character style."""
        config = GenerationConfig(num_samples=5)
        samples = generator.generate_character_samples(
            SHERLOCK_PROFILE,
            config
        )
        
        for sample in samples:
            # Analyze generated text
            analysis = character_analyzer.analyze_character_evolution(
                [sample["text"]],
                ["2024-01-01"],
                SHERLOCK_PROFILE["name"]
            )
            
            # Check personality consistency
            personality = analysis["behavioral_changes"]["behaviors"][0]
            assert abs(
                personality["analytical"] - SHERLOCK_PROFILE["personality"]["analytical"]
            ) < 0.3

    def test_vocabulary_level(self, generator, profile_extractor):
        """Test vocabulary level of generated text."""
        config = GenerationConfig(num_samples=5)
        samples = generator.generate_character_samples(
            SHERLOCK_PROFILE,
            config
        )
        
        for sample in samples:
            # Extract profile from generated text
            profile = profile_extractor.extract_profile(
                [sample["text"]],
                SHERLOCK_PROFILE["name"]
            )
            
            # Check vocabulary level
            assert profile["vocabulary_level"] == SHERLOCK_PROFILE["vocabulary_level"]

    def test_speech_pattern_preservation(self, generator):
        """Test preservation of character speech patterns."""
        config = GenerationConfig(num_samples=10)
        samples = generator.generate_character_samples(
            SHERLOCK_PROFILE,
            config
        )
        
        # Check if some samples contain characteristic phrases
        pattern_found = False
        for sample in samples:
            text = sample["text"].lower()
            for pattern in SHERLOCK_PROFILE["speech_patterns"]:
                if pattern.lower() in text:
                    pattern_found = True
                    break
            if pattern_found:
                break
        
        assert pattern_found

    def test_profile_extraction(self, profile_extractor):
        """Test profile extraction from text samples."""
        profile = profile_extractor.extract_profile(
            SHERLOCK_TEXTS,
            SHERLOCK_PROFILE["name"]
        )
        
        assert profile["name"] == SHERLOCK_PROFILE["name"]
        assert "personality" in profile
        assert "vocabulary_level" in profile
        assert "speech_patterns" in profile
        
        # Check personality traits
        assert abs(
            profile["personality"]["analytical"] -
            SHERLOCK_PROFILE["personality"]["analytical"]
        ) < 0.3

    def test_character_evolution(self, character_analyzer):
        """Test character evolution analysis."""
        evolution = character_analyzer.analyze_character_evolution(
            SHERLOCK_TEXTS,
            ["2024-01-01", "2024-01-02"],
            SHERLOCK_PROFILE["name"]
        )
        
        assert "sentiment_trajectory" in evolution
        assert "vocabulary_evolution" in evolution
        assert "emotional_arcs" in evolution
        assert "interaction_patterns" in evolution
        assert "behavioral_changes" in evolution

    @pytest.mark.parametrize("prompt_type", ["dialogue", "monologue", "action"])
    def test_different_prompt_types(self, generator, prompt_type):
        """Test generation with different prompt types."""
        config = GenerationConfig(num_samples=3)
        samples = generator.generate_character_samples(
            SHERLOCK_PROFILE,
            config
        )
        
        type_samples = [s for s in samples if s["prompt_type"] == prompt_type]
        assert len(type_samples) > 0

    def test_error_handling(self, generator):
        """Test handling of invalid profiles."""
        invalid_profile = {
            "name": "Invalid Character"
            # Missing required fields
        }
        
        with pytest.raises(ValueError):
            generator.generate_character_samples(
                invalid_profile,
                GenerationConfig(num_samples=1)
            )

    def test_batch_generation(self, generator):
        """Test batch generation of samples."""
        config = GenerationConfig(num_samples=20)
        samples = generator.generate_character_samples(
            SHERLOCK_PROFILE,
            config
        )
        
        assert len(samples) == 20
        
        # Check batch consistency
        vocab_levels = [s["style_attributes"]["vocabulary_level"] for s in samples]
        assert len(set(vocab_levels)) <= 3  # Should be fairly consistent

    def test_generation_reproducibility(self, generator):
        """Test reproducibility of generation with same seed."""
        config = GenerationConfig(num_samples=5)
        
        # Generate two batches with same seed
        np.random.seed(42)
        samples1 = generator.generate_character_samples(
            SHERLOCK_PROFILE,
            config
        )
        
        np.random.seed(42)
        samples2 = generator.generate_character_samples(
            SHERLOCK_PROFILE,
            config
        )
        
        # Compare generated texts
        for s1, s2 in zip(samples1, samples2):
            assert s1["text"] == s2["text"]
