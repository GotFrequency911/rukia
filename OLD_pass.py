import subprocess
try:
    command = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='ignore')
    profiles = [line.split(":")[1][1:-1] for line in command.split('\n') if "All User Profile" in line]
    
    print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
    print("-" * 50)
    for profile in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors='ignore')
            password_lines = [line.split(":")[1][1:-1] for line in results.split('\n') if "Key Content" in line]
            password = password_lines[0] if password_lines else "No password found"
            print("{:<30}| {:<}".format(profile, password))
        except subprocess.CalledProcessError:
            print("{:<30}| {:<}".format(profile, "Error reading profile"))

except Exception as e:
    print(f"An error occurred: {e}")

input("\nPress Enter to exit...")
