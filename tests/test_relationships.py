"""
Test suite for relationship dynamics system

Tests relationship types, character relationships, compatibility calculation,
and relationship evolution.
"""

import pytest
from datetime import datetime, timedelta
from character_library.relationships.dynamics import (
    RelationshipType,
    CharacterRelationship,
    get_default_communication_style,
    calculate_relationship_compatibility
)
from character_library.personality.big_five import BigFivePersonality


class TestRelationshipType:
    """Test relationship type enumeration"""

    def test_all_relationship_types_exist(self):
        """Test that all 8 relationship types are defined"""
        types = list(RelationshipType)
        assert len(types) == 8
        assert RelationshipType.FRIENDSHIP in types
        assert RelationshipType.ANTAGONISTIC in types

    def test_relationship_type_values(self):
        """Test that relationship type values are strings"""
        for rel_type in RelationshipType:
            assert isinstance(rel_type.value, str)


class TestCharacterRelationship:
    """Test character relationship representation"""

    def test_create_friendship(self, friendship_relationship):
        """Test creating a friendship relationship"""
        assert friendship_relationship.relationship_type == RelationshipType.FRIENDSHIP
        assert friendship_relationship.strength == 0.8
        assert friendship_relationship.trust_level == 0.7

    def test_create_romantic_relationship(self, romantic_relationship):
        """Test creating a romantic relationship"""
        assert romantic_relationship.relationship_type == RelationshipType.ROMANTIC
        assert romantic_relationship.strength == 0.9
        assert romantic_relationship.trust_level == 0.85

    def test_create_antagonistic_relationship(self, antagonistic_relationship):
        """Test creating an antagonistic relationship"""
        assert antagonistic_relationship.relationship_type == RelationshipType.ANTAGONISTIC
        assert antagonistic_relationship.strength == 0.3
        assert antagonistic_relationship.trust_level == 0.2

    def test_strength_validation(self):
        """Test strength validation (0.0 to 1.0)"""
        with pytest.raises(ValueError, match="strength must be between"):
            CharacterRelationship(
                target_character_id="test",
                relationship_type=RelationshipType.FRIENDSHIP,
                strength=1.5
            )

        with pytest.raises(ValueError, match="strength must be between"):
            CharacterRelationship(
                target_character_id="test",
                relationship_type=RelationshipType.FRIENDSHIP,
                strength=-0.1
            )

    def test_trust_level_validation(self):
        """Test trust level validation (0.0 to 1.0)"""
        with pytest.raises(ValueError, match="trust_level must be between"):
            CharacterRelationship(
                target_character_id="test",
                relationship_type=RelationshipType.FRIENDSHIP,
                trust_level=2.0
            )

    def test_default_last_interaction(self):
        """Test that last_interaction defaults to current time"""
        rel = CharacterRelationship(
            target_character_id="test",
            relationship_type=RelationshipType.FRIENDSHIP
        )
        assert rel.last_interaction is not None
        assert isinstance(rel.last_interaction, datetime)

    def test_update_strength_positive(self, friendship_relationship):
        """Test updating relationship strength positively"""
        initial_strength = friendship_relationship.strength
        friendship_relationship.update_strength(0.1, "had a great conversation")
        assert friendship_relationship.strength > initial_strength
        assert len(friendship_relationship.shared_history) > 0

    def test_update_strength_negative(self, friendship_relationship):
        """Test updating relationship strength negatively"""
        initial_strength = friendship_relationship.strength
        friendship_relationship.update_strength(-0.2, "had an argument")
        assert friendship_relationship.strength < initial_strength

    def test_update_strength_clamping(self, friendship_relationship):
        """Test that strength is clamped between 0.0 and 1.0"""
        friendship_relationship.update_strength(1.0, "very positive interaction")
        assert friendship_relationship.strength <= 1.0

        friendship_relationship.update_strength(-2.0, "terrible interaction")
        assert friendship_relationship.strength >= 0.0

    def test_update_trust_positive(self, friendship_relationship):
        """Test updating trust level positively"""
        initial_trust = friendship_relationship.trust_level
        friendship_relationship.update_trust(0.15)
        assert friendship_relationship.trust_level > initial_trust

    def test_update_trust_negative(self, friendship_relationship):
        """Test updating trust level negatively"""
        initial_trust = friendship_relationship.trust_level
        friendship_relationship.update_trust(-0.1)
        assert friendship_relationship.trust_level < initial_trust

    def test_update_trust_clamping(self, friendship_relationship):
        """Test that trust level is clamped between 0.0 and 1.0"""
        friendship_relationship.update_trust(2.0)
        assert friendship_relationship.trust_level <= 1.0

        friendship_relationship.update_trust(-2.0)
        assert friendship_relationship.trust_level >= 0.0

    def test_add_conflict_point(self, friendship_relationship):
        """Test adding conflict points to relationship"""
        initial_conflicts = len(friendship_relationship.conflict_points)
        friendship_relationship.add_conflict_point("disagreement about politics")
        assert len(friendship_relationship.conflict_points) == initial_conflicts + 1

    def test_add_duplicate_conflict_point(self, friendship_relationship):
        """Test that duplicate conflicts are not added"""
        conflict = "disagreement about work"
        friendship_relationship.add_conflict_point(conflict)
        friendship_relationship.add_conflict_point(conflict)
        assert friendship_relationship.conflict_points.count(conflict) == 1

    def test_add_support_area(self, friendship_relationship):
        """Test adding support areas to relationship"""
        initial_supports = len(friendship_relationship.support_areas)
        friendship_relationship.add_support_area("emotional support")
        assert len(friendship_relationship.support_areas) == initial_supports + 1

    def test_add_duplicate_support_area(self, friendship_relationship):
        """Test that duplicate support areas are not added"""
        support = "career advice"
        friendship_relationship.add_support_area(support)
        friendship_relationship.add_support_area(support)
        assert friendship_relationship.support_areas.count(support) == 1

    def test_get_compatibility_score_high(self, romantic_relationship):
        """Test compatibility score for strong relationship"""
        score = romantic_relationship.get_compatibility_score()
        assert score > 0.8

    def test_get_compatibility_score_with_conflicts(self, friendship_relationship):
        """Test compatibility score with conflicts"""
        friendship_relationship.add_conflict_point("frequent arguments")
        friendship_relationship.add_conflict_point("different values")
        score = friendship_relationship.get_compatibility_score()
        # Conflicts should reduce compatibility
        assert score < (friendship_relationship.strength + friendship_relationship.trust_level) / 2.0

    def test_get_compatibility_score_with_supports(self, friendship_relationship):
        """Test compatibility score with support areas"""
        friendship_relationship.add_support_area("emotional support")
        friendship_relationship.add_support_area("career advice")
        friendship_relationship.add_support_area("shared interests")
        score = friendship_relationship.get_compatibility_score()
        # Support areas should increase compatibility
        base_score = (friendship_relationship.strength + friendship_relationship.trust_level) / 2.0
        assert score >= base_score

    def test_get_description(self, friendship_relationship):
        """Test getting relationship description"""
        description = friendship_relationship.get_description()
        assert "friendship" in description
        assert "strong" in description

    def test_get_description_moderate(self):
        """Test description for moderate relationship"""
        rel = CharacterRelationship(
            target_character_id="test",
            relationship_type=RelationshipType.PROFESSIONAL,
            strength=0.5,
            trust_level=0.5
        )
        description = rel.get_description()
        assert "moderate" in description

    def test_get_description_weak(self):
        """Test description for weak relationship"""
        rel = CharacterRelationship(
            target_character_id="test",
            relationship_type=RelationshipType.ACQUAINTANCE,
            strength=0.3,
            trust_level=0.2
        )
        description = rel.get_description()
        assert "weak" in description

    def test_is_positive(self, friendship_relationship):
        """Test checking if relationship is positive"""
        assert friendship_relationship.is_positive() == True

    def test_is_negative(self, antagonistic_relationship):
        """Test checking if relationship is negative"""
        assert antagonistic_relationship.is_negative() == True

    def test_is_positive_boundary_conditions(self):
        """Test is_positive at boundary conditions"""
        # Exactly 0.5 should not be positive
        rel = CharacterRelationship(
            target_character_id="test",
            relationship_type=RelationshipType.FRIENDSHIP,
            strength=0.5,
            trust_level=0.6
        )
        assert rel.is_positive() == False

        # Just above 0.5 should be positive
        rel2 = CharacterRelationship(
            target_character_id="test2",
            relationship_type=RelationshipType.FRIENDSHIP,
            strength=0.51,
            trust_level=0.6
        )
        assert rel2.is_positive() == True

    def test_to_dict(self, friendship_relationship):
        """Test converting relationship to dictionary"""
        rel_dict = friendship_relationship.to_dict()
        assert isinstance(rel_dict, dict)
        assert rel_dict['target_character_id'] == "friend_123"
        assert rel_dict['relationship_type'] == "friendship"
        assert rel_dict['strength'] == 0.8
        assert rel_dict['trust_level'] == 0.7

    def test_from_dict(self, friendship_relationship):
        """Test creating relationship from dictionary"""
        rel_dict = friendship_relationship.to_dict()
        restored = CharacterRelationship.from_dict(rel_dict)
        assert restored.target_character_id == friendship_relationship.target_character_id
        assert restored.relationship_type == friendship_relationship.relationship_type
        assert restored.strength == friendship_relationship.strength
        assert restored.trust_level == friendship_relationship.trust_level

    def test_shared_history_management(self, friendship_relationship):
        """Test that shared history is managed properly"""
        # Add many interactions
        for i in range(150):
            friendship_relationship.update_strength(0.01, f"interaction {i}")

        # History should be limited
        assert len(friendship_relationship.shared_history) <= 100


