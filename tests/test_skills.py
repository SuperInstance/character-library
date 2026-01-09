"""
Test suite for character skills and skill trees

Tests individual skills, skill progression, skill trees,
and mastery systems.
"""

import pytest
from datetime import datetime
from character_library.core.skills import (
    CharacterSkill,
    SkillTree,
    SkillCategory
)


class TestCharacterSkill:
    """Test individual character skills"""

    def test_create_basic_skill(self):
        """Test creating a basic skill"""
        skill = CharacterSkill(
            name="test_skill",
            category="cognitive"
        )
        assert skill.name == "test_skill"
        assert skill.category == "cognitive"
        assert skill.current_level == 1.0
        assert skill.max_level == 10.0
        assert skill.experience_points == 0

    def test_create_skill_with_level(self):
        """Test creating a skill with initial level"""
        skill = CharacterSkill(
            name="advanced_skill",
            category="technical",
            current_level=5.0
        )
        assert skill.current_level == 5.0

    def test_skill_level_validation_upper_bound(self):
        """Test that skill level cannot exceed max_level"""
        with pytest.raises(ValueError, match="current_level must be between"):
            CharacterSkill(
                name="overpowered_skill",
                category="cognitive",
                current_level=11.0,
                max_level=10.0
            )

    def test_skill_level_validation_lower_bound(self):
        """Test that skill level cannot be negative"""
        with pytest.raises(ValueError, match="current_level must be between"):
            CharacterSkill(
                name="invalid_skill",
                category="cognitive",
                current_level=-1.0
            )

    def test_skill_prerequisites(self):
        """Test skill prerequisites"""
        skill = CharacterSkill(
            name="advanced_math",
            category="cognitive",
            prerequisites=["basic_math", "algebra"]
        )
        assert len(skill.prerequisites) == 2
        assert "basic_math" in skill.prerequisites

    def test_skill_specializations(self):
        """Test skill specializations"""
        skill = CharacterSkill(
            name="programming",
            category="technical",
            specializations=["python", "javascript", "rust"]
        )
        assert len(skill.specializations) == 3
        assert "python" in skill.specializations

    def test_practice_skill_improvement(self, cognitive_skill):
        """Test that practicing a skill improves it"""
        initial_level = cognitive_skill.current_level
        improvement = cognitive_skill.practice(
            difficulty=0.7,
            performance=0.8,
            time_spent=2.0
        )
        assert improvement > 0
        assert cognitive_skill.current_level > initial_level

    def test_practice_skill_experience_gain(self, cognitive_skill):
        """Test that practicing gains experience points"""
        initial_xp = cognitive_skill.experience_points
        cognitive_skill.practice(
            difficulty=0.5,
            performance=0.7,
            time_spent=1.5
        )
        assert cognitive_skill.experience_points > initial_xp

    def test_practice_updates_last_practiced(self, cognitive_skill):
        """Test that practicing updates last_practiced timestamp"""
        assert cognitive_skill.last_practiced is None
        cognitive_skill.practice(
            difficulty=0.5,
            performance=0.5,
            time_spent=1.0
        )
        assert cognitive_skill.last_practiced is not None
        assert isinstance(cognitive_skill.last_practiced, datetime)

    def test_practice_skill_level_cap(self, cognitive_skill):
        """Test that skill level caps at max_level"""
        # Set skill near max
        cognitive_skill.current_level = 9.99
        cognitive_skill.practice(
            difficulty=1.0,
            performance=1.0,
            time_spent=100.0
        )
        assert cognitive_skill.current_level <= cognitive_skill.max_level

    def test_use_skill_success(self, cognitive_skill):
        """Test using a skill successfully"""
        initial_uses = cognitive_skill.total_uses
        cognitive_skill.use(success=True)
        assert cognitive_skill.total_uses == initial_uses + 1
        assert cognitive_skill.successful_uses == 1

    def test_use_skill_failure(self, cognitive_skill):
        """Test using a skill unsuccessfully"""
        initial_uses = cognitive_skill.total_uses
        cognitive_skill.use(success=False)
        assert cognitive_skill.total_uses == initial_uses + 1
        assert cognitive_skill.successful_uses == 0

    def test_get_success_rate_no_uses(self, cognitive_skill):
        """Test success rate when skill hasn't been used"""
        assert cognitive_skill.get_success_rate() == 0.0

    def test_get_success_rate_with_uses(self, cognitive_skill):
        """Test success rate calculation"""
        cognitive_skill.use(success=True)
        cognitive_skill.use(success=True)
        cognitive_skill.use(success=False)
        # 2 out of 3 = 0.666...
        success_rate = cognitive_skill.get_success_rate()
        assert abs(success_rate - 0.666) < 0.01

    def test_get_mastery_level_novice(self):
        """Test mastery level for novice"""
        skill = CharacterSkill(name="test", category="cognitive", current_level=1.0)
        assert skill.get_mastery_level() == "Novice"

    def test_get_mastery_level_apprentice(self):
        """Test mastery level for apprentice"""
        skill = CharacterSkill(name="test", category="cognitive", current_level=3.0)
        assert skill.get_mastery_level() == "Apprentice"

    def test_get_mastery_level_journeyman(self):
        """Test mastery level for journeyman"""
        skill = CharacterSkill(name="test", category="cognitive", current_level=5.0)
        assert skill.get_mastery_level() == "Journeyman"

    def test_get_mastery_level_expert(self):
        """Test mastery level for expert"""
        skill = CharacterSkill(name="test", category="cognitive", current_level=7.0)
        assert skill.get_mastery_level() == "Expert"

    def test_get_mastery_level_master(self):
        """Test mastery level for master"""
        skill = CharacterSkill(name="test", category="cognitive", current_level=9.0)
        assert skill.get_mastery_level() == "Master"

    def test_get_mastery_level_grandmaster(self):
        """Test mastery level for grandmaster"""
        skill = CharacterSkill(name="test", category="cognitive", current_level=9.8)
        assert skill.get_mastery_level() == "Grandmaster"

    def test_add_specialization(self, cognitive_skill):
        """Test adding a specialization to a skill"""
        initial_count = len(cognitive_skill.specializations)
        cognitive_skill.add_specialization("new_specialization")
        assert len(cognitive_skill.specializations) == initial_count + 1
        assert "new_specialization" in cognitive_skill.specializations

    def test_add_duplicate_specialization(self, cognitive_skill):
        """Test that duplicate specializations are not added"""
        spec = "existing_spec"
        cognitive_skill.add_specialization(spec)
        initial_count = len(cognitive_skill.specializations)
        cognitive_skill.add_specialization(spec)
        assert len(cognitive_skill.specializations) == initial_count

    def test_to_dict(self, cognitive_skill):
        """Test converting skill to dictionary"""
        skill_dict = cognitive_skill.to_dict()
        assert isinstance(skill_dict, dict)
        assert skill_dict['name'] == cognitive_skill.name
        assert skill_dict['category'] == cognitive_skill.category
        assert skill_dict['current_level'] == cognitive_skill.current_level
        assert 'mastery_level' in skill_dict
        assert 'success_rate' in skill_dict


