# Password Generator Dashboard

An interactive web app built with Python and Streamlit that generates passwords in three styles: random, memorable (word-based), and numeric PIN.

## Project Structure

```text id="c5x2a8"
.
├── README.md
├── requirements.txt
└── src
    ├── password_generator.py
    ├── dashboard.py
    └── images/
```

- `src/password_generator.py`: the password generator classes `PinGeneratorPassword`, `RandomPasswordGenerator`, and `MemorablePasswordGenerator`
- `src/dashboard.py`: the Streamlit web interface
- `src/images/`: images used by the dashboard
- `requirements.txt`: project dependencies

## Password Types

| Generator                    | Description                                                                         |
| ---------------------------- | ----------------------------------------------------------------------------------- |
| `PinGeneratorPassword`       | Numeric PIN of a chosen length                                                      |
| `RandomPasswordGenerator`    | Random letters, with optional numbers and symbols                                   |
| `MemorablePasswordGenerator` | Several dictionary words joined by a separator, with optional random capitalization |

Example:

```python id="7q8z2m"
from src.password_generator import RandomPasswordGenerator

generator = RandomPasswordGenerator(
    length=12,
    include_numbers=True,
    include_symbols=True
)

print(generator.generator())
```

## Installation

```bash id="x3d9ma"
git clone https://github.com/mahnazghssm/Password-Generator.git
cd Password-Generator
pip install -r requirements.txt
```

The NLTK words corpus is downloaded automatically the first time you run the project.

## Usage

Run the dashboard:

```bash id="z5s1kq"
streamlit run src/dashboard.py
```

This opens the app in your browser on localhost.

To try the generators in the terminal:

```bash id="p4c6vn"
python src/password_generator.py
```

## License

This project is licensed under the MIT License.
