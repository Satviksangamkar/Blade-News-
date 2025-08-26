#!/usr/bin/env python3
"""
GitHub Repository Creation and Push Script
Automates the process of creating a GitHub repository and pushing code
"""

import subprocess
import sys
import os
import requests
import json
from getpass import getpass

def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return None

def create_github_repo():
    """Create GitHub repository using GitHub CLI or manual instructions"""
    
    print("🚀 GitHub Repository Setup")
    print("=" * 50)
    
    # Check if GitHub CLI is available
    gh_result = run_command("gh --version", "Checking GitHub CLI")
    
    if gh_result:
        print("\n📋 GitHub CLI detected! Using automated setup...")
        
        # Check if user is authenticated
        auth_result = run_command("gh auth status", "Checking GitHub authentication")
        
        if not auth_result:
            print("\n🔐 Please authenticate with GitHub CLI:")
            run_command("gh auth login", "GitHub authentication")
        
        # Get repository name
        repo_name = "telegram-news-scraper"
        description = "High-performance intelligent news scraping system with MongoDB Atlas, Google Gemini AI, and advanced caching mechanisms"
        
        print(f"\n📦 Creating repository: {repo_name}")
        create_cmd = f'gh repo create {repo_name} --public --description "{description}" --source=. --remote=origin --push'
        
        result = run_command(create_cmd, "Creating GitHub repository")
        
        if result:
            print(f"\n🎉 Repository created successfully!")
            print(f"🌐 View your repository at: https://github.com/YOUR_USERNAME/{repo_name}")
            return True
        else:
            print("\n⚠️ Automated creation failed. Using manual instructions...")
    
    # Manual instructions
    print("\n📋 Manual GitHub Repository Setup")
    print("=" * 50)
    print("1. Go to https://github.com and sign in")
    print("2. Click the '+' icon → 'New repository'")
    print("3. Repository name: telegram-news-scraper")
    print("4. Description: High-performance intelligent news scraping system with MongoDB Atlas, Google Gemini AI, and advanced caching mechanisms")
    print("5. Make it PUBLIC")
    print("6. DO NOT initialize with README, .gitignore, or license")
    print("7. Click 'Create repository'")
    print("\nAfter creating the repository, run these commands:")
    print("\n" + "=" * 50)
    print("git remote add origin https://github.com/YOUR_USERNAME/telegram-news-scraper.git")
    print("git branch -M main")
    print("git push -u origin main")
    print("=" * 50)
    
    return False

def push_to_github():
    """Push code to GitHub repository"""
    
    print("\n📤 Pushing to GitHub")
    print("=" * 50)
    
    # Check if remote exists
    remote_result = run_command("git remote -v", "Checking git remotes")
    
    if not remote_result or "origin" not in remote_result:
        print("❌ No remote origin found. Please create the GitHub repository first.")
        return False
    
    # Push to GitHub
    print("\n🔄 Pushing code to GitHub...")
    
    # Rename branch to main
    run_command("git branch -M main", "Renaming branch to main")
    
    # Push to GitHub
    push_result = run_command("git push -u origin main", "Pushing to GitHub")
    
    if push_result:
        print("\n🎉 Successfully pushed to GitHub!")
        print("🌐 Your repository is now live on GitHub!")
        return True
    else:
        print("\n❌ Failed to push to GitHub. Please check your repository URL and try again.")
        return False

def main():
    """Main function"""
    
    print("🚀 Telegram News Scraper - GitHub Repository Setup")
    print("=" * 60)
    
    # Check if we're in a git repository
    if not os.path.exists(".git"):
        print("❌ Not in a git repository. Please run 'git init' first.")
        return
    
    # Check if we have commits
    commit_result = run_command("git log --oneline", "Checking git commits")
    if not commit_result:
        print("❌ No commits found. Please commit your changes first.")
        return
    
    print(f"✅ Found {len(commit_result.splitlines())} commits")
    
    # Create GitHub repository
    repo_created = create_github_repo()
    
    if repo_created:
        # Push to GitHub
        push_to_github()
    else:
        print("\n📝 Please follow the manual instructions above to create your repository.")
        print("Then run the push commands shown above.")

if __name__ == "__main__":
    main()
