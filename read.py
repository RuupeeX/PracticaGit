'''
Inicio
'''
def read_and_sort_file(file_path):
	with open(file_path, 'r', encoding='utf-8') as file:
		names = file.readlines()
	
	# busqueda del name
	names = [name.strip() for name in names]
	names.sort()
	
	# imprime el name
	for name in names:
		print(name)
