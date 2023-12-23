# Log Parsing Script

This script is designed to parse HTTP request logs, compute metrics, and print statistics. It reads log entries from stdin, extracts relevant information, and provides insights into the accumulated data.

## Usage

### Prerequisites

- Python 3.x
- Ubuntu 20.04 LTS

### Installation

No specific installation is required. Ensure you have Python 3.x installed on your system.

### Running the Script

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. Navigate to the project directory:

   ```bash
   cd log-parsing-project
   ```

3. Run the log generator script to generate sample log entries:

   ```bash
   ./log_generator.py | ./log_parser.py
   ```

## Scripts

### 1. log_generator.py

This script generates random HTTP request logs for testing purposes. It produces log entries with random IP addresses, dates, request paths, status codes, and file sizes.

### 2. log_parser.py

The main log parsing script. It reads log entries from stdin, computes metrics, and prints statistics. The statistics include the total file size and the count of each HTTP status code.

## File Structure

- `log_generator.py`: Script to generate random log entries.
- `log_parser.py`: Main log parsing script.
- `README.md`: Project documentation.

## Author

- **Your Name**
- GitHub: [your-username](https://github.com/your-username)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
