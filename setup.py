import os
import stat
import sys

HOOK_CONTENT = """#!/usr/bin/env python
import subprocess
import sys

print("Running tests before push...")

result = subprocess.run([sys.executable, "run_test.py"])

if result.returncode != 0:
    print("Push aborted due to test failures.")
    sys.exit(1)

print("Tests passed. Proceeding with push.")
sys.exit(0)
"""

def main():
    git_hooks_dir = os.path.join(".git", "hooks")
    hook_path = os.path.join(git_hooks_dir, "pre-push")

    # Ensure we're in a git repo
    if not os.path.isdir(git_hooks_dir):
        print(".git/hooks directory not found. Are you in a Git repo?")
        sys.exit(1)

    # Write the hook
    with open(hook_path, "w", newline="\n") as f:
        f.write(HOOK_CONTENT)

    # Make executable (Unix-based systems)
    try:
        st = os.stat(hook_path)
        os.chmod(hook_path, st.st_mode | stat.S_IEXEC)
    except Exception as e:
        print(f"Could not set executable permissions: {e}")

    print("pre-push hook installed successfully!")

if __name__ == "__main__":
    main()