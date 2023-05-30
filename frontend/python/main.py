from pyscript import Element

# render title
title = Element("title")
title.write("calculator")

# submit form function
def submit(*args, **kwargs):
    i_type = Element('i_type').value
    output = Element('calc_input')

    output.element.value = f"{i_type}" 