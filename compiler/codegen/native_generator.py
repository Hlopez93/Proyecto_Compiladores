import os
import subprocess
import time

class NativeGenerator:
    def __init__(
        self,
        optimized_ir="output.opt.ll",
        object_file="output.o"
    ):
        self.optimized_ir = optimized_ir
        self.object_file = object_file

    def generate_object_file(self):
        start = time.time()
        if not os.path.exists(self.optimized_ir):
            raise Exception(
                f"No existe archivo IR optimizado: {self.optimized_ir}"
            )
        try:
            cmd = [
                "llc",
                "-filetype=obj",
                self.optimized_ir,
                "-o",
                self.object_file
            ]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                raise Exception(result.stderr)
            elapsed = round(
                (time.time() - start) * 1000,
                2
            )
            return {
                "archivo": self.object_file,
                "tiempo_ms": elapsed
            }
        except FileNotFoundError:
            raise Exception(
                "llc no encontrado. Instale LLVM."
            )

    def generate_linux_executable(
        self,
        executable_name="programa_linux"
    ):
        start = time.time()
        cmd = [
            "clang",
            self.object_file,
            "-o",
            executable_name
        ]
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            raise Exception(result.stderr)
        elapsed = round(
            (time.time() - start) * 1000,
            2
        )
        return {
            "archivo": executable_name,
            "tiempo_ms": elapsed
        }

    def generate_windows_executable(
        self,
        executable_name="programa.exe"
    ):
        start = time.time()
        cmd = [
            "x86_64-w64-mingw32-gcc",
            self.object_file,
            "-o",
            executable_name
        ]
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            raise Exception(result.stderr)
        elapsed = round(
            (time.time() - start) * 1000,
            2
        )
        return {
            "archivo": executable_name,
            "tiempo_ms": elapsed
        }

    def generate_all(self, targets):
        obj_info = self.generate_object_file()
        generated = {}
        # Linux
        if "linux" in targets:
            linux_info = self.generate_linux_executable()
            generated["linux"] = {
                "archivo": linux_info["archivo"],
                "objeto_ms": obj_info["tiempo_ms"],
                "link_ms": linux_info["tiempo_ms"],
                "total_ms":
                    obj_info["tiempo_ms"] +
                    linux_info["tiempo_ms"]
            }
        # Windows
        if "windows" in targets:
            windows_info = self.generate_windows_executable()
            generated["windows"] = {
                "archivo": windows_info["archivo"],
                "objeto_ms": obj_info["tiempo_ms"],
                "link_ms": windows_info["tiempo_ms"],
                "total_ms":
                    obj_info["tiempo_ms"] +
                    windows_info["tiempo_ms"]
            }
        return generated