import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def block_ip(ip_address):
    """
    Executes a Windows netsh command to block the specified IP address.
    Requires Administrator privileges.
    """
    if not ip_address or ip_address == "N/A" or ip_address == "Unknown":
        logging.warning("Invalid IP address. Skipping block action.")
        return False

    rule_name = f"Block_IP_{ip_address}"
    command = f'netsh advfirewall firewall add rule name="{rule_name}" dir=in action=block remoteip={ip_address}'

    try:
        # Run the command with subprocess
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            logging.info(f"Successfully created firewall rule to block IP: {ip_address}")
            return True
        else:
            if "requires elevation" in result.stderr.lower() or "requires elevation" in result.stdout.lower():
                logging.error(f"Simulation: Failed to block IP {ip_address} natively. Administrator privileges required. (Logged Action)")
            else:
                logging.error(f"Failed to block IP {ip_address}: {result.stderr.strip()} {result.stdout.strip()}")
            return False

    except Exception as e:
        logging.error(f"Error executing block command for IP {ip_address}: {e}")
        return False

def alert_admin(message):
    """
    Simulates sending an alert to the administrator.
    """
    logging.warning(f"🚨 ADMIN ALERT: {message}")
