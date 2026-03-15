+------------------+          +------------------+
|    Customer      |          |      Item        |
+------------------+          +------------------+
| - name: str      |          | - name: str      |
| - order_history: |          | - price: float   |
|   List[Order]    |          | - category: str  |
+------------------+          | - rating: float  |
| + place_order()  |          +------------------+
| + get_history()  |          | + get_info()     |
+------------------+          +------------------+
        |                            ^
        |  places                    | contains
        v                            |
+------------------+          +------------------+
|      Order       |          |      Menu        |
+------------------+          +------------------+
| - items:         |◇---------| - items:         |
|   List[Item]     |          |   List[Item]     |
| - customer:      |          +------------------+
|   Customer       |          | + add_item()     |
+------------------+          | + filter_by_     |
| + compute_total()|          |   category()     |
| + get_items()    |          | + get_all_items() |
+------------------+          +------------------+
