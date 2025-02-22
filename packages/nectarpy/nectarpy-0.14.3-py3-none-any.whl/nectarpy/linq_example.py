class LinqExample:
    """Client for sending queries to Nectar"""

    def __init__(self):
        """Constructor: LinqExample."""
        print("LinqExample initialized.")

    def example_methods(self):
        """Example method that prints a running message."""
        print("[example_methods] running...")

if __name__ == "__main__":
    client = LinqExample()
    client.example_methods()
