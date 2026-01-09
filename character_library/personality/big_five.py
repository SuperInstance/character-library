"""
Big Five Personality Traits (OCEAN Model)

The Big Five personality traits, also known as the Five Factor Model,
is a widely accepted model in personality psychology that describes
human personality through five main dimensions.

Dimensions:
- Openness: Creativity, curiosity, preference for variety
- Conscientiousness: Organization, discipline, goal-orientation
- Extraversion: Social energy, stimulation-seeking, expressiveness
- Agreeableness: Cooperation, trust, compassion
- Neuroticism: Emotional stability, reactivity, stress response
"""

from typing import Dict
from dataclasses import dataclass


@dataclass
class BigFivePersonality:
    """
    Big Five personality traits (OCEAN)

    Attributes:
        openness: Openness to experience (0.0 to 1.0)
            - High: Creative, curious, adventurous
            - Low: Practical, conventional, prefers routine

        conscientiousness: Organization and discipline (0.0 to 1.0)
            - High: Organized, disciplined, achievement-oriented
            - Low: Spontaneous, flexible, casual

        extraversion: Social energy and stimulation (0.0 to 1.0)
            - High: Outgoing, energetic, assertive
            - Low: Reserved, reflective, prefers solitude

        agreeableness: Cooperation and social harmony (0.0 to 1.0)
            - High: Cooperative, trusting, compassionate
            - Low: Competitive, critical, skeptical

        neuroticism: Emotional stability and reactivity (0.0 to 1.0)
            - High: Sensitive, anxious, moody
            - Low: Confident, calm, emotionally stable
    """
    openness: float = 0.5
    conscientiousness: float = 0.5
    extraversion: float = 0.5
    agreeableness: float = 0.5
    neuroticism: float = 0.5

    def __post_init__(self):
        """Validate trait values are in valid range"""
        for trait_name, value in [
            ('openness', self.openness),
            ('conscientiousness', self.conscientiousness),
            ('extraversion', self.extraversion),
            ('agreeableness', self.agreeableness),
            ('neuroticism', self.neuroticism)
        ]:
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{trait_name} must be between 0.0 and 1.0, got {value}")

    def to_dict(self) -> Dict[str, float]:
        """Convert personality to dictionary"""
        return {
            'openness': self.openness,
            'conscientiousness': self.conscientiousness,
            'extraversion': self.extraversion,
            'agreeableness': self.agreeableness,
            'neuroticism': self.neuroticism
        }

    @classmethod
    def from_dict(cls, data: Dict[str, float]) -> 'BigFivePersonality':
        """Create personality from dictionary"""
        return cls(**data)

    def get_description(self) -> str:
        """Get a textual description of the personality profile"""
        descriptions = []

        # Openness
        if self.openness > 0.7:
            descriptions.append("highly creative and curious")
        elif self.openness < 0.3:
            descriptions.append("practical and conventional")
        else:
            descriptions.append("balanced in openness")

        # Conscientiousness
        if self.conscientiousness > 0.7:
            descriptions.append("highly organized and disciplined")
        elif self.conscientiousness < 0.3:
            descriptions.append("spontaneous and flexible")

        # Extraversion
        if self.extraversion > 0.7:
            descriptions.append("very outgoing and energetic")
        elif self.extraversion < 0.3:
            descriptions.append("reserved and reflective")

        # Agreeableness
        if self.agreeableness > 0.7:
            descriptions.append("very cooperative and compassionate")
        elif self.agreeableness < 0.3:
            descriptions.append("competitive and skeptical")

        # Neuroticism
        if self.neuroticism > 0.7:
            descriptions.append("emotionally sensitive")
        elif self.neuroticism < 0.3:
            descriptions.append("emotionally stable and confident")

        return ", ".join(descriptions)

    def calculate_compatibility(self, other: 'BigFivePersonality') -> float:
        """
        Calculate compatibility with another personality profile

        Returns:
            float: Compatibility score from 0.0 to 1.0
        """
        # Calculate absolute differences
        openness_diff = abs(self.openness - other.openness)
        conscientiousness_diff = abs(self.conscientiousness - other.conscientiousness)
        extraversion_diff = abs(self.extraversion - other.extraversion)
        agreeableness_diff = abs(self.agreeableness - other.agreeableness)
        neuroticism_diff = abs(self.neuroticism - other.neuroticism)

        # Average difference
        avg_diff = (openness_diff + conscientiousness_diff +
                   extraversion_diff + agreeableness_diff +
                   neuroticism_diff) / 5.0

        # Convert to compatibility (lower difference = higher compatibility)
        compatibility = 1.0 - avg_diff

        return compatibility

    def blend(self, other: 'BigFivePersonality', weight: float = 0.5) -> 'BigFivePersonality':
        """
        Blend this personality with another

        Args:
            other: The other personality to blend with
            weight: Weight for this personality (0.0 to 1.0)
                    1.0 = fully this personality, 0.0 = fully other personality

        Returns:
            BigFivePersonality: A new blended personality
        """
        return BigFivePersonality(
            openness=self.openness * weight + other.openness * (1 - weight),
            conscientiousness=self.conscientiousness * weight + other.conscientiousness * (1 - weight),
            extraversion=self.extraversion * weight + other.extraversion * (1 - weight),
            agreeableness=self.agreeableness * weight + other.agreeableness * (1 - weight),
            neuroticism=self.neuroticism * weight + other.neuroticism * (1 - weight)
        )
