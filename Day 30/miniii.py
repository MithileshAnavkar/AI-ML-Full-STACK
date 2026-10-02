class Timer:
    def __enter__(self):
        print("Starting...")

    def __exit__(self, exc_type, exc_value, tracebook):
        print("Finished...")

with Timer():
    print("Code is running")