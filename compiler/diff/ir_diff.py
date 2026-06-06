from difflib import ndiff


def generate_diff(original, manual):

    diff = []

    for line in ndiff(
        original.splitlines(),
        manual.splitlines()
    ):

        if line.startswith("- "):
            diff.append({
                "type": "removed",
                "text": line[2:]
            })

        elif line.startswith("+ "):
            diff.append({
                "type": "added",
                "text": line[2:]
            })

        elif line.startswith("  "):
            diff.append({
                "type": "same",
                "text": line[2:]
            })

    return diff