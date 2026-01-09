"""
Enneagram Personality Types

The Enneagram is a model of the human psyche that describes nine
interconnected personality types. Each type has core motivations,
fears, and paths for growth and stress.

Types:
1. The Reformer - Principled, purposeful, self-controlled
2. The Helper - Generous, demonstrative, people-pleasing
3. The Achiever - Adaptive, excelling, driven
4. The Individualist - Expressive, dramatic, self-absorbed
5. The Investigator - Perceptive, innovative, secretive
6. The Loyalist - Engaging, responsible, anxious
7. The Enthusiast - Spontaneous, versatile, scattered
8. The Challenger - Self-confident, decisive, willful
9. The Peacemaker - Easygoing, receptive, reassuring
"""

from enum import Enum


class EnneagramType(Enum):
    """Enneagram personality types with detailed descriptions"""

    TYPE_1_REFORMER = "1 - The Reformer"
    """Principled, purposeful, self-controlled, perfectionist"""

    TYPE_2_HELPER = "2 - The Helper"
    """Generous, demonstrative, people-pleasing, possessive"""

    TYPE_3_ACHIEVER = "3 - The Achiever"
    """Adaptive, excelling, driven, image-conscious"""

    TYPE_4_INDIVIDUALIST = "4 - The Individualist"
    """Expressive, dramatic, self-absorbed, temperamental"""

    TYPE_5_INVESTIGATOR = "5 - The Investigator"
    """Perceptive, innovative, secretive, isolated"""

    TYPE_6_LOYALIST = "6 - The Loyalist"
    """Engaging, responsible, anxious, suspicious"""

    TYPE_7_ENTHUSIAST = "7 - The Enthusiast"
    """Spontaneous, versatile, scattered, excessive"""

    TYPE_8_CHALLENGER = "8 - The Challenger"
    """Self-confident, decisive, willful, confrontational"""

    TYPE_9_PEACEMAKER = "9 - The Peacemaker"
    """Easygoing, receptive, reassuring, complacent"""

    def get_core_motivation(self) -> str:
        """Get the core motivation for this type"""
        motivations = {
            self.TYPE_1_REFORMER: "To be good, to have integrity, to balance things",
            self.TYPE_2_HELPER: "To be loved, to be needed, to be appreciated",
            self.TYPE_3_ACHIEVER: "To be valuable, to be successful, to be admired",
            self.TYPE_4_INDIVIDUALIST: "To be themselves, to express themselves, to be authentic",
            self.TYPE_5_INVESTIGATOR: "To be capable, to understand, to master knowledge",
            self.TYPE_6_LOYALIST: "To be secure, to be supported, to have guidance",
            self.TYPE_7_ENTHUSIAST: "To be satisfied, to be content, to find fulfillment",
            self.TYPE_8_CHALLENGER: "To be self-reliant, to be strong, to protect themselves",
            self.TYPE_9_PEACEMAKER: "To have peace, to be harmonious, to avoid conflict"
        }
        return motivations.get(self, "Unknown")

    def get_core_fear(self) -> str:
        """Get the core fear for this type"""
        fears = {
            self.TYPE_1_REFORMER: "Being corrupt, defective, evil",
            self.TYPE_2_HELPER: "Being unwanted, unloved, unnecessary",
            self.TYPE_3_ACHIEVER: "Being worthless, failures, incapable",
            self.TYPE_4_INDIVIDUALIST: "Being deficient, flawed, ordinary",
            self.TYPE_5_INVESTIGATOR: "Being useless, helpless, incapable",
            self.TYPE_6_LOYALIST: "Being without support, guidance, security",
            self.TYPE_7_ENTHUSIAST: "Being deprived, trapped in emotional pain",
            self.TYPE_8_CHALLENGER: "Being harmed, controlled, violated",
            self.TYPE_9_PEACEMAKER: "Being lost, separated, in conflict"
        }
        return fears.get(self, "Unknown")

    def get_growth_path(self) -> str:
        """Get the growth path (integration) for this type"""
        growth_paths = {
            self.TYPE_1_REFORMER: "Move toward Type 7 - Become more spontaneous and joyful",
            self.TYPE_2_HELPER: "Move toward Type 4 - Become more self-aware and authentic",
            self.TYPE_3_ACHIEVER: "Move toward Type 6 - Become more cooperative and committed",
            self.TYPE_4_INDIVIDUALIST: "Move toward Type 1 - Become more principled and objective",
            self.TYPE_5_INVESTIGATOR: "Move toward Type 8 - Become more confident and decisive",
            self.TYPE_6_LOYALIST: "Move toward Type 9 - Become more trusting and peaceful",
            self.TYPE_7_ENTHUSIAST: "Move toward Type 5 - Become more focused and deep",
            self.TYPE_8_CHALLENGER: "Move toward Type 2 - Become more vulnerable and loving",
            self.TYPE_9_PEACEMAKER: "Move toward Type 3 - Become more self-directed and energetic"
        }
        return growth_paths.get(self, "Unknown")

    def get_stress_path(self) -> str:
        """Get the stress path (disintegration) for this type"""
        stress_paths = {
            self.TYPE_1_REFORMER: "Move toward Type 4 - Become moody and irrational",
            self.TYPE_2_HELPER: "Move toward Type 8 - Become aggressive and controlling",
            self.TYPE_3_ACHIEVER: "Move toward Type 9 - Become disengaged and apathetic",
            self.TYPE_4_INDIVIDUALIST: "Move toward Type 2 - Become clingy and dependent",
            self.TYPE_5_INVESTIGATOR: "Move toward Type 7 - Become scattered and hyperactive",
            self.TYPE_6_LOYALIST: "Move toward Type 3 - Become image-conscious and workaholic",
            self.TYPE_7_ENTHUSIAST: "Move toward Type 1 - Become critical and perfectionistic",
            self.TYPE_8_CHALLENGER: "Move toward Type 5 - Become withdrawn and isolated",
            self.TYPE_9_PEACEMAKER: "Move toward Type 6 - Become anxious and pessimistic"
        }
        return stress_paths.get(self, "Unknown")

    def get_description(self) -> str:
        """Get detailed description of this type"""
        return f"""
{self.value}

Core Motivation: {self.get_core_motivation()}
Core Fear: {self.get_core_fear()}

Growth Path: {self.get_growth_path()}
Stress Path: {self.get_stress_path()}
        """.strip()
