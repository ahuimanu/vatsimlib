from data_reader import reader


def main():
    print("VATSIM LIB")
    json_data = reader.init()
    vgs = reader.get_vatsim_general(json_data)
    print(vgs)

    pilots = reader.get_vatsim_pilots(json_data)
    print(f"number of pilots this update: {len(pilots)}")


if __name__ == "__main__":
    main()
