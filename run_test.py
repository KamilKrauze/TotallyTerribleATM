import sys
import time
import unittest

def main():
    print("Running tests before push...\n")

    start_time = time.time()

    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=".", pattern="test_*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    end_time = time.time()

    print("\n==== TEST SUMMARY ====")
    print(f"Total tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Time: {end_time - start_time:.2f}s")

    # Exit with proper code so Git hook can detect failure
    if result.wasSuccessful():
        print("\nAll tests passed.")
        sys.exit(0)
    else:
        print("\nTests failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()