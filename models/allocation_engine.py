def allocate_costs(rate_card, usage_data):
    allocations = []

    for item in usage_data:
        team = item["team"]
        application = item["application"]
        vcpu_hours = item["vcpu_hours"]
        gb_ram_hours = item["gb_ram_hours"]
        storage_gb = item["storage_gb"]

        total_cost = (
            vcpu_hours * rate_card["compute_per_vcpu_hour"] +
            gb_ram_hours * rate_card["memory_per_gb_hour"] +
            storage_gb * rate_card["storage_per_gb"]
        )

        allocations.append({
            "team": team,
            "application": application,
            "allocated_cost": round(total_cost, 2)
        })

    return allocations


if __name__ == "__main__":
    sample_rate_card = {
        "compute_per_vcpu_hour": 0.5,
        "memory_per_gb_hour": 0.2,
        "storage_per_gb": 1.0
    }

    sample_usage_data = [
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

    allocations = allocate_costs(sample_rate_card, sample_usage_data)

    print("\nCost Allocation Report:\n")
    for item in allocations:
        print(
            f"Team: {item['team']}, "
            f"Application: {item['application']}, "
            f"Allocated Cost: ${item['allocated_cost']}"
        )
