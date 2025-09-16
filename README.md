# NASOW package

Welcome to the (small and simple) NASOW script! NASOW stands for **Nameserver reSolver for WSL**. It's a simple small python script which synchronizes DNS servers for WSL from Windows.
This repository contains its source code and documentation.

## Features

- **Sync DNS**: Automatically synchronizes DNS servers for WSL from Windows.
- **Customizable**: Easily configure the WSL distribution and DNS settings.
- **Seamless Integration**: Works with Windows PowerShell and WSL.

## Installation

To get started with the NASOW project, follow these steps:

1. Clone the repository:
  ```bash
  git clone https://github.com/jpweng/nasow.git
  ```
2. Navigate to the project directory:
  ```bash
  cd nasow
  ```
3. Ensure you have Python installed. Install this package:
  ```bash
  pip install .
  ```

## Usage

Run the application with the following command:
```bash
python C:\path\to\package\nasow\add_ns.py
```

### Workflow
The script will:
1. Retrieve DNS servers from Windows.
2. Read the current DNS configuration in WSL.
3. Merge and write the updated DNS configuration back to WSL.

## Contributing

Contributions are welcome! Please follow these steps (or push directly to the _master_ branch):

1. Fork the repository.
2. Create a new branch:
  ```bash
  git switch -c feature-name
  ```
3. Commit your changes:
  ```bash
  git commit -m "Add feature-name"
  ```
4. Push to your branch:
  ```bash
  git push origin feature-name
  ```
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or feedback, please contact jpaul.wenger@gmail.com.