def load_file(file: str) -> str:
    """Загружает данные из файла"""

    with open(file, encoding="utf-8") as f:
        return f.read()


def parse_request(request: dict) -> list[tuple]:
    """Разбивает запрос на список кортежей: команда, значение"""

    commands = {key: request.get(key) for key in sorted(request) if key.count("cmd")}
    values = {key: request.get(key) for key in sorted(request) if key.count("value")}

    return list(zip(commands.values(), values.values()))


if __name__ == "__main__":
    pass
