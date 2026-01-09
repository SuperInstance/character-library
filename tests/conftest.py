"""
Shared pytest fixtures for character-library tests

This module provides common fixtures used across all test files.
"""

import pytest
from datetime import datetime
from character_library.personality.big_five import BigFivePersonality
from character_library.personality.enneagram import EnneagramType
from character_library.personality.mbti import MBTIType
from character_library.emotion.emotions import BasicEmotion, EmotionalState
from character_library.relationships.dynamics import RelationshipType, CharacterRelationship
from character_library.core.skills import CharacterSkill, SkillTree, SkillCategory


# ============================================================================
# Personality Fixtures
# ============================================================================

@pytest.fixture
def sample_big_five():
    """Create a sample Big Five personality"""
    return BigFivePersonality(
        openness=0.8,
        conscientiousness=0.7,
        extraversion=0.6,
        agreeableness=0.5,
        neuroticism=0.3
    )


@pytest.fixture
def high_openness_personality():
    """Create a personality with high openness"""
    return BigFivePersonality(
        openness=0.95,
        conscientiousness=0.5,
        extraversion=0.5,
        agreeableness=0.5,
        neuroticism=0.5
    )


@pytest.fixture
def low_openness_personality():
    """Create a personality with low openness"""
    return BigFivePersonality(
        openness=0.2,
        conscientiousness=0.7,
        extraversion=0.5,
        agreeableness=0.6,
        neuroticism=0.4
    )


@pytest.fixture
def all_enneagram_types():
    """Provide all Enneagram types"""
    return list(EnneagramType)


@pytest.fixture
def sample_enneagram():
    """Create a sample Enneagram type"""
    return EnneagramType.TYPE_7_ENTHUSIAST


@pytest.fixture
def all_mbti_types():
    """Provide all MBTI types"""
    return list(MBTIType)


@pytest.fixture
def sample_mbti():
    """Create a sample MBTI type"""
    return MBTIType.ENFP


# ============================================================================
# Emotional State Fixtures
# ============================================================================

@pytest.fixture
def joy_emotion():
    """Create a joy emotional state"""
    return EmotionalState(
        primary_emotion=BasicEmotion.JOY,
        intensity=0.8,
        valence=0.7,
        arousal=0.6,
        duration_minutes=30,
        triggers=["good news", "achievement"],
        visible_cues=["smiles", "bright eyes"]
    )


@pytest.fixture
def fear_emotion():
    """Create a fear emotional state"""
    return EmotionalState(
        primary_emotion=BasicEmotion.FEAR,
        intensity=0.7,
        valence=-0.6,
        arousal=0.8,
        duration_minutes=15,
        triggers=["threat", "uncertainty"],
        visible_cues=["widened eyes", "tense muscles"]
    )


@pytest.fixture
def neutral_emotion():
    """Create a neutral emotional state"""
    return EmotionalState(
        primary_emotion=BasicEmotion.TRUST,
        intensity=0.3,
        valence=0.0,
        arousal=0.3,
        duration_minutes=60,
        triggers=[],
        visible_cues=[]
    )


@pytest.fixture
def all_basic_emotions():
    """Provide all basic emotions"""
    return list(BasicEmotion)


# ============================================================================
# Relationship Fixtures
# ============================================================================

@pytest.fixture
def friendship_relationship():
    """Create a friendship relationship"""
    return CharacterRelationship(
        target_character_id="friend_123",
        relationship_type=RelationshipType.FRIENDSHIP,
        strength=0.8,
        trust_level=0.7,
        communication_style="casual and supportive"
    )


@pytest.fixture
def romantic_relationship():
    """Create a romantic relationship"""
    return CharacterRelationship(
        target_character_id="partner_456",
        relationship_type=RelationshipType.ROMANTIC,
        strength=0.9,
        trust_level=0.85,
        communication_style="intimate and vulnerable"
    )


@pytest.fixture
def antagonistic_relationship():
    """Create an antagonistic relationship"""
    return CharacterRelationship(
        target_character_id="rival_789",
        relationship_type=RelationshipType.ANTAGONISTIC,
        strength=0.3,
        trust_level=0.2,
        communication_style="guarded and critical"
    )


# ============================================================================
# Skill Fixtures
# ============================================================================

@pytest.fixture
def cognitive_skill():
    """Create a cognitive skill"""
    return CharacterSkill(
        name="problem_solving",
        category="cognitive",
        current_level=6.0,
        experience_points=500,
        prerequisites=["critical_thinking"],
        specializations=["analytical", "creative"]
    )


@pytest.fixture
def social_skill():
    """Create a social skill"""
    return CharacterSkill(
        name="empathy",
        category="social",
        current_level=7.5,
        experience_points=800,
        prerequisites=[],
        specializations=["emotional_support", "conflict_resolution"]
    )


@pytest.fixture
def skill_tree():
    """Create a skill tree with multiple skills"""
    tree = SkillTree(
        name="Leadership Skills",
        description="Skills for effective leadership"
    )

    # Add skills to tree
    tree.add_skill(CharacterSkill(
        name="communication",
        category="social",
        current_level=5.0
    ), unlock_level=0.0)

    tree.add_skill(CharacterSkill(
        name="decision_making",
        category="cognitive",
        current_level=4.0,
        prerequisites=["communication"]
    ), unlock_level=3.0)

    tree.add_skill(CharacterSkill(
        name="team_building",
        category="social",
        current_level=3.0,
        prerequisites=["communication"]
    ), unlock_level=4.0)

    return tree


# ============================================================================
# Helper Fixtures
# ============================================================================

@pytest.fixture
def current_time():
    """Provide current time"""
    return datetime.now()


@pytest.fixture
def sample_character_data():
    """Provide sample character data for testing"""
    return {
        'id': 'char_001',
        'name': 'Test Character',
        'archetype': 'INNOVATOR',
        'big_five': BigFivePersonality(
            openness=0.8,
            conscientiousness=0.7,
            extraversion=0.6,
            agreeableness=0.5,
            neuroticism=0.3
        ),
        'enneagram': EnneagramType.TYPE_7_ENTHUSIAST,
        'mbti': MBTIType.ENFP
    }
