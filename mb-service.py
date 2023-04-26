import argparse
from flask import Flask, jsonify
import libs.mandelbrot as mandelbrot

app = Flask(__name__)

@app.route('/mandelbrot/<int:max_iter>', methods=['GET'])
def get_mandelbrot(max_iter):
    mandel_result = mandelbrot.mandel(max_iter)
    return jsonify({"result": mandel_result.result})

# Parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description='Mandelbrot Service')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind the service (default: 0.0.0.0)')
    parser.add_argument('--port', type=int, default=8000, help='Port to bind the service (default: 8000)')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    app.run(host=args.host, port=args.port)
    
    