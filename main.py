import data_ingestion
import simulate_iot_data  # Ensure this module is correctly implemented
import dashboard  # Ensure this module is correctly implemented

def main():
    print("=== Health Monitoring Dashboard ===2")
    print("1. Simulate Health Data")
    print("2. Start Data Ingestion")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        simulate_iot_data.simulate_health_data()
    elif choice == '2':
        dashboard.run_dashboard()
    elif choice == '3':
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please try again.")
        main()

if __name__ == "__main__":
    main()
