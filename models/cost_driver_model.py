def calculate_cost_drivers(total_cost, total_vcpu_hours, total_gb_ram_hours, total_storage_gb):
    drivers = {}

    drivers["cost_per_vcpu_hour"] = round(total_cost / total_vcpu_hours, 4) if total_vcpu_hours else 0
    drivers["cost_per_gb_ram_hour"] = round(total_cost / total_gb_ram_hours, 4) if total_gb_ram_hours else 0
    drivers["cost_per_gb_storage"] = round(total_cost / total_storage_gb, 4) if total_storage_gb else 0

    return drivers


if __name__ == "__main__":
    example = calculate_cost_drivers(
        total_cost=100000,
        total_vcpu_hours=200000,
        total_gb_ram_hours=500000,
        total_storage_gb=100000
    )

    print("Cost Drivers:")
    for k, v in example.items():
        print(f"{k}: ${v}")
