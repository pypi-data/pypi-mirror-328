"""Example script for training character writing style models."""
import os
from pathlib import Path
import json
import logging

from adpa.training.character_style.trainer import (
    CharacterStyleTrainer,
    CharacterStyleConfig,
    CharacterProfile
)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Example character profiles
CHARACTERS = {
    "sherlock": {
        "name": "Sherlock Holmes",
        "personality": {
            "analytical": 0.9,
            "formality": 0.8,
            "emotion": 0.3
        },
        "vocabulary_level": "academic",
        "speech_patterns": [
            "Elementary, my dear {name}",
            "The game is afoot",
            "When you eliminate the impossible..."
        ],
        "tone": "analytical",
        "background": "Brilliant detective with exceptional deductive reasoning"
    },
    "watson": {
        "name": "Dr. John Watson",
        "personality": {
            "analytical": 0.6,
            "formality": 0.7,
            "emotion": 0.6
        },
        "vocabulary_level": "medical",
        "speech_patterns": [
            "By Jove!",
            "Holmes, this is remarkable",
            "I must admit..."
        ],
        "tone": "formal_narrative",
        "background": "Military doctor and loyal friend to Sherlock Holmes"
    }
}

# Example prompt templates
PROMPT_TEMPLATES = [
    "{name} describes a crime scene: {background}",
    "{name} explains their deduction process: {background}",
    "{name} writes a letter to a friend about recent events",
    "{name} documents a case in their personal journal"
]

def main():
    # Create directories
    base_dir = Path("training_runs/character_style")
    base_dir.mkdir(parents=True, exist_ok=True)
    
    # Configure training
    config = CharacterStyleConfig(
        name="character-gpt",
        description="GPT model fine-tuned for character writing styles",
        base_model="gpt-3.5-turbo",
        training_data_path=str(base_dir / "train.json"),
        character_profiles=CHARACTERS,
        style_attributes=["tone", "vocabulary", "pacing"],
        prompt_templates=PROMPT_TEMPLATES,
        batch_size=4,
        learning_rate=1e-5,
        num_epochs=3,
        consistency_threshold=0.8,
        temperature_range={"min": 0.7, "max": 0.9},
        max_generation_length=1000
    )
    
    # Initialize trainer
    trainer = CharacterStyleTrainer(config)
    
    # Prepare training data
    logger.info("Preparing training data...")
    trainer.prepare_training_data()
    
    # Train model
    logger.info("Starting training...")
    trainer.train()
    
    # Generate example texts
    logger.info("\nGenerating example texts:")
    
    prompt = "Describe the mysterious footprints found in the garden"
    
    for character in ["sherlock", "watson"]:
        logger.info(f"\nGenerating text as {character}:")
        generated_text = trainer.generate_character_text(
            character=character,
            prompt=prompt,
            max_length=500
        )
        
        # Evaluate generation
        metrics = trainer.evaluate_generation(
            generated_text,
            trainer.characters[character]
        )
        
        logger.info("\nEvaluation metrics:")
        for metric, value in metrics.items():
            logger.info(f"{metric}: {value:.4f}")

def create_example_dataset():
    """Create an example dataset for training."""
    dataset = []
    
    # Example writing prompts
    prompts = [
        "Describe the scene at the crime scene",
        "Write about your first impression of {other_character}",
        "Document your thoughts on the current case",
        "Explain your deduction process to {other_character}",
        "Write a letter to Scotland Yard about recent events"
    ]
    
    for char_name, char_data in CHARACTERS.items():
        char = CharacterProfile.from_dict(char_data)
        
        # Generate examples for each prompt
        for prompt in prompts:
            other_char = "Watson" if char_name == "sherlock" else "Holmes"
            formatted_prompt = prompt.replace("{other_character}", other_char)
            
            example = {
                "character": char_name,
                "prompt": formatted_prompt,
                "style_attributes": {
                    "tone": char.tone,
                    "vocabulary_level": char.vocabulary_level,
                    "personality": char.personality
                }
            }
            dataset.append(example)
    
    # Save dataset
    output_dir = Path("data/character_style")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    with open(output_dir / "training_data.json", "w") as f:
        json.dump(dataset, f, indent=2)
    
    logger.info(f"Created example dataset with {len(dataset)} examples")

if __name__ == "__main__":
    create_example_dataset()
    main()
