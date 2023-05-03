from flask import Blueprint, request, jsonify, Response
from libs.mandelbrot import mandel, mandel_ascii

bp = Blueprint('mb_service', __name__)

@bp.route('/actuator/health', methods=['GET'])
def health():
    return 'health'

@bp.route('/mandel_python/mandel_text_memory/<int:max_iter>/<int:height>/<int:width>', methods=['GET'])
def get_mandelbrot(max_iter, height, width):
    
    mandel_result = mandel_ascii(max_iter, height, width)
    return "<pre>" + mandel_result.result + "</pre>"
    