# **Hotel Game**

## Descripción

**Hotel Game** es un juego desarrollado con **Python** y **Kivy**, pensado para ser ejecutado en **Android**. En este juego, puedes mover una bola por la pantalla utilizando botones de control y cambiar su color al chocar con los límites.

## Características

- Movimiento en cuatro direcciones (arriba, abajo, izquierda, derecha).

- Cambio de color aleatorio al chocar con los bordes.

- Botón de reset para volver a la posición inicial.

- Diseñado con una interfaz simple y funcional.

## Instalación

### Requisitos

- Python 3.13

- Kivy

- Buildozer (para generar la APK en Android)

- Java JDK (para compilar en Android)

### Instalación de dependencias

Si estás en una máquina virtual con Kali Linux, asegúrate de tener todo instalado:

```bash
sudo apt update
sudo apt install -y python3-pip git
pip install --upgrade pip
pip install kivy buildozer
```

### Generar APK para Android

Ejecuta el siguiente comando dentro del proyecto:

```bash
buildozer -v android debug
```

Esto generará un archivo APK en `bin/*.apk`.

### Instalación en Android

Para instalar la APK en un dispositivo Android, transfiere el archivo APK y ábrelo para instalarlo manualmente.

## Uso

- Usa los botones de dirección para mover la bola.

- Presiona Reset para volver a la posición original.

- La bola cambiará de color al chocar con los bordes.

## Contribuir

Si quieres mejorar este proyecto:

1. Haz un fork del repositorio.

2. Clona el proyecto:

```bash
git clone https://github.com/royvao/hotel-game.git
```

3. Crea una rama para tu mejora:

```bash
git checkout -b nueva-funcionalidad
```

4. Sube tus cambios y haz un pull request.

## Licencia

Este proyecto está bajo la licencia **MIT**. Puedes usarlo libremente, pero déjanos un crédito si lo modificas.

## Contacto

Si tienes dudas o sugerencias, puedes abrir un *issue* en GitHub o contactarme en royvao@gmail.com