#!/usr/bin/env python3
from .core import ask_openai, unroll_prompt_from_file, unroll_prompt
from .code_review_utils import extract_commit_diff
import subprocess
import tempfile
import os
import shutil
import shlex
import sys
from typing import Tuple, Dict, Optional, List
from .manual_prompt_engineering import edit_prompt_interactively

ERROR_AFTER_TIMER: str = (
    "ERROR_AFTER_TIMER"  # For servers: after wait_time, process must be running.
)
OK_AFTER_TIMER: str = "OK_AFTER_TIMER"  # For servers: after wait_time, if no errors are detected, it is considered OK.
WAIT_UNTIL_FINISH: str = "WAIT_UNTIL_FINISH"  # Always wait until the process finishes.


def use_tree_command(directory: str) -> str:
    """
    Build a tree-like listing of the contents of a directory and return the output.
    This function prints exactly what the linux command "tree" prints, but ignores the .git directory.

    Args:
        directory (str): The directory to list.
    Returns:
        str: The tree listing as a string.
    """
    import os
    from typing import List

    def tree(dir_path: str, prefix: str = "") -> List[str]:
        # List all entries and filter out '.git'
        entries: List[str] = sorted(
            entry for entry in os.listdir(dir_path) if entry != ".git"
        )
        lines: List[str] = []
        for index, entry in enumerate(entries):
            path: str = os.path.join(dir_path, entry)
            # Decide which connector to use depending on the position
            if index == len(entries) - 1:
                connector: str = "└── "
                new_prefix: str = prefix + "    "
            else:
                connector: str = "├── "
                new_prefix: str = prefix + "│   "
            lines.append(prefix + connector + entry)
            if os.path.isdir(path):
                lines.extend(tree(path, new_prefix))
        return lines

    # Use the directory's basename as the root name (like tree does)
    root_name: str = os.path.basename(os.path.abspath(directory))
    output_lines: List[str] = [root_name]
    output_lines.extend(tree(directory))

    # Count the total directories and files, ignoring .git
    total_dirs: int = 0
    total_files: int = 0
    for root, dirs, files in os.walk(directory):
        # Remove '.git' from directories to ignore it in the count
        dirs[:] = [d for d in dirs if d != ".git"]
        total_dirs += len(dirs)
        total_files += len(files)
    output_lines.append("")
    output_lines.append(f"{total_dirs} directories, {total_files} files")

    return "\n".join(output_lines)


def execute_python_command(python_code: str, directory: str) -> str:
    """
    Execute provided Python code in a temporary script file.
    The function attempts to use a Python 3 interpreter if available.
    On Windows, it first checks for 'python3' and, if not found, falls back to
    the default Python interpreter (sys.executable).

    Args:
        python_code (str): The Python code to execute.
        directory (str): The working directory for execution.

    Returns:
        str: The standard output of the executed command.
    """
    # Create a temporary file for the script (outside the target directory)
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as temp_file:
        temp_file.write(python_code)
        temp_file.flush()
        temp_filename: str = temp_file.name

    try:
        # On POSIX systems, make the script executable (this is optional for Python)
        if os.name != "nt":
            os.chmod(temp_filename, 0o755)

        # Determine which Python interpreter to use.
        if os.name == "nt":
            # On Windows, try to locate 'python3' first.
            python_path: Optional[str] = shutil.which("python3")
            if python_path:
                command: List[str] = [python_path, temp_filename]
                result = subprocess.run(
                    command, cwd=directory, capture_output=True, text=True
                )
            else:
                # Fallback: use the current Python interpreter.
                command = [sys.executable, temp_filename]
                result = subprocess.run(
                    command, cwd=directory, capture_output=True, text=True
                )
        else:
            # On POSIX, try to locate 'python3' first.
            python_path = shutil.which("python3")
            if python_path:
                command = [python_path, temp_filename]
            else:
                # Fallback: use the current Python interpreter.
                command = [sys.executable, temp_filename]
            result = subprocess.run(
                command, cwd=directory, capture_output=True, text=True
            )
    finally:
        # Clean up the temporary file.
        os.remove(temp_filename)

    return result.stdout


