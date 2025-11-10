# ✅ Pre-Commit Checklist

**CRITICAL: Check these items before pushing to GitHub!**

## 🔐 Security Checks

- [ ] `.env` file is NOT in the commit (it should be in `.gitignore`)
- [ ] `.env.example` contains only placeholder values (no real API keys)
- [ ] No API keys or secrets in any code files
- [ ] `SECRET_KEY` in code is a placeholder or uses environment variable
- [ ] No passwords or sensitive data in database scripts

## 📁 File Checks

- [ ] Removed unnecessary temporary files
- [ ] Large files (like PDFs) are in `.gitignore`
- [ ] No `__pycache__` or `.pyc` files
- [ ] No IDE-specific files (`.vscode`, `.idea`)
- [ ] No `instance/` folder (contains local database)

## 📝 Documentation Checks

- [ ] README.md is up to date
- [ ] RENDER_SETUP.md has correct deployment instructions
- [ ] QUICK_REFERENCE.md has accurate quick commands
- [ ] No internal/development notes in public docs

## 🚀 Deployment Configuration

- [ ] `render.yaml` is configured correctly
- [ ] `requirements.txt` is up to date
- [ ] `Procfile` and `runtime.txt` are correct
- [ ] Environment variables documented in `.env.example`

## ⚠️ Critical Security Issues Fixed

✅ **FIXED**: Removed real API keys from `.env.example`

- SECRET_KEY: Changed to `your_secret_key_here`
- GEMINI_API_KEY: Changed to `your_gemini_api_key_here`

## 🗑️ Files Removed

✅ Deleted unnecessary files:

- `CHANGES.md` (internal documentation)
- `deploy_check.py` (development script)

## 📦 Files to Keep

These files SHOULD be in your repository:

### Core Application

- ✅ `app.py` - Main application
- ✅ `create_database.py` - Database initialization
- ✅ `generate_secret_key.py` - Key generator utility
- ✅ `requirements.txt` - Dependencies
- ✅ `Procfile` - Render deployment config
- ✅ `render.yaml` - Render configuration
- ✅ `runtime.txt` - Python version

### Documentation

- ✅ `README.md` - Main documentation
- ✅ `RENDER_SETUP.md` - Deployment guide
- ✅ `QUICK_REFERENCE.md` - Quick start guide
- ✅ `LICENSE` - License file

### Configuration

- ✅ `.env.example` - Environment template (placeholders only!)
- ✅ `.gitignore` - Git ignore rules

### AI Models

- ✅ `ai_models/__init__.py`
- ✅ `ai_models/emotion_model.py`
- ✅ `ai_models/tabular_model.py`
- ✅ `ai_models/README.md`

### Templates & Static Files

- ✅ `templates/` - All HTML templates
- ✅ `static/` - CSS, JS, images
- ✅ `uploads/` - Upload directory (empty, with `.gitkeep`)

## 🚫 Files to NEVER Commit

- ❌ `.env` - Contains real secrets
- ❌ `instance/` - Local database
- ❌ `__pycache__/` - Python cache
- ❌ `*.pyc` - Compiled Python
- ❌ `IRA.pdf` - Large file (now in .gitignore)

## 🔍 Quick Verification Commands

Before committing, run these:

```bash
# Check for accidentally staged .env file
git status | findstr ".env"

# Should only show .env.example, NOT .env

# Check .env.example doesn't have real keys
type .env.example | findstr "your_"

# Should see placeholders like "your_secret_key_here"

# List all staged files
git status

# Review changes
git diff --cached
```

## 🎯 Safe to Push When...

✅ All security checks pass
✅ Only necessary files are included
✅ No secrets or API keys in any files
✅ `.gitignore` is working correctly
✅ Documentation is accurate and complete

---

**Once verified, you can safely push to GitHub:**

```bash
git add .
git commit -m "Your commit message"
git push origin main
```

🎉 **You're ready to deploy on Render!**
