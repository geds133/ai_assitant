from flask import Blueprint, Flask, request, render_template, jsonify

bp = Blueprint('main', __name__, url_prefix='', template_folder='templates', static_folder='static', static_url_path='/static')

# Index route (GET)
@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Route for POST request
@bp.route('/post-data', methods=['POST'])
def post_data():
    data = request.get_json()  # Get the JSON data from the POST request
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Return the data back as a response for demonstration purposes
    return jsonify({
        "message": "Data received successfully",
        "data": data
    }), 200

# Run the Flask app
if __name__ == '__main__':

    app = Flask(__name__)
    app.debug = True
    app.register_blueprint(bp)
    app.run(host='0.0.0.0', port=5000)
