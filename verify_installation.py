#!/usr/bin/env python3
"""
Character Library - Installation Verification Script

This script verifies that the character library package is correctly installed
and all modules can be imported successfully.
"""

import sys

def verify_imports():
    """Verify that all modules can be imported"""
    print("Verifying Character Library Installation")
    print("=" * 70)

    tests_passed = 0
    tests_failed = 0

    # Test 1: Import main package
    print("\n1. Testing main package import...")
    try:
        import character_library
        print(f"   ✓ character_library imported successfully")
        print(f"   ✓ Version: {character_library.__version__}")
        tests_passed += 1
    except ImportError as e:
        print(f"   ✗ Failed to import character_library: {e}")
        tests_failed += 1
        return False

    # Test 2: Import personality frameworks
    print("\n2. Testing personality frameworks...")
    try:
        from character_library import BigFivePersonality, EnneagramType, MBTIType
        print(f"   ✓ BigFivePersonality imported")
        print(f"   ✓ EnneagramType imported")
        print(f"   ✓ MBTIType imported")
        tests_passed += 1
    except ImportError as e:
        print(f"   ✗ Failed to import personality frameworks: {e}")
        tests_failed += 1

    # Test 3: Import emotional modeling
    print("\n3. Testing emotional modeling...")
    try:
        from character_library import BasicEmotion, EmotionalState
        print(f"   ✓ BasicEmotion imported")
        print(f"   ✓ EmotionalState imported")
        tests_passed += 1
    except ImportError as e:
        print(f"   ✗ Failed to import emotional modeling: {e}")
        tests_failed += 1

    # Test 4: Import relationships
    print("\n4. Testing relationship dynamics...")
    try:
        from character_library import RelationshipType, CharacterRelationship
        print(f"   ✓ RelationshipType imported")
        print(f"   ✓ CharacterRelationship imported")
        tests_passed += 1
    except ImportError as e:
        print(f"   ✗ Failed to import relationship dynamics: {e}")
        tests_failed += 1

    # Test 5: Import core classes
    print("\n5. Testing core classes...")
    try:
        from character_library import CharacterArchetype
        print(f"   ✓ CharacterArchetype imported")
        print(f"   ✓ Available archetypes: {len(CharacterArchetype)}")
        tests_passed += 1
    except ImportError as e:
        print(f"   ✗ Failed to import core classes: {e}")
        tests_failed += 1

    # Test 6: Create a personality
    print("\n6. Testing personality creation...")
    try:
        from character_library import BigFivePersonality
        personality = BigFivePersonality(
            openness=0.8,
            conscientiousness=0.7,
            extraversion=0.6,
            agreeableness=0.5,
            neuroticism=0.3
        )
        print(f"   ✓ Created BigFivePersonality")
        print(f"   ✓ Personality description: {personality.get_description()[:50]}...")
        tests_passed += 1
    except Exception as e:
        print(f"   ✗ Failed to create personality: {e}")
        tests_failed += 1

    # Test 7: Test emotional states
    print("\n7. Testing emotional states...")
    try:
        from character_library import BasicEmotion, EmotionalState
        emotion = EmotionalState(
            primary_emotion=BasicEmotion.JOY,
            intensity=0.8,
            valence=0.7,
            arousal=0.6
        )
        print(f"   ✓ Created EmotionalState")
        print(f"   ✓ Description: {emotion.get_description()}")
        tests_passed += 1
    except Exception as e:
        print(f"   ✗ Failed to create emotional state: {e}")
        tests_failed += 1

    # Test 8: Check agent support
    print("\n8. Checking agent integration support...")
    try:
        import character_library
        if character_library.AGENT_SUPPORT:
            print(f"   ✓ Agent integration available")
            print(f"   ✓ CharacterAgent can be imported")
        else:
            print(f"   ℹ Agent integration not available (requires hierarchical-memory)")
            print(f"   ℹ Install with: pip install character-library[agent]")
        tests_passed += 1
    except Exception as e:
        print(f"   ℹ Could not verify agent support: {e}")
        tests_failed += 1

    # Summary
    print("\n" + "=" * 70)
    print(f"Verification Complete")
    print(f"  Tests Passed: {tests_passed}")
    print(f"  Tests Failed: {tests_failed}")

    if tests_failed == 0:
        print(f"\n✓ All tests passed! Character library is correctly installed.")
        return True
    else:
        print(f"\n✗ Some tests failed. Please check the errors above.")
        return False


def show_package_info():
    """Show package information"""
    import character_library
    import os

    print("\n" + "=" * 70)
    print("Package Information")
    print("=" * 70)

    print(f"\nPackage: character-library")
    print(f"Version: {character_library.__version__}")
    print(f"Author: {character_library.__author__}")
    print(f"Location: {os.path.dirname(character_library.__file__)}")

    print(f"\nAvailable exports:")
    exports = character_library.__all__
    for export in exports[:10]:
        print(f"  - {export}")
    if len(exports) > 10:
        print(f"  ... and {len(exports) - 10} more")


if __name__ == "__main__":
    success = verify_imports()
    if success:
        show_package_info()
        sys.exit(0)
    else:
        sys.exit(1)
