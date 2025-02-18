"""Example script for extracting character profiles from text."""
import logging
from pathlib import Path
import json
from adpa.training.character_style.profile_extractor import ProfileExtractor

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Example text passages for Sherlock Holmes
SHERLOCK_TEXTS = [
    """
    "My name is Sherlock Holmes. It is my business to know what other people do not know."
    Holmes examined the paper carefully with his double-powered lens.
    "The deduction is elementary, my dear Watson. Notice the peculiar chemical composition
    of the ink, combined with the distinctive watermark of the paper manufacturer."
    """,
    """
    "You know my methods, Watson. There was not one of them which I did not apply to the inquiry.
    Three separate times did I make the circuit of the house, and examined the paths leading
    to the road. The ground was dry and hard, but still I gathered evidence of footprints."
    """,
    """
    Sherlock Holmes sat in his leather armchair, his keen eyes focused intently on the
    curious object before him. His fingers, long and sensitive, traced the edges of the
    mysterious package while his mind processed every detail with mathematical precision.
    """
]

# Example text passages for Dr. Watson
WATSON_TEXTS = [
    """
    I had called upon my friend Sherlock Holmes one day in the autumn of last year and found
    him in deep conversation with a very stout, florid-faced, elderly gentleman with fiery red hair.
    As a medical man, I couldn't help but notice the signs of anxiety in our visitor's demeanor.
    """,
    """
    "By Jove, Holmes!" I exclaimed, "This is extraordinary! How could you possibly deduce
    all that from such seemingly trivial details?" As always, I found myself amazed by
    my friend's remarkable powers of observation and analysis.
    """,
    """
    As Holmes's longtime friend and chronicler, I have witnessed countless demonstrations
    of his unique methods. Though I am a medical man by training, I must admit that the
    science of deduction as practiced by Holmes remains somewhat beyond my grasp.
    """
]

def main():
    # Initialize extractor
    extractor = ProfileExtractor()
    
    # Extract profiles
    characters = {
        "Sherlock Holmes": SHERLOCK_TEXTS,
        "Dr. Watson": WATSON_TEXTS
    }
    
    output_dir = Path("extracted_profiles")
    output_dir.mkdir(exist_ok=True)
    
    for character, texts in characters.items():
        logger.info(f"\nExtracting profile for {character}...")
        
        # Extract profile
        profile = extractor.extract_profile(texts, character)
        
        # Save profile
        output_path = output_dir / f"{character.lower().replace(' ', '_')}.json"
        extractor.save_profile(profile, output_path)
        
        # Print profile summary
        logger.info(f"\nProfile for {character}:")
        logger.info(f"Vocabulary Level: {profile['vocabulary_level']}")
        logger.info("Personality Traits:")
        for trait, score in profile['personality'].items():
            logger.info(f"  - {trait}: {score:.2f}")
        logger.info("Speech Patterns:")
        for pattern in profile['speech_patterns'][:3]:
            logger.info(f"  - {pattern}")
        logger.info(f"Tone: {profile['tone']}")
        logger.info(f"Background: {profile['background'][:200]}...")

def create_example_dataset():
    """Create an example dataset from extracted profiles."""
    output_dir = Path("training_data")
    output_dir.mkdir(exist_ok=True)
    
    # Initialize extractor
    extractor = ProfileExtractor()
    
    # Process characters
    dataset = []
    for character, texts in [
        ("Sherlock Holmes", SHERLOCK_TEXTS),
        ("Dr. Watson", WATSON_TEXTS)
    ]:
        # Extract profile
        profile = extractor.extract_profile(texts, character)
        
        # Create training examples
        for text in texts:
            example = {
                "character": character,
                "text": text,
                "profile": profile,
                "style_attributes": {
                    "tone": profile["tone"],
                    "vocabulary_level": profile["vocabulary_level"],
                    "personality": profile["personality"]
                }
            }
            dataset.append(example)
    
    # Save dataset
    with open(output_dir / "character_examples.json", "w") as f:
        json.dump(dataset, f, indent=2)
    
    logger.info(f"Created dataset with {len(dataset)} examples")

if __name__ == "__main__":
    main()
    create_example_dataset()
