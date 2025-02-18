def test_example():
    import colex  # Every public namespace is available under `colex`

    print(colex.RED + "Hello red!")
    print("Still red...")
    print(colex.RESET, "Back to normal")

    # Optionally, you can import submodules or constants like this
    from colex import color, style, RESET

    print(style.ITALIC + color.GREEN + "Hello italic green" + RESET)

    # You may want to use this helper function to have color param at the end
    from colex import colorize

    print(colorize("Hello blue!", colex.BLUE))

    # Note that `colex` is using ANSI escape codes,
    # therefore any string can be annotated with `ColorValue`
    from colex import ColorValue

    my_color: ColorValue = "\x1b[31m"  # The ANSI code for red
    print(my_color + "Hello red, again")
