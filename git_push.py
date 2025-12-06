import subprocess
import sys

def run_command(command, description, exit_on_error=True):
    """Run a shell command and handle errors."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print(f"✅ {description} successful.")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}: {e}")
        if e.stdout:
            print(f"Output: {e.stdout}")
        if e.stderr:
            print(f"Error: {e.stderr}")
        if exit_on_error:
            sys.exit(1)
        return None

def main():
    print("🚀 Starting Git push automation for DermalScan-AI...")

    # Step 1: Check current branch
    print("\n1️⃣ Checking current branch...")
    branches = run_command("git branch", "Branch check")
    if branches is None:
        print("Failed to check branch. Aborting.")
        sys.exit(1)
    current_branch = None
    for line in branches.split('\n'):
        if line.startswith('*'):
            current_branch = line[2:].strip()
            break
    print(f"Current branch: {current_branch}")

    if current_branch not in ['main', 'master']:
        print(f"⚠️  Warning: You are on branch '{current_branch}'. Ensure it's the correct branch (main or master) before pushing.")
        proceed = input("Do you want to proceed anyway? (y/n): ").lower()
        if proceed != 'y':
            print("Aborting.")
            sys.exit(0)

    # Step 2: Check for changes
    print("\n2️⃣ Checking for changes...")
    status = run_command("git status --porcelain", "Status check")
    if not status:
        print("ℹ️  No changes to commit. Working tree is clean.")
        # Still try to push if ahead of origin
        print("\n4️⃣ Attempting to push (in case local is ahead)...")
        push_command = f"git push origin {current_branch}"
        push_result = run_command(push_command, "Pushing to origin", exit_on_error=False)
        if push_result is not None:
            print("\n🎉 Push completed successfully!")
        else:
            print("\nℹ️  Push failed. Check permissions or authentication.")
        return

    # Step 3: Add all changed files
    print("\n3️⃣ Adding all changed files...")
    run_command("git add .", "Adding files")

    # Step 4: Commit changes
    print("\n4️⃣ Committing changes...")
    commit_result = run_command('git commit -m "Updated code"', "Committing changes", exit_on_error=False)
    if commit_result is None:
        print("ℹ️  Commit failed (possibly no changes or already committed). Skipping to push.")

    # Step 5: Push to origin
    print("\n5️⃣ Pushing to origin...")
    push_command = f"git push origin {current_branch}"
    push_result = run_command(push_command, "Pushing to origin", exit_on_error=False)
    if push_result is not None:
        print("\n🎉 All steps completed successfully! Changes pushed to GitHub.")
    else:
        print("\nℹ️  Push failed. This may be due to authentication issues or lack of permissions. Ensure you have write access to the repository and are authenticated (e.g., via GitHub CLI or SSH).")

if __name__ == "__main__":
    main()
