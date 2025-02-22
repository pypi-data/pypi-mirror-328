import coma

if __name__ == "__main__":
    # coma.register("test", lambda: print("Success"))
    try:
        coma.wake()
    except coma.WakeException as e:
        print(f"Failed. {e.args[0]}")
        coma.wake(args=["fake"])
