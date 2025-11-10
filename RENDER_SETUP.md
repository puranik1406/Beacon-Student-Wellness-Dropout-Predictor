# 🚀 Render Deployment Setup Guide

Quick guide to deploy IRA on Render with AI Chatbot enabled.

## Prerequisites

- GitHub account with your IRA repository
- Render account (free tier works)
- Google account (for Gemini API key)

## Step 1: Get Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the generated API key (you'll need this in Step 3)

**Keep this key safe!** Don't share it publicly or commit it to GitHub.

## Step 2: Deploy to Render

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Render will auto-detect `render.yaml` configuration
5. Click **"Create Web Service"**
6. Wait for initial deployment to complete

**Note:** Render automatically generates a secure `SECRET_KEY` for you - no action needed!

## Step 3: Configure Environment Variables

1. In your Render service dashboard, click **"Environment"** in the left sidebar
2. Find the `GEMINI_API_KEY` variable
3. Click **"Edit"** or the pencil icon
4. Paste your API key from Step 1
5. Click **"Save Changes"**
6. Render will automatically redeploy your service

## Step 4: Verify Deployment

1. Wait for the redeployment to complete (check the **Logs** tab)
2. Look for this message in the logs:
   ```
   ✅ Gemini API configured successfully
   ```
3. Visit your deployed site URL (e.g., `https://ira-studentwellness.onrender.com`)
4. Login as a student (demo credentials in README)
5. Test the AI chatbot - it should now provide intelligent responses!

## Troubleshooting

### "Gemini API key not configured" message

**Problem:** You see this in the logs or chatbot doesn't work properly.

**Solution:**

1. Go to Render Dashboard → Your Service → **Environment**
2. Verify `GEMINI_API_KEY` is set with your actual API key
3. Click **"Save Changes"** to trigger redeploy
4. Check logs for "✅ Gemini API configured successfully"

### Chatbot gives fallback responses

**Problem:** Chatbot responds with "Note: Gemini API key not configured"

**Solution:**

- Ensure you've added the API key in Step 3
- Verify the API key is valid (test at [Google AI Studio](https://aistudio.google.com))
- Check Render logs for any API configuration errors

### Service won't start or crashes

**Problem:** Service shows "Deploy failed" or keeps restarting

**Solution:**

1. Check the **Logs** tab for specific error messages
2. Verify all environment variables are set correctly
3. Ensure your API key doesn't have spaces or newlines
4. Try manually triggering a redeploy: **Manual Deploy** → **Deploy latest commit**

## Environment Variables Reference

| Variable | Value | Set By |
|----------|-------|--------|
| `PYTHON_VERSION` | `3.11.0` | Auto (render.yaml) |
| `SECRET_KEY` | Auto-generated | Render |
| `RENDER` | `true` | Auto (render.yaml) |
| `DISABLE_AI_MODELS` | `true` | Auto (render.yaml) |
| `GEMINI_API_KEY` | Your API key | **Manual (You)** |

## Free Tier Limits

Render free tier includes:

- ✅ 750 hours per month
- ✅ Auto-sleep after 15 min inactivity
- ✅ 512 MB RAM
- ✅ Shared CPU

**Note:** AI models are disabled on Render free tier to reduce memory usage. The chatbot and core
functionality work perfectly!

## Support

- 📧 Contact: See [README.md](README.md) for founder emails
- 🐛 Issues: Open a GitHub issue
- 📖 Documentation: See [README.md](README.md)

---

**Built with ❤️ by the IRA Team**
