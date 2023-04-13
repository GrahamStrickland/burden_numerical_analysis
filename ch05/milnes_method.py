#!/usr/bin/env python3


def predictor(f_vals: list[float], h: float) -> float:
    return f_vals[0] + ((4.*h)/3.)*(2.*f_vals[1] - f_vals[2] + 2.*f_vals[3])


def corrector(f_vals: list[float], h: float) -> float:
    return f_vals[0] + (h/3.)*(2.*f_vals[1] + 4.*f_vals[2] + f_vals[3])


def main():
    f_vals = 
    print()


if __name__ == "__main__":
    main()
