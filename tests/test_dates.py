import re
from collections import defaultdict
from collections import OrderedDict
import sys
sys.path.append('../user_query_optimizer')
import optimizer
import sqlparse

def test_dates(queries, presto_op):
    # dictionary from test-query-file -> list of line numbers in that query with an approx optimization
    correct_ops = {
        'test-query-2.txt': [3]
    }
    test_ops = {}

    for ind, query in enumerate(queries):
        # Parse query and extract ctes
        # Strip comments to help sqlparse correctly extract the identifier list
        formatted_query = str(sqlparse.format(query, strip_comments = True)).strip()
        parsed_queries = presto_op._parse_query(formatted_query)

        presto_op._checkDateParse(parsed_queries)

        # Find subquery in original query again, and adjust line numbers
        adjusted_opts = presto_op._adjust_linenums(formatted_query)

        # Add optimizations for current query to dictionary for all test files
        if len(adjusted_opts) > 0:
            test_ops['test-query-' + str(ind + 1) + '.txt'] = adjusted_opts.keys()

        # Sort list of lines for comparison
        for k, v in test_ops.iteritems():
            test_ops[k] = sorted(v)

    assert len(test_ops) == 1
    assert test_ops == correct_ops