def execute_bash_command(bash_code: str, directory: str) -> str:
    """
    Execute provided bash code in a temporary script file.
    On POSIX systems, this uses bash.
    On Windows, it first checks for bash availability (e.g. Git Bash, WSL)
    and if not found falls back to the default shell.

    Args:
        bash_code (str): The bash code to execute.
        directory (str): The working directory for execution.
    Returns:
        str: The standard output of the executed command.
    """
    # Create a temporary file for the script (outside the target directory)
    with tempfile.NamedTemporaryFile(mode="w", suffix=".sh", delete=False) as temp_file:
        temp_file.write(bash_code)
        temp_file.flush()
        temp_filename: str = temp_file.name

    try:
        # On POSIX systems, make the script executable.
        if os.name != "nt":
            os.chmod(temp_filename, 0o755)

        # Determine which shell to use.
        if os.name == "nt":
            # On Windows, try to locate bash first.
            bash_path: Optional[str] = shutil.which("bash")
            if bash_path:
                command: List[str] = [bash_path, temp_filename]
                result = subprocess.run(
                    command, cwd=directory, capture_output=True, text=True
                )
            else:
                # Fallback: use the default shell via shell=True.
                # Note: The code is written as bash, so execution may be affected.
                result = subprocess.run(
                    temp_filename,
                    cwd=directory,
                    capture_output=True,
                    text=True,
                    shell=True,
                )
        else:
            # On POSIX, use bash.
            result = subprocess.run(
                ["bash", temp_filename], cwd=directory, capture_output=True, text=True
            )
    finally:
        # Clean up the temporary file.
        os.remove(temp_filename)

    return result.stdout


def refactor_code(replace_map: Dict[str, str], directory: str) -> Tuple[str, str]:
    """
    Refactor code based on a replacement map.

    Args:
        replace_map (Dict[str, str]): A dictionary with keys and corresponding replacement values.
        directory (str): The working directory for execution.
    Returns:
        Tuple[str, str]: A tuple containing the bash script code and its command output.
    """
    refactor_prompt: str = unroll_prompt_from_file("Refactor.txt", unroll=True)

    for key, value in replace_map.items():
        refactor_prompt = refactor_prompt.replace(f"[{key}]", value)

    bash_file_code: str = ask_openai(refactor_prompt, "high")

    command_output: str = execute_bash_command(bash_file_code, directory)

    return bash_file_code, command_output


def retrieve_information(
    replace_map: Dict[str, str], directory: str
) -> Tuple[str, str]:
    """
    Refactor code based on a replacement map.

    Args:
        replace_map (Dict[str, str]): A dictionary with keys and corresponding replacement values.
        directory (str): The working directory for execution.
    Returns:
        Tuple[str, str]: A tuple containing the bash script code and its command output.
    """
    refactor_prompt: str = unroll_prompt_from_file("RetrieveInfomaton.txt", unroll=True)

    for key, value in replace_map.items():
        refactor_prompt = refactor_prompt.replace(f"[{key}]", value)

    bash_file_code: str = ask_openai(refactor_prompt, "high")

    command_output: str = execute_bash_command(bash_file_code, directory)

    return bash_file_code, command_output


def summarize_work_done(replace_map: Dict[str, str], directory: str) -> str:
    """
    Summarize the work done based on a replacement map.

    Args:
        replace_map (Dict[str, str]): A dictionary with keys and corresponding replacement values.
        directory (str): The working directory for execution.
    Returns:
        str: The summary of the work done.
    """
    summary_prompt: str = unroll_prompt_from_file("RefactorSummary.txt", unroll=True)

    for key, value in replace_map.items():
        summary_prompt = summary_prompt.replace(f"[{key}]", value)

    summary: str = ask_openai(summary_prompt, "high")

    return summary


