# Google Gemini API Setup Guide

This guide will help you set up Google's Gemini API for the Healthcare AI Expert application.

## Getting Your Gemini API Key

### 1. Go to Google AI Studio

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key (it starts with "AI")

### 2. Set Up Environment Variables

#### For Local Development:
Create a `.env` file in your project root:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

#### For Render Deployment:
1. Go to your Render dashboard
2. Select your web service
3. Go to "Environment" tab
4. Add environment variable:
   - **Key**: `GOOGLE_API_KEY`
   - **Value**: Your Gemini API key

## Free Tier Limits

The free tier of Gemini API includes:
- **Gemini 1.5 Flash**: 15 requests per minute
- **Gemini 1.5 Pro**: 2 requests per minute
- **Gemini 1.0 Pro**: 15 requests per minute

## Model Information

### Gemini 1.5 Flash (Default)
- **Speed**: Very fast
- **Quality**: Good for general tasks
- **Cost**: Free tier available
- **Best for**: Real-time applications, quick responses

### Gemini 1.5 Pro
- **Speed**: Moderate
- **Quality**: Higher quality responses
- **Cost**: Free tier available
- **Best for**: Complex reasoning, detailed analysis

### Gemini 1.0 Pro
- **Speed**: Fast
- **Quality**: Good balance
- **Cost**: Free tier available
- **Best for**: General use cases

## Troubleshooting

### Common Issues

1. **API Key Not Working**:
   - Ensure you're using the correct API key from Google AI Studio
   - Check that the key starts with "AI"
   - Verify the key is not expired

2. **Rate Limiting**:
   - The free tier has rate limits
   - If you hit limits, wait a minute before trying again
   - Consider upgrading to paid tier for higher limits

3. **Model Not Available**:
   - Ensure you're using a supported model name
   - Check Google's documentation for latest model names
   - The app uses "gemini-1.5-flash" by default

### Error Messages

- **"API key not found"**: Check your environment variables
- **"Rate limit exceeded"**: Wait before making more requests
- **"Model not found"**: Verify the model name is correct

## Security Notes

1. **Never commit API keys** to your repository
2. **Use environment variables** for all API keys
3. **Keep your API key private** and don't share it publicly

## Support

- **Google AI Studio**: [makersuite.google.com](https://makersuite.google.com)
- **Gemini Documentation**: [ai.google.dev](https://ai.google.dev)
- **API Reference**: [ai.google.dev/api](https://ai.google.dev/api) 