from sqlparse.sql import Function, Where


# Optimization # 6
def checkFiltering(optimizations, schema, parsed_queries, *db_params):
    msg = "Transformations on partitioned columns are more computationally expensive than direct comparisons." + \
            " Try and move the transformation to the other side of the comparison on the following column: "
    for stmt_list in parsed_queries:
        for stmt in stmt_list:
            seen_stmt = ""
            for token in stmt.tokens:
                if isinstance(token, Where):
                    # newlines in sqlparse sometimes group clauses together - need to recalculate
                    for item in token.tokens:
                        if isinstance(item, Function):
                            params = [str(token) for token in list(item.get_parameters())]
                            for param in params:
                                if param in schema["partitions"]:
                                    lineno = seen_stmt.count("\n")
                                    optimizations[stmt].append((lineno, msg + param))

                seen_stmt += str(token)
