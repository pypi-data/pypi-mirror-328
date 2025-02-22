import pandas as pd
import pytest
import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the src directory to the Python module search path
sys.path.append(os.path.join(parent_dir, "src"))
	

from run_bcsd import within_window

@pytest.mark.parametrize(
    "time, start_window, end_window, expected",
    [
        # Happy path tests
        ("2024-06-05", "2024-06-01", "2024-06-10", True),  # Within window, same year
        ("2024-12-28", "2024-12-25", "2025-01-05", True),  # Within window, year boundary
        ("2024-01-02", "2023-12-25", "2024-01-05", True),  # Within window, year boundary

        # Edge cases
        ("2024-06-01", "2024-06-01", "2024-06-10", True),  # Start of window
        ("2024-06-10", "2024-06-01", "2024-06-10", True),  # End of window
        ("2024-12-25", "2024-12-25", "2025-01-05", True),  # Start of window, year boundary
        ("2025-01-05", "2024-12-25", "2025-01-05", True),  # End of window, year boundary

        # Error cases outside window
        ("2024-05-31", "2024-06-01", "2024-06-10", False),  # Before window
        ("2024-06-11", "2024-06-01", "2024-06-10", False),  # After window
        ("2024-12-24", "2024-12-25", "2025-01-05", False),  # Before window, year boundary
        ("2025-01-06", "2024-12-25", "2025-01-05", False),  # After window, year boundary
    ],
    ids=[
        "within_window_same_year",
        "within_window_year_boundary_1",
        "within_window_year_boundary_2",
        "start_of_window",
        "end_of_window",
        "start_of_window_year_boundary",
        "end_of_window_year_boundary",
        "before_window",
        "after_window",
        "before_window_year_boundary",
        "after_window_year_boundary",
    ],
)
def test_within_window(time, start_window, end_window, expected):
    # Act
    actual = within_window(pd.Timestamp(time), pd.Timestamp(start_window), pd.Timestamp(end_window))

    # Assert
    assert actual == expected
