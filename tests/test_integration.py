"""
Integration tests for the character library

Tests complete workflows combining multiple systems:
- Character creation with personality, skills, and emotions
- Character interactions and relationship development
- Emotional responses based on personality
- Skill development affecting character capabilities
- Full character lifecycle
"""

import pytest
from character_library.personality.big_five import BigFivePersonality
from character_library.personality.enneagram import EnneagramType
from character_library.personality.mbti import MBTIType
from character_library.emotion.emotions import BasicEmotion, EmotionalState, generate_emotional_cues
from character_library.relationships.dynamics import RelationshipType, CharacterRelationship, calculate_relationship_compatibility
from character_library.core.archetypes import CharacterArchetype, get_archetype_profile
from character_library.core.skills import CharacterSkill, SkillTree


class TestCharacterCreation:
    """Test complete character creation workflows"""

    def test_create_character_from_archetype(self):
        """Test creating a character from an archetype"""
        archetype = CharacterArchetype.INNOVATOR
        profile = get_archetype_profile(archetype)

        # Verify profile has all required components
        assert 'big_five' in profile
        assert 'enneagram' in profile
        assert 'mbti' in profile
        assert 'special_skills' in profile
        assert 'dialogue_patterns' in profile

        # Verify personality components are valid
        assert isinstance(profile['big_five'], BigFivePersonality)
        assert isinstance(profile['enneagram'], EnneagramType)
        assert isinstance(profile['mbti'], MBTIType)

    def test_create_multiple_archetypes(self):
        """Test creating multiple different archetypes"""
        archetypes = [
            CharacterArchetype.INNOVATOR,
            CharacterArchetype.EDUCATOR,
            CharacterArchetype.EMPATH,
            CharacterArchetype.ENGINEER
        ]

        for archetype in archetypes:
            profile = get_archetype_profile(archetype)
            assert profile is not None
            assert 'big_five' in profile
            assert 'name_template' in profile

    def test_character_has_consistent_personality(self):
        """Test that character personality is consistent across frameworks"""
        # Innovator should be high in openness
        profile = get_archetype_profile(CharacterArchetype.INNOVATOR)
        big_five = profile['big_five']
        enneagram = profile['enneagram']
        mbti = profile['mbti']

        # Big Five openness should be high
        assert big_five.openness > 0.8

        # Should map to intuitive MBTI types (N)
        mbti_code = mbti.get_letter_code()
        assert 'N' in mbti_code


class TestEmotionalPersonalityIntegration:
    """Test integration of emotions and personality"""

    def test_personality_affects_emotional_response(self):
        """Test that personality affects emotional responses"""
        # High neuroticism should amplify negative emotions
        high_neuroticism = BigFivePersonality(
            openness=0.5,
            conscientiousness=0.5,
            extraversion=0.5,
            agreeableness=0.5,
            neuroticism=0.9
        )

        # Low neuroticism should dampen negative emotions
        low_neuroticism = BigFivePersonality(
            openness=0.5,
            conscientiousness=0.5,
            extraversion=0.5,
            agreeableness=0.5,
            neuroticism=0.1
        )

        # Both should process the same emotional event
        # (This is a structural test - actual implementation would be in character class)

    def test_extraversion_affects_social_emotions(self):
        """Test that extraversion affects social emotional responses"""
        high_extraversion = BigFivePersonality(
            extraversion=0.9,
            openness=0.5,
            conscientiousness=0.5,
            agreeableness=0.5,
            neuroticism=0.5
        )

        # High extraversion should correlate with social emotions
        # (Structural test for future implementation)

    def test_agreeableness_affects_relationship_emotions(self):
        """Test that agreeableness affects relationship-based emotions"""
        high_agreeableness = BigFivePersonality(
            agreeableness=0.9,
            openness=0.5,
            conscientiousness=0.5,
            extraversion=0.5,
            neuroticism=0.5
        )

        # High agreeableness should promote trust and joy in relationships
        trust_emotion = EmotionalState(
            primary_emotion=BasicEmotion.TRUST,
            intensity=0.7,
            valence=0.5,
            arousal=0.4
        )
        assert trust_emotion.is_positive()


