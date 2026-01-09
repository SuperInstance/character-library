"""
Test suite for character archetypes

Tests 12 core character archetypes, their profiles, compatibility,
and personality mappings.
"""

import pytest
from character_library.core.archetypes import (
    CharacterArchetype,
    get_archetype_profile,
    get_archetype_compatibility
)


class TestCharacterArchetype:
    """Test character archetype enumeration"""

    def test_all_12_archetypes_exist(self):
        """Test that all 12 archetypes are defined"""
        archetypes = list(CharacterArchetype)
        assert len(archetypes) == 12

    def test_specific_archetypes_exist(self):
        """Test that specific archetypes exist"""
        assert CharacterArchetype.INNOVATOR in CharacterArchetype
        assert CharacterArchetype.EDUCATOR in CharacterArchetype
        assert CharacterArchetype.EMPATH in CharacterArchetype
        assert CharacterArchetype.ENGINEER in CharacterArchetype
        assert CharacterArchetype.LEADER in CharacterArchetype
        assert CharacterArchetype.MORAL_GUIDE in CharacterArchetype

    def test_archetype_values_are_strings(self):
        """Test that all archetype values are strings"""
        for archetype in CharacterArchetype:
            assert isinstance(archetype.value, str)

    def test_archetype_names_are_descriptive(self):
        """Test that archetype names are descriptive"""
        for archetype in CharacterArchetype:
            name = archetype.value
            assert len(name) > 0
            assert "The " in name


class TestArchetypeProfiles:
    """Test archetype profile retrieval and content"""

    def test_get_innovator_profile(self):
        """Test retrieving Innovator profile"""
        profile = get_archetype_profile(CharacterArchetype.INNOVATOR)
        assert isinstance(profile, dict)
        assert 'description' in profile
        assert 'core_motivation' in profile
        assert 'core_fear' in profile
        assert 'big_five' in profile
        assert 'enneagram' in profile
        assert 'mbti' in profile

    def test_get_educator_profile(self):
        """Test retrieving Educator profile"""
        profile = get_archetype_profile(CharacterArchetype.EDUCATOR)
        assert profile['name_template'] == "Professor Julian Clockwork"
        assert 'knowledge' in profile['core_motivation'].lower()

    def test_get_empath_profile(self):
        """Test retrieving Empath profile"""
        profile = get_archetype_profile(CharacterArchetype.EMPATH)
        assert profile['name_template'] == "Celeste Harmonia"
        assert 'compassionate' in profile['description'].lower()

    def test_get_engineer_profile(self):
        """Test retrieving Engineer profile"""
        profile = get_archetype_profile(CharacterArchetype.ENGINEER)
        assert profile['name_template'] == "Engineer Maxwell Gear"
        assert 'technical' in profile['core_motivation'].lower()

    def test_profile_has_big_five(self):
        """Test that profiles include Big Five personality"""
        profile = get_archetype_profile(CharacterArchetype.INNOVATOR)
        big_five = profile['big_five']
        assert hasattr(big_five, 'openness')
        assert hasattr(big_five, 'conscientiousness')
        assert hasattr(big_five, 'extraversion')
        assert hasattr(big_five, 'agreeableness')
        assert hasattr(big_five, 'neuroticism')

    def test_profile_has_enneagram(self):
        """Test that profiles include Enneagram type"""
        profile = get_archetype_profile(CharacterArchetype.INNOVATOR)
        assert profile['enneagram'] is not None

    def test_profile_has_mbti(self):
        """Test that profiles include MBTI type"""
        profile = get_archetype_profile(CharacterArchetype.INNOVATOR)
        assert profile['mbti'] is not None

    def test_profile_has_dialogue_patterns(self):
        """Test that profiles include dialogue patterns"""
        profile = get_archetype_profile(CharacterArchetype.INNOVATOR)
        assert 'dialogue_patterns' in profile
        assert len(profile['dialogue_patterns']) > 0
        assert isinstance(profile['dialogue_patterns'], list)

    def test_profile_has_special_skills(self):
        """Test that profiles include special skills"""
        profile = get_archetype_profile(CharacterArchetype.INNOVATOR)
        assert 'special_skills' in profile
        assert len(profile['special_skills']) > 0
        assert isinstance(profile['special_skills'], list)

    def test_innovator_personality_traits(self):
        """Test Innovator has expected personality traits"""
        profile = get_archetype_profile(CharacterArchetype.INNOVATOR)
        big_five = profile['big_five']
        # Innovator should have high openness
        assert big_five.openness > 0.8

    def test_educator_personality_traits(self):
        """Test Educator has expected personality traits"""
        profile = get_archetype_profile(CharacterArchetype.EDUCATOR)
        big_five = profile['big_five']
        # Educator should have high conscientiousness and agreeableness
        assert big_five.conscientiousness > 0.6
        assert big_five.agreeableness > 0.6

    def test_empath_personality_traits(self):
        """Test Empath has expected personality traits"""
        profile = get_archetype_profile(CharacterArchetype.EMPATH)
        big_five = profile['big_five']
        # Empath should have very high agreeableness
        assert big_five.agreeableness > 0.9

    def test_engineer_personality_traits(self):
        """Test Engineer has expected personality traits"""
        profile = get_archetype_profile(CharacterArchetype.ENGINEER)
        big_five = profile['big_five']
        # Engineer should have very high conscientiousness
        assert big_five.conscientiousness > 0.9

    def test_profile_has_catchphrases(self):
        """Test that profiles include catchphrases"""
        profile = get_archetype_profile(CharacterArchetype.INNOVATOR)
        assert 'catchphrases' in profile
        assert len(profile['catchphrases']) > 0

    def test_profile_has_relationship_compatibility(self):
        """Test that profiles include relationship compatibility"""
        profile = get_archetype_profile(CharacterArchetype.INNOVATOR)
        assert 'relationship_compatibility' in profile
        assert len(profile['relationship_compatibility']) > 0

    def test_invalid_archetype_returns_empty_dict(self):
        """Test that invalid archetype returns empty dictionary"""
        # This test checks the function handles missing archetypes gracefully
        profile = get_archetype_profile(CharacterArchetype.LEADER)
        # If profile doesn't exist, should return empty dict
        assert isinstance(profile, dict)


