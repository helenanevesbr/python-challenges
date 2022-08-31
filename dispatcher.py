def add_lines():
    print(f"Insira linhas de texto")

    set_of_lines = []
    while True:
        data = input()
        if str.lower(data) == "":
            break
        set_of_lines.append(data)

    if not set_of_lines:
        print(f"Nenhuma linha não vazia lida!!")
        exit()

    return set_of_lines