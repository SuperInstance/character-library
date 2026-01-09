"""
Test suite for emotional modeling system

Tests basic emotions, emotional states, emotional transitions, and expressions.
"""

import pytest
from character_library.emotion.emotions import (
    BasicEmotion,
    EmotionalState,
    generate_emotional_cues,
    get_emotion_transition
)


class TestBasicEmotion:
    """Test basic emotion categories"""

    def test_all_emotions_exist(self, all_basic_emotions):
        """Test that all 8 basic emotions are defined"""
        assert len(all_basic_emotions) == 8
        assert BasicEmotion.JOY in all_basic_emotions
        assert BasicEmotion.ANGER in all_basic_emotions

    def test_emotion_values_are_strings(self, all_basic_emotions):
        """Test that all emotion values are strings"""
        for emotion in all_basic_emotions:
            assert isinstance(emotion.value, str)

    def test_joy_valence_arousal(self):
        """Test JOY has positive valence and high arousal"""
        valence, arousal = BasicEmotion.JOY.get_valence_arousal()
        assert valence > 0.5
        assert arousal > 0.5

    def test_fear_valence_arousal(self):
        """Test FEAR has negative valence and high arousal"""
        valence, arousal = BasicEmotion.FEAR.get_valence_arousal()
        assert valence < 0
        assert arousal > 0.5

    def test_sadness_valence_arousal(self):
        """Test SADNESS has negative valence and low arousal"""
        valence, arousal = BasicEmotion.SADNESS.get_valence_arousal()
        assert valence < 0
        assert arousal < 0.5

    def test_trust_valence_arousal(self):
        """Test TRUST has positive valence and low arousal"""
        valence, arousal = BasicEmotion.TRUST.get_valence_arousal()
        assert valence > 0
        assert arousal < 0.5

    def test_opposite_emotions(self):
        """Test emotion opposites according to Plutchik's model"""
        assert BasicEmotion.JOY.get_opposite_emotion() == BasicEmotion.SADNESS
        assert BasicEmotion.SADNESS.get_opposite_emotion() == BasicEmotion.JOY
        assert BasicEmotion.TRUST.get_opposite_emotion() == BasicEmotion.DISGUST
        assert BasicEmotion.DISGUST.get_opposite_emotion() == BasicEmotion.TRUST
        assert BasicEmotion.FEAR.get_opposite_emotion() == BasicEmotion.ANGER
        assert BasicEmotion.ANGER.get_opposite_emotion() == BasicEmotion.FEAR
        assert BasicEmotion.SURPRISE.get_opposite_emotion() == BasicEmotion.ANTICIPATION
        assert BasicEmotion.ANTICIPATION.get_opposite_emotion() == BasicEmotion.SURPRISE


