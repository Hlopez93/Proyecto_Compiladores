import subprocess
import os


class ManualIRRunner:

    def run(self):

        if not os.path.exists("manual_opt.ll"):
            raise Exception("No existe manual_opt.ll")

        exe_name = "manual_program"

        subprocess.run(
            [
                "clang",
                "manual_opt.ll",
                "-o",
                exe_name
            ],
            check=True
        )

        result = subprocess.run(
            [f"./{exe_name}"],
            capture_output=True,
            text=True
        )

        return result.stdout