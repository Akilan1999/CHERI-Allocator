import paramiko
from scp import SCPClient
import os

def ssh_execute_and_retrieve(
    remote_host, remote_user, remote_password, 
    remote_program, remote_output_path, local_save_path
):
    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the remote machine
        print("Connecting to remote host...")
        # ssh.connect(remote_host, username=remote_user, password=remote_password)
        ssh.connect(remote_host, username=remote_user)
        print("Connected successfully.")
        
        # Execute the remote program
        print(f"Running remote program: {remote_program}")
        stdin, stdout, stderr = ssh.exec_command(remote_program)
        stdout.channel.recv_exit_status()  # Wait for command to finish
        
        # Display the program's output
        print("Program output:")
        for line in stdout.readlines():
            print(line.strip())
        print("Program errors (if any):")
        for line in stderr.readlines():
            print(line.strip())
        
        # Use SCP to retrieve output files
        print(f"Retrieving files from {remote_output_path} to {local_save_path}...")
        with SCPClient(ssh.get_transport()) as scp:
            scp.get(remote_output_path, local_path=local_save_path)
        print(f"Files retrieved successfully to {local_save_path}.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ssh.close()
        print("Connection closed.")

if __name__ == "__main__":
    # Remote server details
    remote_host = "192.0.0.3"  # Replace with the remote host IP
    remote_user = "akilan"           # Replace with the remote username
    remote_password = ""   # Replace with the remote password
    
    # Program to execute and file paths
    remote_program = "/path/to/your/program --option"  # Command to run
    remote_output_path = "/path/to/remote/output/*"    # Path to the output files
    local_save_path = "./downloaded_files"            # Local folder to save the files
    
    # Create the local save path directory if it doesn't exist
    os.makedirs(local_save_path, exist_ok=True)
    
    # Run the function
    ssh_execute_and_retrieve(
        remote_host, remote_user, remote_password, 
        remote_program, remote_output_path, local_save_path
    )
