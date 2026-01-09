#!/usr/bin/env python3
"""
Validate test suite structure

Checks that all test files are properly structured and can be imported.
"""

import sys
from pathlib import Path


def check_file_exists(filepath, description):
    """Check if a file exists"""
    if filepath.exists():
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} NOT FOUND")
        return False


def check_test_structure():
    """Validate test structure"""
    print("="*70)
    print("Validating Character Library Test Suite")
    print("="*70)

    tests_dir = Path("tests")
    all_good = True

    # Check test directory
    print("\n📁 Test Directory:")
    all_good &= check_file_exists(tests_dir, "Tests directory")

    # Check test files
    print("\n📝 Test Files:")
    test_files = [
        "tests/__init__.py",
        "tests/conftest.py",
        "tests/test_personality.py",
        "tests/test_emotion.py",
        "tests/test_relationships.py",
        "tests/test_archetypes.py",
        "tests/test_skills.py",
        "tests/test_integration.py",
        "tests/README.md",
    ]

    for test_file in test_files:
        all_good &= check_file_exists(Path(test_file), f"Test file")

    # Check configuration files
    print("\n⚙️  Configuration Files:")
    config_files = [
        "pytest.ini",
        "run_tests.py",
        "TESTING_GUIDE.md",
        "TEST_SUITE_SUMMARY.md",
    ]

    for config_file in config_files:
        all_good &= check_file_exists(Path(config_file), f"Config file")

    # Count tests
    print("\n🔢 Test Count:")
    total_tests = 0
    test_files_py = [
        "tests/test_personality.py",
        "tests/test_emotion.py",
        "tests/test_relationships.py",
        "tests/test_archetypes.py",
        "tests/test_skills.py",
        "tests/test_integration.py",
    ]

    for test_file in test_files_py:
        filepath = Path(test_file)
        if filepath.exists():
            content = filepath.read_text()
            test_count = content.count("def test_")
            total_tests += test_count
            print(f"   {test_file}: ~{test_count} tests")

    print(f"\n   **Total: ~{total_tests} tests**")

    # Check imports
    print("\n📦 Checking Imports:")
    try:
        from character_library.personality.big_five import BigFivePersonality
        print("   ✅ BigFivePersonality")
    except ImportError as e:
        print(f"   ❌ BigFivePersonality: {e}")
        all_good = False

    try:
        from character_library.personality.enneagram import EnneagramType
        print("   ✅ EnneagramType")
    except ImportError as e:
        print(f"   ❌ EnneagramType: {e}")
        all_good = False

    try:
        from character_library.personality.mbti import MBTIType
        print("   ✅ MBTIType")
    except ImportError as e:
        print(f"   ❌ MBTIType: {e}")
        all_good = False

    try:
        from character_library.emotion.emotions import BasicEmotion, EmotionalState
        print("   ✅ BasicEmotion, EmotionalState")
    except ImportError as e:
        print(f"   ❌ Emotion imports: {e}")
        all_good = False

    try:
        from character_library.relationships.dynamics import RelationshipType, CharacterRelationship
        print("   ✅ RelationshipType, CharacterRelationship")
    except ImportError as e:
        print(f"   ❌ Relationship imports: {e}")
        all_good = False

    try:
        from character_library.core.archetypes import CharacterArchetype
        print("   ✅ CharacterArchetype")
    except ImportError as e:
        print(f"   ❌ CharacterArchetype: {e}")
        all_good = False

    try:
        from character_library.core.skills import CharacterSkill, SkillTree
        print("   ✅ CharacterSkill, SkillTree")
    except ImportError as e:
        print(f"   ❌ Skill imports: {e}")
        all_good = False

    # Summary
    print("\n" + "="*70)
    if all_good:
        print("✅ All checks passed! Test suite is properly structured.")
        print("\nNext steps:")
        print("1. Install pytest: pip install pytest pytest-cov")
        print("2. Run tests: pytest")
        print("3. Or use: python run_tests.py")
    else:
        print("❌ Some checks failed. Please review the errors above.")
        return 1
    print("="*70)

    return 0


if __name__ == "__main__":
    sys.exit(check_test_structure())
