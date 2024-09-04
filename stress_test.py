import subprocess

def cpu_stress_test():
    print("Performing CPU stress test...")
    subprocess.run(["stress", "--cpu", "4", "--timeout", "30"])

def memory_stress_test():
    print("Performing memory stress test...")
    subprocess.run(["stress", "--vm", "2", "--vm-bytes", "1G", "--timeout", "120"])

def disk_stress_test():
    print("Performing disk stress test...")
    subprocess.run(["stress", "--hdd", "2", "--timeout", "30"])

def sql_stress_test():
    print("Preparing SQL stress test (creating tables)...")
    # Preparing the database by creating the necessary tables
    subprocess.run(["sysbench", "--db-driver=mysql", "--mysql-user=root",
                    "--mysql-db=test", "--tables=10", "--table-size=10000", "oltp_read_write", "prepare"])

    print("Running SQL stress test to generate ~700+ queries per second...")
    # Running the stress test with increased threads and table size to achieve 700+ queries/sec
    subprocess.run(["sysbench", "--db-driver=mysql", "--mysql-user=root",
                    "--mysql-db=test", "--tables=10", "--table-size=10000", "--threads=256", "--time=60", "oltp_read_write", "run"])

    print("Cleaning up after SQL stress test (dropping tables)...")
    # Cleaning up the tables after the test
    subprocess.run(["sysbench", "--db-driver=mysql", "--mysql-db=test", "--tables=10", "--table-size=10000", "oltp_read_write", "cleanup"])



def main():
    while True:
        print("\nSelect an option:")
        print("1. CPU Stress Test")
        print("2. Memory Stress Test")
        print("3. Disk Stress Test")
        print("4. SQL Stress Test")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            cpu_stress_test()
        elif choice == '2':
            memory_stress_test()
        elif choice == '3':
            disk_stress_test()
        elif choice == '4':
            sql_stress_test()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
