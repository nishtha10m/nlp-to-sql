def generate_sql(parsed, table_name, columns):
    op = parsed["operation"]
    metric = parsed["metric"]
    group = parsed["group"]

    if op in ["total", "sum"]:
        agg = f"SUM({metric})"
    elif op in ["average", "avg"]:
        agg = f"AVG({metric})"
    elif op == "count":
        agg = "COUNT(*)"
    else:
        return None

    if group:
        return f"SELECT {group}, {agg} FROM {table_name} GROUP BY {group};"
    else:
        return f"SELECT {agg} FROM {table_name};"