class TestCommunicationStyles:
    """Test communication style functions"""

    def test_get_friendship_communication_style(self):
        """Test communication style for friendship"""
        style = get_default_communication_style(RelationshipType.FRIENDSHIP)
        assert "casual" in style
        assert "supportive" in style

    def test_get_mentorship_communication_style(self):
        """Test communication style for mentorship"""
        style = get_default_communication_style(RelationshipType.MENTORSHIP)
        assert "guiding" in style
        assert "patient" in style

    def test_get_rivalry_communication_style(self):
        """Test communication style for rivalry"""
        style = get_default_communication_style(RelationshipType.RIVALRY)
        assert "competitive" in style
        assert "challenging" in style

    def test_get_romantic_communication_style(self):
        """Test communication style for romantic"""
        style = get_default_communication_style(RelationshipType.ROMANTIC)
        assert "intimate" in style
        assert "vulnerable" in style

    def test_get_family_communication_style(self):
        """Test communication style for family"""
        style = get_default_communication_style(RelationshipType.FAMILY)
        assert "familiar" in style
        assert "caring" in style

    def test_get_professional_communication_style(self):
        """Test communication style for professional"""
        style = get_default_communication_style(RelationshipType.PROFESSIONAL)
        assert "respectful" in style
        assert "task-oriented" in style

    def test_get_alliance_communication_style(self):
        """Test communication style for alliance"""
        style = get_default_communication_style(RelationshipType.ALLIANCE)
        assert "collaborative" in style
        assert "strategic" in style

    def test_get_antagonistic_communication_style(self):
        """Test communication style for antagonistic"""
        style = get_default_communication_style(RelationshipType.ANTAGONISTIC)
        assert "guarded" in style
        assert "critical" in style