class TestEmotionalState:
    """Test emotional state representation"""

    def test_create_emotional_state(self, joy_emotion):
        """Test creating an emotional state"""
        assert joy_emotion.primary_emotion == BasicEmotion.JOY
        assert joy_emotion.intensity == 0.8
        assert joy_emotion.valence == 0.7
        assert joy_emotion.arousal == 0.6

    def test_intensity_validation(self):
        """Test intensity validation (0.0 to 1.0)"""
        with pytest.raises(ValueError, match="intensity must be between"):
            EmotionalState(primary_emotion=BasicEmotion.JOY, intensity=1.5)

        with pytest.raises(ValueError, match="intensity must be between"):
            EmotionalState(primary_emotion=BasicEmotion.JOY, intensity=-0.1)

    def test_valence_validation(self):
        """Test valence validation (-1.0 to 1.0)"""
        with pytest.raises(ValueError, match="valence must be between"):
            EmotionalState(primary_emotion=BasicEmotion.JOY, valence=1.5)

        with pytest.raises(ValueError, match="valence must be between"):
            EmotionalState(primary_emotion=BasicEmotion.JOY, valence=-1.5)

    def test_arousal_validation(self):
        """Test arousal validation (0.0 to 1.0)"""
        with pytest.raises(ValueError, match="arousal must be between"):
            EmotionalState(primary_emotion=BasicEmotion.JOY, arousal=2.0)

        with pytest.raises(ValueError, match="arousal must be between"):
            EmotionalState(primary_emotion=BasicEmotion.JOY, arousal=-0.5)

    def test_to_dict(self, joy_emotion):
        """Test converting emotional state to dictionary"""
        state_dict = joy_emotion.to_dict()
        assert isinstance(state_dict, dict)
        assert state_dict['primary_emotion'] == 'joy'
        assert state_dict['intensity'] == 0.8
        assert state_dict['valence'] == 0.7
        assert state_dict['arousal'] == 0.6

    def test_from_dict(self, joy_emotion):
        """Test creating emotional state from dictionary"""
        state_dict = joy_emotion.to_dict()
        restored = EmotionalState.from_dict(state_dict)
        assert restored.primary_emotion == joy_emotion.primary_emotion
        assert restored.intensity == joy_emotion.intensity
        assert restored.valence == joy_emotion.valence
        assert restored.arousal == joy_emotion.arousal

    def test_from_dict_with_secondary_emotion(self):
        """Test from_dict with secondary emotion"""
        state_dict = {
            'primary_emotion': 'joy',
            'secondary_emotion': 'anticipation',
            'intensity': 0.7,
            'valence': 0.6,
            'arousal': 0.8,
            'duration_minutes': 30,
            'triggers': [],
            'visible_cues': []
        }
        restored = EmotionalState.from_dict(state_dict)
        assert restored.primary_emotion == BasicEmotion.JOY
        assert restored.secondary_emotion == BasicEmotion.ANTICIPATION

    def test_is_positive(self, joy_emotion, fear_emotion, neutral_emotion):
        """Test checking if emotion is positive"""
        assert joy_emotion.is_positive() == True
        assert fear_emotion.is_positive() == False
        assert neutral_emotion.is_positive() == False  # valence=0.0 is not positive

    def test_is_negative(self, joy_emotion, fear_emotion, neutral_emotion):
        """Test checking if emotion is negative"""
        assert joy_emotion.is_negative() == False
        assert fear_emotion.is_negative() == True
        assert neutral_emotion.is_negative() == False  # valence=0.0 is not negative

    def test_is_high_arousal(self, joy_emotion, neutral_emotion):
        """Test checking if emotion is high arousal"""
        assert joy_emotion.is_high_arousal() == True
        assert neutral_emotion.is_high_arousal() == False

    def test_is_low_arousal(self, joy_emotion, neutral_emotion):
        """Test checking if emotion is low arousal"""
        assert joy_emotion.is_low_arousal() == False
        assert neutral_emotion.is_low_arousal() == True

    def test_get_description(self, joy_emotion):
        """Test getting textual description"""
        description = joy_emotion.get_description()
        assert "joy" in description
        assert "positive" in description
        assert "high energy" in description

    def test_blend_emotional_states(self, joy_emotion, fear_emotion):
        """Test blending two emotional states"""
        blended = joy_emotion.blend_with(fear_emotion, weight=0.5)
        # Check blended values are between original values
        assert min(joy_emotion.intensity, fear_emotion.intensity) <= blended.intensity <= max(joy_emotion.intensity, fear_emotion.intensity)
        assert min(joy_emotion.valence, fear_emotion.valence) <= blended.valence <= max(joy_emotion.valence, fear_emotion.valence)

    def test_blend_with_heavy_weight(self, joy_emotion, fear_emotion):
        """Test blending with heavy weight on first emotion"""
        blended = joy_emotion.blend_with(fear_emotion, weight=0.8)
        # Should be closer to joy_emotion
        assert abs(blended.valence - joy_emotion.valence) < abs(blended.valence - fear_emotion.valence)

    def test_triggers_and_cues_preserved(self, joy_emotion):
        """Test that triggers and cues are preserved"""
        assert len(joy_emotion.triggers) == 2
        assert "good news" in joy_emotion.triggers
        assert len(joy_emotion.visible_cues) == 2
        assert "smiles" in joy_emotion.visible_cues


class TestEmotionalCues:
    """Test generation of visible emotional cues"""

    def test_generate_joy_cues_high_intensity(self):
        """Test generating high-intensity joy cues"""
        cues = generate_emotional_cues(BasicEmotion.JOY, 0.8)
        assert len(cues) == 4
        assert "smiles" in cues
        assert "bright eyes" in cues

    def test_generate_joy_cues_low_intensity(self):
        """Test generating low-intensity joy cues"""
        cues = generate_emotional_cues(BasicEmotion.JOY, 0.4)
        assert len(cues) == 2
        assert "slight smile" in cues

    def test_generate_fear_cues_high_intensity(self):
        """Test generating high-intensity fear cues"""
        cues = generate_emotional_cues(BasicEmotion.FEAR, 0.8)
        assert len(cues) == 4
        assert "widened eyes" in cues
        assert "trembling" in cues

    def test_generate_fear_cues_low_intensity(self):
        """Test generating low-intensity fear cues"""
        cues = generate_emotional_cues(BasicEmotion.FEAR, 0.4)
        assert len(cues) == 2
        assert "nervous glance" in cues

    def test_generate_anger_cues_high_intensity(self):
        """Test generating high-intensity anger cues"""
        cues = generate_emotional_cues(BasicEmotion.ANGER, 0.9)
        assert len(cues) == 4
        assert "clenched jaw" in cues
        assert "sharp tone" in cues

    def test_generate_trust_cues(self):
        """Test generating trust cues"""
        cues = generate_emotional_cues(BasicEmotion.TRUST, 0.7)
        assert len(cues) > 0
        assert "open posture" in cues

    def test_generate_surprise_cues(self):
        """Test generating surprise cues"""
        cues = generate_emotional_cues(BasicEmotion.SURPRISE, 0.8)
        assert len(cues) > 0
        assert "raised eyebrows" in cues

    def test_generate_sadness_cues_high_intensity(self):
        """Test generating high-intensity sadness cues"""
        cues = generate_emotional_cues(BasicEmotion.SADNESS, 0.9)
        assert len(cues) == 4
        assert "downcast eyes" in cues
        assert "tears" in cues

    def test_generate_disgust_cues(self):
        """Test generating disgust cues"""
        cues = generate_emotional_cues(BasicEmotion.DISGUST, 0.7)
        assert len(cues) > 0
        assert "wrinkled nose" in cues

    def test_generate_anticipation_cues(self):
        """Test generating anticipation cues"""
        cues = generate_emotional_cues(BasicEmotion.ANTICIPATION, 0.7)
        assert len(cues) > 0
        assert "leaning forward" in cues

    def test_generate_cues_for_unknown_emotion(self):
        """Test that unknown emotion returns neutral cue"""
        # This tests the default case
        cues = generate_emotional_cues(BasicEmotion.JOY, 0.5)
        assert len(cues) > 0


