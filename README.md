# Character Library

**Comprehensive Personality Modeling System for AI Characters**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-beta-orange.svg)]()

A standalone Python package for creating psychologically-grounded AI characters with rich personalities, emotional modeling, skill development, and dynamic relationships.

## Features

### Personality Frameworks
- **Big Five (OCEAN)**: Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism
- **Enneagram**: 9 personality types with core motivations and fears
- **MBTI**: 16 personality types with cognitive functions

### Character Archetypes
12 pre-configured archetypes with unique personalities:
- **The Innovator** - Creative visionary who pushes boundaries
- **The Educator** - Patient teacher who inspires learning
- **The Storyteller** - Wise narrator who connects through stories
- **The Creator** - Artistic visionary who brings beauty to life
- **The Philosopher** - Deep thinker who seeks fundamental truths
- **The Analyst** - Rigorous investigator who pursues truth
- **The Leader** - Charismatic guide who unites and inspires
- **The Moral Guide** - Ethical compass who shows the right path
- **The Humorist** - Witty spirit who brings joy through laughter
- **The Empath** - Compassionate listener who heals through understanding
- **The Builder** - Practical visionary who constructs lasting foundations
- **The Engineer** - Systems thinker who solves complex technical challenges

### Emotional Modeling
- 8 basic emotions (Joy, Trust, Fear, Surprise, Sadness, Disgust, Anger, Anticipation)
- Multi-dimensional emotional states (intensity, valence, arousal)
- Visible emotional expressions and cues
- Emotional transitions and decay

### Relationship Dynamics
- 8 relationship types (Friendship, Mentorship, Rivalry, Romantic, etc.)
- Compatibility analysis between characters
- Relationship strength and trust tracking
- Shared history and conflict management

### Skill Development
- Skill trees with prerequisites and specializations
- Experience-based progression
- Mastery levels (Novice to Grandmaster)
- Skill usage tracking

## Installation

### Basic Installation
```bash
pip install character-library
```

### With Agent Integration (requires hierarchical-memory)
```bash
pip install character-library[agent]
```

### From Source
```bash
git clone https://github.com/luciddreamer/character-library.git
cd character-library
pip install -e .
```

## Quick Start

### Creating a Character

```python
from character_library import CharacterLibrary, CharacterArchetype

# Create character library
library = CharacterLibrary()

# Create a character from an archetype
character = library.create_character(CharacterArchetype.INNOVATOR)

# Access personality traits
print(character.name)  # "Dr. Aria Starweaver"
print(character.big_five.openness)  # 0.9
print(character.enneagram.value)  # "7 - The Enthusiast"
print(character.mbti.value)  # "ENFP - The Campaigner"
```

### Generating Dialogue

```python
# Define context
context = {
    'situation': 'problem_solving',
    'topic': 'designing an innovative AI system'
}

# Generate personality-driven dialogue
response = character.generate_dialogue(context)
print(response)
# "Let's think about this from first principles. We need to understand the root cause.
# But what if we approached it completely differently? That's interesting..."
```

### Emotional Modeling

```python
from character_library import BasicEmotion

# Update emotional state
character.update_emotional_state(
    trigger="breakthrough discovery",
    emotion=BasicEmotion.JOY,
    intensity=0.8,
    duration_minutes=30
)

print(character.current_emotional_state.primary_emotion)  # BasicEmotion.JOY
print(character.current_emotional_state.visible_cues)
# ['smiles', 'bright eyes', 'relaxed posture', 'upturned lips']
```

### Skill Development

```python
# Add a new skill
character.add_skill('creative_thinking', 'cognitive', initial_level=6.0)

# Practice the skill
improvement = character.practice_skill(
    skill_name='creative_thinking',
    difficulty=0.8,
    performance=0.9,
    time_spent=2.0  # 2 hours
)

print(f"Skill improved by {improvement:.2f}")
print(f"New level: {character.get_skill_level('creative_thinking'):.1f}")
```

### Relationship Analysis

