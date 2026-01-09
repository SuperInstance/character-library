# Character Library Test Suite

Comprehensive test suite for the character-library package with 80%+ coverage target.

## Test Structure

```
tests/
├── conftest.py              # Shared pytest fixtures
├── test_personality.py      # Big Five, Enneagram, MBTI tests
├── test_emotion.py          # Emotional modeling tests
├── test_relationships.py    # Relationship dynamics tests
├── test_archetypes.py       # Character archetype tests
├── test_skills.py           # Skill development tests
├── test_integration.py      # Full system integration tests
└── README.md               # This file
```

## Test Coverage

### Personality Frameworks (`test_personality.py`)
- **Big Five (OCEAN)**: Trait validation, compatibility, blending, descriptions
- **Enneagram**: 9 personality types, motivations, fears, growth/stress paths
- **MBTI**: 16 personality types, cognitive functions, strengths/weaknesses
- **Integration**: Cross-framework consistency

**Test Count**: ~50 tests
**Coverage Target**: 90%+

### Emotional Modeling (`test_emotion.py`)
- **Basic Emotions**: 8 emotions, valence/arousal, opposites
- **Emotional States**: Intensity, validation, transitions, blending
- **Emotional Cues**: Visible expressions, intensity variations
- **Emotion Transitions**: Event-based state changes

**Test Count**: ~45 tests
**Coverage Target**: 85%+

### Relationship Dynamics (`test_relationships.py`)
- **Relationship Types**: 8 relationship categories
- **Character Relationships**: Strength, trust, evolution
- **Communication Styles**: Default styles per relationship type
- **Compatibility Calculation**: Personality-based compatibility
- **Relationship Development**: Conflicts, support areas, history

**Test Count**: ~55 tests
**Coverage Target**: 85%+

### Character Archetypes (`test_archetypes.py`)
- **12 Archetypes**: Profile retrieval and validation
- **Personality Mappings**: Big Five, Enneagram, MBTI
- **Compatibility**: Archetype pair compatibility
- **Dialogue Patterns**: Voice and communication patterns
- **Archetype Diversity**: Ensuring variety across archetypes

**Test Count**: ~40 tests
**Coverage Target**: 80%+

### Skill Development (`test_skills.py`)
- **Individual Skills**: Creation, validation, practice, usage
- **Skill Progression**: Mastery levels, experience, diminishing returns
- **Skill Trees**: Structure, prerequisites, unlocking
- **Skill Categories**: 8 skill categories
- **Integration**: Prerequisite chains, skill trees

**Test Count**: ~50 tests
**Coverage Target**: 90%+

### Integration Tests (`test_integration.py`)
- **Character Creation**: Full archetype-based creation
- **Emotional-Personality Integration**: Personality affects emotions
- **Relationship Development**: Compatibility and evolution
- **Skill Workflows**: Progression and mastery
- **Complex Workflows**: Multi-system interactions
- **Serialization**: Save/restore functionality

**Test Count**: ~30 tests
**Coverage Target**: 75%+

## Running Tests

### Quick Start

```bash
# Run all tests
python run_tests.py

# Run with coverage
python run_tests.py --coverage

# Run with HTML coverage report
python run_tests.py --coverage --html
```

### Advanced Usage

```bash
# Run specific test category
python run_tests.py -m personality
python run_tests.py -m emotion
python run_tests.py -m relationships
python run_tests.py -m archetypes
python run_tests.py -m skills
python run_tests.py -m integration

# Run specific test file
python run_tests.py -f tests/test_personality.py

# Verbose output
python run_tests.py -v

# Generate coverage reports
python run_tests.py --coverage --html --xml

# Open HTML coverage report in browser
python run_tests.py --report

# Check test installation
python run_tests.py --check
```

### Direct Pytest Usage

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=character_library

# Run specific file
pytest tests/test_personality.py

# Run with verbose output
pytest -v

