import requests
import logging
from typing import List, Tuple

logger = logging.getLogger(__name__)

class DataEnricher:

    def __init__(self, api_base_url: str = 'https://jsonplaceholder.typicode.com', timeout: int = 10):
        self.api_base_url = api_base_url
        self.timeout = timeout

    def enrich_items(self, items: List[str]) -> Tuple[List[dict], List[str]]:
        enriched = []
        transformed_fields = ['id', 'enriched_from_api']

        try:
            for idx, item in enumerate(items):
                enriched_item = {
                    'original': item,
                    'id': idx + 1,
                    'enriched_from_api': False
                }

                try:
                    api_data = self._fetch_from_api(idx)
                    if api_data:
                        enriched_item['api_metadata'] = {
                            'title': api_data.get('title', ''),
                            'status_code': 200
                        }
                        enriched_item['enriched_from_api'] = True
                except Exception as api_error:
                    logger.warning(f'Failed to enrich item {idx + 1}: {api_error}')
                    enriched_item['api_metadata'] = {'error': str(api_error)}

                enriched.append(enriched_item)

        except Exception as e:
            logger.error(f'Error during enrichment: {e}')
            enriched = [{'original': item, 'id': idx + 1, 'error': 'Enrichment failed'} for idx, item in enumerate(items)]

        return enriched, transformed_fields

    def _fetch_from_api(self, item_id: int) -> dict:
        try:
            url = f'{self.api_base_url}/posts/{(item_id % 100) + 1}'
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f'API request failed: {e}')
            raise
