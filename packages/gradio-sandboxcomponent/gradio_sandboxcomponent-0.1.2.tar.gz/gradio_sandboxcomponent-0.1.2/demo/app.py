
from typing import Any
import gradio as gr
from gradio_sandboxcomponent import SandboxComponent

example = SandboxComponent().example_value()


with gr.Blocks() as demo:
    with gr.Tab("Sandbox Demo"):
        with gr.Row():
            gr.Markdown("## Sandbox")
        with gr.Row():
            sandboxUrl = gr.Textbox(
                label="Sandbox URL",
                value='https://www.gradio.app/',
                placeholder="Enter sandbox URL",
                lines=1,
                show_label=True,
            )
            sandboxInteractions = gr.Textbox(
                label="Sandbox Interactions",
                value='[]',
                placeholder="Enter sandbox interactions",
                lines=1,
                show_label=True,
            )
        with gr.Row():
            sandbox = SandboxComponent(
                label="Sandbox Example",
                value=("https://www.gradio.app/", True, []),
                show_label=True)

        def update_outputs(sandboxData: tuple[str, list[Any]]):
            sandboxUrl, _, sandboxInteractions = sandboxData
            print(
                "UPDATING",
                sandboxData
            )
            return sandboxUrl, str(sandboxInteractions)

        sandbox.change(
            update_outputs,
            inputs=[sandbox],
            outputs=[sandboxUrl, sandboxInteractions]
        )

        def update_sandbox_url(url: str):
            sandbox.value = (url, True, [])
            return sandbox.value

        sandboxUrl.change(
            update_sandbox_url,
            inputs=[sandboxUrl],
            outputs=[sandbox]
        )

if __name__ == "__main__":
    demo.launch()
