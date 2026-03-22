from models.cost_driver_model import calculate_cost_drivers

def main():
    drivers = calculate_cost_drivers(
        total_cost=100000,
        total_vcpu_hours=200000,
        total_gb_ram_hours=500000,
        total_storage_gb=100000
    )

    print("\nPrivate Cloud Cost Drivers:\n")
    for k, v in drivers.items():
        print(f"{k}: ${v}")

if __name__ == "__main__":
    main()
