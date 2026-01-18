import re

def parse_query(query, columns):
    query = query.lower()

    # detect grouping (by <column>)
    group_col = None
    for col in columns:
        if f"by {col.lower()}" in query:
            group_col = col
            break

    # detect operation
    op = None
    for word in ["total", "sum", "average", "avg", "count"]:
        if word in query:
            op = word
            break

    # detect metric
    metric = None
    for col in columns:
        if col.lower() in query and col.lower() != group_col.lower():
            metric = col
            break

    return {"operation": op, "group": group_col, "metric": metric}
