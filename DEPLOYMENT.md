# Deployment Guide: GitHub + Render

This guide will walk you through deploying your Healthcare AI Expert application to GitHub and then hosting it on Render.com.

## 🚀 Step 1: Prepare for GitHub

### 1.1 Initialize Git Repository
```bash
# Navigate to your project directory
cd Health-ai-researcher-crewai

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Healthcare AI Expert with CrewAI + Gemini"
```

### 1.2 Create GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click the "+" icon in the top right
3. Select "New repository"
4. Name it: `health-ai-researcher-crewai`
5. Make it **Public** (for free Render deployment)
6. **Don't** initialize with README (we already have one)
7. Click "Create repository"

### 1.3 Push to GitHub
```bash
# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/health-ai-researcher-crewai.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## 🌐 Step 2: Deploy to Render

### 2.1 Create Render Account
1. Go to [Render.com](https://render.com)
2. Sign up with your GitHub account
3. Complete the account setup

### 2.2 Create New Web Service

1. **Click "New +"** in your Render dashboard
2. **Select "Web Service"**
3. **Connect your GitHub repository**:
   - Click "Connect a repository"
   - Select your `health-ai-researcher-crewai` repository
   - Click "Connect"

### 2.3 Configure the Service

Fill in the configuration details:

#### Basic Settings
- **Name**: `health-ai-researcher-crewai` (or your preferred name)
- **Environment**: `Python 3`
- **Region**: Choose closest to your users
- **Branch**: `main`

#### Build & Deploy Settings
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Plan**: **Free** (for testing)

### 2.4 Environment Variables

Click on "Environment" tab and add:

| Variable Name | Value |
|---------------|-------|
| `GOOGLE_API_KEY` | Your Gemini API key |

**To get your Gemini API key:**
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click "Get API key"
4. Copy the key and paste it in Render

### 2.5 Deploy

1. **Click "Create Web Service"**
2. **Wait for deployment** (usually 2-5 minutes)
3. **Monitor the logs** for any errors

## ✅ Step 3: Verify Deployment

### 3.1 Check Health Endpoint
Your app will be available at: `https://your-app-name.onrender.com`

Test the health endpoint:
```bash
curl https://your-app-name.onrender.com/health
```

Expected response:
```json
{
  "status": "healthy",
  "message": "Healthcare AI Expert (CrewAI + Gemini) is running!"
}
```

### 3.2 Test the Web Interface
1. Open your browser
2. Navigate to `https://your-app-name.onrender.com`
3. Try asking a healthcare AI question
4. Verify you get a response

## 🔧 Step 4: Troubleshooting

### Common Issues & Solutions

#### 1. Build Fails
**Error**: `ModuleNotFoundError: No module named 'crewai'`
**Solution**: 
- Check that `requirements.txt` includes `crewai`
- Ensure all dependencies are listed

#### 2. Runtime Error
**Error**: `GOOGLE_API_KEY not found`
**Solution**:
- Verify environment variable is set in Render dashboard
- Check that the key is valid and has quota

#### 3. Application Won't Start
**Error**: `gunicorn: command not found`
**Solution**:
- Ensure `gunicorn` is in `requirements.txt`
- Check that the start command is correct

#### 4. 500 Internal Server Error
**Solution**:
- Check Render logs for detailed error messages
- Verify your Gemini API key is working
- Test locally first

### 4.1 Checking Logs
1. Go to your Render dashboard
2. Click on your service
3. Go to "Logs" tab
4. Look for error messages

### 4.2 Local Testing
Before deploying, test locally:
```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variable
export GOOGLE_API_KEY=your_key_here

# Run locally
python app.py
```

## 🔄 Step 5: Updates & Maintenance

### 5.1 Making Updates
```bash
# Make your changes
git add .
git commit -m "Update: [describe your changes]"
git push origin main
```

Render will automatically redeploy when you push to GitHub.

### 5.2 Environment Variable Updates
1. Go to Render dashboard
2. Click on your service
3. Go to "Environment" tab
4. Update variables as needed
5. Redeploy manually if needed

### 5.3 Monitoring
- **Uptime**: Render provides uptime monitoring
- **Logs**: Check logs regularly for errors
- **Performance**: Monitor response times

## 📊 Step 6: Performance Optimization

### 6.1 Free Tier Limitations
- **Sleep after inactivity**: Free services sleep after 15 minutes
- **Cold starts**: First request after sleep may be slow
- **Bandwidth**: Limited bandwidth on free tier

### 6.2 Optimization Tips
1. **Keep service warm**: Use uptime monitoring services
2. **Optimize dependencies**: Remove unused packages
3. **Cache responses**: Implement response caching
4. **Upgrade plan**: Consider paid plan for production

## 🎉 Success!

Your Healthcare AI Expert is now live on the internet! 

**Your app URL**: `https://your-app-name.onrender.com`

### Next Steps:
1. **Share your app** with others
2. **Monitor performance** in Render dashboard
3. **Add features** and push updates
4. **Consider upgrading** to paid plan for production use

## 📞 Support

If you encounter issues:
1. Check this troubleshooting guide
2. Review Render documentation
3. Check GitHub issues for similar problems
4. Contact Render support if needed

---

**Happy deploying! 🚀** 