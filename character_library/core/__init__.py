"""
Core Character Module

This module contains the core character classes and systems including:
- LuciddreamerCharacter: Main character class
- CharacterLibraryManager: Character library management
- CharacterArchetype: Archetype definitions
- CharacterSkill: Skill system
- SkillTree: Skill progression system
"""

from character_library.core.archetypes import CharacterArchetype, get_archetype_profile, get_archetype_compatibility
from character_library.core.skills import CharacterSkill, SkillTree, SkillCategory

# Try to import main classes from modular structure (may not exist yet)
try:
    from character_library.core.character import LuciddreamerCharacter
except ImportError:
    LuciddreamerCharacter = None

try:
    from character_library.core.library import CharacterLibraryManager
except ImportError:
    CharacterLibraryManager = None

__all__ = [
    "LuciddreamerCharacter",
    "CharacterLibraryManager",
    "CharacterArchetype",
    "CharacterSkill",
    "SkillTree",
    "SkillCategory",
    "get_archetype_profile",
    "get_archetype_compatibility",
]
