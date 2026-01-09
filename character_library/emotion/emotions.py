"""
Emotional Modeling System

This module provides comprehensive emotional modeling for characters based on
psychological research, including basic emotions, emotional dimensions, and
visible emotional expressions.

Basic Emotions:
Based on Robert Plutchik's wheel of emotions, this system models 8 basic emotions:
- Joy, Trust, Fear, Surprise
- Sadness, Disgust, Anger, Anticipation

Emotional Dimensions:
- Intensity: How strong the emotion is (0.0 to 1.0)
- Valence: Positive to negative feeling (-1.0 to 1.0)
- Arousal: Calm to excited (0.0 to 1.0)
"""

from typing import Dict, List, Any
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime


class BasicEmotion(Enum):
    """Basic emotion categories based on psychological research"""

    JOY = "joy"
    """Happiness, pleasure, contentment"""

    TRUST = "trust"
    """Safety, security, confidence in others"""

    FEAR = "fear"
    """Apprehension, anxiety, feeling threatened"""

    SURPRISE = "surprise"
    """Shock, amazement, unexpectedness"""

    SADNESS = "sadness"
    """Sorrow, grief, unhappiness"""

    DISGUST = "disgust"
    """Revulsion, distaste, aversion"""

    ANGER = "anger"
    """Rage, fury, irritation"""

    ANTICIPATION = "anticipation"
    """Expectation, eagerness, preparation"""

    def get_valence_arousal(self) -> tuple:
        """
        Get the typical valence and arousal values for this emotion

        Returns:
            tuple: (valence, arousal) where valence is -1.0 to 1.0
                   and arousal is 0.0 to 1.0
        """
        valence_arousal_map = {
            BasicEmotion.JOY: (0.8, 0.7),
            BasicEmotion.TRUST: (0.7, 0.3),
            BasicEmotion.FEAR: (-0.6, 0.8),
            BasicEmotion.SURPRISE: (0.2, 0.9),
            BasicEmotion.SADNESS: (-0.7, 0.2),
            BasicEmotion.DISGUST: (-0.5, 0.4),
            BasicEmotion.ANGER: (-0.6, 0.8),
            BasicEmotion.ANTICIPATION: (0.4, 0.6)
        }
        return valence_arousal_map.get(self, (0.0, 0.5))

    def get_opposite_emotion(self) -> 'BasicEmotion':
        """Get the opposite emotion according to Plutchik's model"""
        opposites = {
            BasicEmotion.JOY: BasicEmotion.SADNESS,
            BasicEmotion.SADNESS: BasicEmotion.JOY,
            BasicEmotion.TRUST: BasicEmotion.DISGUST,
            BasicEmotion.DISGUST: BasicEmotion.TRUST,
            BasicEmotion.FEAR: BasicEmotion.ANGER,
            BasicEmotion.ANGER: BasicEmotion.FEAR,
            BasicEmotion.SURPRISE: BasicEmotion.ANTICIPATION,
            BasicEmotion.ANTICIPATION: BasicEmotion.SURPRISE
        }
        return opposites.get(self, self)