class TestSkillTree:
    """Test skill tree structure"""

    def test_create_skill_tree(self):
        """Test creating a skill tree"""
        tree = SkillTree(
            name="Combat Skills",
            description="Skills for combat"
        )
        assert tree.name == "Combat Skills"
        assert tree.description == "Skills for combat"
        assert len(tree.skills) == 0

    def test_add_skill_to_tree(self, skill_tree):
        """Test adding a skill to a tree"""
        skill = CharacterSkill(name="leadership", category="leadership")
        skill_tree.add_skill(skill, unlock_level=0.0)
        assert len(skill_tree.skills) == 1
        assert "leadership" in skill_tree.skills

    def test_get_skill_from_tree(self, skill_tree):
        """Test retrieving a skill from a tree"""
        skill = CharacterSkill(name="strategy", category="cognitive")
        skill_tree.add_skill(skill)
        retrieved = skill_tree.get_skill("strategy")
        assert retrieved is not None
        assert retrieved.name == "strategy"

    def test_get_nonexistent_skill(self, skill_tree):
        """Test retrieving a nonexistent skill returns None"""
        retrieved = skill_tree.get_skill("nonexistent")
        assert retrieved is None

    def test_practice_skill_in_tree(self, skill_tree):
        """Test practicing a skill that's in a tree"""
        skill = CharacterSkill(name="diplomacy", category="social")
        skill_tree.add_skill(skill)
        improvement = skill_tree.practice_skill(
            "diplomacy",
            difficulty=0.6,
            performance=0.7,
            time_spent=1.5
        )
        assert improvement is not None
        assert improvement > 0

    def test_practice_nonexistent_skill_in_tree(self, skill_tree):
        """Test practicing a skill not in tree returns None"""
        improvement = skill_tree.practice_skill(
            "nonexistent",
            difficulty=0.5,
            performance=0.5,
            time_spent=1.0
        )
        assert improvement is None

    def test_get_total_experience(self, skill_tree):
        """Test getting total experience across all skills"""
        skill1 = CharacterSkill(name="skill1", category="cognitive", experience_points=100)
        skill2 = CharacterSkill(name="skill2", category="social", experience_points=200)
        skill_tree.add_skill(skill1)
        skill_tree.add_skill(skill2)
        total_xp = skill_tree.get_total_experience()
        assert total_xp == 300

    def test_get_average_level(self, skill_tree):
        """Test getting average skill level"""
        skill1 = CharacterSkill(name="skill1", category="cognitive", current_level=3.0)
        skill2 = CharacterSkill(name="skill2", category="social", current_level=7.0)
        skill_tree.add_skill(skill1)
        skill_tree.add_skill(skill2)
        avg_level = skill_tree.get_average_level()
        assert avg_level == 5.0

    def test_get_average_level_empty_tree(self):
        """Test average level of empty tree is 0"""
        tree = SkillTree(name="Empty", description="Empty tree")
        assert tree.get_average_level() == 0.0

    def test_get_mastered_skills(self, skill_tree):
        """Test getting list of mastered skills"""
        skill1 = CharacterSkill(name="novice_skill", category="cognitive", current_level=3.0)
        skill2 = CharacterSkill(name="master_skill", category="social", current_level=9.5)
        skill3 = CharacterSkill(name="another_master", category="technical", current_level=9.2)
        skill_tree.add_skill(skill1)
        skill_tree.add_skill(skill2)
        skill_tree.add_skill(skill3)
        mastered = skill_tree.get_mastered_skills()
        assert len(mastered) == 2
        assert "master_skill" in mastered
        assert "another_master" in mastered
        assert "novice_skill" not in mastered

    def test_unlock_requirements(self, skill_tree):
        """Test that unlock requirements are stored"""
        skill = CharacterSkill(name="advanced", category="cognitive")
        skill_tree.add_skill(skill, unlock_level=5.0)
        assert "advanced" in skill_tree.unlock_requirements
        assert skill_tree.unlock_requirements["advanced"]["required_level"] == 5.0

    def test_to_dict(self, skill_tree):
        """Test converting skill tree to dictionary"""
        skill = CharacterSkill(name="test_skill", category="cognitive", current_level=5.0)
        skill_tree.add_skill(skill)
        tree_dict = skill_tree.to_dict()
        assert isinstance(tree_dict, dict)
        assert tree_dict['name'] == skill_tree.name
        assert tree_dict['description'] == skill_tree.description
        assert 'skills' in tree_dict
        assert 'total_experience' in tree_dict
        assert 'average_level' in tree_dict
        assert 'mastered_skills' in tree_dict


