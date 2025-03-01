import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.label import Label


kivy.require("2.0.0")

class JuegoLayout(BoxLayout):
    pass

class HotelApp(App):
    def build(self):
        self.label = Label(text="Contador: 0")
        Clock.schedule_interval(self.actualizar, 1)  # Llama a 'actualizar' cada 1 segundo
        return self.label

    def actualizar(self, dt):
        # Aquí actualizas el estado del juego
        contador = int(self.label.text.split(": ")[1]) + 1
        self.label.text = f"Contador: {contador}"

if __name__ == '__main__':
    HotelApp().run()

