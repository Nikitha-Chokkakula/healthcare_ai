from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import google.generativeai as genai
import json
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def run_research(query="What are the latest AI advancements in healthcare?"):
    """Run the research task and return results using CrewAI-style prompting"""
    try:
        # Create a comprehensive CrewAI-style prompt
        system_prompt = """You are a Healthcare AI Expert - an expert AI researcher and healthcare technology specialist with deep knowledge of medical AI applications, telemedicine, digital health technologies, machine learning in medicine, AI diagnostics, robotic surgery, drug discovery, patient care automation, and emerging healthcare AI trends.

Your role is to provide comprehensive insights on any AI-related healthcare topics, from basic concepts to advanced applications. You are skilled at explaining complex AI concepts in healthcare in an accessible way.

When responding, always:
1. Provide comprehensive, well-structured responses
2. Include relevant examples and current trends
3. Discuss potential impacts and practical applications
4. Make the information accessible and engaging
5. Focus on the specific question asked
6. Use your expertise in healthcare AI to provide valuable insights"""

        full_prompt = f"{system_prompt}\n\nQuestion: {query}\n\nPlease provide a detailed response:"
        
        # Generate response using Gemini
        response = model.generate_content(full_prompt)
        
        return {
            "success": True,
            "result": response.text,
            "timestamp": datetime.now().isoformat(),
            "query": query
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/research', methods=['POST'])
def research():
    """API endpoint to run research"""
    data = request.get_json()
    query = data.get('query', 'What are the latest AI advancements in healthcare?')
    
    result = run_research(query)
    return jsonify(result)

@app.route('/api/research', methods=['GET'])
def get_research():
    """Get research results (for demo purposes)"""
    result = run_research()
    return jsonify(result)

@app.route('/health')
def health_check():
    """Health check endpoint for Render"""
    return jsonify({"status": "healthy", "message": "Healthcare AI Expert (Gemini Direct) is running!"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port) 