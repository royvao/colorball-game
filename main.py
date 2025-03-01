from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Ellipse, Color
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
import random

class Juego(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Crear un objeto Color y luego la bola
        with self.canvas:
            self.color = Color(1, 1, 1, 1)  # Color inicial blanco
            self.circulo = Ellipse(pos=(300, 300), size=(50, 50))
        
        self.dx = 0  # Inicializar la velocidad en X
        self.dy = 0  # Inicializar la velocidad en Y
        self.color_changed = False  # Bandera para verificar si el color ya ha cambiado

        # Crear la interfaz de botones en forma de cruz
        self.boton_layout = GridLayout(cols=3, rows=3, size_hint=(None, None), size=(200, 200), pos=(300, 100))

        # Espacio vacío en la parte superior izquierda (sin botón visible)
        self.boton_layout.add_widget(Widget())  # Usamos Widget vacío

        self.boton_arriba = Button(text='Arriba')
        self.boton_arriba.bind(on_press=self.mover_arriba)
        self.boton_arriba.bind(on_release=self.detener_mover)
        self.boton_layout.add_widget(self.boton_arriba)

        # Espacio vacío en la parte superior derecha (sin botón visible)
        self.boton_layout.add_widget(Widget())  # Usamos Widget vacío
        
        self.boton_izquierda = Button(text='Izquierda')
        self.boton_izquierda.bind(on_press=self.mover_izquierda)
        self.boton_izquierda.bind(on_release=self.detener_mover)
        self.boton_layout.add_widget(self.boton_izquierda)

        # Botón de Reset entre Izquierda y Derecha (en la segunda fila, segunda columna)
        self.boton_reset = Button(text='Reset', background_color=(1, 0, 0, 1))  # Rojo
        self.boton_reset.bind(on_press=self.resetear)
        self.boton_layout.add_widget(self.boton_reset)

        self.boton_derecha = Button(text='Derecha')
        self.boton_derecha.bind(on_press=self.mover_derecha)
        self.boton_derecha.bind(on_release=self.detener_mover)
        self.boton_layout.add_widget(self.boton_derecha)

        # Espacio vacío en la parte inferior izquierda (sin botón visible)
        self.boton_layout.add_widget(Widget())  # Usamos Widget vacío

        self.boton_abajo = Button(text='Abajo')
        self.boton_abajo.bind(on_press=self.mover_abajo)
        self.boton_abajo.bind(on_release=self.detener_mover)
        self.boton_layout.add_widget(self.boton_abajo)

        # Espacio vacío en la parte inferior derecha (sin botón visible)
        self.boton_layout.add_widget(Widget())  # Usamos Widget vacío

        # Agregar los botones a la interfaz principal
        self.add_widget(self.boton_layout)

    def mover_izquierda(self, instance):
        self.dx = -5  # Solo afecta al movimiento horizontal
        self.dy = 0   # Restablecer el movimiento vertical
        self.color_changed = False  # Restablecer la bandera para permitir un nuevo cambio de color

    def mover_derecha(self, instance):
        self.dx = 5   # Solo afecta al movimiento horizontal
        self.dy = 0   # Restablecer el movimiento vertical
        self.color_changed = False  # Restablecer la bandera para permitir un nuevo cambio de color

    def mover_arriba(self, instance):
        self.dy = 5   # Solo afecta al movimiento vertical
        self.dx = 0   # Restablecer el movimiento horizontal
        self.color_changed = False  # Restablecer la bandera para permitir un nuevo cambio de color

    def mover_abajo(self, instance):
        self.dy = -5  # Solo afecta al movimiento vertical
        self.dx = 0   # Restablecer el movimiento horizontal
        self.color_changed = False  # Restablecer la bandera para permitir un nuevo cambio de color

    def detener_mover(self, instance):
        # Detener el movimiento cuando se suelta el botón
        self.dx = 0
        self.dy = 0

    def resetear(self, instance):
        # Volver la pelota a la posición inicial
        self.circulo.pos = (300, 300)
        self.dx = 0
        self.dy = 0
        self.color.rgba = (1, 1, 1, 1)  # Restablecer el color a blanco
        self.color_changed = False  # Restablecer la bandera

    def actualizar(self, dt):
        # Mover el círculo según las teclas presionadas
        new_pos_x = self.circulo.pos[0] + self.dx
        new_pos_y = self.circulo.pos[1] + self.dy

        # Obtener las dimensiones de la ventana
        width, height = self.size

        # Verificar si la pelota ha tocado los límites de la pantalla
        if new_pos_x <= 0:  # Limite izquierdo
            new_pos_x = 0
            self.dx = 0
            self.cambiar_color()
        elif new_pos_x + self.circulo.size[0] >= width:  # Limite derecho
            new_pos_x = width - self.circulo.size[0]
            self.dx = 0
            self.cambiar_color()

        if new_pos_y <= 0:  # Limite superior
            new_pos_y = 0
            self.dy = 0
            self.cambiar_color()
        elif new_pos_y + self.circulo.size[1] >= height:  # Limite inferior
            new_pos_y = height - self.circulo.size[1]
            self.dy = 0
            self.cambiar_color()

        # Actualizar la posición de la pelota
        self.circulo.pos = (new_pos_x, new_pos_y)

    def cambiar_color(self):
        # Cambiar el color solo si no ha cambiado ya
        if not self.color_changed:
            self.color.rgba = random.choice([(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1), (1, 1, 0, 1)])
            self.color_changed = True  # Marcar que el color ya ha cambiado

    def on_touch_move(self, touch):
        # Evitar que el movimiento toque cualquier otro objeto no relacionado
        return True

class JuegoApp(App):
    def build(self):
        juego = Juego()
        # Actualizar la posición de la pelota constantemente
        juego.update_clock = Clock.schedule_interval(juego.actualizar, 1.0 / 60.0)
        return juego

if __name__ == '__main__':
    JuegoApp().run()