class TestSkillCategories:
    """Test skill category enumeration"""

    def test_all_categories_exist(self):
        """Test that all skill categories are defined"""
        categories = list(SkillCategory)
        assert len(categories) == 8
        assert SkillCategory.COGNITIVE in categories
        assert SkillCategory.SOCIAL in categories
        assert SkillCategory.TECHNICAL in categories

    def test_category_values_are_strings(self):
        """Test that category values are strings"""
        for category in SkillCategory:
            assert isinstance(category.value, str)

    def test_expected_categories_exist(self):
        """Test that expected categories exist"""
        expected = [
            "cognitive",
            "social",
            "creative",
            "technical",
            "emotional",
            "physical",
            "leadership",
            "wisdom"
        ]
        for expected_cat in expected:
            assert any(cat.value == expected_cat for cat in SkillCategory)


class TestSkillProgression:
    """Test skill progression mechanics"""

    def test_diminishing_returns(self, cognitive_skill):
        """Test that higher levels show diminishing returns"""
        # Practice at low level
        cognitive_skill.current_level = 1.0
        improvement1 = cognitive_skill.practice(
            difficulty=0.5,
            performance=0.5,
            time_spent=1.0
        )

        # Practice at high level with same parameters
        cognitive_skill.current_level = 8.0
        improvement2 = cognitive_skill.practice(
            difficulty=0.5,
            performance=0.5,
            time_spent=1.0
        )

        # Higher level should improve less (diminishing returns)
        assert improvement1 > improvement2

    def test_difficulty_impact(self, cognitive_skill):
        """Test that difficulty impacts improvement"""
        cognitive_skill.current_level = 3.0
        improvement1 = cognitive_skill.practice(
            difficulty=0.3,
            performance=0.8,
            time_spent=1.0
        )
        cognitive_skill.current_level = 3.0
        improvement2 = cognitive_skill.practice(
            difficulty=0.8,
            performance=0.8,
            time_spent=1.0
        )
        # Higher difficulty should give more improvement
        assert improvement2 > improvement1

    def test_performance_impact(self, cognitive_skill):
        """Test that performance impacts improvement"""
        cognitive_skill.current_level = 3.0
        improvement1 = cognitive_skill.practice(
            difficulty=0.5,
            performance=0.4,
            time_spent=1.0
        )
        cognitive_skill.current_level = 3.0
        improvement2 = cognitive_skill.practice(
            difficulty=0.5,
            performance=0.9,
            time_spent=1.0
        )
        # Higher performance should give more improvement
        assert improvement2 > improvement1

    def test_time_spent_impact(self, cognitive_skill):
        """Test that time spent impacts improvement"""
        cognitive_skill.current_level = 3.0
        improvement1 = cognitive_skill.practice(
            difficulty=0.5,
            performance=0.7,
            time_spent=0.5
        )
        cognitive_skill.current_level = 3.0
        improvement2 = cognitive_skill.practice(
            difficulty=0.5,
            performance=0.7,
            time_spent=2.0
        )
        # More time should give more improvement
        assert improvement2 > improvement1

    def test_combined_factors(self, cognitive_skill):
        """Test combined impact of all factors"""
        initial_level = cognitive_skill.current_level
        improvement = cognitive_skill.practice(
            difficulty=0.9,
            performance=0.9,
            time_spent=3.0
        )
        # All high factors should give measurable improvement
        assert improvement > 0
        assert cognitive_skill.current_level > initial_level