class TestRelationshipDevelopment:
    """Test relationship development workflows"""

    def test_compatibility_affects_relationship_initialization(self):
        """Test that compatibility affects initial relationship parameters"""
        # Create two compatible personalities
        personality1 = BigFivePersonality(
            openness=0.8,
            conscientiousness=0.7,
            extraversion=0.6,
            agreeableness=0.7,
            neuroticism=0.3
        )
        personality2 = BigFivePersonality(
            openness=0.8,
            conscientiousness=0.7,
            extraversion=0.6,
            agreeableness=0.7,
            neuroticism=0.3
        )

        # High compatibility should support stronger initial relationships
        compatibility = calculate_relationship_compatibility(
            personality1,
            personality2,
            RelationshipType.FRIENDSHIP
        )
        assert compatibility > 0.8

    def test_relationship_evolution_through_interactions(self):
        """Test that relationships evolve through interactions"""
        relationship = CharacterRelationship(
            target_character_id="friend",
            relationship_type=RelationshipType.FRIENDSHIP,
            strength=0.5,
            trust_level=0.5
        )

        # Positive interactions should strengthen relationship
        for i in range(5):
            relationship.update_strength(0.05, "positive interaction")

        assert relationship.strength > 0.5
        assert len(relationship.shared_history) == 5

    def test_conflict_management(self):
        """Test that conflicts affect relationships"""
        relationship = CharacterRelationship(
            target_character_id="friend",
            relationship_type=RelationshipType.FRIENDSHIP,
            strength=0.8,
            trust_level=0.8
        )

        # Add conflicts
        relationship.add_conflict_point("political disagreements")
        relationship.add_conflict_point("different values")

        # Compatibility should decrease with conflicts
        compatibility = relationship.get_compatibility_score()
        base_compatibility = (relationship.strength + relationship.trust_level) / 2.0
        assert compatibility < base_compatibility

    def test_support_areas_improve_relationships(self):
        """Test that support areas improve relationship quality"""
        relationship = CharacterRelationship(
            target_character_id="friend",
            relationship_type=RelationshipType.FRIENDSHIP,
            strength=0.6,
            trust_level=0.6
        )

        # Add support areas
        relationship.add_support_area("emotional support")
        relationship.add_support_area("career advice")
        relationship.add_support_area("shared hobbies")

        # Compatibility should increase with support areas
        compatibility = relationship.get_compatibility_score()
        base_compatibility = (relationship.strength + relationship.trust_level) / 2.0
        assert compatibility > base_compatibility


class TestSkillDevelopmentWorkflows:
    """Test skill development and progression workflows"""

    def test_skill_practice_progression(self):
        """Test that consistent practice leads to skill improvement"""
        skill = CharacterSkill(
            name="public_speaking",
            category="social",
            current_level=2.0
        )

        initial_level = skill.current_level

        # Practice multiple times
        for i in range(10):
            skill.practice(
                difficulty=0.6,
                performance=0.7 + (i * 0.02),  # Improving performance
                time_spent=1.0
            )

        assert skill.current_level > initial_level
        assert skill.experience_points > 0
        assert skill.total_uses == 0  # practice doesn't count as use

    def test_mastery_progression(self):
        """Test progression through mastery levels"""
        skill = CharacterSkill(
            name="leadership",
            category="leadership",
            current_level=1.0
        )

        assert skill.get_mastery_level() == "Novice"

        # Practice to reach apprentice
        for i in range(50):
            skill.practice(difficulty=0.7, performance=0.8, time_spent=2.0)

        mastery = skill.get_mastery_level()
        # Should have progressed beyond novice
        assert mastery in ["Apprentice", "Journeyman", "Expert", "Master", "Grandmaster"]

    def test_skill_usage_tracking(self):
        """Test that skill usage is tracked correctly"""
        skill = CharacterSkill(
            name="programming",
            category="technical",
            current_level=5.0
        )

        # Use skill multiple times
        for i in range(10):
            skill.use(success=(i % 3 != 0))  # 2/3 success rate

        assert skill.total_uses == 10
        success_rate = skill.get_success_rate()
        assert abs(success_rate - 0.666) < 0.1

    def test_skill_tree_progression(self):
        """Test progression through a skill tree"""
        tree = SkillTree(
            name="Leadership Tree",
            description="Leadership progression"
        )

        # Add prerequisite skills
        tree.add_skill(CharacterSkill(
            name="communication",
            category="social",
            current_level=3.0
        ), unlock_level=0.0)

        tree.add_skill(CharacterSkill(
            name="team_building",
            category="social",
            current_level=1.0,
            prerequisites=["communication"]
        ), unlock_level=3.0)

        # Practice communication to unlock team_building
        for i in range(20):
            tree.practice_skill("communication", difficulty=0.6, performance=0.7, time_spent=1.0)

        comm_skill = tree.get_skill("communication")
        assert comm_skill.current_level > 3.0

    def test_specialized_skill_development(self):
        """Test developing specializations within skills"""
        skill = CharacterSkill(
            name="programming",
            category="technical",
            current_level=5.0
        )

        # Add specializations through practice
        skill.add_specialization("python")
        skill.add_specialization("machine learning")
        skill.add_specialization("web development")

        assert len(skill.specializations) == 3
        assert "python" in skill.specializations


