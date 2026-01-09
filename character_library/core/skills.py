"""
Character Skills and Skill Trees

This module provides a comprehensive skill system for characters including:
- Individual skills with progression
- Skill trees with prerequisites
- Specialization systems
- Experience and mastery tracking
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum


class SkillCategory(Enum):
    """Categories of character skills"""
    COGNITIVE = "cognitive"
    SOCIAL = "social"
    CREATIVE = "creative"
    TECHNICAL = "technical"
    EMOTIONAL = "emotional"
    PHYSICAL = "physical"
    LEADERSHIP = "leadership"
    WISDOM = "wisdom"


@dataclass
class CharacterSkill:
    """
    Character skill with progression tracking

    Attributes:
        name: Name of the skill
        category: Skill category
        current_level: Current skill level (0.0 to 10.0)
        max_level: Maximum achievable level
        experience_points: Total XP earned
        prerequisites: Skills required before this can be learned
        specializations: Specialized areas within this skill
        last_practiced: When this skill was last practiced
    """
    name: str
    category: str
    current_level: float = 1.0
    max_level: float = 10.0
    experience_points: int = 0
    prerequisites: List[str] = field(default_factory=list)
    specializations: List[str] = field(default_factory=list)
    last_practiced: Optional[datetime] = None
    total_uses: int = 0
    successful_uses: int = 0

    def __post_init__(self):
        """Validate skill level"""
        if not 0.0 <= self.current_level <= self.max_level:
            raise ValueError(f"current_level must be between 0.0 and {self.max_level}")

    def practice(self, difficulty: float, performance: float, time_spent: float) -> float:
        """
        Practice the skill and improve

        Args:
            difficulty: Task difficulty (0.0 to 1.0)
            performance: Performance quality (0.0 to 1.0)
            time_spent: Time spent practicing (in hours)

        Returns:
            float: Improvement amount
        """
        # Calculate experience gained
        base_exp = int(difficulty * performance * time_spent * 10)
        self.experience_points += base_exp

        # Calculate level improvement (diminishing returns at higher levels)
        level_factor = (self.max_level - self.current_level) / self.max_level
        improvement = (difficulty * performance * time_spent * level_factor) / 100

        self.current_level = min(self.max_level, self.current_level + improvement)
        self.last_practiced = datetime.now()

        return improvement

    def use(self, success: bool = True):
        """Record a skill usage"""
        self.total_uses += 1
        if success:
            self.successful_uses += 1

    def get_success_rate(self) -> float:
        """Calculate success rate"""
        if self.total_uses == 0:
            return 0.0
        return self.successful_uses / self.total_uses

    def get_mastery_level(self) -> str:
        """Get mastery level description"""
        if self.current_level < 2.0:
            return "Novice"
        elif self.current_level < 4.0:
            return "Apprentice"
        elif self.current_level < 6.0:
            return "Journeyman"
        elif self.current_level < 8.0:
            return "Expert"
        elif self.current_level < 9.5:
            return "Master"
        else:
            return "Grandmaster"

    def add_specialization(self, specialization: str):
        """Add a specialization to this skill"""
        if specialization not in self.specializations:
            self.specializations.append(specialization)

    def to_dict(self) -> Dict[str, Any]:
        """Convert skill to dictionary"""
        return {
            'name': self.name,
            'category': self.category,
            'current_level': self.current_level,
            'max_level': self.max_level,
            'experience_points': self.experience_points,
            'prerequisites': self.prerequisites,
            'specializations': self.specializations,
            'last_practiced': self.last_practiced.isoformat() if self.last_practiced else None,
            'total_uses': self.total_uses,
            'successful_uses': self.successful_uses,
            'mastery_level': self.get_mastery_level(),
            'success_rate': self.get_success_rate()
        }


@dataclass
class SkillTree:
    """
    Skill tree structure for character development

    Attributes:
        name: Name of the skill tree
        description: Description of what this skill tree represents
        skills: Dictionary of skills in the tree
        unlock_requirements: Requirements to unlock skills
        mastery_bonuses: Bonuses granted at mastery levels
    """
    name: str
    description: str
    skills: Dict[str, CharacterSkill] = field(default_factory=dict)
    unlock_requirements: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    mastery_bonuses: Dict[str, Dict[str, float]] = field(default_factory=dict)

    def add_skill(self, skill: CharacterSkill, unlock_level: float = 0.0):
        """
        Add a skill to the tree

        Args:
            skill: The skill to add
            unlock_level: Level required to unlock this skill
        """
        self.skills[skill.name] = skill
        self.unlock_requirements[skill.name] = {'required_level': unlock_level}

    def get_skill(self, skill_name: str) -> Optional[CharacterSkill]:
        """Get a skill from the tree"""
        return self.skills.get(skill_name)

    def practice_skill(self, skill_name: str, difficulty: float,
                      performance: float, time_spent: float) -> Optional[float]:
        """
        Practice a skill in the tree

        Returns:
            float: Improvement amount, or None if skill not found
        """
        skill = self.get_skill(skill_name)
        if skill:
            return skill.practice(difficulty, performance, time_spent)
        return None

    def get_total_experience(self) -> int:
        """Get total experience across all skills"""
        return sum(skill.experience_points for skill in self.skills.values())

    def get_average_level(self) -> float:
        """Get average skill level"""
        if not self.skills:
            return 0.0
        total = sum(skill.current_level for skill in self.skills.values())
        return total / len(self.skills)

    def get_mastered_skills(self) -> List[str]:
        """Get list of mastered skill names"""
        return [name for name, skill in self.skills.items() if skill.current_level >= 9.0]

    def to_dict(self) -> Dict[str, Any]:
        """Convert skill tree to dictionary"""
        return {
            'name': self.name,
            'description': self.description,
            'skills': {name: skill.to_dict() for name, skill in self.skills.items()},
            'unlock_requirements': self.unlock_requirements,
            'mastery_bonuses': self.mastery_bonuses,
            'total_experience': self.get_total_experience(),
            'average_level': self.get_average_level(),
            'mastered_skills': self.get_mastered_skills()
        }
