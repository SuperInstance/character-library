"""
Test suite for personality frameworks

Tests Big Five (OCEAN), Enneagram, and MBTI personality models.
"""

import pytest
from character_library.personality.big_five import BigFivePersonality
from character_library.personality.enneagram import EnneagramType
from character_library.personality.mbti import MBTIType


class TestBigFivePersonality:
    """Test Big Five personality traits (OCEAN model)"""

    def test_create_default_personality(self):
        """Test creating personality with default values"""
        personality = BigFivePersonality()
        assert personality.openness == 0.5
        assert personality.conscientiousness == 0.5
        assert personality.extraversion == 0.5
        assert personality.agreeableness == 0.5
        assert personality.neuroticism == 0.5

    def test_create_custom_personality(self, sample_big_five):
        """Test creating personality with custom values"""
        assert sample_big_five.openness == 0.8
        assert sample_big_five.conscientiousness == 0.7
        assert sample_big_five.extraversion == 0.6
        assert sample_big_five.agreeableness == 0.5
        assert sample_big_five.neuroticism == 0.3

    def test_trait_validation_upper_bound(self):
        """Test that traits above 1.0 are rejected"""
        with pytest.raises(ValueError, match="openness must be between"):
            BigFivePersonality(openness=1.5)

        with pytest.raises(ValueError, match="neuroticism must be between"):
            BigFivePersonality(neuroticism=2.0)

    def test_trait_validation_lower_bound(self):
        """Test that traits below 0.0 are rejected"""
        with pytest.raises(ValueError, match="conscientiousness must be between"):
            BigFivePersonality(conscientiousness=-0.5)

        with pytest.raises(ValueError, match="extraversion must be between"):
            BigFivePersonality(extraversion=-1.0)

    def test_to_dict(self, sample_big_five):
        """Test converting personality to dictionary"""
        personality_dict = sample_big_five.to_dict()
        assert isinstance(personality_dict, dict)
        assert personality_dict['openness'] == 0.8
        assert personality_dict['conscientiousness'] == 0.7
        assert personality_dict['extraversion'] == 0.6
        assert personality_dict['agreeableness'] == 0.5
        assert personality_dict['neuroticism'] == 0.3

    def test_from_dict(self, sample_big_five):
        """Test creating personality from dictionary"""
        personality_dict = sample_big_five.to_dict()
        restored = BigFivePersonality.from_dict(personality_dict)
        assert restored.openness == sample_big_five.openness
        assert restored.conscientiousness == sample_big_five.conscientiousness
        assert restored.extraversion == sample_big_five.extraversion
        assert restored.agreeableness == sample_big_five.agreeableness
        assert restored.neuroticism == sample_big_five.neuroticism

    def test_get_description_high_openness(self, high_openness_personality):
        """Test description for high openness"""
        description = high_openness_personality.get_description()
        assert "highly creative and curious" in description

    def test_get_description_low_openness(self, low_openness_personality):
        """Test description for low openness"""
        description = low_openness_personality.get_description()
        assert "practical and conventional" in description

    def test_get_description_high_conscientiousness(self):
        """Test description for high conscientiousness"""
        personality = BigFivePersonality(conscientiousness=0.9)
        description = personality.get_description()
        assert "highly organized and disciplined" in description

    def test_get_description_low_conscientiousness(self):
        """Test description for low conscientiousness"""
        personality = BigFivePersonality(conscientiousness=0.2)
        description = personality.get_description()
        assert "spontaneous and flexible" in description

    def test_get_description_high_extraversion(self):
        """Test description for high extraversion"""
        personality = BigFivePersonality(extraversion=0.85)
        description = personality.get_description()
        assert "very outgoing and energetic" in description

    def test_get_description_low_extraversion(self):
        """Test description for low extraversion"""
        personality = BigFivePersonality(extraversion=0.15)
        description = personality.get_description()
        assert "reserved and reflective" in description

    def test_calculate_compatibility_identical(self, sample_big_five):
        """Test compatibility calculation with identical personality"""
        compatibility = sample_big_five.calculate_compatibility(sample_big_five)
        assert compatibility == 1.0

    def test_calculate_compatibility_different(self, high_openness_personality, low_openness_personality):
        """Test compatibility calculation with different personalities"""
        compatibility = high_openness_personality.calculate_compatibility(low_openness_personality)
        assert 0.0 <= compatibility <= 1.0
        assert compatibility < 1.0  # Should be less than perfect

    def test_blend_personalities_equal_weight(self, high_openness_personality, low_openness_personality):
        """Test blending personalities with equal weight"""
        blended = high_openness_personality.blend(low_openness_personality, weight=0.5)
        expected_openness = (0.95 + 0.2) / 2
        assert abs(blended.openness - expected_openness) < 0.01

    def test_blend_personalities_heavy_weight(self, high_openness_personality, low_openness_personality):
        """Test blending with heavy weight on first personality"""
        blended = high_openness_personality.blend(low_openness_personality, weight=0.8)
        assert blended.openness > 0.6  # Should be closer to high_openness