def checkpoint_next_action(replace_map: Dict[str, str], directory: str) -> str:
    """
    Determine the next action to take based on the checkpoint prompt.

    Args:
        replace_map (Dict[str, str]): A dictionary with keys and corresponding replacement values.
        directory (str): The working directory for execution.
    Returns:
        str: The result from the checkpoint next action prompt.
    """
    checkpoint_prompt: str = unroll_prompt_from_file(
        "CheckpointerRedirecter.txt", unroll=True
    )

    for key, value in replace_map.items():
        checkpoint_prompt = checkpoint_prompt.replace(f"[{key}]", value)

    result: str = ask_openai(checkpoint_prompt, "high")

    return result


def code_test_command(test_command: str, directory: str) -> str:
    """
    Execute a test command in the specified directory.
    Uses OS detection to run the command appropriately.

    Args:
        test_command (str): The command to run.
        directory (str): The working directory for execution.
    Returns:
        str: The output from executing the test command.
    """
    try:
        if os.name == "nt":
            # On Windows, use shell=True to process the command line properly.
            result = subprocess.run(
                test_command, cwd=directory, capture_output=True, text=True, shell=True
            )
        else:
            # On POSIX systems, split the command into args.
            args: List[str] = shlex.split(test_command)
            result = subprocess.run(args, cwd=directory, capture_output=True, text=True)
    except Exception as e:
        return f"An error occurred while executing the test command: {e}"

    if result.stdout or result.stderr:
        return (
            f"STDOUT:\n{result.stdout}\n"
            f"STDERR:\n{result.stderr}\n"
            f"Exit code: {result.returncode}"
        )
    else:
        return f"Program exited with code {result.returncode}"