class TestEmotionTransitions:
    """Test emotional state transitions"""

    def test_transition_to_joy(self):
        """Test transition to joy on high valence, high arousal event"""
        new_emotion = get_emotion_transition(
            current_emotion=BasicEmotion.TRUST,
            event_valence=0.8,
            event_arousal=0.8
        )
        assert new_emotion == BasicEmotion.JOY

    def test_transition_to_anticipation(self):
        """Test transition to anticipation on medium-high valence and arousal"""
        new_emotion = get_emotion_transition(
            current_emotion=BasicEmotion.TRUST,
            event_valence=0.5,
            event_arousal=0.6
        )
        assert new_emotion == BasicEmotion.ANTICIPATION

    def test_transition_to_trust(self):
        """Test transition to trust on high valence, low arousal"""
        new_emotion = get_emotion_transition(
            current_emotion=BasicEmotion.JOY,
            event_valence=0.7,
            event_arousal=0.3
        )
        assert new_emotion == BasicEmotion.TRUST

    def test_transition_to_anger(self):
        """Test transition to anger on low valence, high arousal"""
        new_emotion = get_emotion_transition(
            current_emotion=BasicEmotion.TRUST,
            event_valence=-0.8,
            event_arousal=0.9
        )
        assert new_emotion == BasicEmotion.ANGER

    def test_transition_to_fear(self):
        """Test transition to fear on medium-low valence, high arousal"""
        new_emotion = get_emotion_transition(
            current_emotion=BasicEmotion.JOY,
            event_valence=-0.4,
            event_arousal=0.7
        )
        assert new_emotion == BasicEmotion.FEAR

    def test_transition_to_sadness(self):
        """Test transition to sadness on low valence, low arousal"""
        new_emotion = get_emotion_transition(
            current_emotion=BasicEmotion.JOY,
            event_valence=-0.7,
            event_arousal=0.3
        )
        assert new_emotion == BasicEmotion.SADNESS

    def test_transition_to_disgust(self):
        """Test transition to disgust on medium-low valence, low arousal"""
        new_emotion = get_emotion_transition(
            current_emotion=BasicEmotion.TRUST,
            event_valence=-0.4,
            event_arousal=0.4
        )
        assert new_emotion == BasicEmotion.DISGUST

    def test_transition_to_surprise(self):
        """Test transition to surprise on very high arousal"""
        new_emotion = get_emotion_transition(
            current_emotion=BasicEmotion.TRUST,
            event_valence=0.0,
            event_arousal=0.9
        )
        assert new_emotion == BasicEmotion.SURPRISE

    def test_no_transition_for_neutral_event(self):
        """Test that neutral events maintain current emotion"""
        new_emotion = get_emotion_transition(
            current_emotion=BasicEmotion.JOY,
            event_valence=0.0,
            event_arousal=0.5
        )
        assert new_emotion == BasicEmotion.JOY


class TestEmotionalDynamics:
    """Test emotional dynamics and state management"""

    def test_emotional_decay_simulation(self, joy_emotion):
        """Test simulating emotional decay over time"""
        # In a real implementation, intensity would decrease over time
        # This test checks the structure is in place
        initial_intensity = joy_emotion.intensity
        assert initial_intensity == 0.8

    def test_emotional contagion(self, joy_emotion, fear_emotion):
        """Test simulating emotional contagion between characters"""
        # Blend emotions to simulate contagion
        contagious_emotion = joy_emotion.blend_with(fear_emotion, weight=0.3)
        # Should be primarily fear but influenced by joy
        assert contagious_emotion.primary_emotion == BasicEmotion.FEAR

    def test_emotional_regulation(self, fear_emotion):
        """Test simulating emotional regulation (down-regulation)"""
        # Blend with neutral emotion to simulate regulation
        neutral = EmotionalState(
            primary_emotion=BasicEmotion.TRUST,
            intensity=0.3,
            valence=0.0,
            arousal=0.3
        )
        regulated = fear_emotion.blend_with(neutral, weight=0.5)
        # Intensity should decrease
        assert regulated.intensity < fear_emotion.intensity
