# ⚡ Quick Reference Guide

Fast answers to common questions about IRA setup and deployment.

## 🔐 Generating a SECRET_KEY

**Easiest Way:**

```bash
python generate_secret_key.py
```

**Alternative Methods:**

```bash
# Python one-liner
python -c "import secrets; print(secrets.token_hex(32))"

# PowerShell (Windows)
-join ((65..90) + (97..122) + (48..57) | Get-Random -Count 64 | % {[char]$_})

# OpenSSL (Linux/Mac)
openssl rand -hex 32
```

## 🤖 Setting Up Gemini API Key

### For Local Development:

1. Get key from: https://makersuite.google.com/app/apikey
2. Add to `.env` file:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

### For Render Deployment:

1. Get key from: https://makersuite.google.com/app/apikey
2. Go to: https://dashboard.render.com
3. Select your service → Environment tab
4. Set `GEMINI_API_KEY` variable
5. Save (auto-redeploys)

## 🚀 First Time Setup (Local)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create environment file
copy .env.example .env

# 3. Generate SECRET_KEY
python generate_secret_key.py
# Copy output to .env file

# 4. (Optional) Add Gemini API key to .env

# 5. Initialize database
python create_database.py

# 6. Run the app
python app.py
```

## 🌐 Deploy to Render

```bash
# 1. Push your code to GitHub
git add .
git commit -m "Initial commit"
git push

# 2. Create web service on Render
# - Connect GitHub repo
# - Render auto-detects render.yaml
# - Click "Create Web Service"

# 3. Add Gemini API key
# - Go to Environment tab
# - Set GEMINI_API_KEY
# - Save (triggers redeploy)
```

See [RENDER_SETUP.md](RENDER_SETUP.md) for detailed instructions.

## 🔍 Troubleshooting

### "Gemini API key not configured"

- **Local:** Add `GEMINI_API_KEY` to `.env` file
- **Render:** Add `GEMINI_API_KEY` in Environment tab

### "Database not found"

```bash
python create_database.py
```

### "Port already in use"

Change port in `app.py` or kill the process using port 5000

### "Module not found"

```bash
pip install -r requirements.txt
```

## 📝 Demo Credentials

### Student:

- Email: `aarav@student.edu`
- Password: `student123`

### Counselor:

- Email: `counselor@ira.edu`
- Password: `counselor123`

## 🔗 Important Links

- **Gemini API Key:** https://makersuite.google.com/app/apikey
- **Render Dashboard:** https://dashboard.render.com
- **Deployed Site:** https://ira-studentwellness.onrender.com/
- **GitHub Repo:** (your repository URL)

## 📚 Documentation Files

- `README.md` - Complete documentation
- `RENDER_SETUP.md` - Deployment guide
- `CHANGES.md` - Recent changes log
- `.env.example` - Environment variables template
- `QUICK_REFERENCE.md` - This file!

## 💡 Pro Tips

1. **Never commit `.env` file** - It's already in `.gitignore`
2. **Use different SECRET_KEY for production** - Generate a new one
3. **Gemini API is free** - Perfect for student projects
4. **Render free tier auto-sleeps** - First request may take 30s
5. **Check logs for issues** - Render Dashboard → Logs tab

---

**Need more help?** Check the full [README.md](README.md) or [RENDER_SETUP.md](RENDER_SETUP.md)
