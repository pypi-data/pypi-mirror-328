import coma

if __name__ == "__main__":
    coma.register("greet", lambda: print("Hello World!"))
    coma.register("default", lambda: print("Default command."))
    try:
        coma.wake()
    except coma.WakeException:
        coma.wake(["default"])
