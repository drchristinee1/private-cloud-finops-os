def generate_rate_card(drivers):
    """
    Convert cost drivers into internal pricing signals (rate card)
    """

    rate_card = {
        "compute_per_vcpu_hour": drivers["cost_per_vcpu_hour"],
        "memory_per_gb_hour": drivers["cost_per_gb_ram_hour"],
        "storage_per_gb": drivers["cost_per_gb_storage"]
    }

    return rate_card


if __name__ == "__main__":
    sample_drivers = {
        "cost_per_vcpu_hour": 0.5,
        "cost_per_gb_ram_hour": 0.2,
        "cost_per_gb_storage": 1.0
    }

    rate_card = generate_rate_card(sample_drivers)

    print("\nInternal Rate Card:\n")
    for k, v in rate_card.items():
        print(f"{k}: ${v}")
