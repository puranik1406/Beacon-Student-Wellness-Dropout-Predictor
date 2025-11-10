#!/usr/bin/env python3
"""
Generate a secure SECRET_KEY for Flask application
Run this script to generate a new secret key for your .env file
"""
import secrets

if __name__ == "__main__":
    secret_key = secrets.token_hex(32)
    
    print("=" * 80)
    print("🔐 Flask SECRET_KEY Generator")
    print("=" * 80)
    print("\nYour new SECRET_KEY:")
    print(f"\n{secret_key}\n")
    print("=" * 80)
    print("\nHow to use:")
    print("1. Copy the key above")
    print("2. Open your .env file (or create one from .env.example)")
    print("3. Replace the SECRET_KEY value with the key above")
    print("\nExample:")
    print(f"SECRET_KEY={secret_key}")
    print("=" * 80)
    print("\n⚠️  IMPORTANT: Keep this key secret! Don't commit it to Git.")
    print("=" * 80)
