import pytest
import time

# Start timer
start_time = time.time()
exit_code = pytest.main([
    "-x",
    "/home/vasilis/PycharmProjects/requests/tests"
])

# Stop timer
end_time = time.time()

total_time = end_time - start_time
print(f"Total execution time: {total_time:.2f} seconds")
