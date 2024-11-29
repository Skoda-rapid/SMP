def center_text(ascii_art):
    lines = ascii_art.splitlines()
    width = max(len(line) for line in lines)
    centered_art = "\n".join(line.center(width) for line in lines)
    return centered_art
