import flet as ft

def main(page: ft.Page): 
    page.title = "INICIO DE SESION"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER 
    
    
    
    titulo = ft.Text(
        value="INICIAR SESION", 
        size=35, 
        weight=ft.FontWeight.BOLD
    )
    
    nombre = ft.TextField(
        label="Nombre de Usuario", 
        hint_text="Juana", 
        width=300,
    )
    
    correo = ft.TextField(
        label="Correo electrónico", 
        hint_text="ejemplo@dominio.com", 
        width=300,
        icon=ft.Icons.EMAIL
    )
    
    password = ft.TextField(
        label="Contraseña", 
        width=300,
        icon=ft.Icons.PASSWORD,
        password=True
    )
    boton_login = ft.Button(content="Iniciar Sesion")

    boton_texto = ft.TextButton(
        content="¿Olvidaste tu contraseña?",
        icon=ft.Icons.STAR_BORDER,
        icon_color=ft.Colors.BLUE_300,
    )

    page.add(titulo, nombre, correo, password, boton_login, boton_texto)

ft.app(target=main)
