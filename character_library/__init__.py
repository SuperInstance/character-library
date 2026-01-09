"""
Character Library - Comprehensive Personality Modeling System for AI Characters

A standalone package for creating psychologically-grounded AI characters with rich
personalities, emotional modeling, skill development, and dynamic relationships.

Core Features:
- 12 archetypal characters with unique personalities
- Big Five, Enneagram, and MBTI personality frameworks
- Emotional modeling and expression
- Character dialogue patterns and voice consistency
- Relationship dynamics and compatibility
- Character skill trees and specialization
- Character growth and evolution
- Agent integration for AI systems

Example:
    >>> from character_library import CharacterLibrary, CharacterArchetype
    >>> library = CharacterLibrary()
    >>> character = library.create_character(CharacterArchetype.INNOVATOR)
    >>> dialogue = character.generate_dialogue({'situation': 'problem_solving'})
"""

__version__ = "1.0.0"
__author__ = "Luciddreamer Team"

# Import archetypes and basic classes that exist
from character_library.core.archetypes import (
    CharacterArchetype,
    get_archetype_profile,
    get_archetype_compatibility
)

# Personality frameworks
from character_library.personality.big_five import BigFivePersonality
from character_library.personality.enneagram import EnneagramType
from character_library.personality.mbti import MBTIType

# Emotional modeling
from character_library.emotion.emotions import (
    BasicEmotion,
    EmotionalState,
    generate_emotional_cues,
    get_emotion_transition
)

# Relationships
from character_library.relationships.dynamics import (
    RelationshipType,
    CharacterRelationship,
    get_default_communication_style,
    calculate_relationship_compatibility
)

# Skills
from character_library.core.skills import CharacterSkill, SkillTree, SkillCategory

# Try to import main character class from modular structure
try:
    from character_library.core.character import LuciddreamerCharacter
except ImportError:
    LuciddreamerCharacter = None

# Try to import library manager from modular structure
try:
    from character_library.core.library import CharacterLibraryManager
except ImportError:
    CharacterLibraryManager = None

# If not available in modular form, try to import from original integration file
if LuciddreamerCharacter is None or CharacterLibraryManager is None:
    try:
        import sys
        import os
        # Add package directory to path
        package_dir = os.path.dirname(__file__)
        if package_dir not in sys.path:
            sys.path.insert(0, package_dir)

        # Import from original file
        from character_library_integration import (
            LuciddreamerCharacter as _LC,
            CharacterLibraryManager as _CLM
        )
        if LuciddreamerCharacter is None:
            LuciddreamerCharacter = _LC
        if CharacterLibraryManager is None:
            CharacterLibraryManager = _CLM
    except ImportError:
        pass

# Agent integration (optional, requires hierarchical-memory)
AGENT_SUPPORT = False
CharacterAgent = None
AgentRole = None

try:
    from character_library.core.agent import CharacterAgent, AgentRole
    AGENT_SUPPORT = True
except ImportError:
    try:
        from character_library_integration import CharacterAgent, AgentRole
        AGENT_SUPPORT = True
    except ImportError:
        pass

__all__ = [
    # Version info
    "__version__",
    "__author__",
    "AGENT_SUPPORT",

    # Core classes
    "LuciddreamerCharacter",
    "CharacterLibraryManager",
    "CharacterArchetype",

    # Personality
    "BigFivePersonality",
    "EnneagramType",
    "MBTIType",

    # Emotion
    "BasicEmotion",
    "EmotionalState",
    "generate_emotional_cues",
    "get_emotion_transition",

    # Relationships
    "RelationshipType",
    "CharacterRelationship",
    "get_default_communication_style",
    "calculate_relationship_compatibility",

    # Skills
    "CharacterSkill",
    "SkillTree",
    "SkillCategory",

    # Archetype helpers
    "get_archetype_profile",
    "get_archetype_compatibility",

    # Agent integration (optional)
    "CharacterAgent",
    "AgentRole",
]

# Convenience exports (only if available)
if CharacterLibraryManager is not None:
    CharacterLibrary = CharacterLibraryManager
else:
    CharacterLibrary = None
