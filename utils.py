
def get_button_on_click(button):
    def button_on_click():
        print("Hello, I'm {}".format(button.text))

    return button_on_click
