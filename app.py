import gradio as gr

def calculator(operation, a, b):
    if operation == "Add":
        return a + b
    elif operation == "Subtract":
        return a - b
    elif operation == "Multiply":
        return a * b
    elif operation == "Divide":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid operation"

demo = gr.Interface(
    fn=calculator,
    inputs=[
        gr.Radio(["Add", "Subtract", "Multiply", "Divide"], label="Operation"),
        gr.Number(label="Input A"),
        gr.Number(label="Input B")
    ],
    outputs="text",
    title="Demo Calculator",
    description="Perform basic arithmetic operations."
)

if _name_ == "_main_":
    demo.launch()
