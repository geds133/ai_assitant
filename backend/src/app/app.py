from flask import Blueprint, Flask, request, render_template, jsonify
from src.agents.ai_interface import ask_llm

bp = Blueprint('main', __name__, url_prefix='', template_folder='templates', static_folder='static', static_url_path='/static')

# Index route (GET)
@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# Route to handle the chatbot queries
@bp.route('/chatbot', methods=['GET'])
def create_chatbot():
 return render_template('chatbot.html')


# Route for POST request
@bp.route('/get-llm-response', methods=['POST'])
def get_llm_response():

    # Here, you can integrate with your language model or provide a placeholder response
    # For demonstration purposes, we will use a simple response
    user_message = request.json.get('message')
    llm_response = ask_llm(user_message)

    # Return the response as JSON
    return jsonify({'response': llm_response}) # Get the JSON data from the POST request

# Run the Flask app
if __name__ == '__main__':

    app = Flask(__name__)
    app.debug = True
    app.register_blueprint(bp)
    app.run(host='0.0.0.0', port=5000)
