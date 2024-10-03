
# Small Cell Base Station Demo

This project is a basic simulation of a small cell base station, showcasing how user devices connect, manage network capacity, and backhaul connections. This demo is useful for understanding the principles behind small cell technology in mobile networks.

## Features
- Simulates a small cell base station with configurable coverage area and user capacity.
- User devices can connect and disconnect from the small cell based on their proximity.
- Simulates different types of backhaul connections (e.g., fiber, satellite) with varying bandwidth.
- Includes basic testing for user connections and capacity limits.

## Project Structure

```
small-cell-base-station-demo/
│
├── src/
│   ├── small_cell.py         # Small cell base station logic
│   ├── user_device.py        # User device logic
│   ├── backhaul.py           # Backhaul connection logic
│   └── main.py               # Main simulation script
│
├── tests/
│   └── test_small_cell.py    # Unit tests for small cell functionality
│
├── README.md                 # Project documentation
└── .gitignore                # Files to be ignored by Git
```

## Requirements

- Python 3.x
- Unit test framework: `unittest` (comes pre-installed with Python)

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/small-cell-base-station-demo.git
   ```
2. Navigate into the project directory:
   ```bash
   cd small-cell-base-station-demo
   ```

## How to Run the Simulation

1. Navigate to the `src/` directory:
   ```bash
   cd src
   ```

2. Run the main simulation script:
   ```bash
   python3 main.py
   ```

The simulation will display user connections, small cell capacity, and backhaul status.

## Example Output

```bash
User Device001 connected.
User Device002 is out of range.
User Device003 connected.
Connected users: 2/10
Coverage area: 150 meters
Backhaul type: fiber
Bandwidth: 100 Mbps
Backhaul updated to satellite with 20 Mbps
User Device001 disconnected.
Connected users: 1/10
```

## Tests

To run the unit tests, navigate to the `tests/` directory and execute the following command:

```bash
python3 test_small_cell.py
```

This will run basic tests to ensure the small cell station manages users correctly.

## Configuration

You can adjust the following parameters in the `main.py` file:

- **Small Cell Capacity**: Maximum number of users that can connect at one time.
- **Coverage Area**: The radius in meters that determines whether a user is in range to connect.
- **Backhaul Type and Bandwidth**: Change the type and bandwidth of the backhaul to simulate different network conditions.

## Future Improvements

- Add more advanced user mobility simulation (moving in and out of coverage).
- Implement a web dashboard for real-time monitoring of small cell status.
- Expand the backhaul simulation to include network latency and failure scenarios.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute by submitting pull requests or reporting issues!