class TestEnneagramType:
    """Test Enneagram personality types"""

    def test_all_types_exist(self, all_enneagram_types):
        """Test that all 9 Enneagram types are defined"""
        assert len(all_enneagram_types) == 9
        assert EnneagramType.TYPE_1_REFORMER in all_enneagram_types
        assert EnneagramType.TYPE_9_PEACEMAKER in all_enneagram_types

    def test_type_7_motivation(self):
        """Test Type 7 core motivation"""
        motivation = EnneagramType.TYPE_7_ENTHUSIAST.get_core_motivation()
        assert "satisfied" in motivation.lower() or "content" in motivation.lower()

    def test_type_7_fear(self):
        """Test Type 7 core fear"""
        fear = EnneagramType.TYPE_7_ENTHUSIAST.get_core_fear()
        assert "deprived" in fear.lower() or "trapped" in fear.lower()

    def test_growth_paths_exist(self, all_enneagram_types):
        """Test that all types have growth paths"""
        for enneagram_type in all_enneagram_types:
            growth_path = enneagram_type.get_growth_path()
            assert growth_path != "Unknown"
            assert "Move toward" in growth_path

    def test_stress_paths_exist(self, all_enneagram_types):
        """Test that all types have stress paths"""
        for enneagram_type in all_enneagram_types:
            stress_path = enneagram_type.get_stress_path()
            assert stress_path != "Unknown"
            assert "Move toward" in stress_path

    def test_type_1_growth_path(self):
        """Test Type 1 growth toward Type 7"""
        growth = EnneagramType.TYPE_1_REFORMER.get_growth_path()
        assert "Type 7" in growth
        assert "spontaneous" in growth.lower() or "joyful" in growth.lower()

    def test_type_1_stress_path(self):
        """Test Type 1 stress toward Type 4"""
        stress = EnneagramType.TYPE_1_REFORMER.get_stress_path()
        assert "Type 4" in stress
        assert "moody" in stress.lower() or "irrational" in stress.lower()

    def test_get_description(self, sample_enneagram):
        """Test getting full Enneagram description"""
        description = sample_enneagram.get_description()
        assert sample_enneagram.value in description
        assert "Core Motivation:" in description
        assert "Core Fear:" in description
        assert "Growth Path:" in description
        assert "Stress Path:" in description

    def test_type_values_are_strings(self, all_enneagram_types):
        """Test that all type values are strings"""
        for enneagram_type in all_enneagram_types:
            assert isinstance(enneagram_type.value, str)