class TestSkillIntegration:
    """Test skill system integration with other systems"""

    def test_skill_with_prerequisites_structure(self):
        """Test that prerequisite structure works"""
        skill = CharacterSkill(
            name="machine_learning",
            category="technical",
            prerequisites=["python", "statistics", "linear_algebra"]
        )
        assert len(skill.prerequisites) == 3
        assert all(isinstance(prereq, str) for prereq in skill.prerequisites)

    def test_skill_tree_prerequisite_flow(self):
        """Test that skill tree can represent prerequisite flow"""
        tree = SkillTree(
            name="Data Science",
            description="Data science skills"
        )

        # Add skills with prerequisites
        tree.add_skill(CharacterSkill(
            name="python",
            category="technical",
            current_level=5.0
        ), unlock_level=0.0)

        tree.add_skill(CharacterSkill(
            name="statistics",
            category="cognitive",
            current_level=4.0,
            prerequisites=["algebra"]
        ), unlock_level=0.0)

        tree.add_skill(CharacterSkill(
            name="machine_learning",
            category="technical",
            current_level=3.0,
            prerequisites=["python", "statistics"]
        ), unlock_level=5.0)

        # Verify structure
        ml_skill = tree.get_skill("machine_learning")
        assert ml_skill is not None
        assert len(ml_skill.prerequisites) == 2

    def test_multiple_skill_trees(self):
        """Test that multiple skill trees can coexist"""
        combat_tree = SkillTree(
            name="Combat",
            description="Combat skills"
        )
        magic_tree = SkillTree(
            name="Magic",
            description="Magic skills"
        )

        combat_tree.add_skill(CharacterSkill(name="sword", category="physical"))
        magic_tree.add_skill(CharacterSkill(name="fireball", category="technical"))

        # Trees should be independent
        assert combat_tree.get_skill("sword") is not None
        assert combat_tree.get_skill("fireball") is None
        assert magic_tree.get_skill("fireball") is not None
        assert magic_tree.get_skill("sword") is None
