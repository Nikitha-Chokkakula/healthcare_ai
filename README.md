# Healthcare AI Expert - CrewAI + Gemini

A sophisticated AI-powered healthcare research assistant built with CrewAI and Google's Gemini API. This application provides comprehensive insights on any AI-related healthcare topics, from basic concepts to advanced applications.

## 🚀 Features

- **CrewAI Framework**: Advanced agent orchestration for complex healthcare AI research
- **Gemini 1.5 Flash**: Powered by Google's latest AI model (free tier)
- **Healthcare AI Expert Agent**: Specialized knowledge in medical AI applications
- **Web Interface**: Beautiful, responsive UI for easy interaction
- **REST API**: Programmatic access to healthcare AI insights
- **Render Deployment Ready**: Complete configuration for cloud hosting

## 🏥 Healthcare AI Expertise

The AI agent specializes in:
- Medical AI applications and diagnostics
- Telemedicine and digital health technologies
- Machine learning in medicine
- AI-powered drug discovery
- Robotic surgery and automation
- Patient care automation
- Emerging healthcare AI trends

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **AI Framework**: CrewAI
- **LLM**: Google Gemini 1.5 Flash
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render.com
- **Styling**: Tailwind CSS

## 📋 Prerequisites

- Python 3.8+
- Google Gemini API key (free tier)
- Git for version control

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/health-ai-researcher-crewai.git
cd health-ai-researcher-crewai
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the project root:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 4. Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 🌐 Usage

### Web Interface
1. Open your browser and navigate to `http://localhost:5000`
2. Enter your healthcare AI question
3. Click "Research" to get comprehensive insights

### API Endpoints

#### Health Check
```bash
GET /health
```

#### Research Query
```bash
POST /api/research
Content-Type: application/json

{
  "query": "What are the latest AI advancements in healthcare?"
}
```

#### Get Default Research
```bash
GET /api/research
```

## 🚀 Deployment to Render

### 1. Push to GitHub
```bash
git add .
git commit -m "Initial commit: Healthcare AI Expert with CrewAI"
git push origin main
```

### 2. Deploy on Render

1. **Sign up/Login** to [Render.com](https://render.com)
2. **Create New Web Service**
3. **Connect your GitHub repository**
4. **Configure the service:**
   - **Name**: `health-ai-researcher-crewai`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

### 3. Environment Variables on Render
Add your environment variables in Render dashboard:
- `GOOGLE_API_KEY`: Your Gemini API key

### 4. Deploy
Click "Create Web Service" and wait for deployment to complete.

## 📁 Project Structure

```
health-ai-researcher-crewai/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Web interface
├── build.sh              # Render build script
├── start.sh              # Render start script
├── Procfile              # Process configuration
├── runtime.txt           # Python version
├── .gitignore           # Git ignore rules
├── README.md            # This file
├── DEPLOYMENT.md        # Detailed deployment guide
└── GEMINI_SETUP.md      # Gemini API setup guide
```

## 🔧 Configuration

### Environment Variables
- `GOOGLE_API_KEY`: Your Google Gemini API key
- `PORT`: Port number (default: 5000)

### Customization
- **Agent Role**: Modify the agent's role in `app.py`
- **Model**: Change Gemini model in the `GeminiLLM` class
- **Styling**: Update `templates/index.html` for UI changes

## 🐛 Troubleshooting

### Common Issues

1. **"GOOGLE_API_KEY not found"**
   - Ensure your `.env` file exists and contains the API key
   - Check that the key is valid and has sufficient quota

2. **"Module not found" errors**
   - Run `pip install -r requirements.txt`
   - Ensure you're using Python 3.8+

3. **Render deployment fails**
   - Check build logs in Render dashboard
   - Ensure all files are committed to GitHub
   - Verify environment variables are set

4. **CrewAI compatibility issues**
   - The custom `GeminiLLM` wrapper handles compatibility
   - Uses private attributes to avoid Pydantic validation issues

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) for the agent framework
- [Google Gemini](https://ai.google.dev/) for the AI model
- [Render](https://render.com) for hosting
- [Flask](https://flask.palletsprojects.com/) for the web framework

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Review the deployment logs in Render
3. Open an issue on GitHub with detailed error information

---

**Built with ❤️ for healthcare AI research** 