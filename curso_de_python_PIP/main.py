# Importar el módulo pyplot con el alias plt
import matplotlib.pyplot as plt
# Crear la figura y los ejes
fig, ax = plt.subplots()
# Dibujar puntos
ax.scatter(x = [1, 2, 3], y = [3, 2, 1])
# Guardar el gráfico en formato png
plt.savefig('diagrama-dispersion.png')
# Mostrar el gráfico
plt.show()

# ¿Que es pip?
# PIP es el gestor de paquetes de python, es posible buscar librerías en la pagina pypi.org.

# Ver la versión de pip pip3 -v.
# Instalación de paquetes pip3 install <libreria>.
# Listar las librerías que se tienen en el entorno de python global pip3 list.
# Listar todas las librerías de python instaladas por el usuario pip3 freeze.