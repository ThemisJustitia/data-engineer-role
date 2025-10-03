"""
You receive newline-delimited JSON clickstream events with nested structures and arrays. 

Build json_to_summary(json_lines: list[str]) that returns:
- A clean events DataFrame with columns: user_id, session_id, event_name, event_ts (tz=UTC), item_id, price, device_type.
- A daily summary DataFrame with: event_date, users, sessions, clicks, purchases, revenue.

Notes:
- metadata.device.type is optional ⇒ fill missing as "unknown".
- items may be an array; explode to one row per item. If missing, keep one row with item_id=None, price=0.
- Parse timestamps to UTC. Drop rows with invalid timestamps.
- Purchases are events with event_name == "purchase", clicks with "click".


De-dupe exact duplicate events by (event_id) if present; otherwise by (user_id, session_id, event_name, event_ts, item_id).
"""

import json
import pandas as pd

def json_to_summary(json_lines: list[str]):
    # TODO: parse the json_lines into a list of dicts
    # TODO: normalize nested fields and explode items
    # TODO: enforce schema, types, timezone, and dedupe
    # TODO: compute daily summary aggregations
    # return event