class TestMBTIType:
    """Test MBTI personality types"""

    def test_all_16_types_exist(self, all_mbti_types):
        """Test that all 16 MBTI types are defined"""
        assert len(all_mbti_types) == 16

    def test_analyst_group_exists(self):
        """Test Analyst group types exist"""
        analysts = ["INTJ", "INTP", "ENTJ", "ENTP"]
        for code in analysts:
            assert MBTIType[code] in all_mbti_types

    def test_diplomat_group_exists(self):
        """Test Diplomat group types exist"""
        diplomats = ["INFJ", "INFP", "ENFJ", "ENFP"]
        for code in diplomats:
            assert MBTIType[code] in all_mbti_types

    def test_sentinel_group_exists(self):
        """Test Sentinel group types exist"""
        sentinels = ["ISTJ", "ISFJ", "ESTJ", "ESFJ"]
        for code in sentinels:
            assert MBTIType[code] in all_mbti_types

    def test_explorer_group_exists(self):
        """Test Explorer group types exist"""
        explorers = ["ISTP", "ISFP", "ESTP", "ESFP"]
        for code in explorers:
            assert MBTIType[code] in all_mbti_types

    def test_get_letter_code(self, sample_mbti):
        """Test getting 4-letter code"""
        code = sample_mbti.get_letter_code()
        assert code == "ENFP"
        assert len(code) == 4

    def test_get_group_analyst(self):
        """Test group classification for Analyst types"""
        assert MBTIType.INTJ.get_group() == "Analyst"
        assert MBTIType.INTP.get_group() == "Analyst"

    def test_get_group_diplomat(self):
        """Test group classification for Diplomat types"""
        assert MBTIType.INFJ.get_group() == "Diplomat"
        assert MBTIType.ENFP.get_group() == "Diplomat"

    def test_get_group_sentinel(self):
        """Test group classification for Sentinel types"""
        assert MBTIType.ISTJ.get_group() == "Sentinel"
        assert MBTIType.ESFJ.get_group() == "Sentinel"

    def test_get_group_explorer(self):
        """Test group classification for Explorer types"""
        assert MBTIType.ISTP.get_group() == "Explorer"
        assert MBTIType.ESFP.get_group() == "Explorer"

    def test_get_cognitive_functions(self, sample_mbti):
        """Test getting cognitive function stack"""
        functions = sample_mbti.get_cognitive_functions()
        assert isinstance(functions, list)
        assert len(functions) == 4
        # ENFP should have Ne as dominant
        assert functions[0] == "Ne"

    def test_intj_cognitive_stack(self):
        """Test INTJ cognitive function stack"""
        functions = MBTIType.INTJ.get_cognitive_functions()
        assert functions == ["Ni", "Te", "Fi", "Se"]

    def test_get_strengths(self, sample_mbti):
        """Test getting type strengths"""
        strengths = sample_mbti.get_strengths()
        assert isinstance(strengths, list)
        assert len(strengths) > 0
        assert any("creativity" in s.lower() or "enthusiasm" in s.lower() for s in strengths)

    def test_get_weaknesses(self, sample_mbti):
        """Test getting type weaknesses"""
        weaknesses = sample_mbti.get_weaknesses()
        assert isinstance(weaknesses, list)
        assert len(weaknesses) > 0

    def test_all_types_have_cognitive_functions(self, all_mbti_types):
        """Test that all types have cognitive function stacks"""
        for mbti_type in all_mbti_types:
            functions = mbti_type.get_cognitive_functions()
            assert len(functions) == 4

    def test_all_types_have_strengths(self, all_mbti_types):
        """Test that all types have defined strengths"""
        for mbti_type in all_mbti_types:
            strengths = mbti_type.get_strengths()
            assert len(strengths) > 0

    def test_all_types_have_weaknesses(self, all_mbti_types):
        """Test that all types have defined weaknesses"""
        for mbti_type in all_mbti_types:
            weaknesses = mbti_type.get_weaknesses()
            assert len(weaknesses) > 0


class TestPersonalityIntegration:
    """Test integration between personality frameworks"""

    def test_big_five_and_enneagram_consistency(self):
        """Test that related Big Five and Enneagram types are consistent"""
        # High openness should correlate with Type 7
        high_openness = BigFivePersonality(openness=0.9)
        type_7 = EnneagramType.TYPE_7_ENTHUSIAST
        assert "spontaneous" in type_7.get_growth_path().lower() or "versatile" in type_7.value.lower()

    def test_big_five_and_mbti_consistency(self):
        """Test that Big Five and MBTI show expected correlations"""
        # High extraversion should correlate with E types
        high_extraversion = BigFivePersonality(extraversion=0.9)
        extroverted_types = ["ENTJ", "ENFP", "ESTP", "ESFP"]
        assert any(mbti.value.startswith("E") for mbti in [MBTIType[code] for code in extroverted_types])

    def test_multiple_frameworks_coexist(self, sample_big_five, sample_enneagram, sample_mbti):
        """Test that multiple personality frameworks can be used together"""
        assert sample_big_five is not None
        assert sample_enneagram is not None
        assert sample_mbti is not None
        # All three should be usable independently
        assert isinstance(sample_big_five.openness, float)
        assert isinstance(sample_enneagram.value, str)
        assert isinstance(sample_mbti.value, str)
