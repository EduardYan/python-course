import subprocess
from io import open

'''
output = subprocess.Popen('ls', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)

print(output.stdout.read())

print(output.stderr.read())

output.wait()
'''

output = subprocess.Popen('ls -a', stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)

listado = output.stdout.read()
jsjsje
error = output.stderr.read()

print(listado)
print(error)

output.wait()


# saving the the salidad en el arhivo
file = open('listado.txt', 'a')
content = str(listado + error)
file.write(content)
file.close()
