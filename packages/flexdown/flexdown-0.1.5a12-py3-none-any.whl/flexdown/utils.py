"""Utility functions for Flexdown."""

import hashlib
import os
from pathlib import Path
import re

from flexdown import constants, types


def get_flexdown_files(path: str | Path) -> list[str]:
    """Recursively get the Flexdown files in a directory.

    Args:
        path: The path to the directory to search.

    Returns:
        The list of Flexdown files in the directory.
    """
    path = Path(path)
    flexdown_files = []
    for root, _, files in os.walk(path):
        root = Path(root)
        flexdown_files.extend(
            [
                str(root / file)
                for file in files
                if file.endswith(constants.FLEXDOWN_EXTENSION)
            ]
        )
    return flexdown_files


def evaluate_templates(line: str, env: types.Env):
    """Evaluate template expressions in a line of text.

    Args:
        line: The line of text to evaluate.
        env: The environment variables to use for evaluation.
    """
    # Find all template placeholders in the line.
    matches = re.findall(constants.TEMPLATE_REGEX_WITHOUT_ESCAPE, line)

    # Iterate over each template placeholder.
    for match in matches:
        try:
            # Evaluate the Python expression and replace the template placeholder
            eval_result = str(eval(match, env, env))
            line = line.replace("{" + match + "}", eval_result)
        except Exception as e:
            # If the evaluation fails, leave the template placeholder unchanged
            raise ValueError(
                f"Failed to evaluate expression '{match}' in '{line}'"
            ) from e

    matches_with_escape = re.findall(constants.TEMPLATE_REGEX, line)

    for match in matches_with_escape:
        line = line.replace("\\{" + match + "}", "{" + match + "}")

    # Return the line with the template placeholders replaced.
    return line


def get_id(s: str) -> str:
    hash_object = hashlib.sha256(s.encode())
    hex_dig = hash_object.hexdigest()
    return "_" + hex_dig


def get_route_from_filepath(
    file: str | Path, root_path: str | Path | None = None
) -> str:
    file = Path(file)
    if root_path:
        root_path = Path(root_path)
        route = file.relative_to(root_path)
    else:
        route = file
    route = str(route).replace(".md", "")
    return f"/{route}"