# Run specific marker
pytest -m personality

# Generate HTML coverage
pytest --cov=character_library --cov-report=html
```

## Test Markers

Tests are categorized using pytest markers:

- `personality`: Personality framework tests
- `emotion`: Emotional modeling tests
- `relationships`: Relationship dynamics tests
- `archetypes`: Character archetype tests
- `skills`: Skill development tests
- `integration`: Integration tests
- `unit`: Unit tests
- `slow`: Long-running tests

## Coverage Goals

| Module | Target | Expected |
|--------|--------|----------|
| Big Five | 95% | 90%+ |
| Enneagram | 95% | 95%+ |
| MBTI | 95% | 90%+ |
| Emotions | 90% | 85%+ |
| Relationships | 90% | 85%+ |
| Archetypes | 85% | 80%+ |
| Skills | 95% | 90%+ |
| Integration | 80% | 75%+ |
| **Overall** | **80%** | **85%+** |

## Test Fixtures

Shared fixtures in `conftest.py`:

### Personality Fixtures
- `sample_big_five`: Standard personality profile
- `high_openness_personality`: High openness (0.95)
- `low_openness_personality`: Low openness (0.2)
- `all_enneagram_types`: All 9 Enneagram types
- `sample_enneagram`: Type 7 Enthusiast
- `all_mbti_types`: All 16 MBTI types
- `sample_mbti`: ENFP type

### Emotional Fixtures
- `joy_emotion`: Joy emotional state
- `fear_emotion`: Fear emotional state
- `neutral_emotion`: Neutral emotional state
- `all_basic_emotions`: All 8 basic emotions

### Relationship Fixtures
- `friendship_relationship`: Strong friendship
- `romantic_relationship`: Strong romantic bond
- `antagonistic_relationship`: Weak antagonistic relationship

### Skill Fixtures
- `cognitive_skill`: Problem-solving skill
- `social_skill`: Empathy skill
- `skill_tree`: Leadership skill tree with multiple skills

## Continuous Integration

The test suite is designed for CI/CD integration:

```yaml
# Example GitHub Actions workflow
- name: Run tests
  run: |
    python run_tests.py --coverage --xml

- name: Upload coverage
  uses: codecov/codecov-action@v2
  with:
    file: ./coverage.xml
```

## Test Development Guidelines

### Writing New Tests

1. **Use descriptive names**: `test_calculate_compatibility_identical_personalities`
2. **Follow AAA pattern**: Arrange, Act, Assert
3. **Use fixtures**: Don't recreate common test data
4. **Test edge cases**: Boundary conditions, invalid inputs
5. **Test independently**: Each test should stand alone

### Example Test

```python
def test_skill_level_capping(cognitive_skill):
    """Test that skill level caps at max_level"""
    # Arrange
    cognitive_skill.current_level = 9.99

    # Act
    cognitive_skill.practice(
        difficulty=1.0,
        performance=1.0,
        time_spent=100.0
    )

    # Assert
    assert cognitive_skill.current_level <= cognitive_skill.max_level
```

## Troubleshooting

### Import Errors

If you get import errors:
```bash
# Install package in development mode
pip install -e .
```

### Missing Dependencies

```bash
# Install test dependencies
pip install pytest pytest-cov
```

### Coverage Not Showing

```bash
# Install pytest-cov
pip install pytest-cov

# Run with coverage explicitly
pytest --cov=character_library --cov-report=term-missing
```

## Contributing

When adding new features:

1. Write tests first (TDD)
2. Ensure 80%+ coverage for new code
3. Add fixtures to `conftest.py` if reused
4. Update this README with new test categories
5. Run full test suite before committing

## Test Statistics

- **Total Test Files**: 6
- **Total Tests**: ~270
- **Total Fixtures**: ~25
- **Coverage Target**: 80%+
- **Expected Coverage**: 85%+

## License

MIT License - See LICENSE file for details.
