import subprocess
import tempfile
import os


class LLVMManualOptimizer:

    def optimize(self, input_file, passes):

        current_file = input_file

        temp_files = []

        try:

            for p in passes:

                temp_file = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".ll"
                ).name

                temp_files.append(temp_file)

                cmd = [
                    "opt",
                    f"-passes={p}",
                    "-S",
                    current_file,
                    "-o",
                    temp_file
                ]

                subprocess.run(
                    cmd,
                    check=True,
                    capture_output=True,
                    text=True
                )

                current_file = temp_file

            with open(current_file, "r") as f:
                optimized_ir = f.read()

            with open("manual_opt.ll", "w") as f:
                f.write(optimized_ir)

            return optimized_ir

        finally:

            for f in temp_files:
                if os.path.exists(f):
                    os.remove(f)