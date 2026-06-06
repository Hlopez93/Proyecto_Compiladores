import os
import subprocess
import time
import shutil


class NativeGenerator:
    def __init__(
        self,
        optimized_ir="output.opt.ll",
        object_file="output.o"
    ):
        self.optimized_ir = optimized_ir
        self.object_file  = object_file

    # ------------------------------------------------------------------ #
    # Utilidad: verifica si un ejecutable está en PATH
    # ------------------------------------------------------------------ #
    @staticmethod
    def _tool_available(name):
        return shutil.which(name) is not None

    # ------------------------------------------------------------------ #
    # Objeto (.o) via llc
    # ------------------------------------------------------------------ #
    def generate_object_file(self):
        if not self._tool_available("llc"):
            raise Exception(
                "llc no encontrado. Instale LLVM (apt install llvm / brew install llvm)."
            )

        if not os.path.exists(self.optimized_ir):
            raise Exception(
                f"No existe archivo IR: {self.optimized_ir}"
            )

        start = time.time()
        result = subprocess.run(
            ["llc", "-filetype=obj", self.optimized_ir, "-o", self.object_file],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            raise Exception(f"llc error: {result.stderr}")

        return {
            "archivo":   self.object_file,
            "tiempo_ms": round((time.time() - start) * 1000, 2)
        }

    # ------------------------------------------------------------------ #
    # Ejecutable Linux via clang o gcc
    # ------------------------------------------------------------------ #
    def generate_linux_executable(self, executable_name="programa_linux"):
        linker = None
        for candidate in ("clang", "gcc"):
            if self._tool_available(candidate):
                linker = candidate
                break

        if linker is None:
            raise Exception(
                "No se encontró clang ni gcc para generar el ejecutable Linux."
            )

        start  = time.time()
        result = subprocess.run(
            [linker, self.object_file, "-o", executable_name],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            raise Exception(f"{linker} error: {result.stderr}")

        return {
            "archivo":   executable_name,
            "tiempo_ms": round((time.time() - start) * 1000, 2)
        }

    # ------------------------------------------------------------------ #
    # Ejecutable Windows via mingw
    # ------------------------------------------------------------------ #
    def generate_windows_executable(self, executable_name="programa.exe"):
        if not self._tool_available("x86_64-w64-mingw32-gcc"):
            raise Exception(
                "x86_64-w64-mingw32-gcc no encontrado. "
                "Instale MinGW (apt install mingw-w64)."
            )

        start  = time.time()
        result = subprocess.run(
            ["x86_64-w64-mingw32-gcc", self.object_file, "-o", executable_name],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            raise Exception(f"mingw error: {result.stderr}")

        return {
            "archivo":   executable_name,
            "tiempo_ms": round((time.time() - start) * 1000, 2)
        }

    # ------------------------------------------------------------------ #
    # Genera todo lo que sea posible; reporta qué se saltó
    # ------------------------------------------------------------------ #
    def generate_all(self, targets):
        generated = {}

        # Sin llc no se puede generar nada — salir limpio
        if not self._tool_available("llc"):
            for t in targets:
                generated[t] = {
                    "skipped": True,
                    "motivo":  "llc no instalado"
                }
            return generated

        try:
            obj_info = self.generate_object_file()
        except Exception as e:
            for t in targets:
                generated[t] = {"skipped": True, "motivo": str(e)}
            return generated

        if "linux" in targets:
            try:
                info = self.generate_linux_executable()
                generated["linux"] = {
                    "archivo":   info["archivo"],
                    "objeto_ms": obj_info["tiempo_ms"],
                    "link_ms":   info["tiempo_ms"],
                    "total_ms":  obj_info["tiempo_ms"] + info["tiempo_ms"]
                }
            except Exception as e:
                generated["linux"] = {"skipped": True, "motivo": str(e)}

        if "windows" in targets:
            try:
                info = self.generate_windows_executable()
                generated["windows"] = {
                    "archivo":   info["archivo"],
                    "objeto_ms": obj_info["tiempo_ms"],
                    "link_ms":   info["tiempo_ms"],
                    "total_ms":  obj_info["tiempo_ms"] + info["tiempo_ms"]
                }
            except Exception as e:
                generated["windows"] = {"skipped": True, "motivo": str(e)}

        return generated