import os

def run_dashboard():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

    print("=== Health Monitoring Dashboard ===")
    print("1. Simulate Health Data")
    print("2. Start Data Ingestion")
    print("3. Exit")

    while True:
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            import simulate_iot_data
            simulate_iot_data.simulate_health_data()
        elif choice == '2':
            import data_ingestion
            data_ingestion.start_ingestion()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
