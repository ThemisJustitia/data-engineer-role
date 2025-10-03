"""
You’re given a daily sales aggregator. 
It should: 
  (a) parse timestamps, 
  (b) filter to one day, 
  (c) de-dupe orders on order_id, and 
  (d) compute revenue = qty * unit_price. 
Fix any bugs, make it correct and idempotent, and explain your changes.
"""


import pandas as pd

def daily_sales(orders_df=pd.DataFrame(), day="2025-10-01", tz="US/Eastern"):
    # filter to the day
    orders_df['order_ts'] = pd.to_datetime(orders_df['order_ts'])  # timezone missing?
    day_start = pd.Timestamp(day).tz_localize(tz)
    day_end = day_start + pd.Timedelta(days=1)
    mask = (orders_df['order_ts'] >= day_start) & (orders_df['order_ts'] <= day_end)  # inclusive end?

    # drop dupes but keep latest row
    orders_df.sort_values('order_ts', inplace=True)
    deduped = orders_df.drop_duplicates(subset=['order_id'], keep='first')

    # compute revenue
    deduped['revenue'] = deduped['qty'] * deduped['unit_price']  # possible dtype?
    day_df = deduped[mask]
    total_qty = day_df['qty'].sum()
    total_rev = day_df['revenue'].sum()

    # return summary
    return {
        "date": day,
        "orders": len(day_df),
        "qty": float(total_qty),
        "revenue": round(total_rev, 2),
    }
