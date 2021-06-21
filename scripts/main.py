import subprocess
import time
import random
import string
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

app = FastAPI()


def time_it(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"{func.__name__} lief {int((end-start)*1000)} ms")

    return wrapper


@time_it
@app.post("/get_python_uml")
async def get_python_uml(
    pythoncode: str = Form(...),
    builtin: bool = Form(False),
    ancestor: bool = Form(False),
    associated: bool = Form(False),
):
    options = ""
    if builtin:
        options += " -b "
    if ancestor:
        options += " -A "
    if associated:
        options += " -S "

    rnd_string = "".join(
        random.choice(string.ascii_lowercase) for i in range(10)
    )
    subprocess.run(f"mkdir /{rnd_string}", shell=True, check=True)
    f = open(f"/{rnd_string}/python.py", "w")
    f.write(pythoncode)
    f.close()
    subprocess.run(
        f"pyreverse {options} -o png /{rnd_string}/python.py",
        shell=True,
        check=True,
        cwd=f"/{rnd_string}/",
    )
    subprocess.run("ls -la", shell=True, check=True, cwd=f"/{rnd_string}/")
    return FileResponse(f"/{rnd_string}/classes.png", media_type="image/png")
