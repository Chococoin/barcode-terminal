#!/usr/bin/env python3
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Crear figura con múltiples subplots
fig = plt.figure(figsize=(20, 10), facecolor='#0a0e27')

# Dimensiones del terminal (en mm)
width = 85
height = 165
depth = 30

def create_box(ax, x, y, z, w, h, d, color='#2c3e50', alpha=1.0, edgecolor='black', linewidth=0.5):
    """Crea un box 3D"""
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

    faces = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
        [vertices[0], vertices[3], vertices[7], vertices[4]],
        [vertices[1], vertices[2], vertices[6], vertices[5]]
    ]

    poly = Poly3DCollection(faces, alpha=alpha, facecolor=color, edgecolor=edgecolor, linewidth=linewidth)
    ax.add_collection3d(poly)
    return poly

def draw_terminal(ax, view_angle):
    """Dibuja el terminal completo"""

    # === CUERPO PRINCIPAL ===
    create_box(ax, -width/2, -height/2, -depth/2, width, height, depth,
              color='#34495e', alpha=0.9, edgecolor='#1a252f', linewidth=1)

    # === PANEL FRONTAL ===
    create_box(ax, -width/2 + 3, -height/2 + 3, depth/2 - 2, width - 6, height - 6, 5,
              color='#1a252f', alpha=1.0, edgecolor='#0a0a0a', linewidth=1)

    # === SCANNER GM67 (MUY PROMINENTE) ===
    scanner_y = height/2 - 50

    # Marco negro del scanner (más grande)
    create_box(ax, -36, scanner_y - 23, depth/2, 72, 46, 10,
              color='#0a0a0a', alpha=1.0, edgecolor='#000000', linewidth=2)

    # Cuerpo metálico del scanner
    create_box(ax, -34, scanner_y - 21, depth/2 + 5, 68, 42, 12,
              color='#1a1a1a', alpha=1.0, edgecolor='#333333', linewidth=1)

    # Ventana de vidrio ROJA del scanner
    create_box(ax, -30, scanner_y - 17, depth/2 + 11, 60, 34, 3,
              color='#aa0000', alpha=0.8, edgecolor='#ff0000', linewidth=2)

    # Líneas ROJAS del sensor láser (MUY VISIBLES)
    for i in range(8):
        y_pos = scanner_y - 15 + i * 4
        create_box(ax, -25, y_pos - 0.3, depth/2 + 12, 50, 0.6, 1,
                  color='#ff0000', alpha=1.0, edgecolor='#ff0000', linewidth=1)

    # Etiqueta blanca "SCANNER"
    create_box(ax, -25, scanner_y - 29, depth/2 + 11, 50, 6, 1,
              color='#ffffff', alpha=1.0, edgecolor='#cccccc', linewidth=1)

    # LEDs del scanner (rojo y verde)
    led_positions = [(-25, scanner_y + 18), (25, scanner_y + 18)]
    led_colors = ['#ff0000', '#00ff00']

    for (led_x, led_y), led_color in zip(led_positions, led_colors):
        create_box(ax, led_x - 2, led_y - 2, depth/2 + 11, 4, 4, 2,
                  color=led_color, alpha=1.0, edgecolor=led_color, linewidth=0.5)

    # === PANTALLA OLED (MUY VISIBLE) ===
    display_y = height/2 - 110

    # Marco negro grande de la pantalla
    create_box(ax, -26, display_y - 15, depth/2, 52, 30, 4,
              color='#000000', alpha=1.0, edgecolor='#000000', linewidth=2)

    # Pantalla VERDE encendida
    create_box(ax, -23, display_y - 12, depth/2 + 4, 46, 24, 2,
              color='#0a3d1a', alpha=1.0, edgecolor='#00ff00', linewidth=1)

    # Líneas de texto VERDES en la pantalla (5 líneas)
    text_lines = [
        {'y': 8, 'width': 35},
        {'y': 4, 'width': 30},
        {'y': 0, 'width': 38},
        {'y': -4, 'width': 25},
        {'y': -8, 'width': 32}
    ]

    for line in text_lines:
        create_box(ax, -line['width']/2, display_y + line['y'] - 1, depth/2 + 6.5,
                  line['width'], 2, 0.8,
                  color='#00ff00', alpha=1.0, edgecolor='#00ff00', linewidth=0.5)

    # Borde resplandeciente verde de la pantalla
    create_box(ax, -24, display_y - 13, depth/2 + 6.2, 48, 26, 1,
              color='#00ff00', alpha=0.4, edgecolor='#00ff00', linewidth=0.5)

    # === BOTONES (4 botones de colores) ===
    button_y = -height/2 + 40
    button_spacing = 19
    button_start_x = -28.5
    button_colors = ['#4CAF50', '#2196F3', '#f44336', '#FF9800']

    for i, color in enumerate(button_colors):
        x = button_start_x + i * button_spacing
        # Base negra
        create_box(ax, x - 6, button_y - 6, depth/2, 12, 12, 2,
                  color='#1a1a1a', alpha=1.0, edgecolor='#000000', linewidth=1)
        # Botón de color
        create_box(ax, x - 5, button_y - 5, depth/2 + 3, 10, 10, 3,
                  color=color, alpha=1.0, edgecolor=color, linewidth=1)

    # === PUERTO USB-C (inferior) ===
    usb_y = -height/2 + 8
    create_box(ax, -6, usb_y - 2.25, -depth/2 - 10, 12, 4.5, 10,
              color='#2a2a2a', alpha=1.0, edgecolor='#606060', linewidth=1)

    create_box(ax, -4.5, usb_y - 1.5, -depth/2 - 8, 9, 3, 7,
              color='#000000', alpha=1.0, edgecolor='#333333', linewidth=0.5)

    # === INTERRUPTOR ROJO (lateral) ===
    create_box(ax, width/2 - 7, height/2 - 32.5, -depth/2 - 2, 5, 15, 4,
              color='#c0392b', alpha=1.0, edgecolor='#8B0000', linewidth=1)

    # === LEDS INDICADORES (superior) ===
    led_indicator_y = height/2 - 15
    led_indicators = [
        {'x': -20, 'color': '#ff0000'},  # Batería
        {'x': 0, 'color': '#00ff00'},    # Power
        {'x': 20, 'color': '#0066ff'}    # Bluetooth
    ]

    for indicator in led_indicators:
        create_box(ax, indicator['x'] - 2, led_indicator_y - 2, depth/2 + 4, 4, 4, 2,
                  color=indicator['color'], alpha=1.0, edgecolor=indicator['color'], linewidth=0.5)

    # === ALTAVOZ/BUZZER ===
    speaker_y = -height/2 + 75
    create_box(ax, -10, speaker_y - 10, depth/2, 20, 20, 2,
              color='#1a1a1a', alpha=1.0, edgecolor='#000000', linewidth=1)

    # Agujeros del altavoz
    for i in range(12):
        angle = (i / 12) * 2 * np.pi
        radius = 6
        x = np.cos(angle) * radius
        y = speaker_y + np.sin(angle) * radius
        create_box(ax, x - 0.5, y - 0.5, depth/2 + 1, 1, 1, 1,
                  color='#000000', alpha=1.0, edgecolor='#000000', linewidth=0.3)

    # === LOGO AZUL ===
    create_box(ax, -20, -height/2 + 16, depth/2 + 4, 40, 8, 1,
              color='#3498db', alpha=1.0, edgecolor='#2980b9', linewidth=1)