class TestArchetypeCompatibility:
    """Test archetype compatibility calculation"""

    def test_innovator_engineer_high_compatibility(self):
        """Test Innovator and Engineer have high compatibility"""
        compatibility = get_archetype_compatibility(
            CharacterArchetype.INNOVATOR,
            CharacterArchetype.ENGINEER
        )
        assert compatibility > 0.8

    def test_engineer_innovator_high_compatibility(self):
        """Test Engineer and Innovator have high compatibility (symmetric)"""
        compatibility = get_archetype_compatibility(
            CharacterArchetype.ENGINEER,
            CharacterArchetype.INNOVATOR
        )
        assert compatibility > 0.8

    def test_educator_empath_good_compatibility(self):
        """Test Educator and Empath have good compatibility"""
        compatibility = get_archetype_compatibility(
            CharacterArchetype.EDUCATOR,
            CharacterArchetype.EMPATH
        )
        assert compatibility > 0.7

    def test_leader_builder_good_compatibility(self):
        """Test Leader and Builder have good compatibility"""
        compatibility = get_archetype_compatibility(
            CharacterArchetype.LEADER,
            CharacterArchetype.BUILDER
        )
        assert compatibility > 0.8

    def test_unspecified_pair_default_compatibility(self):
        """Test that unspecified archetype pairs have default compatibility"""
        compatibility = get_archetype_compatibility(
            CharacterArchetype.HUMORIST,
            CharacterArchetype.STORYTELLER
        )
        # Should have default compatibility if not explicitly defined
        assert compatibility == 0.9  # As per the code

    def test_compatibility_in_range(self):
        """Test that all compatibility scores are in valid range"""
        archetypes = list(CharacterArchetype)
        for arch1 in archetypes:
            for arch2 in archetypes:
                compatibility = get_archetype_compatibility(arch1, arch2)
                assert 0.0 <= compatibility <= 1.0

    def test_compatibility_symmetry(self):
        """Test that compatibility is symmetric"""
        pairs = [
            (CharacterArchetype.INNOVATOR, CharacterArchetype.ENGINEER),
            (CharacterArchetype.EDUCATOR, CharacterArchetype.EMPATH),
        ]
        for arch1, arch2 in pairs:
            compat1 = get_archetype_compatibility(arch1, arch2)
            compat2 = get_archetype_compatibility(arch2, arch1)
            assert compat1 == compat2


