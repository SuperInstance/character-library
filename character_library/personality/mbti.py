"""
MBTI Personality Types

Myers-Briggs Type Indicator (MBTI) is a personality typology based on
Jungian psychology that categorizes people into 16 distinct personality
types based on four dichotomies:

Dichotomies:
- Extraversion (E) vs Introversion (I): Energy direction
- Sensing (S) vs Intuition (N): Information processing
- Thinking (T) vs Feeling (F): Decision making
- Judging (J) vs Perceiving (P): Lifestyle orientation

This results in 16 possible personality types, each with unique
cognitive function preferences and behavioral patterns.
"""

from enum import Enum


class MBTIType(Enum):
    """Myers-Briggs Type Indicator personality types"""

    # Analysts (INTJ, INTP, ENTJ, ENTP)
    INTJ = "INTJ - The Architect"
    """Imaginative, strategic, planner"""

    INTP = "INTP - The Thinker"
    """Logician, innovative, curious"""

    ENTJ = "ENTJ - The Commander"
    """Bold, strategic, leader"""

    ENTP = "ENTP - The Debater"
    """Smart, curious, challenger"""

    # Diplomats (INFJ, INFP, ENFJ, ENFP)
    INFJ = "INFJ - The Advocate"
    """Quiet, mystical, idealist"""

    INFP = "INFP - The Mediator"
    """Poetic, kind, altruist"""

    ENFJ = "ENFJ - The Protagonist"
    """Charismatic, inspiring, leader"""

    ENFP = "ENFP - The Campaigner"
    """Enthusiastic, creative, sociable"""

    # Sentinels (ISTJ, ISFJ, ESTJ, ESFJ)
    ISTJ = "ISTJ - The Logistician"
    """Practical, fact-minded, reliable"""

    ISFJ = "ISFJ - The Defender"
    """Warm, dedicated, protector"""

    ESTJ = "ESTJ - The Executive"
    """Excellent administrator, organizer"""

    ESFJ = "ESFJ - The Consul"
    """Caring, social, traditional"""

    # Explorers (ISTP, ISFP, ESTP, ESFP)
    ISTP = "ISTP - The Virtuoso"
    """Bold, practical, experimenter"""

    ISFP = "ISFP - The Adventurer"
    """Artistic, flexible, charming"""

    ESTP = "ESTP - The Entrepreneur"
    """Smart, energetic, perceptive"""

    ESFP = "ESFP - The Entertainer"
    """Spontaneous, energetic, enthusiastic"""

    def get_letter_code(self) -> str:
        """Get the 4-letter MBTI code"""
        return self.value.split()[0]

    def get_group(self) -> str:
        """Get the temperament group"""
        code = self.get_letter_code()

        if code in ["INTJ", "INTP", "ENTJ", "ENTP"]:
            return "Analyst"
        elif code in ["INFJ", "INFP", "ENFJ", "ENFP"]:
            return "Diplomat"
        elif code in ["ISTJ", "ISFJ", "ESTJ", "ESFJ"]:
            return "Sentinel"
        else:
            return "Explorer"

    def get_cognitive_functions(self) -> list:
        """Get the cognitive function stack for this type"""
        code = self.get_letter_code()

        # Cognitive function stacks for each type
        function_stacks = {
            "INTJ": ["Ni", "Te", "Fi", "Se"],
            "INTP": ["Ti", "Ne", "Si", "Fe"],
            "ENTJ": ["Te", "Ni", "Se", "Fi"],
            "ENTP": ["Ne", "Ti", "Fe", "Si"],

            "INFJ": ["Ni", "Fe", "Ti", "Se"],
            "INFP": ["Fi", "Ne", "Si", "Te"],
            "ENFJ": ["Fe", "Ni", "Se", "Ti"],
            "ENFP": ["Ne", "Fi", "Te", "Si"],

            "ISTJ": ["Si", "Te", "Fi", "Ne"],
            "ISFJ": ["Si", "Fe", "Ti", "Ne"],
            "ESTJ": ["Te", "Si", "Ne", "Fi"],
            "ESFJ": ["Fe", "Si", "Ne", "Ti"],

            "ISTP": ["Ti", "Se", "Ni", "Fe"],
            "ISFP": ["Fi", "Se", "Ni", "Te"],
            "ESTP": ["Se", "Ti", "Fe", "Ni"],
            "ESFP": ["Se", "Fi", "Te", "Ni"]
        }

        return function_stacks.get(code, [])

    def get_strengths(self) -> list:
        """Get common strengths for this type"""
        code = self.get_letter_code()

        strengths_map = {
            "INTJ": ["Strategic thinking", "Long-term planning", "Independence", "Perfectionism"],
            "INTP": ["Analysis", "Curiosity", "Objectivity", "Flexibility"],
            "ENTJ": ["Leadership", "Efficiency", "Confidence", "Strategic planning"],
            "ENTP": ["Innovation", "Debate", "Adaptability", "Quick thinking"],

            "INFJ": ["Insight", "Empathy", "Idealism", "Creativity"],
            "INFP": ["Compassion", "Creativity", "Open-mindedness", "Loyalty"],
            "ENFJ": ["Charisma", "Leadership", "Empathy", "Communication"],
            "ENFP": ["Enthusiasm", "Creativity", "Social skills", "Flexibility"],

            "ISTJ": ["Reliability", "Organization", "Loyalty", "Practicality"],
            "ISFJ": ["Support", "Loyalty", "Attention to detail", "Warmth"],
            "ESTJ": ["Organization", "Leadership", "Efficiency", "Reliability"],
            "ESFJ": ["Social skills", "Loyalty", "Practicality", "Care"],

            "ISTP": ["Problem-solving", "Adaptability", "Calmness", "Practical skills"],
            "ISFP": ["Artistry", "Flexibility", "Observation", "Kindness"],
            "ESTP": ["Boldness", "Quick thinking", "Adaptability", "Practicality"],
            "ESFP": ["Enthusiasm", "Social skills", "Spontaneity", "Energy"]
        }

        return strengths_map.get(code, [])

    def get_weaknesses(self) -> list:
        """Get common weaknesses for this type"""
        code = self.get_letter_code()

        weaknesses_map = {
            "INTJ": ["Arrogance", "Perfectionism", "Impatience", "Judgmental"],
            "INTP": ["Procrastination", "Insensitivity", "Absent-mindedness", "Dislike of rules"],
            "ENTJ": ["Intolerance", "Impatience", "Stubbornness", "Coldness"],
            "ENTP": ["Argumentativeness", "Difficulty focusing", "Sensitivity", "Dislike of routine"],

            "INFJ": ["Burnout", "Extremism", "Private", "Perfectionism"],
            "INFP": ["Too idealistic", "Difficult to get to know", "Impractical", "Self-critical"],
            "ENFJ": ["Too selfless", "Unrealistic", "Too sensitive", "Fluctuating self-esteem"],
            "ENFP": ["Stressful", "Overthinking", "Emotional", "Difficulty focusing"],

            "ISTJ": ["Judgmental", "Insensitive", "Blame themselves", "Rigid"],
            "ISFJ": ["Modest", "Take things too personally", "Repress feelings", "Overload"],
            "ESTJ": ["Stubborn", "Uncomfortable with change", "Judgmental", "Difficulty relaxing"],
            "ESFJ": ["Insecure", "Vulnerable to criticism", "Needy", "Self-sacrificing"],

            "ISTP": ["Private", "Insensitive", "Easily bored", "Commitment-phobic"],
            "ISFP": ["Too sensitive", "Fluctuating self-esteem", "Unpredictable", "Dislike of conflict"],
            "ESTP": ["Impatient", "Risk-prone", "Miss the bigger picture", "Unstructured"],
            "ESFP": ["Sensitive", "Bored easily", "Poor long-term planners", "Conflict-averse"]
        }

        return weaknesses_map.get(code, [])
