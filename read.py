import os
import config


def read_ion_data(nion: int) -> list:
    path_to_ion = os.path.join(config.ions_path, f"ion{nion}.dat")

    with open(path_to_ion, "r") as f:
        return [config.strip() for config in f.readlines()]
