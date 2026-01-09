"""
Relationship Dynamics System

This module models relationships between characters, including relationship types,
strength, trust, communication styles, and relationship evolution.

Relationship Types:
- Friendship: Casual, supportive connections
- Mentorship: Teaching and guidance relationships
- Rivalry: Competitive but respectful opposition
- Romantic: Intimate, romantic partnerships
- Family: Familial bonds and obligations
- Professional: Work-related connections
- Alliance: Strategic partnerships
- Antagonistic: Hostile or opposing relationships
"""

from typing import Dict, List
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime


class RelationshipType(Enum):
    """Types of relationships between characters"""

    FRIENDSHIP = "friendship"
    """Casual, supportive relationship"""

    MENTORSHIP = "mentorship"
    """Teaching and guidance relationship"""

    RIVALRY = "rivalry"
    """Competitive relationship"""

    ROMANTIC = "romantic"
    """Intimate, romantic relationship"""

    FAMILY = "family"
    """Familial relationship"""

    PROFESSIONAL = "professional"
    """Work-related relationship"""

    ALLIANCE = "alliance"
    """Strategic partnership"""

    ANTAGONISTIC = "antagonistic"
    """Hostile or opposing relationship"""


@dataclass
class CharacterRelationship:
    """
    Relationship between two characters

    Attributes:
        target_character_id: ID of the character this relationship is with
        relationship_type: Type of relationship
        strength: Relationship strength (0.0 to 1.0)
        trust_level: How much trust exists (0.0 to 1.0)
        communication_style: Description of communication patterns
        shared_history: Important events in the relationship
        conflict_points: Sources of tension or disagreement
        support_areas: Areas where they support each other
        last_interaction: When they last interacted
    """
    target_character_id: str
    relationship_type: RelationshipType
    strength: float = 0.5
    trust_level: float = 0.5
    communication_style: str = "neutral"
    shared_history: List[str] = field(default_factory=list)
    conflict_points: List[str] = field(default_factory=list)
    support_areas: List[str] = field(default_factory=list)
    last_interaction: datetime = None

    def __post_init__(self):
        """Validate relationship parameters"""
        if not 0.0 <= self.strength <= 1.0:
            raise ValueError(f"strength must be between 0.0 and 1.0, got {self.strength}")
        if not 0.0 <= self.trust_level <= 1.0:
            raise ValueError(f"trust_level must be between 0.0 and 1.0, got {self.trust_level}")

        if self.last_interaction is None:
            self.last_interaction = datetime.now()

    def update_strength(self, delta: float, interaction_type: str):
        """
        Update relationship strength based on interaction

        Args:
            delta: Change in strength (can be positive or negative)
            interaction_type: Description of the interaction
        """
        self.strength = max(0.0, min(1.0, self.strength + delta))
        self.last_interaction = datetime.now()

        # Add to shared history
        history_entry = f"{datetime.now().strftime('%Y-%m-%d')}: {interaction_type}"
        self.shared_history.append(history_entry)

        # Keep history manageable
        if len(self.shared_history) > 100:
            self.shared_history = self.shared_history[-50:]

    def update_trust(self, delta: float):
        """
        Update trust level

        Args:
            delta: Change in trust level (can be positive or negative)
        """
        self.trust_level = max(0.0, min(1.0, self.trust_level + delta))

    def add_conflict_point(self, conflict: str):
        """Add a source of tension to the relationship"""
        if conflict not in self.conflict_points:
            self.conflict_points.append(conflict)

    def add_support_area(self, support: str):
        """Add an area where characters support each other"""
        if support not in self.support_areas:
            self.support_areas.append(support)

    def get_compatibility_score(self) -> float:
        """
        Calculate overall compatibility score

        Returns:
            float: Compatibility from 0.0 to 1.0
        """
        # High trust and strong relationship = high compatibility
        base_score = (self.strength + self.trust_level) / 2.0

        # Fewer conflicts = higher compatibility
        conflict_penalty = len(self.conflict_points) * 0.05

        # More support areas = higher compatibility
        support_bonus = len(self.support_areas) * 0.03

        return max(0.0, min(1.0, base_score - conflict_penalty + support_bonus))

    def get_description(self) -> str:
        """Get a textual description of the relationship"""
        strength_desc = "strong" if self.strength > 0.7 else "moderate" if self.strength > 0.4 else "weak"
        trust_desc = "high" if self.trust_level > 0.7 else "moderate" if self.trust_level > 0.4 else "low"

        return f"A {strength_desc} {self.relationship_type.value} relationship with {trust_desc} trust"

    def is_positive(self) -> bool:
        """Check if the relationship is positive"""
        return self.strength > 0.5 and self.trust_level > 0.5

    def is_negative(self) -> bool:
        """Check if the relationship is negative"""
        return self.strength < 0.3 or self.trust_level < 0.3

    def to_dict(self) -> Dict:
        """Convert relationship to dictionary"""
        return {
            'target_character_id': self.target_character_id,
            'relationship_type': self.relationship_type.value,
            'strength': self.strength,
            'trust_level': self.trust_level,
            'communication_style': self.communication_style,
            'shared_history': self.shared_history,
            'conflict_points': self.conflict_points,
            'support_areas': self.support_areas,
            'last_interaction': self.last_interaction.isoformat() if self.last_interaction else None
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'CharacterRelationship':
        """Create relationship from dictionary"""
        type_map = {rt.value: rt for rt in RelationshipType}

        return cls(
            target_character_id=data['target_character_id'],
            relationship_type=type_map[data['relationship_type']],
            strength=data.get('strength', 0.5),
            trust_level=data.get('trust_level', 0.5),
            communication_style=data.get('communication_style', 'neutral'),
            shared_history=data.get('shared_history', []),
            conflict_points=data.get('conflict_points', []),
            support_areas=data.get('support_areas', []),
            last_interaction=datetime.fromisoformat(data['last_interaction']) if data.get('last_interaction') else None
        )


def get_default_communication_style(relationship_type: RelationshipType) -> str:
    """Get default communication style for a relationship type"""
    styles = {
        RelationshipType.FRIENDSHIP: "casual and supportive",
        RelationshipType.MENTORSHIP: "guiding and patient",
        RelationshipType.RIVALRY: "competitive and challenging",
        RelationshipType.ROMANTIC: "intimate and vulnerable",
        RelationshipType.FAMILY: "familiar and caring",
        RelationshipType.PROFESSIONAL: "respectful and task-oriented",
        RelationshipType.ALLIANCE: "collaborative and strategic",
        RelationshipType.ANTAGONISTIC: "guarded and critical"
    }
    return styles.get(relationship_type, "neutral")


def calculate_relationship_compatibility(
    personality1,
    personality2,
    relationship_type: RelationshipType
) -> float:
    """
    Calculate compatibility between two characters for a relationship type

    Args:
        personality1: First character's personality (BigFive)
        personality2: Second character's personality (BigFive)
        relationship_type: Type of relationship to assess

    Returns:
        float: Compatibility score from 0.0 to 1.0
    """
    # Get personality traits
    if hasattr(personality1, 'big_five'):
        p1 = personality1.big_five
    else:
        p1 = personality1

    if hasattr(personality2, 'big_five'):
        p2 = personality2.big_five
    else:
        p2 = personality2

    # Calculate trait differences
    trait_diffs = {
        'openness': abs(p1.openness - p2.openness),
        'conscientiousness': abs(p1.conscientiousness - p2.conscientiousness),
        'extraversion': abs(p1.extraversion - p2.extraversion),
        'agreeableness': abs(p1.agreeableness - p2.agreeableness),
        'neuroticism': abs(p1.neuroticism - p2.neuroticism)
    }

    # Relationship-specific compatibility factors
    if relationship_type == RelationshipType.FRIENDSHIP:
        # Friends benefit from similar openness and agreeableness
        weights = {
            'openness': 0.3,
            'agreeableness': 0.3,
            'extraversion': 0.2,
            'conscientiousness': 0.1,
            'neuroticism': 0.1
        }
    elif relationship_type == RelationshipType.ROMANTIC:
        # Romantic partners benefit from complementary traits
        weights = {
            'openness': 0.2,
            'agreeableness': 0.3,
            'extraversion': 0.2,
            'conscientiousness': 0.2,
            'neuroticism': 0.1
        }
    elif relationship_type == RelationshipType.MENTORSHIP:
        # Mentorships work with different experience levels
        weights = {
            'openness': 0.3,
            'conscientiousness': 0.2,
            'agreeableness': 0.2,
            'extraversion': 0.15,
            'neuroticism': 0.15
        }
    elif relationship_type == RelationshipType.RIVALRY:
        # Rivals benefit from some differences
        weights = {
            'conscientiousness': 0.4,
            'openness': 0.3,
            'extraversion': 0.2,
            'agreeableness': 0.05,
            'neuroticism': 0.05
        }
    else:
        # Default equal weights
        weights = {
            'openness': 0.2,
            'conscientiousness': 0.2,
            'extraversion': 0.2,
            'agreeableness': 0.2,
            'neuroticism': 0.2
        }

    # Calculate weighted compatibility
    weighted_diff = sum(trait_diffs[trait] * weights[trait] for trait in weights)
    compatibility = 1.0 - weighted_diff

    return max(0.0, min(1.0, compatibility))
