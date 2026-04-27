import os

import config
import compute


def main() -> None:
    print("FACOF - FAC on terminal framework")
    print()

    elem = input("\tAtom symbol: ")
    nelec = int(input("\tSelec the number of bound electrons: "))
    gen_tr = input("\tGenerate transition table? (y/n): ")
    if gen_tr != "y" and nelec > 1:
        gen_ai = input("\tGenerate autoionization rates? (y/n): ")
    else:
        gen_ai = None

    if gen_tr == "y":
        compute.compute_tr(elem, nelec, config.UTA_FLAG, config.CI_FLAG)
        print("\tAtomic structure and transitions file generated!")
        return
    elif gen_ai == "y":
        compute.compute_ai(elem, nelec, config.UTA_FLAG, config.CI_FLAG)
        print("\tAutoionization rates file generated!")
    else:
        compute.compute_lev(elem, nelec, config.UTA_FLAG, config.CI_FLAG)
        print("\tAtomic structure file generated!")
        return


if __name__ == "__main__":
    main()