def fix_single_code_file(
    answer: str,
    execution_command: str,
    reasoning_effort: str,
    wait_time: Optional[float],
    mode: str,
    max_retries: int = 5,
) -> Optional[str]:
    """
    Iteratively writes the provided code (answer) to a temporary file, launches it using the specified
    execution_command, checks for startup errors according to the specified wait_time and mode, and,
    if errors are detected, attempts to fix them by sending an update request to OpenAI.
    The temporary file is deleted after execution.

    Parameters:
      answer (str): The code to execute.
      execution_command (str): Command to execute the code (e.g., "node").
      reasoning_effort (str): The reasoning effort for execution (error fixes use 'medium').
      wait_time (Optional[float]): Time in seconds to wait after process launch to check status.
                                   If None, waits until the process finishes.
      mode (str): One of the following modes:
                  ERROR_AFTER_TIMER: For servers. After wait_time seconds, process must have finished (with exit code 0).
                  OK_AFTER_TIMER: For scripts. After wait_time seconds, if no errors are detected, it is considered OK.
                  WAIT_UNTIL_FINISH: Waits for the process to finish, then checks the exit code.
      max_retries (int, optional): Maximum number of retries allowed (default is 5).
    Returns:
      Optional[str]: The final code (answer) that was executed successfully, or None if execution fails after maximum retries.
    """
    attempts: int = 0
    while attempts < max_retries:
        try:
            with tempfile.NamedTemporaryFile(
                mode="w", delete=False, suffix=".js", encoding="utf-8"
            ) as tmp_file:
                tmp_file.write(answer)
                tmp_filepath: str = tmp_file.name
        except Exception as exc:
            print("Failed to write to temporary file:", exc)
            return None

        # Ensure the execution command is available
        exec_cmd: Optional[str] = shutil.which(execution_command)
        if not exec_cmd:
            print(f"Error: {execution_command} is not installed or not found in PATH.")
            return None

        print(f"Launching with '{exec_cmd} {tmp_filepath}' ...")

        process = subprocess.Popen(
            [exec_cmd, tmp_filepath],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        success: bool = False
        error_message: str = ""

        if wait_time is not None and mode != WAIT_UNTIL_FINISH:
            if mode == ERROR_AFTER_TIMER:
                # Use wait(timeout=...) to check if the process finishes in time.
                try:
                    ret: int = process.wait(timeout=wait_time)
                    if ret == 0:
                        success = True
                    else:
                        outs, errs = process.communicate()
                        error_message = (
                            errs.strip()
                            if errs.strip()
                            else f"{execution_command} exited with code {ret}"
                        )
                        print(
                            f"\nError detected: Process terminated in ERROR_AFTER_TIMER mode:\n{error_message}"
                        )
                except subprocess.TimeoutExpired:
                    # Process did not finish in time.
                    process.terminate()
                    process.wait()
                    error_message = f"{execution_command} did not finish within {wait_time} seconds."
                    print(f"\nError detected: {error_message}")

            elif mode == OK_AFTER_TIMER:
                try:
                    ret: int = process.wait(timeout=wait_time)
                    if ret == 0:
                        success = True
                    else:
                        outs, errs = process.communicate()
                        error_message = (
                            errs.strip()
                            if errs.strip()
                            else f"{execution_command} exited with code {ret}"
                        )
                        print(
                            f"\nError detected in OK_AFTER_TIMER mode:\n{error_message}"
                        )
                except subprocess.TimeoutExpired:
                    # Process is still running after wait_time which is acceptable in OK_AFTER_TIMER.
                    success = True
                    process.terminate()
                    process.wait()

        else:
            # WAIT_UNTIL_FINISH mode or no wait_time provided.
            retcode: int = process.wait()
            if retcode == 0:
                success = True
            else:
                outs, errs = process.communicate()
                error_message = (
                    errs.strip()
                    if errs.strip()
                    else f"{execution_command} exited with code {retcode}"
                )
                print(f"\nError detected in WAIT_UNTIL_FINISH mode:\n{error_message}")

        try:
            os.unlink(tmp_filepath)
        except Exception as e:
            print(f"Warning: Could not delete temporary file {tmp_filepath}: {e}")

        if success:
            print(f"\n{execution_command} executed successfully under mode {mode}.")
            return answer
        else:
            attempts += 1
            print(
                f"\nAttempt {attempts}/{max_retries}: Error encountered. Attempting to fix the error by updating the code with reasoning set to '{reasoning_effort}'..."
            )
            fix_file_content: str = unroll_prompt_from_file("CodeFixer.txt")
            fix_file_content = unroll_prompt(fix_file_content)
            new_user_prompt: str = fix_file_content.replace("[FILE_CODE]", answer)
            new_user_prompt = new_user_prompt.replace("[ERROR]", error_message)
            new_user_prompt = new_user_prompt.replace(
                "[EXECUTE_COMMAND]", execution_command + " " + tmp_filepath
            )
            new_answer: Optional[str] = ask_openai(new_user_prompt, reasoning_effort)
            if new_answer is None:
                print("Failed to receive a fixed code from OpenAI. Exiting.")
                return None
            answer = new_answer
            print("Updated code received. Retrying execution...\n")

    print("Maximum retries reached in fix_single_code_file. Exiting.")
    return None


def execute_major_coding_task(
    task_instruction: str, directory: str, test_command: str, max_retries: int = 15
) -> Optional[Dict[str, str]]:
    """
    Execute a major coding task.

    Args:
        task_instruction (str): The task instruction.
        directory (str): The directory where the task will be executed.
        test_command (str): The command used to test the code.
        max_retries (int, optional): Maximum number of retries allowed (default is 15).
    Returns:
        Optional[Dict[str, str]]: The replacement map with updated values if finished,
                                  or None if the task could not be completed.
    """
    # Setup git repository and branch "ai-refactor"
    if not os.path.exists(os.path.join(directory, ".git")):
        subprocess.run(["git", "init"], cwd=directory, check=True)
        subprocess.run(
            ["git", "commit", "--allow-empty", "-m", "Initial commit"],
            cwd=directory,
            check=True,
        )
    try:
        subprocess.run(
            ["git", "checkout", "-b", "ai-refactor"], cwd=directory, check=True
        )
    except subprocess.CalledProcessError:
        subprocess.run(["git", "checkout", "ai-refactor"], cwd=directory, check=True)

    # Capture the current commit hash at this moment
    base_commit_hash = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=directory,
        stdout=subprocess.PIPE,
        text=True,
        check=True,
    ).stdout.strip()

    replace_map: Dict[str, str] = {
        "TASK_INSTRUCTION_PLACEHOLDER": task_instruction,
        "TREE_COMMAND_PLACEHOLDER": use_tree_command(directory),
        "EXTRACTED_INFORMATION_PLACEHOLDER": "",
        "WORK_DONE_PLACEHOLDER": "",
        "TEST_OUTPUT_COMMAND": "No command was executed to test the code",
        "TEST_COMMAND": test_command,
    }

    attempts: int = 0
    while attempts < max_retries:
        response: str = checkpoint_next_action(replace_map, directory)

        if response == "refactor":
            bash_file_code, command_output = refactor_code(replace_map, directory)
            # Perform git commit steps after refactoring
            subprocess.run(["git", "add", "."], cwd=directory, check=True)
            subprocess.run(
                ["git", "commit", "-m", "refactor"], cwd=directory, check=True
            )
            # Use the stored base commit hash to extract the diff
            full_diff = extract_commit_diff(base_commit_hash, directory)
            replace_map["WORK_DONE_PLACEHOLDER"] = full_diff

            replace_map["BASH_SCRIPT_PLACEHOLDER"] = bash_file_code

            replace_map["TEST_OUTPUT_COMMAND"] = code_test_command(
                test_command, directory
            )
            replace_map["TREE_COMMAND_PLACEHOLDER"] = use_tree_command(directory)
            replace_map["EXTRACTED_INFORMATION_PLACEHOLDER"] = ""

        elif response == "finish":
            return replace_map
        elif response == "retrieve":
            bash_file_code, command_output = retrieve_information(
                replace_map, directory
            )
            replace_map["EXTRACTED_INFORMATION_PLACEHOLDER"] = command_output

        attempts += 1

    print("Maximum retries reached in execute_major_coding_task. Exiting loop.")
    return None


