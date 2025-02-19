import subprocess
import os
from typing import Optional, List, Tuple
from .core import unroll_prompt_from_file, ask_openai

__all__ = [
    "extract_commit_diff",
    "extract_changed_files_content",
    "exctract_diff_along_with_files",
    "reduce_review_input_content",
    "create_review_from_changes_input",
]


def extract_commit_diff(revision: str) -> Optional[str]:
    """
    Extracts and returns the git diff between the given revision and HEAD.
    If an error occurs, prints the error message and returns None.
    """
    try:
        commit_diff = subprocess.check_output(
            ["git", "diff", "-U999999", revision, "HEAD"], stderr=subprocess.STDOUT
        ).decode("utf-8", errors="ignore")
        return commit_diff
    except subprocess.CalledProcessError as e:
        print(
            "Error retrieving git diff between",
            revision,
            "and HEAD:\n",
            e.output.decode(),
        )
        return None


def extract_changed_files_content(revision: str) -> Tuple[List[str], str]:
    """
    Extracts the list of changed files (from git diff --name-only) between the given revision and HEAD.
    For each changed file that exists and is smaller than 20kB, reads its full content and
    formats it with a header and separator.
    Returns a tuple:
      (changed_files_list, aggregated_files_content)
    If an error occurs while retrieving the file list, returns ([], "").
    """
    try:
        changed_files_output = (
            subprocess.check_output(
                ["git", "diff", "--name-only", revision, "HEAD"],
                stderr=subprocess.STDOUT,
            )
            .decode("utf-8")
            .strip()
        )
        changed_files: List[str] = (
            changed_files_output.split("\n") if changed_files_output else []
        )
    except subprocess.CalledProcessError as e:
        print(
            "Error retrieving changed files between",
            revision,
            "and HEAD:\n",
            e.output.decode(),
        )
        return [], ""

    files_content = ""
    for cf in changed_files:
        cf = cf.strip()
        # Use os.path functions to ensure OS-independence
        if cf and os.path.isfile(cf):
            try:
                # Check that the file is smaller than 20kB (20 * 1024 bytes)
                if os.path.getsize(cf) < 20 * 1024:
                    with open(cf, "r", encoding="utf-8", errors="ignore") as f:
                        file_content = f.read()
                    files_content += f"\n# File: {cf}\n{file_content}\n\n---\n"
                else:
                    # Skip files that are 20kB or larger
                    continue
            except Exception as err:
                print(f"Error reading file {cf}: {err}")
    return changed_files, files_content


def exctract_diff_along_with_files(revision: str) -> str:
    commit_diff = extract_commit_diff(revision)
    if commit_diff is None:
        return [], ""
    changed_files, files_content = extract_changed_files_content(revision)

    return (
        "1. Commit Diff:\n"
        + commit_diff.strip()
        + "\n\n2. New File Contents:\n"
        + files_content.strip()
    )


def reduce_review_input_content(
    input_content: str, reasoning_effort: str = "high"
) -> str:
    user_prompt = unroll_prompt_from_file("ReduceReviewInfo.txt")
    user_prompt = user_prompt.replace(
        "[CODE_DIFFS_CONCATENATED_WITH_FILE_CONTENTS]", input_content
    )

    reduced_input_content = ask_openai(user_prompt, reasoning_effort)

    return reduced_input_content


def create_review_from_changes_input(
    input_content: str, reasoning_effort: str = "high"
) -> str:
    user_prompt = unroll_prompt_from_file("ReviewCode.txt")
    user_prompt = user_prompt.replace("[APPLYIED_CHANGES]", input_content)

    review_message = ask_openai(user_prompt, reasoning_effort)

    return review_message
