import difflib

class DiffGenerator:

    @staticmethod
    def generate(original, optimized):

        original_lines = original.splitlines()
        optimized_lines = optimized.splitlines()

        diff = difflib.HtmlDiff().make_table(
            original_lines,
            optimized_lines,
            fromdesc="IR Original",
            todesc="IR Manual",
            context=False,
            numlines=0
        )

        return diff