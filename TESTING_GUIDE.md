# Character Library Testing Guide

## Quick Start

### Install Test Dependencies

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install test dependencies
pip install pytest pytest-cov

# Or install with dev extras
pip install -e ".[dev]"
```

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=character_library

# Run specific test file
pytest tests/test_personality.py

# Run with verbose output
pytest -v

# Run specific test
pytest tests/test_personality.py::TestBigFivePersonality::test_create_default_personality
```

### Using Test Runner

```bash
# Run all tests
python3 run_tests.py

# Run with coverage and HTML report
python3 run_tests.py --coverage --html

# Run specific marker
python3 run_tests.py -m personality

# Run specific file
python3 run_tests.py -f tests/test_emotion.py

# Open coverage report
python3 run_tests.py --report
```

## Test Categories

### 1. Personality Tests (~50 tests)
```bash
pytest tests/test_personality.py
```
Tests:
- Big Five personality traits (OCEAN)
- Enneagram 9 types
- MBTI 16 types
- Personality compatibility and blending

### 2. Emotion Tests (~45 tests)
```bash
pytest tests/test_emotion.py
```
Tests:
- 8 basic emotions
- Emotional states and transitions
- Emotional cues and expressions
- Valence and arousal

### 3. Relationship Tests (~55 tests)
```bash
pytest tests/test_relationships.py
```
Tests:
- 8 relationship types
- Relationship dynamics and evolution
- Compatibility calculation
- Trust and strength management

### 4. Archetype Tests (~40 tests)
```bash
pytest tests/test_archetypes.py
```
Tests:
- 12 character archetypes
- Archetype profiles
- Archetype compatibility
- Dialogue patterns

### 5. Skill Tests (~50 tests)
```bash
pytest tests/test_skills.py
```
Tests:
- Individual skills
- Skill progression
- Skill trees
- Mastery levels

### 6. Integration Tests (~30 tests)
```bash
pytest tests/test_integration.py
```
Tests:
- Full character creation
- Multi-system workflows
- Serialization
- Cross-system integration

## Coverage Goals

| Module | Target |
|--------|--------|
| Personality | 90%+ |
| Emotion | 85%+ |
| Relationships | 85%+ |
| Archetypes | 80%+ |
| Skills | 90%+ |
| Integration | 75%+ |
| **Overall** | **80%+** |

## Test Markers

Run specific test categories:

```bash
# Personality tests
pytest -m personality

# Emotion tests
pytest -m emotion

# Relationship tests
pytest -m relationships

# Archetype tests
pytest -m archetypes

# Skill tests
pytest -m skills

# Integration tests
pytest -m integration
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: |
          pip install -e ".[dev]"
      - name: Run tests
        run: |
          pytest --cov=character_library --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v2
        with:
          file: ./coverage.xml
```

## Troubleshooting

### Import Errors
```bash
# Install package in development mode
pip install -e .
```

### Missing pytest
```bash
pip install pytest pytest-cov
```

### Permission Issues
```bash
# Use virtual environment
python3 -m venv venv
source venv/bin/activate
pip install pytest pytest-cov
```

## Writing New Tests

1. Add test file to `tests/`
2. Use fixtures from `conftest.py`
3. Follow naming: `test_<function>_<scenario>`
4. Add markers for categorization

Example:
```python
import pytest

class TestMyFeature:
    def test_basic_functionality(self, sample_fixture):
        result = my_function(sample_fixture)
        assert result == expected_value
```

## Test Statistics

- **Total Tests**: ~270
- **Test Files**: 6
- **Fixtures**: 25+
- **Coverage Target**: 80%+

For more details, see [tests/README.md](tests/README.md)
