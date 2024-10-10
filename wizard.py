import os

import config
import compute


def main() -> None:
    print("FACOF - FAC on terminal framework")
    print()

    elem = input("\tAtom symbol: ")
    nelec = int(input("\tSelec the number of bound electrons: "))
    gen_tr = input("\tGenerate transition table? (y/n): ")

    if gen_tr == "y":
        compute.compute_tr(elem, nelec, config.uta_flag, config.ci_flag)
        print("\tAtomic structure and transitions files generated!")

    if gen_tr == "n":
        compute.compute_lev(elem, nelec, config.uta_flag, config.ci_flag)
        print("\tAtomic structure files generated!")


if __name__ == "__main__":
    main()
