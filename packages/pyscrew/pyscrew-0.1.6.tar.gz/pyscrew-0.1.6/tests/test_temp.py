import pyscrew

if __name__ == "__main__":
    print(pyscrew.list_scenarios())

    # List available scenarios with their descriptions
    scenarios = pyscrew.list_scenarios()
    print("Available scenarios:", scenarios)

    # Load and process data from a specific scenario
    data = pyscrew.get_data(
        "injection-molding-manipulations-upper-workpiece",
        handle_duplicates="first",
        handle_missings="mean",
        target_length=1500,
        force_download=False,
    )

    # Access the data
    print("Available measurements:", data.keys())
    print("Number of torque measurements:", len(data["torque values"]))

    x_values = data["torque values"]
    y_values = data["class values"]

    # Describe y values
    print("Unique class values:", set(y_values))
    print("Class distribution:", {c: y_values.count(c) for c in set(y_values)})
