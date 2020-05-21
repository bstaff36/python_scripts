import subprocess
process = subprocess.Popen(['echo' , 'additional output'], stdout = subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
stdout, stderr = process.communicate()
print(stdout)
print(stdout.decode('utf-8'))  #decode byte-array into utf-8 string