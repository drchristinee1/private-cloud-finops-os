from models.cost_driver_model import calculate_cost_drivers
from models.rate_card_generator import generate_rate_card
from models.allocation_engine import allocate_costs


def main():
    # Step 1: Calculate cost drivers
    drivers = calculate_cost_drivers(
        total_cost=100000,
        total_vcpu_hours=200000,
        total_gb_ram_hours=500000,
        total_storage_gb=100000
    )

    print("\nPrivate Cloud Cost Drivers (Capacity Economics):\n")
    for k, v in drivers.items():
        print(f"{k}: ${v}")

    # Step 2: Generate internal pricing
    rate_card = generate_rate_card(drivers)

    print("\nInternal Rate Card (Pricing Signals):\n")
    for k, v in rate_card.items():
        print(f"{k}: ${v}")

    # Step 3: Allocate cost by team/application
    usage_data = [
        {
            "team": "Payments",
            "application": "Checkout-Service",
            "vcpu_hours": 1000,
            "gb_ram_hours": 2000,
            "storage_gb": 500
        },
        {
            "team": "Analytics",
            "application": "Reporting-Engine",
            "vcpu_hours": 1500,
            "gb_ram_hours": 2500,
            "storage_gb": 700
        }
    ]

    allocations = allocate_costs(rate_card, usage_data)

    print("\nCost Allocation Report (Accountability Layer):\n")
    for item in allocations:
        print(
            f"Team: {item['team']}, "
            f"Application: {item['application']}, "
            f"Allocated Cost: ${item['allocated_cost']}"
        )


if __name__ == "__main__":
    main()
