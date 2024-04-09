class Name:
    def __init__(self, name, hobby) -> None:
        if name not in ["Богдан", "Анонім", "Арсен"]:
            raise ValueError("Дозволені імена: Богдан, Анонім, Арсен")
        self.name = name

        if hobby == "":
            raise ValueError("Хобі не введено")

a = Name("Арсенотрон", "Волейбол")