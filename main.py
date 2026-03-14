import flet as ft

def main(page: ft.Page): 
    page.title = "INICIO DE SESION"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 

    USUARIO_CORRECTO = "admin"
    CORREO_CORRECTO = "admin@dominio.com"
    CONTRA_CORRECTA = "1234"
    
    titulo = ft.Text(
        value="INICIAR SESION", 
        size=35, 
        weight=ft.FontWeight.BOLD
    )
    
    nombre = ft.TextField(
        label="Nombre de Usuario", 
        hint_text="Juana", 
        width=300,
        icon=ft.Icons.PERSON
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

    def iniciar_sesion(e):
        if nombre.value == USUARIO_CORRECTO and correo.value == CORREO_CORRECTO and password.value == CONTRA_CORRECTA:
            
            page.clean()

            barra = ft.NavigationBar(
                destinations=[
                    ft.NavigationBarDestination(icon=ft.Icons.HOME, label="HOME"),
                    ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="EXPLORAR"),
                    ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="PERFIL"),
                ]
            )

            page.navigation_bar = barra

            titulo_panel = ft.Text(
                "Panel Principal",
                size=40,
                weight=ft.FontWeight.BOLD
            )

            bienvenida = ft.Text(
                "Bienvenido al sistema",
                size=20
            )

            page.add(titulo_panel, bienvenida)

        else:
            page.snack_bar = ft.SnackBar(
                ft.Text("Usuario, correo o contraseña incorrectos")
            )
            page.snack_bar.open = True

        page.update()

    boton_login = ft.ElevatedButton(
        "Iniciar Sesion",
        on_click=iniciar_sesion
    )

    boton_texto = ft.TextButton(
        content="¿Olvidaste tu contraseña?",
        icon=ft.Icons.STAR_BORDER,
        icon_color=ft.Colors.BLUE_300,
    )
    
    page.add(titulo, nombre, correo, password, boton_login, boton_texto)

ft.app(target=main)
