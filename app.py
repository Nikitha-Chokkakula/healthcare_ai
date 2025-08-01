from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import google.generativeai as genai
import json
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure Gemini
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        logger.error("GOOGLE_API_KEY not found in environment variables")
        raise ValueError("GOOGLE_API_KEY is required")
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    logger.info("Gemini API configured successfully")
except Exception as e:
    logger.error(f"Failed to configure Gemini API: {e}")
    model = None

def run_research(query="What are the latest AI advancements in healthcare?"):
    """Run the research task and return results using CrewAI-style prompting"""
    try:
        if not model:
            return {
                "success": False,
                "error": "Gemini API not configured properly",
                "timestamp": datetime.now().isoformat()
            }
        
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
        
        logger.info(f"Generating response for query: {query}")
        
        # Generate response using Gemini
        response = model.generate_content(full_prompt)
        
        logger.info("Response generated successfully")
        
        return {
            "success": True,
            "result": response.text,
            "timestamp": datetime.now().isoformat(),
            "query": query
        }
    except Exception as e:
        logger.error(f"Error in run_research: {e}")
        return {
            "success": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

@app.route('/')
def index():
    """Main page"""
    try:
        return render_template('index.html')
    except Exception as e:
        logger.error(f"Error rendering index: {e}")
        return jsonify({"error": "Failed to load page", "details": str(e)}), 500

@app.route('/api/research', methods=['POST'])
def research():
    """API endpoint to run research"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        query = data.get('query', 'What are the latest AI advancements in healthcare?')
        logger.info(f"Received research request: {query}")
        
        result = run_research(query)
        return jsonify(result)
    except Exception as e:
        logger.error(f"Error in research endpoint: {e}")
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

@app.route('/api/research', methods=['GET'])
def get_research():
    """Get research results (for demo purposes)"""
    try:
        logger.info("Received GET research request")
        result = run_research()
        return jsonify(result)
    except Exception as e:
        logger.error(f"Error in GET research endpoint: {e}")
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

@app.route('/health')
def health_check():
    """Health check endpoint for Render"""
    try:
        # Test Gemini API connection
        api_status = "healthy" if model else "unhealthy"
        
        return jsonify({
            "status": "healthy", 
            "message": "Healthcare AI Expert (Gemini Direct) is running!",
            "api_status": api_status,
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        logger.error(f"Error in health check: {e}")
        return jsonify({"status": "unhealthy", "error": str(e)}), 500

@app.route('/test')
def test():
    """Test endpoint for debugging"""
    return jsonify({
        "message": "Test endpoint working",
        "timestamp": datetime.now().isoformat(),
        "environment": "production" if os.environ.get('RENDER') else "development"
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found", "path": request.path}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"Starting Flask app on port {port}")
    app.run(debug=False, host='0.0.0.0', port=port) 