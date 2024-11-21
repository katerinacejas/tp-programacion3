import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Suponiendo que tienes los resultados en el DataFrame 'df'

# Simula algunos datos para Backtracking, Warnsdorff y Branch & Bound
# Asume que ya tienes los resultados para cada técnica
results = [
    {"N": 5, "Backtracking": 5000, "Warnsdorff": 1000, "Branch & Bound": 300},
    {"N": 6, "Backtracking": 20000, "Warnsdorff": 4000, "Branch & Bound": 1500},
    {"N": 7, "Backtracking": 50000, "Warnsdorff": 8000, "Branch & Bound": 2500},
]

df = pd.DataFrame(results)

# Graficar barras apiladas
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df["N"], df["Backtracking"], label="Backtracking")
ax.bar(df["N"], df["Warnsdorff"], bottom=df["Backtracking"], label="Warnsdorff")
ax.bar(df["N"], df["Branch & Bound"], bottom=df["Backtracking"] + df["Warnsdorff"], label="Branch & Bound")

ax.set_xlabel("Tamaño del Tablero (N)")
ax.set_ylabel("Nodos Explorados")
ax.set_title("Comparación de Nodos Explorados por Técnica")
ax.legend()
plt.grid(True)
plt.show()

# Gráfico de Nodos Explorados con escala logarítmica
plt.figure(figsize=(10, 5))
plt.plot(df["N"], df["Nodes Explored"], marker='o', label="Nodos Explorados")
plt.xlabel("Tamaño del Tablero (N)")
plt.ylabel("Nodos Explorados (Escala Logarítmica)")
plt.title("Nodos Explorados con Escala Logarítmica")
plt.legend()
plt.yscale("log")  # Cambio a escala logarítmica
plt.grid(True)
plt.show()

# Gráfico de Tiempo de Ejecución con escala logarítmica
plt.figure(figsize=(10, 5))
plt.plot(df["N"], df["Time Taken (s)"], marker='o', color="r", label="Tiempo de Ejecución")
plt.xlabel("Tamaño del Tablero (N)")
plt.ylabel("Tiempo (s) (Escala Logarítmica)")
plt.title("Tiempo de Ejecución con Escala Logarítmica")
plt.legend()
plt.yscale("log")  # Cambio a escala logarítmica
plt.grid(True)
plt.show()

# Supongamos que tienes un DataFrame con los tiempos de ejecución para cada técnica y cada tamaño de tablero
heatmap_data = pd.DataFrame({
    'Backtracking': [0.2, 2.5, 30],
    'Warnsdorff': [0.1, 1.0, 12],
    'Branch & Bound': [0.15, 1.5, 15],
}, index=[5, 6, 7])

# Crear un Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt=".2f", cbar_kws={'label': 'Tiempo de Ejecución (s)'})
plt.title("Heatmap de Tiempos de Ejecución por Técnica y Tamaño de Tablero")
plt.xlabel("Técnica")
plt.ylabel("Tamaño del Tablero (N)")
plt.show()
