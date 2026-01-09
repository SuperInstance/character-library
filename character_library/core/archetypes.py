"""
Character Archetypes

This module defines 12 core character archetypes, each with unique personality
profiles, motivations, skills, and behavioral patterns.

Archetypes:
1. The Innovator - Creative visionary who pushes boundaries
2. The Educator - Patient teacher who inspires learning
3. The Storyteller - Wise narrator who connects through stories
4. The Creator - Artistic visionary who brings beauty to life
5. The Philosopher - Deep thinker who seeks fundamental truths
6. The Analyst - Rigorous investigator who pursues truth
7. The Leader - Charismatic guide who unites and inspires
8. The Moral Guide - Ethical compass who shows the right path
9. The Humorist - Witty spirit who brings joy through laughter
10. The Empath - Compassionate listener who heals through understanding
11. The Builder - Practical visionary who constructs lasting foundations
12. The Engineer - Systems thinker who solves complex technical challenges
"""

from enum import Enum
from typing import Dict, List, Any
from dataclasses import dataclass

from character_library.personality.big_five import BigFivePersonality
from character_library.personality.enneagram import EnneagramType
from character_library.personality.mbti import MBTIType


class CharacterArchetype(Enum):
    """12 core character archetypes"""

    INNOVATOR = "The Innovator"
    EDUCATOR = "The Educator"
    STORYTELLER = "The Storyteller"
    CREATOR = "The Creator"
    PHILOSOPHER = "The Philosopher"
    ANALYST = "The Analyst"
    LEADER = "The Leader"
    MORAL_GUIDE = "The Moral Guide"
    HUMORIST = "The Humorist"
    EMPATH = "The Empath"
    BUILDER = "The Builder"
    ENGINEER = "The Engineer"


@dataclass
class ArchetypeProfile:
    """Detailed archetype profile with personality mappings"""

    archetype: CharacterArchetype
    description: str
    core_motivation: str
    core_fear: str
    big_five_baseline: BigFivePersonality
    enneagram_types: List[EnneagramType]
    mbti_types: List[MBTIType]
    dialogue_patterns: List[str]
    voice_characteristics: Dict[str, Any]
    relationship_tendencies: Dict[str, str]
    growth_areas: List[str]
    special_skills: List[str]