class TestCompatibilityCalculation:
    """Test relationship compatibility calculation"""

    def test_calculate_compatibility_identical_personalities(self):
        """Test compatibility with identical personalities"""
        personality = BigFivePersonality(
            openness=0.7,
            conscientiousness=0.6,
            extraversion=0.5,
            agreeableness=0.6,
            neuroticism=0.4
        )
        compatibility = calculate_relationship_compatibility(
            personality,
            personality,
            RelationshipType.FRIENDSHIP
        )
        assert compatibility == 1.0

    def test_calculate_compatibility_different_personalities(self):
        """Test compatibility with different personalities"""
        personality1 = BigFivePersonality(
            openness=0.9,
            conscientiousness=0.7,
            extraversion=0.6,
            agreeableness=0.5,
            neuroticism=0.3
        )
        personality2 = BigFivePersonality(
            openness=0.3,
            conscientiousness=0.6,
            extraversion=0.4,
            agreeableness=0.7,
            neuroticism=0.5
        )
        compatibility = calculate_relationship_compatibility(
            personality1,
            personality2,
            RelationshipType.FRIENDSHIP
        )
        assert 0.0 <= compatibility <= 1.0

    def test_friendship_compatibility_weights(self):
        """Test that friendship weights openness and agreeableness"""
        # Similar openness and agreeableness should help friendship
        personality1 = BigFivePersonality(
            openness=0.8,
            agreeableness=0.8,
            conscientiousness=0.5,
            extraversion=0.5,
            neuroticism=0.5
        )
        personality2 = BigFivePersonality(
            openness=0.8,
            agreeableness=0.8,
            conscientiousness=0.4,
            extraversion=0.6,
            neuroticism=0.4
        )
        compatibility = calculate_relationship_compatibility(
            personality1,
            personality2,
            RelationshipType.FRIENDSHIP
        )
        assert compatibility > 0.8

    def test_romantic_compatibility_weights(self):
        """Test that romantic weights agreeableness highly"""
        # High agreeableness helps romantic relationships
        personality1 = BigFivePersonality(
            agreeableness=0.9,
            openness=0.5,
            conscientiousness=0.5,
            extraversion=0.5,
            neuroticism=0.5
        )
        personality2 = BigFivePersonality(
            agreeableness=0.9,
            openness=0.5,
            conscientiousness=0.5,
            extraversion=0.5,
            neuroticism=0.5
        )
        compatibility = calculate_relationship_compatibility(
            personality1,
            personality2,
            RelationshipType.ROMANTIC
        )
        assert compatibility > 0.8

    def test_rivalry_compatibility_different(self):
        """Test that rivals can have different personalities"""
        # Rivals can be compatible despite differences
        personality1 = BigFivePersonality(
            openness=0.5,
            conscientiousness=0.9,
            extraversion=0.5,
            agreeableness=0.5,
            neuroticism=0.5
        )
        personality2 = BigFivePersonality(
            openness=0.5,
            conscientiousness=0.8,
            extraversion=0.5,
            agreeableness=0.3,
            neuroticism=0.4
        )
        compatibility = calculate_relationship_compatibility(
            personality1,
            personality2,
            RelationshipType.RIVALRY
        )
        # Should still have decent compatibility
        assert compatibility > 0.5

    def test_compatibility_with_character_objects(self):
        """Test compatibility calculation with character-like objects"""
        class MockCharacter:
            def __init__(self, big_five):
                self.big_five = big_five

        char1 = MockCharacter(BigFivePersonality(
            openness=0.7,
            conscientiousness=0.6,
            extraversion=0.5,
            agreeableness=0.6,
            neuroticism=0.4
        ))
        char2 = MockCharacter(BigFivePersonality(
            openness=0.7,
            conscientiousness=0.6,
            extraversion=0.5,
            agreeableness=0.6,
            neuroticism=0.4
        ))

        compatibility = calculate_relationship_compatibility(
            char1,
            char2,
            RelationshipType.FRIENDSHIP
        )
        assert compatibility == 1.0

    def test_all_relationship_types_have_compatibility(self):
        """Test that all relationship types can calculate compatibility"""
        personality1 = BigFivePersonality()
        personality2 = BigFivePersonality()

        for rel_type in RelationshipType:
            compatibility = calculate_relationship_compatibility(
                personality1,
                personality2,
                rel_type
            )
            assert 0.0 <= compatibility <= 1.0
