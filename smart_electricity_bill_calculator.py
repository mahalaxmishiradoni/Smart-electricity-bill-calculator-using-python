def get_customer_details():
    """Ask for customer details and return them with non-negative units."""
    customer_name = input("Enter customer name: ").strip()
    customer_id = input("Enter customer ID: ").strip()

    while True:
        try:
            units_consumed = float(input("Enter electricity units consumed: "))
            if units_consumed < 0:
                print("Units consumed cannot be negative. Please try again.")
            else:
                return customer_name, customer_id, units_consumed
        except ValueError:
            print("Please enter a valid number of units.")


def calculate_bill(units):
    """Return energy charge, service charge, and final bill amount."""
    if units <= 100:
        rate_per_unit = 2
    elif units <= 200:
        rate_per_unit = 4
    elif units <= 500:
        rate_per_unit = 6
    else:
        rate_per_unit = 8

    energy_charge = units * rate_per_unit
    service_charge = 100
    final_amount = energy_charge + service_charge
    return energy_charge, service_charge, final_amount


def display_bill(customer_name, customer_id, units, energy_charge,
                 service_charge, final_amount):
    """Print an itemized electricity bill."""
    print("\n" + "=" * 38)
    print("           ELECTRICITY BILL")
    print("=" * 38)
    print(f"Customer name   : {customer_name}")
    print(f"Customer ID     : {customer_id}")
    print(f"Units consumed  : {units:g}")
    print("-" * 38)
    print(f"Energy charge   : ₹{energy_charge:,.2f}")
    print(f"Service charge  : ₹{service_charge:,.2f}")
    print("-" * 38)
    print(f"Final amount    : ₹{final_amount:,.2f}")
    print("=" * 38)


if __name__ == "__main__":
    name, customer_id, units = get_customer_details()
    energy, service, total = calculate_bill(units)
    display_bill(name, customer_id, units, energy, service, total)