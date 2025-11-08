#!/usr/bin/env python3
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Crear figura
fig = plt.figure(figsize=(16, 12), facecolor='#0a0e27')
ax = fig.add_subplot(111, projection='3d', facecolor='#0a0e27')

# Dimensiones del terminal (en mm)
width = 85
height = 165
depth = 30

def create_box(x, y, z, w, h, d, color='#2c3e50', alpha=1.0, edgecolor='black'):
    """Crea un box 3D"""
    # Definir vértices del box
    vertices = [
        [x, y, z],
        [x + w, y, z],
        [x + w, y + h, z],
        [x, y + h, z],
        [x, y, z + d],
        [x + w, y, z + d],
        [x + w, y + h, z + d],
        [x, y + h, z + d]
    ]

    # Definir las 6 caras del box
    faces = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],  # Bottom
        [vertices[2], vertices[3], vertices[7], vertices[6]],  # Top
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # Front
        [vertices[4], vertices[5], vertices[6], vertices[7]],  # Back
        [vertices[0], vertices[3], vertices[7], vertices[4]],  # Left
        [vertices[1], vertices[2], vertices[6], vertices[5]]   # Right
    ]

    # Crear colección de polígonos
    poly = Poly3DCollection(faces, alpha=alpha, facecolor=color, edgecolor=edgecolor, linewidth=0.5)
    ax.add_collection3d(poly)
    return poly

# === CUERPO PRINCIPAL ===
create_box(-width/2, -height/2, -depth/2, width, height, depth,
          color='#34495e', alpha=0.95, edgecolor='#1a252f')

# === PANEL FRONTAL ===
create_box(-width/2 + 3, -height/2 + 3, depth/2 - 2, width - 6, height - 6, 5,
          color='#1a252f', alpha=1.0, edgecolor='black')

# === SCANNER GM67 (grande y prominente) ===
scanner_y = height/2 - 50

# Marco del scanner
create_box(-36, scanner_y - 23, depth/2, 72, 46, 10,
          color='#0a0a0a', alpha=1.0, edgecolor='#333333')

# Cuerpo del scanner
create_box(-34, scanner_y - 21, depth/2 + 5, 68, 42, 12,
          color='#1a1a1a', alpha=1.0, edgecolor='#444444')

# Ventana de vidrio del scanner (roja)
create_box(-30, scanner_y - 17, depth/2 + 11, 60, 34, 3,
          color='#660000', alpha=0.7, edgecolor='#ff0000')

# Líneas rojas del scanner (sensor láser)
for i in range(8):
    y_pos = scanner_y - 15 + i * 4
    create_box(-25, y_pos - 0.25, depth/2 + 11.5, 50, 0.5, 1,
              color='#ff0000', alpha=0.9, edgecolor='#ff0000')

# Etiqueta "SCANNER"
create_box(-25, scanner_y - 29, depth/2 + 11, 50, 6, 1,
          color='#ffffff', alpha=0.8, edgecolor='#cccccc')

# LEDs del scanner
led_positions = [(-25, scanner_y + 18), (25, scanner_y + 18)]
led_colors = ['#ff0000', '#00ff00']

for (led_x, led_y), led_color in zip(led_positions, led_colors):
    # Simular esfera LED con pequeño box
    create_box(led_x - 2, led_y - 2, depth/2 + 11, 4, 4, 2,
              color=led_color, alpha=1.0, edgecolor=led_color)

# === PANTALLA OLED ===
display_y = height/2 - 110

# Marco de la pantalla
create_box(-26, display_y - 15, depth/2, 52, 30, 4,
          color='#000000', alpha=1.0, edgecolor='#222222')

# Pantalla activa (verde)
create_box(-23, display_y - 12, depth/2 + 4, 46, 24, 2,
          color='#1a4d2e', alpha=1.0, edgecolor='#00ff00')

# Líneas de texto simuladas en la pantalla
text_lines = [
    {'y': 8, 'width': 35, 'color': '#00ff00'},
    {'y': 4, 'width': 30, 'color': '#00cc00'},
    {'y': 0, 'width': 38, 'color': '#00ff00'},
    {'y': -4, 'width': 25, 'color': '#00aa00'},
    {'y': -8, 'width': 32, 'color': '#00dd00'}
]

for line in text_lines:
    create_box(-line['width']/2, display_y + line['y'] - 1, depth/2 + 6.5,
              line['width'], 2, 0.5,
              color=line['color'], alpha=0.9, edgecolor=line['color'])

