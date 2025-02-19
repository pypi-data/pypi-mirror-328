"""
Módulo que contiene las funciones para imprimir texto con colores.

Contenido
---------
- Clase Output: contiene las funciones para imprimir texto con colores.
"""
import locale
import os
import time
from datetime import datetime
from .colors import Colors
from .alignment import Alignment


class Output:
    """Clase que contiene las funciones para imprimir texto con colores."""
    @staticmethod
    def print(text: object, color: str = Colors.DEFAULT,
              alignment: str = Alignment.LEFT, width: int = 0) -> None:
        """Imprime un texto con un color y alineación.

        Args:
            text (object): Texto a imprimir.
            color (str, optional): Color a aplicar al texto.
            alignment (str, optional): Alineación del texto ('left', 'center', 'right').
            width (int, optional): Ancho para centrar el texto. Si no se proporciona,
            se usará el ancho de la terminal.
        """
        # Validar el color
        color = Colors.validate_color(color)
        # Validar la alineación
        alignment = Alignment.validate_alignment(alignment)

        text = Colors.colorize(str(text), color)

        if width == 0:
            width = Output.get_console_size()[0]

        if alignment == Alignment.CENTER:
            print(text.center(width))
        elif alignment == Alignment.RIGHT:
            print(text.rjust(width))
        else:
            print(text.ljust(width))

    @staticmethod
    def clear() -> None:
        """Limpia la consola."""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def get_console_size() -> tuple[int, int]:
        """Obtiene el tamaño de la consola.

        Returns:
            tuple[int, int]: Tamaño de la consola.
        """
        try:
            return os.get_terminal_size()
        except OSError:
            # Proporcionar un tamaño de consola predeterminado
            return (80, 24)

    @staticmethod
    def press_enter_to_continue() -> None:
        """Pide al usuario que presione Enter para continuar."""
        input(
            f"Presione {Colors.colorize('ENTER', Colors.YELLOW)} para continuar...")

    @staticmethod
    def show_error(message: str) -> None:
        """Muestra un mensaje de error.

        Args:
            message (str): Mensaje de error.
        """
        Output.print(message, Colors.RED)

    @staticmethod
    def show_warning(message: str) -> bool:
        """Muestra un mensaje de advertencia.

        Args:
            message (str): Mensaje de advertencia.

        Returns:
            bool: True si el usuario responde afirmativamente, False en caso contrario.
        """
        while True:
            response = input(f"{Colors.colorize(message, Colors.YELLOW)}\n" +
                             "¿Desea continuar? (s/n) ").lower()
            if response in ("s", "y"):
                return True
            return False

    @staticmethod
    def confirm(message: str) -> bool:
        """Muestra un mensaje de confirmación al usuario y solicita una respuesta
        afirmativa o negativa.

        Args:
            message (str): Mensaje de confirmación a mostrar.

        Returns:
            bool: True si el usuario responde afirmativamente, False en caso contrario.

        """
        while True:
            response = input(f"{message} (s/n) ").lower()
            if response in ("s", "y"):
                return True
            return False

    @staticmethod
    def typewriter_effect(text: str) -> None:
        """Imprime los caracteres de la cadena de texto uno por uno en un intervalo de
        tiempo determinado para simular el efecto de que se está escribiendo en tiempo
        real.

        Args:
            text (str): La cadena de texto que se quiere imprimir con efecto de tipeo.
        """
        # Itera a través de cada carácter en la cadena de texto
        for char in text:
            # Imprime el carácter sin un salto de línea al final, y hace flush del
            # flujo de salida inmediatamente
            print(char, end='', flush=True)
            # Espera un breve intervalo de tiempo antes de imprimir el siguiente carácter
            time.sleep(0.05)
        # Imprime un salto de línea al final para separar esta salida de la próxima en la consola
        print("\n")

    @staticmethod
    def set_locale(region: str) -> None:
        """Establece la localidad regional de la consola.

        Args:
            region (str): Localidad regional a establecer.
        """
        locale.setlocale(locale.LC_ALL, region)

    @staticmethod
    def format_int(value: int) -> str:
        """Formatea un número entero con separadores de miles y decimales.

        Args:
            value (int): Número entero a formatear.

        Returns:
            str: Número entero formateado con separadores de miles y decimales.
        """
        return locale.format_string("%d", value, grouping=True)

    @staticmethod
    def format_float(value: float) -> str:
        """Formatea un número decimal con separadores de miles y decimales.

        Args:
            value (float): Número decimal a formatear.

        Returns:
            str: Número decimal formateado con separadores de miles y decimales.
        """
        return locale.format_string("%.2f", value, grouping=True)

    @staticmethod
    def format_currency(value: float) -> str:
        """Formatea un número como una cantidad de dinero con separadores de miles y decimales.

        Args:
            value (float): Número a formatear como una cantidad de dinero.

        Returns:
            str: Número formateado como una cantidad de dinero con separadores de miles y decimales.
        """
        # locale.setlocale(locale.LC_ALL, locale.getlocale()[0])
        return locale.currency(value, grouping=True)

    @staticmethod
    def format_percentage(value: float) -> str:
        """Formatea un número como un porcentaje con separadores de miles y decimales.

        Args:
            value (float): Número a formatear como un porcentaje.

        Returns:
            str: Número formateado como un porcentaje con separadores de miles y decimales.
        """
        return locale.format_string("%.2f%%", value, grouping=True)

    @staticmethod
    def format_date(date_str: str) -> str:
        """Formatea una fecha en el formato del locale configurado en la computadora.

        Args:
            date_str (str): Fecha en formato AAAA-MM-DD.

        Returns:
            str: Fecha formateada en el formato local.
        """
        # Convertir la fecha de string a objeto datetime.date
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

        # Formatear la fecha según el locale
        # "%x" usa el formato de fecha del locale
        return date_obj.strftime("%x") + "\n"

    @staticmethod
    def print_title(title: str, color: str, underline: str = "*",
                    alignment: str = Alignment.LEFT, width: int = 0) -> None:
        """Imprime un título con un color y un subrayado.

        Args:
            title (str): Título a imprimir.
            color (str): Color del título.
            underline (str, optional): Carácter de subrayado. Por defecto es "*".
        """
        # Validar el color
        color = Colors.validate_color(color)

        if width == 0:
            width = Output.get_console_size()[0]

        if alignment == Alignment.CENTER:
            # Imprimir el título con el color especificado
            print(Colors.colorize(title.center(width), color))
            # Imprimir el subrayado con el color especificado
            print(Colors.colorize((underline * len(title)).center(width), color))
        elif alignment == Alignment.RIGHT:
            # Imprimir el título con el color especificado
            print(Colors.colorize(title.rjust(width), color))
            # Imprimir el subrayado con el color especificado
            print(Colors.colorize((underline * len(title)).rjust(width), color))
        else:
            # Imprimir el título con el color especificado
            print(Colors.colorize(title, color))
            # Imprimir el subrayado con el color especificado
            print(Colors.colorize(underline * len(title), color))

    @staticmethod
    def show_progress_bar(iteration: int, total: int, length: int = 50) -> None:
        """Muestra una barra de progreso en la consola.

        Args:
            iteration (int): Iteración actual.
            total (int): Número total de iteraciones.
            length (int, optional): Longitud de la barra de progreso. Por defecto es 50.
        """
        percent = f"{100 * (iteration / float(total)):.1f}"
        filled_length = int(length * iteration // total)
        progress_bar = '█' * filled_length + '-' * (length - filled_length)
        print(f'\r|{progress_bar}| {percent}% Completo', end='\r')
        if iteration == total:
            print()
