import os
import logging

# Set up logging for admin actions
admin_log_file = 'admin_actions.log'
logging.basicConfig(
    filename=admin_log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def view_logs(log_file='logs/download_log.txt'):
    """View the contents of the specified log file."""
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            print(file.read())
    else:
        print(f"Log file '{log_file}' does not exist.")

def clear_logs(log_file='logs/download_log.txt'):
    """Clear the contents of the specified log file."""
    if os.path.exists(log_file):
        open(log_file, 'w').close()
        logging.info("Cleared download log.")
        print(f"Log file '{log_file}' has been cleared.")
    else:
        print(f"Log file '{log_file}' does not exist.")

def view_admin_logs():
    """View the contents of the admin actions log file."""
    if os.path.exists(admin_log_file):
        with open(admin_log_file, 'r') as file:
            print(file.read())
    else:
        print(f"Admin log file '{admin_log_file}' does not exist.")

def log_admin_action(action):
    """Log an admin action."""
    logging.info(action)

def main():
    while True:
        print("\nAdmin Control Panel")
        print("1. View Download Logs")
        print("2. Clear Download Logs")
        print("3. View Admin Logs")
        print("4. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            view_logs()
        elif choice == '2':
            clear_logs()
        elif choice == '3':
            view_admin_logs()
        elif choice == '4':
            log_admin_action("Exited admin control panel.")
            print("Exiting admin control panel.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
