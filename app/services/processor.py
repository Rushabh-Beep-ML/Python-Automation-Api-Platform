import logging
from typing import List

logger = logging.getLogger(__name__)

class DataProcessor:

    def clean_whitespace(self, items: List[str]) -> List[str]:
        cleaned = []
        for item in items:
            if isinstance(item, str):
                stripped = item.strip()
                if stripped:
                    cleaned.append(stripped)
        logger.debug(f'Cleaned whitespace: {len(items)} items -> {len(cleaned)} items')
        return cleaned

    def remove_duplicates(self, items: List[str]) -> List[str]:
        seen = set()
        unique = []
        for item in items:
            if isinstance(item, str) and item not in seen:
                seen.add(item)
                unique.append(item)
        logger.debug(f'Removed duplicates: {len(items)} items -> {len(unique)} items')
        return unique

    def normalize_case(self, items: List[str], case_type: str = 'lower') -> List[str]:
        normalized = []
        for item in items:
            if not isinstance(item, str):
                normalized.append(item)
                continue

            if case_type == 'lower':
                normalized.append(item.lower())
            elif case_type == 'upper':
                normalized.append(item.upper())
            elif case_type == 'title':
                normalized.append(item.title())
            elif case_type == 'sentence':
                if item:
                    normalized.append(item[0].upper() + item[1:].lower() if len(item) > 1 else item.upper())
                else:
                    normalized.append(item)
            else:
                normalized.append(item)

        logger.debug(f'Normalized case to {case_type}: {len(items)} items')
        return normalized

    def parse_key_value(self, items: List[str]) -> List[dict]:
        parsed = []
        for item in items:
            if not isinstance(item, str):
                parsed.append({'raw': item})
                continue

            if ':' in item:
                parts = item.split(':', 1)
                parsed.append({
                    'key': parts[0].strip(),
                    'value': parts[1].strip() if len(parts) > 1 else ''
                })
            else:
                parsed.append({'raw': item})

        logger.debug(f'Parsed key-value pairs: {len(parsed)} items')
        return parsed
