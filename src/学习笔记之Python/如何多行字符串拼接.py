# -*- coding: utf-8 -*-
"""
@author: Hao
"""

start_timestamp = "2018-01-01 00:00:00"
end_timestamp = "2018-01-02 00:00:00"

# =============================================================================
# SELECT "timestamp", col1
# FROM tbl
# WHERE "timestamp" >= '2018-01-01 00:00:00' AND "timestamp" <= '2018-01-02 00:00:00'
# ORDER BY "timestamp" ASC
# =============================================================================
query = """
    SELECT "timestamp", col1
    FROM tbl
    WHERE "timestamp" >= '"""             \
    + start_timestamp +                 \
    """' AND "timestamp" <= '"""        \
    + end_timestamp +                   \
    """'
    ORDER BY "timestamp" ASC
    """

print(query)

# =============================================================================
# SELECT "timestamp", col1
# FROM tbl
# WHERE "timestamp" >= '2018-01-01 00:00:00' AND "timestamp" <= '2018-01-02 00:00:00'
# ORDER BY "timestamp" ASC
# =============================================================================
query = ("""
    SELECT "timestamp", col1
    FROM tbl
    WHERE "timestamp" >= '"""
    + start_timestamp +
    """' AND "timestamp" <= '"""
    + end_timestamp +
    """'
    ORDER BY "timestamp" ASC
    """)

print(query)