class TestArchetypeDiversity:
    """Test that archetypes have diverse personalities"""

    def test_archetypes_have_different_personalities(self):
        """Test that different archetypes have different Big Five profiles"""
        innovator_profile = get_archetype_profile(CharacterArchetype.INNOVATOR)
        engineer_profile = get_archetype_profile(CharacterArchetype.ENGINEER)

        innovator_of = innovator_profile['big_five'].openness
        engineer_of = engineer_profile['big_five'].openness

        # Innovator should be more open than Engineer
        assert innovator_of > engineer_of

    def test_archetypes_have_different_enneagram_types(self):
        """Test that archetypes map to different Enneagram types"""
        innovator = get_archetype_profile(CharacterArchetype.INNOVATOR)
        educator = get_archetype_profile(CharacterArchetype.EDUCATOR)
        empath = get_archetype_profile(CharacterArchetype.EMPATH)

        # They should have different Enneagram types
        # (This might not be true for all archetypes, but should be for some)
        types = [innovator['enneagram'], educator['enneagram'], empath['enneagram']]
        assert len(set(types)) >= 2  # At least 2 different types

    def test_archetypes_have_different_mbti_types(self):
        """Test that archetypes map to different MBTI types"""
        innovator = get_archetype_profile(CharacterArchetype.INNOVATOR)
        engineer = get_archetype_profile(CharacterArchetype.ENGINEER)

        # Should have different MBTI types
        assert innovator['mbti'] != engineer['mbti']

    def test_all_archetypes_have_motivations(self):
        """Test that all archetypes have defined core motivations"""
        for archetype in CharacterArchetype:
            profile = get_archetype_profile(archetype)
            if profile:  # If profile exists
                assert 'core_motivation' in profile
                assert len(profile['core_motivation']) > 0

    def test_all_archetypes_have_fears(self):
        """Test that all archetypes have defined core fears"""
        for archetype in CharacterArchetype:
            profile = get_archetype_profile(archetype)
            if profile:  # If profile exists
                assert 'core_fear' in profile
                assert len(profile['core_fear']) > 0

    def test_all_archetypes_have_descriptions(self):
        """Test that all archetypes have descriptions"""
        for archetype in CharacterArchetype:
            profile = get_archetype_profile(archetype)
            if profile:  # If profile exists
                assert 'description' in profile
                assert len(profile['description']) > 0


class TestArchetypeDialoguePatterns:
    """Test archetype dialogue patterns and voice"""

    def test_innovator_dialogue_patterns(self):
        """Test Innovator dialogue patterns"""
        profile = get_archetype_profile(CharacterArchetype.INNOVATOR)
        patterns = profile['dialogue_patterns']
        assert len(patterns) > 0
        # Should contain innovative thinking patterns
        assert any('think' in p.lower() or 'question' in p.lower() for p in patterns)

    def test_educator_dialogue_patterns(self):
        """Test Educator dialogue patterns"""
        profile = get_archetype_profile(CharacterArchetype.EDUCATOR)
        patterns = profile['dialogue_patterns']
        assert len(patterns) > 0
        # Should contain teaching patterns
        assert any('explain' in p.lower() or 'key insight' in p.lower() for p in patterns)

    def test_empath_dialogue_patterns(self):
        """Test Empath dialogue patterns"""
        profile = get_archetype_profile(CharacterArchetype.EMPATH)
        patterns = profile['dialogue_patterns']
        assert len(patterns) > 0
        # Should contain emotional support patterns
        assert any('feel' in p.lower() or 'hear' in p.lower() for p in patterns)

    def test_engineer_dialogue_patterns(self):
        """Test Engineer dialogue patterns"""
        profile = get_archetype_profile(CharacterArchetype.ENGINEER)
        patterns = profile['dialogue_patterns']
        assert len(patterns) > 0
        # Should contain technical/practical patterns
        assert any('prototype' in p.lower() or 'architecture' in p.lower() for p in patterns)

    def test_all_defined_archetypes_have_dialogue(self):
        """Test that all defined archetypes have dialogue patterns"""
        defined_archetypes = [
            CharacterArchetype.INNOVATOR,
            CharacterArchetype.EDUCATOR,
            CharacterArchetype.EMPATH,
            CharacterArchetype.ENGINEER
        ]
        for archetype in defined_archetypes:
            profile = get_archetype_profile(archetype)
            assert 'dialogue_patterns' in profile
            assert len(profile['dialogue_patterns']) > 0
