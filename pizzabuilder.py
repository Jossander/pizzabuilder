import flet as ft
 
def main(page: ft.Page):
    page.title= "pizza builder"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 500
    page.window.height= 700
    page.bgcolor = ft.Colors.BLACK  
 
    def changeToppings(e):
        vegetalesBaseImage.visible = vegetalesSwitch.value
        pepperoniBaseImage.visible = pepperoniSwitch.value  
        hongosBaseImage.visible = hongosSwitch.value   
        page.update()   
 
    pizzaBaseImage = ft.Image(src="images/masadepizza.png", width=400, height=400)
 
    # 🔥 Ajustados para que sí se vean
    vegetalesBaseImage = ft.Image(src="images/vegetales.png", width=280, height=280, visible=False, left=60, top=60)
    pepperoniBaseImage = ft.Image(src="images/pepperoni.png", width=280, height=280, visible=False, left=60, top=60)
    hongosBaseImage = ft.Image(src="images/hongos.png", width=280, height=280, visible=False, left=60, top=60)
 
    areadelapizza = ft.Stack(
        width=400,
        height=400,
        controls=[pizzaBaseImage, vegetalesBaseImage, pepperoniBaseImage, hongosBaseImage]
    )
 
    vegetalesSwitch = ft.Switch(label= "Vegetales", on_change= changeToppings)
    pepperoniSwitch = ft.Switch(label= "Pepperoni", on_change= changeToppings)
    hongosSwitch = ft.Switch(label= "Hongos", on_change= changeToppings)
 
    page.add(areadelapizza, vegetalesSwitch, pepperoniSwitch, hongosSwitch)
 
ft.run(main=main)
  