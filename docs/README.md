# ⚔️ Odin's Spear

<figure><img src=".gitbook/assets/logo.png" alt="Odin's Spear Logo"><figcaption></figcaption></figure>

## Overview

Odin's Spear is a Python library designed to streamline and enhance your experience with Odin's API by [Rev.io](https://www.rev.io/blog/solutions/rev-io-odin-api). If you've worked with BroadWorks for years and struggled with its outdated interface and limitations, Odin's API feels like a breath of fresh air—offering a modern user interface, automation, and comprehensive API access.

With Odin's Spear, managing users, hunt groups, call centers, and other telecom operations becomes significantly easier. This library encapsulates Odin's API functionality, making it accessible, efficient, and user-friendly.

## Features

- **Bulk User Management:** Create and manage thousands of users, hunt groups, and call centers in minutes.
- **Error Handling:** Automatically manage authentication, request design, and error handling.
- **Advanced Tools:** Features like call flow visualization, group audit reports, and bulk management of telecom entities.
- **Alias Assignment Locator:** The first feature release addresses a long-standing issue by allowing you to easily locate where an alias is assigned within BroadWorks—saving you time and frustration.

## Why Odin's Spear?

Working with BroadWorks for over five years was a challenge, with its 90s-style UI and rigid functionality. When Rev.io introduced Odin, with its modern interface and API, it revolutionized how telecom management could be done. However, even with these advancements, some tasks remained cumbersome, like locating alias assignments. 

Odin's Spear is the solution. It simplifies your workflow by automating repetitive tasks, handling errors, and making API interactions as smooth as possible. Whether you're managing 10 users or 10,000, Odin's Spear has you covered.

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- An Odin account

### Installation

Install Odin's Spear using pip:

```bash
pip install odins-spear
```

### Basic Usage

Here's a simple example to get you started:

```python
from odins_spear.api import API

# Initialize the API with your credentials
my_api = api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN-INSTANCE-1")
my_api.authenticate()

# Locate an alias assignment
alias_info = my_api.scripter.find_alias('ServiceProviderID', 'GroupID', alias=0)
print(alias_info)
```

For more detailed usage and examples, check out our [Documentation](#-documentation).

## 📖 Documentation

We provide extensive documentation to help you get started quickly and take full advantage of Odin's Spear's capabilities:

- [Odin's Spear Documentation](https://docs.jordan-prescott.com/odins_spear)

Odins Official API docs
- [Odin API Documentaion](https://doc.odinapi.net/)

## Contributing

We welcome contributions! If you'd like to contribute, please fork the project, make your changes then submit a pull request. 
For issues to work on please see our [project](https://github.com/users/Jordan-Prescott/projects/2).

## License

This project is licensed under the MIT License—see the [LICENSE.md](LICENSE) file for details.

## Support

If you encounter any issues or have questions, feel free to open an issue on GitHub.

## Acknowledgements

Special thanks to the developers at Rev.io for creating the Odin API and to the engineers who provided invaluable feedback and feature suggestions.
