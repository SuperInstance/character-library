#!/usr/bin/env python3
"""
Basic Character Library Usage Example

This example demonstrates the core features of the character library:
- Creating characters from archetypes
- Generating personality-driven dialogue
- Managing emotional states
- Developing skills
- Building relationships
"""

from character_library import (
    CharacterLibrary,
    CharacterArchetype,
    BasicEmotion,
    RelationshipType
)


def main():
    """Demonstrate basic character library features"""

    print("=" * 70)
    print("Character Library - Basic Usage Example")
    print("=" * 70)

    # Initialize the character library
    library = CharacterLibrary()

    # Create characters from different archetypes
    print("\n1. Creating Characters")
    print("-" * 70)

    innovator = library.create_character(CharacterArchetype.INNOVATOR)
    print(f"Created: {innovator.name}")
    print(f"  Archetype: {innovator.archetype.value}")
    print(f"  Openness: {innovator.big_five.openness:.2f}")
    print(f"  Skills: {', '.join(list(innovator.skills.keys())[:3])}")

    educator = library.create_character(CharacterArchetype.EDUCATOR)
    print(f"\nCreated: {educator.name}")
    print(f"  Archetype: {educator.archetype.value}")
    print(f"  Agreeableness: {educator.big_five.agreeableness:.2f}")

    empath = library.create_character(CharacterArchetype.EMPATH)
    print(f"\nCreated: {empath.name}")
    print(f"  Archetype: {empath.archetype.value}")
    print(f"  Empathy: {empath.big_five.agreeableness:.2f}")

    # Generate personality-driven dialogue
    print("\n2. Generating Dialogue")
    print("-" * 70)

    context = {
        'situation': 'problem_solving',
        'topic': 'designing an innovative educational system'
    }

    print(f"\nScenario: {context['situation']} - {context['topic']}\n")

    print(f"{innovator.name}:")
    print(f"  '{innovator.generate_dialogue(context)}'")

    print(f"\n{educator.name}:")
    print(f"  '{educator.generate_dialogue(context)}'")

    print(f"\n{empath.name}:")
    print(f"  '{empath.generate_dialogue(context)}'")

    # Emotional modeling
    print("\n3. Emotional Modeling")
    print("-" * 70)

    print(f"\n{innovator.name}'s emotional state:")
    print(f"  Primary emotion: {innovator.current_emotional_state.primary_emotion.value}")
    print(f"  Intensity: {innovator.current_emotional_state.intensity:.1%}")
    print(f"  Valence: {innovator.current_emotional_state.valence:+.1f}")

    # Update emotional state
    innovator.update_emotional_state(
        trigger="breakthrough discovery",
        emotion=BasicEmotion.JOY,
        intensity=0.8,
        duration_minutes=30
    )

    print(f"\nAfter breakthrough discovery:")
    print(f"  Primary emotion: {innovator.current_emotional_state.primary_emotion.value}")
    print(f"  Intensity: {innovator.current_emotional_state.intensity:.1%}")
    print(f"  Visible cues: {', '.join(innovator.current_emotional_state.visible_cues[:3])}")

    # Skill development
    print("\n4. Skill Development")
    print("-" * 70)

    skill_name = 'creative_thinking'
    initial_level = innovator.get_skill_level(skill_name)
    print(f"\n{innovator.name}'s {skill_name} level: {initial_level:.1f}")

    # Practice the skill
    improvement = innovator.practice_skill(
        skill_name=skill_name,
        difficulty=0.8,
        performance=0.9,
        time_spent=2.0
    )

    new_level = innovator.get_skill_level(skill_name)
    print(f"  Practiced for 2 hours with 90% performance")
    print(f"  Improvement: {improvement:.3f}")
    print(f"  New level: {new_level:.1f}")

    # Relationship dynamics
    print("\n5. Relationship Dynamics")
    print("-" * 70)

    compatibility = innovator.get_relationship_compatibility(educator)
    print(f"\nCompatibility between {innovator.name} and {educator.name}:")
    print(f"  {compatibility:.1%}")

    # Create relationship
    innovator.add_relationship(
        target_character_id=educator.id,
        relationship_type=RelationshipType.FRIENDSHIP,
        initial_strength=compatibility
    )

    print(f"\nRelationship established: {RelationshipType.FRIENDSHIP.value}")
    print(f"  Initial strength: {compatibility:.1%}")

    # Simulate interaction
    innovator.update_relationship(
        target_character_id=educator.id,
        interaction_type="collaborative brainstorming",
        impact=0.05  # Positive interaction
    )

    relationship = innovator.relationships[educator.id]
    print(f"  Strength after interaction: {relationship.strength:.1%}")

    # Library statistics
    print("\n6. Library Statistics")
    print("-" * 70)

    stats = library.get_library_statistics()
    print(f"\nTotal characters: {stats['total_characters']}")
    print(f"Total skills across all characters: {stats['total_skills_developed']}")
    print(f"Average relationships per character: {stats['average_relationship_count']:.1f}")

    print("\n" + "=" * 70)
    print("Example completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
