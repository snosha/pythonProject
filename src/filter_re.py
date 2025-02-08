import re
from typing import Dict, List


def filter_operations_by_description(operations: List[Dict], search_term: str) -> List[Dict]:
    if not search_term.strip():  # Проверка на пустую строку
        return operations

    pattern = re.compile(re.escape(search_term), re.IGNORECASE)
    return [op for op in operations if pattern.search(op.get("description", ""))]


def count_operations_by_category(operations: List[Dict], categories: List[str]) -> Dict[str, int]:
    category_counts = {category: 0 for category in categories}

    for operation in operations:
        description = operation.get("description", "").lower()
        for category in categories:
            if category.lower() in description:  # Возможны пересечения категорий
                category_counts[category] += 1

    return category_counts
