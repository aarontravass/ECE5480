import subprocess

ip_list = []
print("Enter 5 different IP addresses separated by new lines")
for _ in range(5):
    ip_list.append(input())
for ip in ip_list:
    proc = subprocess.Popen(['ping', '-n', '3', ip], stdout=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    if proc.returncode == 0:
        print('{} is UP'.format(ip))
    else:
        print('{} is DOWN <OR> there is a NETWORK ERROR'.format(ip))
