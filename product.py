def get_compatible_subshell_distributions(nelec: int, max_subshell_ocupation: list):
    a = [nelec] + [0 for _ in max_subshell_ocupation[1:]]

    while True:
        i = 0
        while (
            a[i] >= max_subshell_ocupation[i] + 1
            and i < len(max_subshell_ocupation) - 1
        ):
            a[i + 1] += a[i] - max_subshell_ocupation[i]
            a[i] = max_subshell_ocupation[i]
            i += 1
        if a[-1] >= max_subshell_ocupation[-1] + 1:
            return

        yield a

        i0 = 1
        surplus = 0
        while True:
            for i in range(i0, len(max_subshell_ocupation)):
                if a[i] < max_subshell_ocupation[i]:
                    a[i] += 1
                    surplus += 1
                    break
                else:
                    surplus -= a[i]
                    a[i] = 0
            else:
                return

            if a[0] >= surplus:
                break
            else:
                surplus -= a[i0]
                a[i0] = 0
                i0 += 1
                if i0 == len(max_subshell_ocupation):
                    return

        a[0] -= surplus