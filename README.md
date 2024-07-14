# DeepFormPusher (Python)

DeepFormPusher is an automated form interaction tool designed to stress test and interact with online forms. This project uses Selenium and Faker to simulate user input and submit forms repeatedly.

## Getting Started

To get started with this project, follow the steps below to clone and install the application on your local machine.

### Prerequisites

Make sure you have the following installed on your machine:

- [Python](https://www.python.org/downloads/)
- [Selenium](https://selenium.dev/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/alfargenis/DeepFormPusher.git
   cd DeepFormPusher
   ```

2. **Install the required Python packages**

   ```bash
   pip install selenium faker
   ```

### Configuration

Before running any script, make sure to update the email, password, and Google Form URL in the respective script files. Each script is independent and must be configured separately.

### Usage

To run each form interaction script, execute the corresponding command for each script:

- For `pavaV1.py`:

  ```bash
  python pavaV1.py
  ```

- For `paraWEmail.py`:

  ```bash
  python paraWEmail.py
  ```

- For `penV1.py`:

  ```bash
  python penV1.py
  ```

- For `penV2.py`:

  ```bash
  python penV2.py
  ```

- For `penWNumber.py`:

  ```bash
  python penWNumber.py
  ```

### Script Functions

Each script has a specific purpose:

- **pavaV1.py**: Interacts with a specific form setup.
- **paraWEmail.py**: Fills out forms using randomly generated email addresses.
- **penV1.py**: Submits forms based on a particular set of parameters.
- **penV2.py**: An updated version of penV1 with additional functionalities.
- **penWNumber.py**: Fills forms with randomly generated phone numbers.

### Learn More

- [Selenium Documentation](https://selenium.dev/documentation/en/)
- [Faker Documentation](https://faker.readthedocs.io/en/master/)

### Contributing

If you want to contribute to this project, please open an issue or submit a pull request.
