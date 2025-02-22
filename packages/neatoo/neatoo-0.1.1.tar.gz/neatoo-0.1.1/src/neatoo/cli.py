# src/neatoo/cli.py
import argparse
import subprocess
from pathlib import Path
from typing import List, Optional, Tuple


def run_command(cmd: List[str], verbose: bool = False) -> Tuple[int, str]:
    """Run a command and return its exit code and output"""
    if verbose:
        print(f"Running: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode, result.stdout + result.stderr
    except Exception as e:
        return 1, str(e)


def format_code(paths: List[Path], verbose: bool = False):
    """Format code in the given paths"""
    for path in paths:
        if verbose:
            print(f"Formatting {path}")

        # Run black
        exit_code, output = run_command(["black", str(path)], verbose)
        print(output)  # Always print black output
        if exit_code != 0:
            print(f"Black formatting failed:\n{output}")

        # Run isort
        exit_code, output = run_command(["isort", str(path)], verbose)
        print(output)  # Always print isort output
        if exit_code != 0:
            print(f"isort formatting failed:\n{output}")


def check_code(paths: List[Path], verbose: bool = False):
    """Check code in the given paths"""
    for path in paths:
        if verbose:
            print(f"Checking {path}")

        # Check with black
        exit_code, output = run_command(["black", "--check", str(path)], verbose)
        print(output)  # Always print black check output
        if exit_code != 0:
            print(f"Black check failed:\n{output}")

        # Check with isort
        exit_code, output = run_command(["isort", "--check-only", str(path)], verbose)
        print(output)  # Always print isort check output
        if exit_code != 0:
            print(f"isort check failed:\n{output}")

        # Check with flake8
        exit_code, output = run_command(["flake8", str(path)], verbose)
        print(output)  # Always print flake8 output
        if exit_code != 0:
            print(f"flake8 check failed:\n{output}")


def test_code(paths: List[Path], verbose: bool = False):
    """Run tests for the given paths"""
    # For test command, we ignore the paths and just run pytest on tests/
    exit_code, output = run_command(["pytest", "-sv", "tests/"], verbose)
    if verbose or exit_code != 0:
        print(output)
    if exit_code != 0:
        raise Exception("Tests failed")


def create_parser() -> argparse.ArgumentParser:
    """Create and configure argument parser"""
    parser = argparse.ArgumentParser(
        description="Neatoo - Python code tools",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Add global options
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )

    # Create subcommands
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Command to execute"
    )

    # format
    format_parser = subparsers.add_parser("format", help="Format Python code")
    format_parser.add_argument(
        "paths", nargs="+", type=Path, help="Files or directories to format"
    )

    # check
    check_parser = subparsers.add_parser("check", help="Check Python code")
    check_parser.add_argument(
        "paths", nargs="+", type=Path, help="Files or directories to check"
    )

    # test
    test_parser = subparsers.add_parser("test", help="Run Python tests")
    test_parser.add_argument(
        "paths", nargs="+", type=Path, help="Test files or directories to run"
    )

    return parser


def main(args: Optional[List[str]] = None) -> int:
    """Main entry point

    Args:
        args: Command line arguments (defaults to sys.argv[1:])

    Returns:
        Exit code (0 for success, non-zero for error)
    """
    parser = create_parser()
    args = parser.parse_args(args)

    try:
        if args.command == "format":
            format_code(args.paths, args.verbose)
        elif args.command == "check":
            check_code(args.paths, args.verbose)
        elif args.command == "test":
            test_code(args.paths, args.verbose)
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
