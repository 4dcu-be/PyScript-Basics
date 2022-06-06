counter = 0

pyscript.write('pyscript_status', 'PyScript Loaded Successfully')

def increase_counter(*ags, **kws):
    global counter
    counter += 1
    button = Element('clicks')
    # button.element.innerHTML = f"Count {counter}"
    button.element.innerHTML = f"Count <strong>{counter}</strong>"

def toggle_text(*ags, **kws):
    text = Element('toggle_text')
    button = Element('toggle')

    if "hidden" in text.element.classList:
        text.remove_class("hidden")
        button.element.innerHTML = "Hide Text"
    else:
        text.add_class("hidden")
        button.element.innerHTML = "Show Text"