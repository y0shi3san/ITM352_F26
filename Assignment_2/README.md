# Sales Dashboard User Guide

Run `V4.py` from the repository root:

```text
python Assignment_2/V4.py
```

At startup, choose one of the following sources:

- **Sales Data (online)**: the primary hosted CSV.
- **Alternate sales data (Google Sheets)**: the alternate hosted CSV.

The dashboard loads the selected CSV, then displays a menu of analyses. Enter
the menu number to run an analysis; choose **Exit the program** to quit. If a
data source cannot be loaded, the error is displayed and the dashboard stops
rather than continuing with missing data.

## Region and product percentages

Choose **Sales by region and product with percentages**. The pivot table
contains quantity and total sales (`quantity * unit_price`) for each region
and product, plus:

- `quantity_pct_of_region`: that product's share of the region's total quantity.
- `sales_pct_of_region`: that product's share of the region's total sales.

For example, if products in one region account for 20 and 30 units, their
quantity percentages are 40% and 60%. Percentages are calculated separately
within each region; each nonzero regional total therefore sums to 100%.
Zero-value regional totals are shown as undefined percentages.

The analytic recognizes either `product` or `produce_name` as the product
column, so the two selectable datasets can use either name.
