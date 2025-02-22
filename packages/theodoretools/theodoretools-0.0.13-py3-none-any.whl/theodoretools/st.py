import io
import os
import streamlit as st
from streamlit_javascript import st_javascript
import qrcode
import os

import asyncio
is_debug = os.getenv("DEBUG_MODE", "false").lower() == "true"


def run_shell_command(command, cwd):
    asyncio.run(
        run_subprocess(command, cwd)
    )


async def run_subprocess(command, cwd):
    # Create placeholder for live output
    output_placeholder = st.empty()
    accumulated_output = []

    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=cwd,
    )

    # Read stdout stream
    while True:
        line = await process.stdout.readline()
        if not line:
            break

        line = line.decode().strip()
        accumulated_output.append(line)

        # Update display with all output so far
        output_placeholder.code('\n'.join(accumulated_output))

    # Get any remaining output and errors
    stdout, stderr = await process.communicate()
    if stderr:
        st.write("Subprocess errors:")
        st.code(stderr.decode())


def get_st_href():
    return st_javascript("await fetch('').then(r => window.parent.location.href)")


def generate_qr_code(
        url: str,
        title: str = f"Website QR Code Expander"
):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format="PNG")
    img_byte_arr = img_byte_arr.getvalue()

    st.markdown("\n")
    st.markdown("\n")
    st.markdown("\n")
    st.markdown("\n")
    st.markdown("\n")
    st.markdown("\n")

    with st.expander(title):
        st.image(img_byte_arr, caption=url)


def set_hidden_js(js_string: str):
    st.components.v1.html(js_string, height=0, width=0)


def st_debug_info(data: any, title: str):
    if is_debug:
        if isinstance(data, str):
            data = data.replace("\\n", "\n")
        with st.expander(f"debug_info {title}: Expand/Collapse"):
            st.write(data)


def st_info(data: any, title: str = ""):
    if title != "":
        st.write(title)

    s = str(data).replace('\\n', '\n')
    st.info(s)