def setup_axis(ax, title, elev, azim):
    """Configura un eje 3D"""
    # Establecer límites
    max_range = max(width, height, depth) / 1.3
    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])

    # Ángulo de vista
    ax.view_init(elev=elev, azim=azim)

    # Configurar colores
    ax.set_facecolor('#0a0e27')
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('#1a252f')
    ax.yaxis.pane.set_edgecolor('#1a252f')
    ax.zaxis.pane.set_edgecolor('#1a252f')
    ax.grid(color='#1a252f', linestyle='-', linewidth=0.5, alpha=0.3)

    # Etiquetas
    ax.set_xlabel('X (mm)', color='white', fontsize=9)
    ax.set_ylabel('Y (mm)', color='white', fontsize=9)
    ax.set_zlabel('Z (mm)', color='white', fontsize=9)
    ax.tick_params(colors='white', labelsize=7)

    # Título
    ax.set_title(title, color='#4CAF50', fontsize=13, fontweight='bold', pad=15)

# === VISTA 1: FRONTAL (para ver pantalla y scanner) ===
ax1 = fig.add_subplot(131, projection='3d')
draw_terminal(ax1, 'frontal')
setup_axis(ax1, 'Vista Frontal\n(Display OLED + Scanner GM67)', elev=5, azim=0)

# === VISTA 2: 3/4 ===
ax2 = fig.add_subplot(132, projection='3d')
draw_terminal(ax2, '3/4')
setup_axis(ax2, 'Vista 3/4\n(Perspectiva general)', elev=20, azim=45)

# === VISTA 3: LATERAL ===
ax3 = fig.add_subplot(133, projection='3d')
draw_terminal(ax3, 'lateral')
setup_axis(ax3, 'Vista Lateral\n(Perfil del dispositivo)', elev=10, azim=90)

# Título general
fig.suptitle('Terminal Portátil de Códigos de Barras - 85 x 165 x 30 mm',
             color='#4CAF50', fontsize=18, fontweight='bold', y=0.98)

# Agregar leyenda de componentes
legend_text = """
COMPONENTES PRINCIPALES:
━━━━━━━━━━━━━━━━━━━━━━
🔴 SCANNER GM67 (superior): Ventana roja + líneas láser
🟢 DISPLAY OLED (centro): Pantalla verde 1.3" con texto
🔵 4 BOTONES (inferior): Verde/Azul/Rojo/Naranja
🔴 3 LEDs (top): Batería/Power/Bluetooth
⚫ ALTAVOZ (centro-inferior): Buzzer piezo
🔴 SWITCH (lateral): Interruptor ON/OFF
🔌 USB-C (inferior): Puerto de carga
"""

fig.text(0.5, 0.02, legend_text, ha='center', va='bottom',
         color='white', fontsize=9, family='monospace',
         bbox=dict(boxstyle='round', facecolor='#1a252f', alpha=0.8, edgecolor='#4CAF50'))

plt.tight_layout(rect=[0, 0.12, 1, 0.96])

# Guardar imagen
output_path = '/home/user/barcode-terminal/render-3d-static.png'
plt.savefig(output_path, dpi=200, facecolor='#0a0e27', edgecolor='none', bbox_inches='tight')
print(f"✅ Render guardado en: {output_path}")
print(f"📊 Vistas generadas: Frontal, 3/4, y Lateral")
print(f"🔍 Componentes destacados: Scanner GM67 (rojo) y Display OLED (verde)")