def apply_changes_to_code(
    code: str,
    changes: str,
    reasoning_effort: str,
    interactive: bool,
) -> str:
    """
    Apply requested modifications to a code file.

    This function retrieves a prompt template for single file code modifications,
    inserts the provided code content and requested changes, and (if enabled)
    allows for interactive editing of the prompt before sending it to OpenAI.

    Args:
        code (str): The current content of the code.
        changes (str): The changes to be applied to the code.
        reasoning_effort (str): The reasoning effort level used for requesting changes.
        interactive (bool): Whether to allow interactive editing of the prompt.

    Returns:
        str: The updated code with the applied modifications.

    Improvements made:
      - Provided a clear docstring and type annotations.
      - Renamed intermediate variables for enhanced readability.
      - Consolidated prompt modifications to enhance maintainability.
    """
    # Retrieve the base prompt template for modifying a single code file.
    prompt_template: str = unroll_prompt_from_file("SingleFileCodeModifications.txt")
    # Insert the current file content and the requested changes into the prompt.
    prompt_filled: str = prompt_template.replace("[FILE_CONTENT]", code).replace(
        "[REQUEST_CHANGES]", changes
    )
    # If interactive mode is enabled, allow the user to edit the prompt.
    if interactive:
        prompt_filled = edit_prompt_interactively(prompt_filled)

    # Obtain and return the updated code from OpenAI.
    return ask_openai(prompt_filled, reasoning_effort)