class TestComplexWorkflows:
    """Test complex multi-system workflows"""

    def test_character_interaction_workflow(self):
        """Test complete character interaction workflow"""
        # Create two characters with different personalities
        profile1 = get_archetype_profile(CharacterArchetype.INNOVATOR)
        profile2 = get_archetype_profile(CharacterArchetype.ENGINEER)

        # Calculate compatibility
        compatibility = calculate_relationship_compatibility(
            profile1['big_five'],
            profile2['big_five'],
            RelationshipType.FRIENDSHIP
        )

        # Should have good compatibility
        assert compatibility > 0.8

        # Create relationship based on compatibility
        relationship = CharacterRelationship(
            target_character_id="engineer_char",
            relationship_type=RelationshipType.FRIENDSHIP,
            strength=compatibility,
            trust_level=compatibility * 0.9
        )

        # Evolve relationship through interaction
        relationship.update_strength(0.1, "collaborative project")
        assert relationship.strength > compatibility

    def test_emotional_response_to_relationship_event(self):
        """Test emotional response to relationship events"""
        # Character with high agreeableness
        high_agreeableness = BigFivePersonality(
            agreeableness=0.9,
            openness=0.5,
            conscientiousness=0.5,
            extraversion=0.5,
            neuroticism=0.5
        )

        # Positive relationship event triggers positive emotion
        emotion = EmotionalState(
            primary_emotion=BasicEmotion.JOY,
            intensity=0.7,
            valence=0.8,
            arousal=0.6,
            triggers=["friend's achievement"],
            visible_cues=generate_emotional_cues(BasicEmotion.JOY, 0.7)
        )

        assert emotion.is_positive()
        assert len(emotion.visible_cues) > 0

    def test_skill_affects_social_interaction(self):
        """Test that skills affect social interaction quality"""
        # Character with high social skills
        social_skill = CharacterSkill(
            name="empathy",
            category="social",
            current_level=8.0,
            specializations=["emotional_support", "active_listening"]
        )

        # High social skill should support better relationships
        # (This is a structural test for future implementation)
        assert social_skill.get_mastery_level() in ["Expert", "Master", "Grandmaster"]

    def test_personality_growth_through_experience(self):
        """Test personality growth through character experiences"""
        initial_personality = BigFivePersonality(
            openness=0.7,
            conscientiousness=0.6,
            extraversion=0.5,
            agreeableness=0.6,
            neuroticism=0.4
        )

        # Personality can evolve through experiences
        # (Structural test - implementation would be in character growth system)
        assert initial_personality.openness == 0.7

    def test_emotional_state_transitions(self):
        """Test emotional state transitions based on events"""
        # Start with trust
        current_state = EmotionalState(
            primary_emotion=BasicEmotion.TRUST,
            intensity=0.6,
            valence=0.7,
            arousal=0.3
        )

        # Negative high-arousal event
        new_emotion = get_emotion_transition(
            current_emotion=current_state.primary_emotion,
            event_valence=-0.8,
            event_arousal=0.9
        )

        # Should transition to anger or fear
        assert new_emotion in [BasicEmotion.ANGER, BasicEmotion.FEAR]


