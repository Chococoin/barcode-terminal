# Lista de Componentes - Terminal Portátil de Códigos de Barras

## Especificaciones Generales del Dispositivo

- **Dimensiones**: 85mm (ancho) x 165mm (alto) x 30mm (profundidad)
- **Peso**: ~175 gramos
- **Factor de forma**: Dispositivo portátil de mano, ergonómico
- **Carcasa**: Plástico ABS/PC con esquinas redondeadas (radio: 10mm)
- **Color principal**: Gris oscuro / Negro mate

---

## Componentes Principales (de arriba hacia abajo)

### 1. ZONA SUPERIOR

#### A. LEDs Indicadores (3 unidades)
- **Posición**: Parte superior del dispositivo, centrados horizontalmente
- **Espaciado**: 20mm entre cada LED
- **Tamaño**: 3.6mm de diámetro cada uno
- **Colores y funciones**:
  - LED Izquierdo (ROJO): Indicador de batería baja
  - LED Centro (VERDE): Power/Encendido
  - LED Derecho (AZUL): Conectividad Bluetooth

#### B. Scanner GM67 de Códigos de Barras 2D/1D
- **Posición**: 50mm desde la parte superior del dispositivo
- **Dimensiones totales**: 72mm x 46mm x 17mm (incluyendo marco)
- **Marco exterior**: Negro brillante, metálico
- **Cuerpo del scanner**: 68mm x 42mm, color negro mate
- **Ventana de vidrio**: 60mm x 34mm
  - Material: Vidrio protector con tinte rojo oscuro
  - Color: Rojo translúcido (#aa0000 con 80% opacidad)
  - Transparencia: Semi-transparente para permitir paso del láser
- **Sensor láser interno**: 8 líneas horizontales rojas
  - Color: Rojo brillante (#ff0000)
  - Ancho de cada línea: 50mm
  - Grosor de cada línea: 0.6mm
  - Espaciado vertical: 4mm entre líneas
- **Etiqueta "SCANNER"**:
  - Dimensiones: 50mm x 6mm
  - Color: Blanco
  - Posición: Debajo de la ventana de vidrio
- **LEDs del scanner** (2 unidades):
  - LED izquierdo: Rojo (indicador de error/scanning)
  - LED derecho: Verde (confirmación de lectura exitosa)
  - Tamaño: 4mm x 4mm
  - Posición: Esquinas superiores del scanner

### 2. ZONA CENTRAL

#### C. Pantalla OLED SSD1306
- **Posición**: Centro del dispositivo, 110mm desde la parte superior
- **Marco de la pantalla**: 52mm x 30mm x 4mm
  - Color: Negro mate
  - Grosor del bisel: 3mm por lado
- **Área visible de pantalla**: 46mm x 24mm
  - Resolución: 128x64 píxeles
  - Tipo: OLED monocromático
  - Color de fondo: Verde oscuro (#0a3d1a)
  - Color del texto: Verde brillante (#00ff00)
- **Contenido simulado en pantalla**:
  - 5 líneas de texto horizontales con diferentes longitudes
  - Línea 1 (superior): 35mm de ancho (título/header)
  - Línea 2: 30mm de ancho
  - Línea 3: 38mm de ancho
  - Línea 4: 25mm de ancho
  - Línea 5 (inferior): 32mm de ancho
  - Grosor de cada línea de texto: 2mm
  - Espaciado vertical: 4mm entre líneas
- **Efecto de resplandor**:
  - Borde verde semi-transparente alrededor de la pantalla
  - Dimensiones del resplandor: 48mm x 26mm
  - Opacidad: 40%

#### D. Altavoz/Buzzer Piezo
- **Posición**: 75mm desde la parte inferior
- **Forma**: Circular
- **Diámetro**: 20mm
- **Color**: Negro mate
- **Rejilla**: 12 agujeros pequeños distribuidos circularmente
  - Radio de distribución: 6mm desde el centro
  - Tamaño de cada agujero: 1mm x 1mm

### 3. ZONA INFERIOR

#### E. Logo/Marca
- **Posición**: 20mm desde la parte inferior
- **Dimensiones**: 40mm x 8mm x 1mm
- **Color**: Azul (#3498db) con resplandor azul oscuro (#2980b9)
- **Acabado**: Ligeramente elevado del panel frontal

#### F. Botonera (4 botones táctiles)
- **Posición**: 40mm desde la parte inferior
- **Distribución horizontal**:
  - Espaciado entre botones: 19mm
  - Posición inicial: -28.5mm desde el centro
- **Dimensiones de cada botón**:
  - Base: 12mm x 12mm (cuadrada con bordes redondeados), color negro
  - Botón superior: 10mm x 10mm, altura 3mm
- **Colores de los botones** (de izquierda a derecha):
  1. SCAN (Verde): #4CAF50
  2. OK (Azul): #2196F3
  3. CANCEL (Rojo): #f44336
  4. MENU (Naranja): #FF9800
- **Características**: Cada botón tiene ligero resplandor del mismo color

### 4. COMPONENTES LATERALES Y TRASEROS

#### G. Interruptor ON/OFF
- **Posición**: Lateral derecho, 25mm desde la parte superior
- **Dimensiones**: 5mm x 15mm x 4mm
- **Color**: Rojo oscuro (#c0392b)
- **Tipo**: Interruptor deslizable (slide switch)

#### H. Puerto USB-C
- **Posición**: Borde inferior del dispositivo, centrado
- **Altura desde el borde**: 8mm
- **Carcasa exterior**: 12mm x 4.5mm
  - Color: Gris oscuro metálico (#2a2a2a)
- **Puerto interno**: 9mm x 3mm
  - Color: Negro
- **Profundidad total**: 10mm desde la carcasa

#### I. Detalles de Ventilación (opcional)
- **Posición**: Lateral izquierdo
- **Cantidad**: 5 ranuras verticales
- **Dimensiones de cada ranura**: 2mm x 15mm
- **Espaciado vertical**: 15mm entre ranuras
- **Color**: Negro

---

## Materiales y Acabados

- **Carcasa principal**: Plástico ABS color gris oscuro (#34495e) con acabado mate
- **Panel frontal**: Plástico negro (#1a252f) con textura ligeramente granulada
- **Componentes metálicos**: Acabado metalizado en bordes del scanner y puerto USB-C
- **Pantalla**: Vidrio protector sobre OLED
- **Scanner**: Vidrio templado con recubrimiento anti-reflejante

---

## Iluminación y Efectos Visuales

- **LEDs indicadores**: Luz constante o parpadeante según estado
- **Scanner**: Líneas láser rojas visibles a través del vidrio
- **Pantalla OLED**: Retroiluminación verde con contraste alto
- **Botones**: Ligero resplandor/halo del color correspondiente

---

# PROMPT PARA GENERACIÓN DE RENDER 3D

```
Genera un render 3D fotorrealista de un terminal portátil de mano para lectura de códigos de barras con las siguientes especificaciones:

DIMENSIONES Y FORMA:
- Dispositivo rectangular de 85mm x 165mm x 30mm (ancho x alto x profundidad)
- Bordes redondeados con radio de 10mm en todas las esquinas
- Carcasa principal color gris oscuro mate (#34495e)
- Panel frontal ligeramente empotrado color negro (#1a252f)
- Factor de forma ergonómico tipo "handheld scanner"

COMPONENTES FRONTALES (de arriba hacia abajo):

1. ZONA SUPERIOR (primeros 50mm):
   - 3 LEDs indicadores pequeños en fila horizontal (rojo, verde, azul) a 15mm del borde superior
   - Scanner de códigos de barras GM67 grande y prominente:
     * Marco negro metálico de 72mm x 46mm
     * Ventana de vidrio ROJA TRANSLÚCIDA de 60mm x 34mm en el centro
     * 8 líneas láser ROJAS horizontales visibles dentro del vidrio (muy importante: estas deben ser MUY VISIBLES)
     * Etiqueta blanca "SCANNER" debajo de la ventana
     * 2 LEDs pequeños en las esquinas superiores (rojo y verde)

2. ZONA CENTRAL (55mm - 125mm desde arriba):
   - Pantalla OLED rectangular de 52mm x 30mm:
     * Marco NEGRO grueso alrededor
     * Área de display VERDE BRILLANTE de 46mm x 24mm
     * 5 líneas de texto simuladas en VERDE (#00ff00) sobre fondo verde oscuro
     * Resplandor verde sutil alrededor de la pantalla
     * MUY IMPORTANTE: La pantalla debe estar ENCENDIDA y claramente VISIBLE

3. ZONA MEDIA-INFERIOR (125mm - 140mm):
   - Altavoz circular negro de 20mm de diámetro con rejilla de agujeros pequeños

4. ZONA INFERIOR (últimos 40mm):
   - Logo azul rectangular de 40mm x 8mm
   - 4 botones circulares en fila horizontal con colores:
     * Verde (#4CAF50) - izquierda
     * Azul (#2196F3)
     * Rojo (#f44336)
     * Naranja (#FF9800) - derecha
   - Cada botón de 10mm de diámetro con base negra

COMPONENTES LATERALES:
- Lateral derecho: Interruptor rojo deslizable de 5mm x 15mm
- Borde inferior: Puerto USB-C centrado (12mm x 4.5mm, color gris metálico)

ILUMINACIÓN Y AMBIENTE:
- Iluminación profesional tipo estudio con 3 luces (principal, relleno, contraluz)
- Fondo degradado oscuro (azul oscuro a negro)
- Sombras suaves bajo el dispositivo
- Efecto de resplandor en LEDs y pantalla
- Reflexiones realistas en superficies metálicas y vidrio

VISTAS REQUERIDAS:
- Vista frontal directa (para ver claramente pantalla y scanner)
- Vista 3/4 en perspectiva (45° horizontal, 20° vertical)
- Vista lateral (perfil del dispositivo)

IMPORTANTE:
- El scanner con vidrio rojo y líneas láser debe ser MUY PROMINENTE y VISIBLE
- La pantalla OLED verde debe estar ENCENDIDA con texto claramente visible
- Materiales realistas: plástico mate, vidrio, metal cepillado
- Calidad de render: Alta resolución, antialiasing, sombras suaves

Estilo visual: Render de producto profesional, tipo "product showcase" para catálogo técnico o presentación de inversores.
```

---

## Notas Adicionales

Este prompt está optimizado para ser usado con herramientas de generación 3D como:
- MidJourney (con parámetros `--style raw --v 6`)
- DALL-E 3
- Stable Diffusion (con modelos orientados a productos/renders técnicos)
- Leonardo AI (modelo PhotoReal)
- Otras IAs generativas con capacidad de interpretación de descripciones técnicas detalladas

Para mejores resultados, considera dividir el prompt en secciones si la IA tiene límite de tokens, priorizando:
1. Forma general y dimensiones
2. Scanner (componente más importante)
3. Pantalla OLED (segundo componente más importante)
4. Resto de componentes y detalles

---

**Última actualización**: 2025-11-08
**Versión del documento**: 1.0
**Proyecto**: Terminal Portátil de Códigos de Barras - Prototipo v1
