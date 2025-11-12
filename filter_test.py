filter_params = [
    {"filter_key": "RG_TargetName", "filter_symbol": "like"},
    {"filter_key": "lastModifiedBy", "filter_symbol": "like"}
]

filter_expression_dict = {
    "extract_type": "specific",
    "RG_TargetName": ["GIPR","CAdherin"],
    "lastModifiedBy": []
}

from typing import List, Dict, Optional
from collections import defaultdict

from typing import List, Dict, Optional
from collections import defaultdict

def get_expression(
    filter_params: List[Dict],
    filter_expression_dict: Dict = None,
    expr: Optional[str] = None
) -> Optional[str]:
    """
    Build combined filter expression from params and dict, skipping empty lists.
    """
    
    key_values_map = defaultdict(set)
    key_symbol_map = {}

    # --- Step 1: gather values from filter_params ---
    for param in filter_params:
        key = param.get("filter_key")
        symbol = param.get("filter_symbol", "like")
        values = param.get("filter_value", [])

        if not key or not values:
            continue

        if isinstance(values, list):
            key_values_map[key].update(values)
        else:
            key_values_map[key].add(values)

        key_symbol_map[key] = symbol

    # --- Step 2: gather values from filter_expression_dict ---
    if filter_expression_dict and filter_expression_dict.get("extract_type") == "specific":
        for param in filter_params:
            key = param.get("filter_key")
            symbol = param.get("filter_symbol", "like")

            dict_values = filter_expression_dict.get(key, [])
            if not dict_values:
                continue  # ✅ skip empty lists safely

            wildcard_values = [f"%{val}%" for val in dict_values]
            key_values_map[key].update(wildcard_values)
            key_symbol_map[key] = symbol

    # --- Step 3: build expressions ---
    expressions = []
    for key, values in key_values_map.items():
        if not values:
            continue  # ✅ skip if values are still empty

        symbol = key_symbol_map.get(key, "like")
        or_exprs = [f"metadata['{key}'] {symbol} '{v}'" for v in values]
        
        # ✅ only build expression if there's something to join
        if not or_exprs:
            continue

        expr_str = f"({' || '.join(or_exprs)})" if len(or_exprs) > 1 else or_exprs[0]
        expressions.append(expr_str)

    # --- Step 4: combine with existing expr ---
    if not expressions:
        return expr  # ✅ no new filters, just return base condition

    final_expr = " && ".join(expressions)
    if expr:
        final_expr = f"{expr} && {final_expr}"

    return final_expr

# Example usage
result_expr = get_expression(filter_params, filter_expression_dict, expr="partition_key=='9mBfKx2bu2mi9NdJ2KJ7Zo_Unstruct_tppm_train_program_Ver_4_1_qa'")
print(result_expr)