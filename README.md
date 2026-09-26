# Smart Electricity Bill Calculator

A beginner-friendly Python console program that collects customer details,
calculates an electricity bill, and prints a formatted bill.

## Requirements

- Python 3
- No external libraries

## Run the program

Open a terminal in this project folder and run:

```bash
python smart_electricity_bill_calculator.py
```

## Program flow

1. `get_customer_details()` asks for the customer's name, customer ID, and units consumed. It converts the units to a number and asks again if the input is invalid or negative.
2. `calculate_bill(units)` chooses the rate for the matching consumption range and returns the energy charge, fixed service charge, and final amount.
3. `display_bill(...)` prints the customer details and itemized charges in a clean bill layout.
4. The main block calls these functions in order.

## Electricity rates

The rate for a range is applied to all units consumed:

| Units consumed | Rate per unit |
| --- | ---: |
| 0–100 | ₹2 |
| More than 100–200 | ₹4 |
| More than 200–500 | ₹6 |
| More than 500 | ₹8 |

A fixed service charge of ₹100 is added to the energy charge.