class ConsoleReader:
    def read_art_type():
        art_type = (
            input(
                "Введіть 'text' для текстового ASCII-арту або 'shape' для фігурного ASCII-арту: "
            )
            .strip()
            .lower()
        )
        while art_type not in ["text", "shape"]:
            print("Невірний вибір. Спробуйте знову.")
            art_type = (
                input(
                    "Введіть 'text' для текстового ASCII-арту або 'shape' для фігурного ASCII-арту: "
                )
                .strip()
                .lower()
            )
        return art_type

    def read_text_parameters():
        text = input("Введіть текст для ASCII-арту: ")
        symbol = (
            input("Введіть символ для текстового ASCII-арту (за замовчуванням '*'): ")
            or "*"
        )
        width = ConsoleReader.read_width()
        height = ConsoleReader.read_height()
        alignment = ConsoleReader.read_alignment()
        color_mode = ConsoleReader.read_color_mode()
        return {
            "text": text,
            "symbol": symbol,
            "width": width,
            "height": height,
            "alignment": alignment,
            "color_mode": color_mode,
        }

    def read_shape_parameters():
        shape_type = input("Введіть тип фігури (cube, sphere): ").strip().lower()
        symbol = (
            input("Введіть символ для фігурного ASCII-арту (за замовчуванням '*'): ")
            or "*"
        )
        size = input(
            "Введіть розмір фігури (натисніть Enter для значення за замовчуванням 5): "
        )
        size = int(size) if size.isdigit() else 5
        color_mode = ConsoleReader.read_color_mode()  # Кольоровий режим
        return {
            "shape_type": shape_type,
            "symbol": symbol,
            "size": size,
            "color_mode": color_mode,
        }

    def read_width():
        width = input(
            "Введіть ширину ASCII-арту (натисніть Enter для значення за замовчуванням 40): "
        )
        return int(width) if width.isdigit() else 40

    def read_height():
        height = input(
            "Введіть висоту ASCII-арту (натисніть Enter для значення за замовчуванням 10): "
        )
        return int(height) if height.isdigit() else 10

    def read_alignment():
        alignment = (
            input("Оберіть вирівнювання (left, center, right): ").strip().lower()
        )
        while alignment not in ["left", "center", "right"]:
            print("Невірний вибір. Спробуйте знову.")
            alignment = (
                input("Оберіть вирівнювання (left, center, right): ").strip().lower()
            )
        return alignment

    def read_color_mode():
        color_mode = input("Оберіть режим кольору (bw або gray): ").strip().lower()
        while color_mode not in ["bw", "gray"]:
            print("Невірний вибір. Спробуйте знову.")
            color_mode = input("Оберіть режим кольору (bw або gray): ").strip().lower()
        return color_mode
