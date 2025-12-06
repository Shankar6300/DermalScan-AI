import subprocess
import sys

def run_command(command, description):
    """Run a shell command and handle errors."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print(f"✅ {description} successful.")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}: {e}")
        print(f"Output: {e.stdout}")
        print(f"Error: {e.stderr}")
        sys.exit(1)

def main():
    print("🚀 Starting Git push automation for DermalScan-AI...")

    # Step 1: Check current branch
    print("\n1️⃣ Checking current branch...")
    branches = run_command("git branch", "Branch check")
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

    # Step 2: Add all changed files
    print("\n2️⃣ Adding all changed files...")
    run_command("git add .", "Adding files")

    # Step 3: Commit changes
    print("\n3️⃣ Committing changes...")
    run_command('git commit -m "Updated code"', "Committing changes")

    # Step 4: Push to origin
    print("\n4️⃣ Pushing to origin...")
    push_command = f"git push origin {current_branch}"
    run_command(push_command, "Pushing to origin")

    print("\n🎉 All steps completed successfully! Changes pushed to GitHub.")

if __name__ == "__main__":
    main()
