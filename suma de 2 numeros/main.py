import flet as ft

def main(page: ft.Page):
    page.title = "suma de dos numeros"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "black"

    
    img= ft.Image(src="travis.jpg", width=100, height=100)

    
    txt_num1 = ft.TextField(label="Primer número", width=150)
    txt_num2 = ft.TextField(label="Segundo número", width=150)

    
    txt_resultado = ft.Text(value="Resultado: ", size=25)

    
    def calcular_suma(e):
        try:
            num1 = float(txt_num1.value.strip())
            num2 = float(txt_num2.value.strip())
            resultado = num1 + num2
            txt_resultado.value = f"Resultado: {resultado}"
        except ValueError:
            txt_resultado.value = "Error: Ingresa valores válidos"
        page.update()  

    def limpiar(e):
        txt_num1.value = ""
        txt_num2.value = ""
        txt_resultado.value = "Resultado: "
        page.update()  
    
    btn_sumar = ft.ElevatedButton(text="Sumar", on_click=calcular_suma)
    btn_limpiar = ft.ElevatedButton(text="Limpiar", on_click=limpiar)

    
    page.add(
        ft.Row(
            [
                img,  
                ft.Column(
                    [
                        txt_num1,  
                        txt_num2,  
                        ft.Row([btn_sumar, btn_limpiar], spacing=10), 
                        txt_resultado  
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=30
        )
    )


ft.app(target=main)

