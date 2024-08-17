#!/usr/bin/env python3
from collections.abc import Callable
from typing import TextIO


LONG_BORDER = 108
SHORT_BORDER = 60


def runge_kutta_fehlberg(
    function: Callable[[float, ...], float],
    a: float,
    b: float,
    alpha: float,
    tol: float,
    hmax: float,
    hmin: float,
    file: TextIO = None,
    solution: Callable[[float], float] = None,
) -> list[float]:
    """To approximate the solution of the initial-value problem y' = f(t, y),
    a <= t <= b, y(a) = alpha, with local truncation error within a given tolerance.
    INPUT endpoints a, b; initial condition alpha; tolerance TOL; maximum step size
    hmax; minimum step size hmin.
    OUTPUT t, w, h, where w approximates y(t) and the step size h was used or a
    message that the minimum step size was exceeded.
    """
    # output table heading
    if solution:
        output_string = f"{'-'*LONG_BORDER}\nt_i\t\t\tw_i\t\t\th\t\t\ty_i=y(t_i)\t\t"
        output_string += f"|y_i - w_i|\n{'-'*LONG_BORDER}"
    else:
        output_string = f"{'-'*SHORT_BORDER}\nt_i\t\t\tw_i\t\t\th\n{'-'*SHORT_BORDER}"
    if not file:
        print(output_string)
    else:
        file.write(output_string + "\n")

    # STEP 1:
    t: float = a
    w: float = alpha
    h: float = hmax
    flag: bool = True
    solutions = [w]

    # output row
    row_output(t, w, file=file, solution=solution)

    # STEP 2: while (FLAG = 1) do Steps 3-11.
    while flag and not isinstance(w, complex):
        # STEP 3:
        try:
            k_1 = h * function(t, w)
            k_2 = h * function(t + (1.0 / 4.0) * h, w + (1.0 / 4.0) * k_1)
            k_3 = h * function(
                t + (3.0 / 8.0) * h, w + (3.0 / 32.0) * k_1 + (9.0 / 32.0) * k_2
            )
            k_4 = h * function(
                t + (12.0 / 13.0) * h,
                w
                + (1932.0 / 2197.0) * k_1
                - (7200.0 / 2197.0) * k_2
                + (7296.0 / 2197.0) * k_3,
            )
            k_5 = h * function(
                t + h,
                w
                + (439.0 / 216.0) * k_1
                - 8.0 * k_2
                + (3680.0 / 513.0) * k_3
                - (845.0 / 4104.0) * k_4,
            )
            k_6 = h * function(
                t + (1.0 / 2.0) * h,
                w
                - (8.0 / 27.0) * k_1
                + 2.0 * k_2
                - (3544.0 / 2565.0) * k_3
                + (1859.0 / 4104.0) * k_4
                - (11.0 / 40.0) * k_5,
            )

            # STEP 4: Note: R = 1/h |w_{i+1}^~ - w_{i+1}| ~= |tau_{i+1}(h)|
            r = (1.0 / h) * abs(
                (1.0 / 360.0) * k_1
                - (128.0 / 4275.0) * k_3
                - (2197.0 / 75240.0) * k_4
                + (1.0 / 50.0) * k_5
                + (2.0 / 55.0) * k_6
            )

            # STEP 5: If R <= TOL then do Steps 6 and 7
            if r <= tol:
                # STEP 6:
                t = t + h  # Approximation accepted
                w = w + (
                    (25.0 / 216.0) * k_1
                    + (1408.0 / 2565.0) * k_3
                    + (2197.0 / 4104.0) * k_4
                    - (1.0 / 5.0) * k_5
                )

                # STEP 7:
                row_output(t, w, h, file=file, solution=solution)
                solutions.append(w)

            # STEP 8:
            delta = 0.84 * (tol / r) ** (1.0 / 4.0)

            # STEP 9: Calculate new h
            if delta <= 0.1:
                h = 0.1 * h
            elif delta >= 4.0:
                h = 4.0 * h
            else:
                h = delta * h

            # STEP 10:
            if h > hmax:
                h = hmax

            # STEP 11:
            if t >= b:
                flag = False
            elif t + h > b:
                h = b - t
            elif h < hmin:
                flag = False
                raise ArithmeticError(
                    "Minimum h exceeded, procedure completed unsuccessfully."
                )

        except ZeroDivisionError as e:
            print(e)
            return []

    # STEP 12: stop
    if solution:
        output_string = "-" * LONG_BORDER + "\n"
    else:
        output_string = "-" * SHORT_BORDER + "\n"

    if not file:
        print(output_string)
    else:
        file.write(output_string)
    return solutions


def row_output(
    t_i: float,
    w_i: float,
    h: float = 0.0,
    file: TextIO = None,
    solution: Callable[[float], float] = None,
) -> None:
    """Function to output row of table."""
    if solution:
        output = "{:.10f}\t\t{:.10f}\t\t{:.10f}\t\t{:.10f}\t\t{:.10f}".format(
            t_i, w_i, h, solution(t_i), abs(solution(t_i) - w_i)
        )
    else:
        output = "{:.10f}\t\t{:.10f}\t\t{:.10f}".format(t_i, w_i, h)

    if not file:
        print(output)
    else:
        file.write(output + "\n")