# Borde iluminado de la pantalla
create_box(-24, display_y - 13, depth/2 + 6, 48, 26, 1.5,
          color='#00ff00', alpha=0.3, edgecolor='#00ff00')

# === BOTONES (4 botones táctiles) ===
button_y = -height/2 + 40
button_spacing = 19
button_start_x = -28.5
button_colors = ['#4CAF50', '#2196F3', '#f44336', '#FF9800']

for i, color in enumerate(button_colors):
    x = button_start_x + i * button_spacing
    # Base del botón
    create_box(x - 6, button_y - 6, depth/2, 12, 12, 2,
              color='#1a1a1a', alpha=1.0, edgecolor='#000000')
    # Botón superior
    create_box(x - 5, button_y - 5, depth/2 + 3, 10, 10, 3,
              color=color, alpha=1.0, edgecolor=color)

# === PUERTO USB-C ===
usb_y = -height/2 + 8
create_box(-6, usb_y - 2.25, -depth/2 - 10, 12, 4.5, 10,
          color='#2a2a2a', alpha=1.0, edgecolor='#606060')

# Interior del puerto
create_box(-4.5, usb_y - 1.5, -depth/2 - 8, 9, 3, 7,
          color='#000000', alpha=1.0, edgecolor='#333333')

# === INTERRUPTOR ON/OFF (lateral) ===
create_box(width/2 - 7, height/2 - 32.5, -depth/2 - 2, 5, 15, 4,
          color='#c0392b', alpha=1.0, edgecolor='#8B0000')

# === LEDS INDICADORES SUPERIORES ===
led_indicator_y = height/2 - 15
led_indicators = [
    {'x': -20, 'color': '#ff0000'},  # BAT
    {'x': 0, 'color': '#00ff00'},    # PWR
    {'x': 20, 'color': '#0066ff'}    # BLE
]

for indicator in led_indicators:
    create_box(indicator['x'] - 1.8, led_indicator_y - 1.8, depth/2 + 4, 3.6, 3.6, 2,
              color=indicator['color'], alpha=1.0, edgecolor=indicator['color'])

# === ALTAVOZ/BUZZER ===
speaker_y = -height/2 + 75
create_box(-10, speaker_y - 10, depth/2, 20, 20, 2,
          color='#1a1a1a', alpha=1.0, edgecolor='#000000')

# Rejilla del altavoz (círculo de agujeros)
for i in range(12):
    angle = (i / 12) * 2 * np.pi
    radius = 6
    x = np.cos(angle) * radius
    y = speaker_y + np.sin(angle) * radius
    create_box(x - 0.4, y - 0.4, depth/2 + 1, 0.8, 0.8, 1,
              color='#000000', alpha=1.0, edgecolor='#000000')

# === LOGO/MARCA ===
create_box(-20, -height/2 + 16, depth/2 + 4, 40, 8, 1,
          color='#3498db', alpha=0.9, edgecolor='#2980b9')

# === CONFIGURACIÓN DE LA VISTA ===
ax.set_xlabel('X (mm)', color='white', fontsize=10)
ax.set_ylabel('Y (mm)', color='white', fontsize=10)
ax.set_zlabel('Z (mm)', color='white', fontsize=10)

# Establecer límites
max_range = max(width, height, depth) / 1.5
ax.set_xlim([-max_range, max_range])
ax.set_ylim([-max_range, max_range])
ax.set_zlim([-max_range, max_range])

# Ángulo de vista
ax.view_init(elev=20, azim=45)

# Configurar colores del gráfico
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('#1a252f')
ax.yaxis.pane.set_edgecolor('#1a252f')
ax.zaxis.pane.set_edgecolor('#1a252f')
ax.grid(color='#1a252f', linestyle='-', linewidth=0.5, alpha=0.3)

# Color de los ejes
ax.tick_params(colors='white', labelsize=8)

# Título
ax.set_title('Terminal Portátil de Códigos de Barras\n85 x 165 x 30 mm',
             color='#4CAF50', fontsize=16, fontweight='bold', pad=20)

# Ajustar layout
plt.tight_layout()

# Guardar imagen
output_path = '/home/user/barcode-terminal/render-3d-static.png'
plt.savefig(output_path, dpi=150, facecolor='#0a0e27', edgecolor='none', bbox_inches='tight')
print(f"Render guardado en: {output_path}")

# También mostrar en pantalla si es posible
# plt.show()