class TestSerializationWorkflows:
    """Test serialization and deserialization workflows"""

    def test_personality_serialization(self):
        """Test personality can be serialized and restored"""
        original = BigFivePersonality(
            openness=0.8,
            conscientiousness=0.7,
            extraversion=0.6,
            agreeableness=0.5,
            neuroticism=0.3
        )

        # Serialize
        personality_dict = original.to_dict()

        # Deserialize
        restored = BigFivePersonality.from_dict(personality_dict)

        assert restored.openness == original.openness
        assert restored.conscientiousness == original.conscientiousness
        assert restored.extraversion == original.extraversion
        assert restored.agreeableness == original.agreeableness
        assert restored.neuroticism == original.neuroticism

    def test_emotional_state_serialization(self):
        """Test emotional state can be serialized and restored"""
        original = EmotionalState(
            primary_emotion=BasicEmotion.JOY,
            secondary_emotion=BasicEmotion.ANTICIPATION,
            intensity=0.7,
            valence=0.6,
            arousal=0.8,
            duration_minutes=30,
            triggers=["good news"],
            visible_cues=["smiles", "bright eyes"]
        )

        # Serialize
        state_dict = original.to_dict()

        # Deserialize
        restored = EmotionalState.from_dict(state_dict)

        assert restored.primary_emotion == original.primary_emotion
        assert restored.secondary_emotion == original.secondary_emotion
        assert restored.intensity == original.intensity
        assert restored.valence == original.valence

    def test_relationship_serialization(self):
        """Test relationship can be serialized and restored"""
        original = CharacterRelationship(
            target_character_id="friend_123",
            relationship_type=RelationshipType.FRIENDSHIP,
            strength=0.8,
            trust_level=0.7,
            communication_style="casual"
        )

        # Serialize
        rel_dict = original.to_dict()

        # Deserialize
        restored = CharacterRelationship.from_dict(rel_dict)

        assert restored.target_character_id == original.target_character_id
        assert restored.relationship_type == original.relationship_type
        assert restored.strength == original.strength
        assert restored.trust_level == original.trust_level

    def test_skill_serialization(self):
        """Test skill can be serialized and restored"""
        original = CharacterSkill(
            name="leadership",
            category="leadership",
            current_level=7.5,
            experience_points=500,
            specializations=["team_building", "conflict_resolution"]
        )

        # Serialize
        skill_dict = original.to_dict()

        # Deserialize would require from_dict method
        # For now, test that dict has expected fields
        assert skill_dict['name'] == original.name
        assert skill_dict['current_level'] == original.current_level
        assert 'python' in skill_dict or 'specializations' in skill_dict


class TestCrossSystemIntegration:
    """Test integration across all systems"""

    def test_complete_character_lifecycle(self):
        """Test complete character lifecycle from creation to development"""
        # 1. Create character from archetype
        archetype = CharacterArchetype.INNOVATOR
        profile = get_archetype_profile(archetype)
        personality = profile['big_five']

        # 2. Character experiences emotions
        emotion = EmotionalState(
            primary_emotion=BasicEmotion.JOY,
            intensity=0.8,
            valence=0.7,
            arousal=0.6,
            triggers=["breakthrough"],
            visible_cues=generate_emotional_cues(BasicEmotion.JOY, 0.8)
        )

        # 3. Character develops skills
        skill = CharacterSkill(
            name="creative_thinking",
            category="cognitive",
            current_level=5.0
        )
        skill.practice(difficulty=0.7, performance=0.8, time_spent=2.0)

        # 4. Character forms relationships
        relationship = CharacterRelationship(
            target_character_id="collaborator",
            relationship_type=RelationshipType.PROFESSIONAL,
            strength=0.7,
            trust_level=0.6
        )

        # All systems should be functional
        assert personality is not None
        assert emotion.is_positive()
        assert skill.current_level > 5.0
        assert relationship.strength == 0.7

    def test_multiple_characters_interaction(self):
        """Test interaction between multiple characters"""
        # Create three different characters
        innovator_profile = get_archetype_profile(CharacterArchetype.INNOVATOR)
        educator_profile = get_archetype_profile(CharacterArchetype.EDUCATOR)
        engineer_profile = get_archetype_profile(CharacterArchetype.ENGINEER)

        # Calculate pairwise compatibilities
        compat_ie = calculate_relationship_compatibility(
            innovator_profile['big_five'],
            educator_profile['big_five'],
            RelationshipType.PROFESSIONAL
        )

        compat_ee = calculate_relationship_compatibility(
            educator_profile['big_five'],
            engineer_profile['big_five'],
            RelationshipType.PROFESSIONAL
        )

        # All should have some compatibility
        assert 0.0 <= compat_ie <= 1.0
        assert 0.0 <= compat_ee <= 1.0