@dataclass
class EmotionalState:
    """
    Current emotional state of a character

    Attributes:
        primary_emotion: The dominant emotion
        secondary_emotion: Optional secondary emotion
        intensity: Strength of the emotion (0.0 to 1.0)
        valence: Positive to negative feeling (-1.0 to 1.0)
        arousal: Calm to excited (0.0 to 1.0)
        duration_minutes: How long the emotion will last
        triggers: What caused this emotional state
        visible_cues: Observable expressions of this emotion
    """
    primary_emotion: BasicEmotion
    secondary_emotion: BasicEmotion = None
    intensity: float = 0.5
    valence: float = 0.5
    arousal: float = 0.5
    duration_minutes: int = 30
    triggers: List[str] = field(default_factory=list)
    visible_cues: List[str] = field(default_factory=list)

    def __post_init__(self):
        """Validate emotional state parameters"""
        if not 0.0 <= self.intensity <= 1.0:
            raise ValueError(f"intensity must be between 0.0 and 1.0, got {self.intensity}")
        if not -1.0 <= self.valence <= 1.0:
            raise ValueError(f"valence must be between -1.0 and 1.0, got {self.valence}")
        if not 0.0 <= self.arousal <= 1.0:
            raise ValueError(f"arousal must be between 0.0 and 1.0, got {self.arousal}")

    def to_dict(self) -> Dict[str, Any]:
        """Convert emotional state to dictionary"""
        return {
            'primary_emotion': self.primary_emotion.value,
            'secondary_emotion': self.secondary_emotion.value if self.secondary_emotion else None,
            'intensity': self.intensity,
            'valence': self.valence,
            'arousal': self.arousal,
            'duration_minutes': self.duration_minutes,
            'triggers': self.triggers,
            'visible_cues': self.visible_cues
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'EmotionalState':
        """Create emotional state from dictionary"""
        primary = BasicEmotion(data['primary_emotion'])
        secondary = BasicEmotion(data['secondary_emotion']) if data.get('secondary_emotion') else None

        return cls(
            primary_emotion=primary,
            secondary_emotion=secondary,
            intensity=data.get('intensity', 0.5),
            valence=data.get('valence', 0.5),
            arousal=data.get('arousal', 0.5),
            duration_minutes=data.get('duration_minutes', 30),
            triggers=data.get('triggers', []),
            visible_cues=data.get('visible_cues', [])
        )

    def is_positive(self) -> bool:
        """Check if the emotion is positive"""
        return self.valence > 0.0

    def is_negative(self) -> bool:
        """Check if the emotion is negative"""
        return self.valence < 0.0

    def is_high_arousal(self) -> bool:
        """Check if the emotion is high arousal (excited)"""
        return self.arousal > 0.6

    def is_low_arousal(self) -> bool:
        """Check if the emotion is low arousal (calm)"""
        return self.arousal < 0.4

    def get_description(self) -> str:
        """Get a textual description of the emotional state"""
        intensity_desc = "mildly" if self.intensity < 0.4 else "moderately" if self.intensity < 0.7 else "intensely"

        if self.is_high_arousal():
            arousal_desc = "high energy"
        elif self.is_low_arousal():
            arousal_desc = "calm"
        else:
            arousal_desc = "moderate energy"

        valence_desc = "positive" if self.is_positive() else "negative" if self.is_negative() else "neutral"

        return f"{intensity_desc} {valence_desc} {self.primary_emotion.value} with {arousal_desc}"

    def blend_with(self, other: 'EmotionalState', weight: float = 0.5) -> 'EmotionalState':
        """
        Blend this emotional state with another

        Args:
            other: The other emotional state to blend with
            weight: Weight for this emotion (0.0 to 1.0)

        Returns:
            EmotionalState: A new blended emotional state
        """
        return EmotionalState(
            primary_emotion=self.primary_emotion if weight > 0.5 else other.primary_emotion,
            secondary_emotion=self.primary_emotion if weight <= 0.5 else other.primary_emotion,
            intensity=self.intensity * weight + other.intensity * (1 - weight),
            valence=self.valence * weight + other.valence * (1 - weight),
            arousal=self.arousal * weight + other.arousal * (1 - weight),
            duration_minutes=int(self.duration_minutes * weight + other.duration_minutes * (1 - weight)),
            triggers=self.triggers + other.triggers,
            visible_cues=self.visible_cues + other.visible_cues
        )


def generate_emotional_cues(emotion: BasicEmotion, intensity: float) -> List[str]:
    """
    Generate visible emotional cues based on emotion and intensity

    Args:
        emotion: The basic emotion
        intensity: Emotion intensity (0.0 to 1.0)

    Returns:
        List[str]: List of visible emotional cues
    """
    high_intensity = intensity > 0.6

    cues_map = {
        BasicEmotion.JOY: [
            "smiles", "bright eyes", "relaxed posture", "upturned lips"
        ] if high_intensity else ["slight smile", "relaxed shoulders"],

        BasicEmotion.TRUST: [
            "open posture", "steady gaze", "relaxed shoulders", "calm breathing"
        ],

        BasicEmotion.FEAR: [
            "widened eyes", "tense muscles", "quick breathing", "trembling"
        ] if high_intensity else ["nervous glance", "slightly tense"],

        BasicEmotion.SURPRISE: [
            "raised eyebrows", "open mouth", "slight lean back", "widened eyes"
        ],

        BasicEmotion.SADNESS: [
            "downcast eyes", "slumped shoulders", "quiet voice", "tears"
        ] if high_intensity else ["subtle frown", "lowered head"],

        BasicEmotion.DISGUST: [
            "wrinkled nose", "turned away", "tight lips", "furrowed brow"
        ],

        BasicEmotion.ANGER: [
            "clenched jaw", "tense posture", "sharp tone", "flushed face"
        ] if high_intensity else ["furrowed brow", "tight lips"],

        BasicEmotion.ANTICIPATION: [
            "leaning forward", "bright eyes", "alert posture", "subtle smile"
        ]
    }

    return cues_map.get(emotion, ["neutral expression"])


def get_emotion_transition(current_emotion: BasicEmotion,
                           event_valence: float,
                           event_arousal: float) -> BasicEmotion:
    """
    Determine emotion transition based on an event's characteristics

    Args:
        current_emotion: The current emotional state
        event_valence: Event valence (-1.0 to 1.0)
        event_arousal: Event arousal (0.0 to 1.0)

    Returns:
        BasicEmotion: The new emotion based on the event
    """
    # High valence, high arousal -> Joy or Anticipation
    if event_valence > 0.5 and event_arousal > 0.6:
        return BasicEmotion.JOY
    elif event_valence > 0.3 and event_arousal > 0.5:
        return BasicEmotion.ANTICIPATION

    # High valence, low arousal -> Trust
    elif event_valence > 0.5 and event_arousal < 0.5:
        return BasicEmotion.TRUST

    # Low valence, high arousal -> Fear or Anger
    if event_valence < -0.5 and event_arousal > 0.6:
        return BasicEmotion.ANGER
    elif event_valence < -0.3 and event_arousal > 0.5:
        return BasicEmotion.FEAR

    # Low valence, low arousal -> Sadness or Disgust
    elif event_valence < -0.5 and event_arousal < 0.5:
        return BasicEmotion.SADNESS
    elif event_valence < -0.3:
        return BasicEmotion.DISGUST

    # Medium valence, high arousal -> Surprise
    elif event_arousal > 0.7:
        return BasicEmotion.SURPRISE

    # Default: keep current emotion
    return current_emotion
