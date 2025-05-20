# auntypelz-hiringos

This repository contains the code and plans for the **AuntyPelz Hiring OS** project.

## Overview
AuntyPelz Hiring OS is designed to streamline and automate the hiring process, leveraging modern SaaS boilerplates and automation scripts. The project includes:
- A SaaS boilerplate (from Async Labs)
- Custom scripts for planning and issue management
- Documentation and plans for rapid MVP development

## Project Structure
- `saas/` — Contains the SaaS boilerplate (cloned from [Async Labs SaaS](https://github.com/async-labs/saas))
- `linear_plan_to_issues.py` — Script to convert linear plans into GitHub issues
- `plan.md` — Project plan and setup notes
- `venv/` — Python virtual environment (not included in version control)

## Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/curaceldev1/auntypelz-hiringos.git
   cd auntypelz-hiringos
   ```
2. **Set up the SaaS boilerplate:**
   Follow the instructions in `saas/README.md` to install dependencies and configure the SaaS app.
3. **Set up Python environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt  # if requirements.txt is present
   ```

## Usage
- Use the SaaS app as your base for the hiring platform.
- Use `linear_plan_to_issues.py` to automate the creation of GitHub issues from your project plan.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the `saas/` directory for third-party license details. 