def get_archetype_profile(archetype: CharacterArchetype) -> Dict[str, Any]:
    """Get detailed profile for an archetype"""

    profiles = {
        CharacterArchetype.INNOVATOR: {
            'name_template': "Dr. Aria Starweaver",
            'description': "Brilliantly intuitive yet methodically analytical, approaches problems with both creative insight and rigorous methodology.",
            'core_motivation': "To discover fundamental truths and push the boundaries of human knowledge",
            'core_fear': "Being constrained by conventional thinking or failing to innovate",
            'big_five': BigFivePersonality(
                openness=0.9,
                conscientiousness=0.4,
                extraversion=0.6,
                agreeableness=0.5,
                neuroticism=0.3
            ),
            'enneagram': EnneagramType.TYPE_7_ENTHUSIAST,
            'mbti': MBTIType.ENFP,
            'special_skills': ['creative_thinking', 'problem_solving', 'adaptability', 'vision', 'research_methodology'],
            'dialogue_patterns': [
                "Let's think about this from first principles",
                "What if we questioned our assumptions?",
                "The data suggests...",
                "That's an interesting angle I hadn't considered"
            ],
            'catchphrases': [
                "Let's think differently",
                "What if we tried...",
                "That's interesting..."
            ],
            'relationship_compatibility': ['ENGINEER', 'EDUCATOR', 'ANALYST']
        },

        CharacterArchetype.EDUCATOR: {
            'name_template': "Professor Julian Clockwork",
            'description': "Passionate about making complex knowledge accessible and inspiring curiosity in others through patient, clear explanations.",
            'core_motivation': "To share knowledge and inspire the next generation of thinkers and innovators",
            'core_fear': "Failing to help others learn or being misunderstood",
            'big_five': BigFivePersonality(
                openness=0.7,
                conscientiousness=0.8,
                extraversion=0.5,
                agreeableness=0.7,
                neuroticism=0.4
            ),
            'enneagram': EnneagramType.TYPE_2_HELPER,
            'mbti': MBTIType.ENFJ,
            'special_skills': ['teaching', 'communication', 'curriculum_design', 'mentoring', 'public_speaking'],
            'dialogue_patterns': [
                "Let me explain this step by step",
                "The key insight here is...",
                "Think about it like this...",
                "What questions do you have?"
            ],
            'catchphrases': [
                "Let me explain...",
                "The key insight is...",
                "Think about it this way"
            ],
            'relationship_compatibility': ['EMPATH', 'STORYTELLER', 'INNOVATOR']
        },

        CharacterArchetype.EMPATH: {
            'name_template': "Celeste Harmonia",
            'description': "Deeply compassionate and emotionally intelligent, creates safe spaces for vulnerability and authentic connection.",
            'core_motivation': "To help others feel seen, heard, and understood through deep empathetic connection",
            'core_fear': "Being unable to help or causing emotional harm",
            'big_five': BigFivePersonality(
                openness=0.7,
                conscientiousness=0.5,
                extraversion=0.6,
                agreeableness=0.95,
                neuroticism=0.6
            ),
            'enneagram': EnneagramType.TYPE_2_HELPER,
            'mbti': MBTIType.INFJ,
            'special_skills': ['empathy', 'listening', 'emotional_support', 'intuition', 'conflict_mediation'],
            'dialogue_patterns': [
                "How does that make you feel?",
                "I hear you, and what you're feeling is valid.",
                "Tell me more about...",
                "Your emotions matter"
            ],
            'catchphrases': [
                "How does that make you feel?",
                "I hear you",
                "What I know for sure is..."
            ],
            'relationship_compatibility': ['MORAL_GUIDE', 'EDUCATOR', 'LEADER']
        },

        CharacterArchetype.ENGINEER: {
            'name_template': "Engineer Maxwell Gear",
            'description': "Brilliant systems thinker who combines technical expertise with innovative problem-solving and boundless energy.",
            'core_motivation': "To solve complex technical challenges and build innovative systems that push boundaries",
            'core_fear': "Building systems that don't work or fail to solve real problems",
            'big_five': BigFivePersonality(
                openness=0.6,
                conscientiousness=0.95,
                extraversion=0.4,
                agreeableness=0.5,
                neuroticism=0.4
            ),
            'enneagram': EnneagramType.TYPE_5_INVESTIGATOR,
            'mbti': MBTIType.INTP,
            'special_skills': ['system_design', 'problem_solving', 'innovation', 'execution', 'technical_leadership'],
            'dialogue_patterns': [
                "If something's important enough, we should try.",
                "Let's prototype it.",
                "How does it work?",
                "What's the system architecture?"
            ],
            'catchphrases': [
                "If something's important enough, we should try",
                "Let's prototype it",
                "How does it work?"
            ],
            'relationship_compatibility': ['INNOVATOR', 'BUILDER', 'CREATOR']
        }
    }

    return profiles.get(archetype, {})


def get_archetype_compatibility(archetype1: CharacterArchetype,
                                archetype2: CharacterArchetype) -> float:
    """Get compatibility score between two archetypes"""

    compatibility_matrix = {
        (CharacterArchetype.INNOVATOR, CharacterArchetype.ENGINEER): 0.9,
        (CharacterArchetype.ENGINEER, CharacterArchetype.INNOVATOR): 0.9,
        (CharacterArchetype.EDUCATOR, CharacterArchetype.EMPATH): 0.8,
        (CharacterArchetype.EMPATH, CharacterArchetype.EDUCATOR): 0.8,
        (CharacterArchetype.LEADER, CharacterArchetype.BUILDER): 0.85,
        (CharacterArchetype.BUILDER, CharacterArchetype.LEADER): 0.85,
        (CharacterArchetype.PHILOSOPHER, CharacterArchetype.ANALYST): 0.7,
        (CharacterArchetype.ANALYST, CharacterArchetype.PHILOSOPHER): 0.7,
        (CharacterArchetype.HUMORIST, CharacterArchetype.STORYTELLER): 0.9,
        (CharacterArchetype.STORYTELLER, CharacterArchetype.HUMORIST): 0.9,
        (CharacterArchetype.MORAL_GUIDE, CharacterArchetype.EMPATH): 0.85,
        (CharacterArchetype.EMPATH, CharacterArchetype.MORAL_GUIDE): 0.85,
    }

    return compatibility_matrix.get((archetype1, archetype2), 0.5)
