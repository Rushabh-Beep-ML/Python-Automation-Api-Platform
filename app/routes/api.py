from flask import Blueprint, request, jsonify, current_app
import logging
from app.services.processor import DataProcessor
from app.services.enricher import DataEnricher

api_bp = Blueprint('api', __name__)
logger = logging.getLogger(__name__)

@api_bp.route('/process', methods=['POST'])
def process_data():
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400

        raw_input = data.get('raw_input', '').strip()
        operations = data.get('operations', [])

        if not raw_input:
            return jsonify({'error': 'raw_input cannot be empty'}), 400

        if current_app.config['MAX_INPUT_SIZE'] and len(raw_input) > current_app.config['MAX_INPUT_SIZE']:
            return jsonify({'error': 'Input exceeds maximum allowed size'}), 413

        processor = DataProcessor()
        enricher = DataEnricher(
            api_base_url=current_app.config['EXTERNAL_API_BASE_URL'],
            timeout=current_app.config['API_TIMEOUT']
        )

        processed_items = raw_input.split('\n')

        if 'clean_whitespace' in operations:
            processed_items = processor.clean_whitespace(processed_items)

        if 'remove_duplicates' in operations:
            processed_items = processor.remove_duplicates(processed_items)

        if 'normalize_case' in operations:
            case_type = data.get('case_type', 'lower')
            processed_items = processor.normalize_case(processed_items, case_type)

        transformed_fields = []
        if 'external_api_enrich' in operations:
            processed_items, api_fields = enricher.enrich_items(processed_items)
            transformed_fields = api_fields

        result = {
            'success': True,
            'processed_items': processed_items,
            'summary': {
                'total_items': len(processed_items),
                'operations_applied': operations,
                'transformed_fields': transformed_fields
            }
        }

        logger.info(f'Successfully processed {len(processed_items)} items with operations: {operations}')
        return jsonify(result), 200

    except ValueError as ve:
        logger.warning(f'Validation error: {ve}')
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        logger.error(f'Error processing data: {e}')
        return jsonify({'error': 'Internal server error during processing'}), 500

@api_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200
