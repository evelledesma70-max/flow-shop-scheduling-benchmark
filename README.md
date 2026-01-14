# Benchmark de Flow Shop Scheduling

Este repositorio contiene un benchmark completo para el problema de **Flow Shop Scheduling**, aplicado a un entorno industrial simulado (fábrica de bebidas).

El proyecto evalúa el tiempo total de procesamiento (makespan) de distintos conjuntos de trabajos procesados secuencialmente en múltiples máquinas.

---

## 📌 Objetivo del proyecto

- Simular un sistema de producción tipo Flow Shop
- Evaluar el desempeño del sistema usando datasets de diferentes tamaños
- Calcular el makespan total
- Facilitar la comparación entre escenarios pequeños, medianos y grandes

---

## 🧠 Contexto del problema

Cada trabajo debe pasar por las siguientes máquinas en el mismo orden:

1. Limpieza de botellas
2. Llenado
3. Taponado
4. Etiquetado

---

## 📂 Estructura del proyecto

- `main.py`: código principal ejecutable
- `data/`: datasets organizados por tamaño
- `README_DATASETS.md`: descripción de los datasets
- `requirements.txt`: dependencias del proyecto

---

## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/flow-shop-scheduling-benchmark.git


Instalar dependencias

pip install -r requirements.txt

Ejecutar el código

python main.py


