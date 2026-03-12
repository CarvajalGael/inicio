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
        )  
    
    page.add(titulo,correo, password )

ft.app(target=main)