```python
# Create another character
other_character = library.create_character(CharacterArchetype.ENGINEER)

# Calculate compatibility
compatibility = character.get_relationship_compatibility(other_character)
print(f"Compatibility: {compatibility:.1%}")  # "Compatibility: 90.0%"

# Add relationship
character.add_relationship(
    target_character_id=other_character.id,
    relationship_type=RelationshipType.FRIENDSHIP,
    initial_strength=compatibility
)
```

## Advanced Usage

### Custom Personality Profiles

```python
from character_library import BigFivePersonality, LuciddreamerCharacter

# Create custom personality
custom_personality = BigFivePersonality(
    openness=0.95,
    conscientiousness=0.7,
    extraversion=0.5,
    agreeableness=0.6,
    neuroticism=0.3
)

# Create character with custom personality
character = LuciddreamerCharacter(
    name="Dr. Nova Star",
    archetype=CharacterArchetype.INNOVATOR,
    big_five=custom_personality
)
```

### Personality Growth

```python
# Simulate personality growth through experiences
character.experience_growth_event(
    growth_type="major_success",
    impact=0.8,
    context={
        "project": "AI breakthrough",
        "recognition": "international"
    }
)

# Personality traits will adjust based on experience
print(f"New openness: {character.big_five.openness:.2f}")
```

### Character Serialization

```python
# Save character to dict
character_dict = character.to_dict()

# Load character from dict
restored_character = LuciddreamerCharacter.from_dict(character_dict)
```

## Integration with Agent Systems

### Optional Agent Integration

The package includes optional agent integration that requires the `hierarchical-memory` package:

```python
# Install with agent support
pip install character-library[agent]

# Create character agent with memory
from character_library import CharacterAgent, AgentRole

agent = CharacterAgent(
    character=character,
    role=AgentRole.CONVERSATION_PARTNER,
    memory_system=memory_system  # HierarchicalMemorySystem instance
)

# Agent can make personality-driven decisions
response = await agent.perceive_and_respond(situation)
```

## Architecture

### Package Structure

```
character_library/
├── core/
│   ├── character.py      # Main character class
│   ├── library.py        # Library management
│   ├── archetypes.py     # Archetype definitions
│   └── skills.py         # Skill system
├── personality/
│   ├── big_five.py       # Big Five model
│   ├── enneagram.py      # Enneagram types
│   └── mbti.py           # MBTI types
├── emotion/
│   └── emotions.py       # Emotional modeling
├── relationships/
│   └── dynamics.py       # Relationship system
└── growth/
    └── evolution.py      # Character development
```

## Documentation

- [Full Documentation](docs/CHARACTER_LIBRARY_INTEGRATION_GUIDE.md)
- [API Reference](docs/api/)
- [Examples](examples/)
- [Character Archetypes](docs/archetypes.md)

## Examples

See the [examples/](examples/) directory for complete working examples:

- `basic_usage.py` - Basic character creation and dialogue
- `emotional_modeling.py` - Emotional state management
- `relationships.py` - Relationship dynamics
- `skill_development.py` - Skill progression
- `character_demo.py` - Comprehensive demonstration

Run the demo:
```bash
python -m character_library.examples.character_demo
```

## Testing

```bash
# Install development dependencies
pip install character-library[dev]

# Run tests
pytest

# Run tests with coverage
pytest --cov=character_library
```

## Performance

- Character creation: <100ms
- Dialogue generation: <200ms
- Compatibility calculation: <50ms
- Skill practice: <10ms

## Requirements

- Python 3.8+
- NumPy 1.20+

### Optional Dependencies

- `hierarchical-memory>=1.0.0` - For agent integration

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

Built as part of the Luciddreamer project for creating psychologically-grounded AI characters.

## Citation

If you use this package in your research, please cite:

```bibtex
@software{character_library,
  title={Character Library: Comprehensive Personality Modeling for AI Characters},
  author={Luciddreamer Team},
  year={2024},
  url={https://github.com/luciddreamer/character-library}
}
```

## Status

This is Tool #3 (9/10 priority) in the Luciddreamer Tool Library - a comprehensive character personality system for AI agents.
