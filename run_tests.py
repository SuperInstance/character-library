#!/usr/bin/env python3
"""
Test runner script for character-library

Provides convenient scripts for running tests with various options:
- Basic test run
- With coverage reporting
- With specific markers
- Verbose output
"""

import subprocess
import sys
import argparse
from pathlib import Path


def run_command(cmd, description):
    """Run a command and print results"""
    print(f"\n{'='*70}")
    print(f"Running: {description}")
    print(f"Command: {' '.join(cmd)}")
    print('='*70)

    result = subprocess.run(cmd)

    if result.returncode != 0:
        print(f"\n❌ {description} failed with return code {result.returncode}")
        return False
    else:
        print(f"\n✅ {description} succeeded!")
        return True


def run_basic_tests(verbose=False):
    """Run basic tests without coverage"""
    cmd = [sys.executable, "-m", "pytest", "tests/"]
    if verbose:
        cmd.append("-v")
    return run_command(cmd, "Basic Tests")


def run_with_coverage(verbose=False, html=False, xml=False):
    """Run tests with coverage reporting"""
    cmd = [sys.executable, "-m", "pytest", "tests/", "--cov=character_library"]

    if html:
        cmd.append("--cov-report=html")
    if xml:
        cmd.append("--cov-report=xml")
    if verbose:
        cmd.append("-v")

    return run_command(cmd, "Tests with Coverage")


def run_specific_marker(marker, verbose=False):
    """Run tests with specific marker"""
    cmd = [sys.executable, "-m", "pytest", "tests/", "-m", marker]
    if verbose:
        cmd.append("-v")
    return run_command(cmd, f"Tests with marker: {marker}")


def run_specific_file(test_file, verbose=False):
    """Run specific test file"""
    cmd = [sys.executable, "-m", "pytest", test_file]
    if verbose:
        cmd.append("-v")
    return run_command(cmd, f"Test file: {test_file}")


def run_coverage_report():
    """Open HTML coverage report in browser"""
    import webbrowser
    html_file = Path("htmlcov/index.html")

    if html_file.exists():
        print(f"\n🌐 Opening coverage report in browser...")
        webbrowser.open(f"file://{html_file.absolute()}")
        return True
    else:
        print(f"\n❌ Coverage report not found. Run tests with --html first.")
        return False


def check_test_installation():
    """Check if pytest and coverage tools are installed"""
    print("Checking test installation...")

    try:
        import pytest
        print(f"✅ pytest {pytest.__version__} installed")
    except ImportError:
        print("❌ pytest not installed. Run: pip install pytest")
        return False

    try:
        import pytest_cov
        print(f"✅ pytest-cov installed")
    except ImportError:
        print("⚠️  pytest-cov not installed. Coverage reports unavailable.")
        print("   Install with: pip install pytest-cov")

    return True


def main():
    """Main test runner"""
    parser = argparse.ArgumentParser(
        description="Test runner for character-library",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          # Run all tests
  %(prog)s --coverage               # Run with coverage
  %(prog)s --coverage --html        # Run with HTML coverage report
  %(prog)s -m personality           # Run personality tests only
  %(prog)s -f test_emotion.py       # Run specific test file
  %(prog)s --report                 # Open coverage report in browser
        """
    )

    # Main options
    parser.add_argument("-v", "--verbose", action="store_true",
                       help="Verbose output")
    parser.add_argument("--coverage", action="store_true",
                       help="Run tests with coverage reporting")
    parser.add_argument("--html", action="store_true",
                       help="Generate HTML coverage report")
    parser.add_argument("--xml", action="store_true",
                       help="Generate XML coverage report (for CI)")

    # Filtering options
    parser.add_argument("-m", "--marker", type=str,
                       help="Run tests with specific marker (personality, emotion, etc.)")
    parser.add_argument("-f", "--file", type=str,
                       help="Run specific test file")

    # Utility options
    parser.add_argument("--report", action="store_true",
                       help="Open HTML coverage report in browser")
    parser.add_argument("--check", action="store_true",
                       help="Check if test dependencies are installed")

    args = parser.parse_args()

    # Check installation
    if args.check:
        check_test_installation()
        return 0

    # Open coverage report
    if args.report:
        if not run_coverage_report():
            return 1
        return 0

    # Validate arguments
    if args.marker and args.file:
        print("❌ Cannot specify both --marker and --file")
        return 1

    # Run tests based on arguments
    success = True

    if args.file:
        success = run_specific_file(args.file, args.verbose)
    elif args.marker:
        success = run_specific_marker(args.marker, args.verbose)
    elif args.coverage or args.html or args.xml:
        success = run_with_coverage(args.verbose, args.html, args.xml)
    else:
        success = run_basic_tests(args.verbose)

    # Print summary
    print("\n" + "="*70)
    if success:
        print("✅ All tests passed!")
        print("="*70)

        if args.coverage or args.html:
            print("\n📊 Coverage reports generated:")
            if args.html:
                print("   - HTML: htmlcov/index.html")
            if args.xml:
                print("   - XML: coverage.xml")
            print("   - Terminal: see above")
            print("\n💡 Run 'python run_tests.py --report' to view HTML report")
    else:
        print("❌ Some tests failed!")
        print("="*70)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
