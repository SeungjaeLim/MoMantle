from MoMantle.loader.loader import load_data


def main():
    pokemon_data = load_data("./asset/pokemon", [True, False, False, False])
    leagueoflegend_data = load_data("./asset/leagueoflegend", [True, True, False, False])

if __name__ == "__main__":
    main()
    