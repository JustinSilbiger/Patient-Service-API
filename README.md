<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/se-2024/PATIENT_SERVICE_API">
    <img src="images/logo.png" alt="Logo">
  </a>
  
  <h3 align="center">Patient Service API</h3>

  <p align="center">
    A robust API for managing patient details in a hospital management system.
    <br />
    <a href="https://github.com/se-2024/PATIENT_SERVICE_API/blob/main/docs/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/se-2024/PATIENT_SERVICE_API/issues">Report Bug</a>
    ·
    <a href="https://github.com/se-2024/PATIENT_SERVICE_API/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#development">Development</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#testing">Testing</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This is a Python-based RESTful API that is part of the Hospital Management System. It allows for the saving and retrieving of patient details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![FastAPI][FastAPI]][FastAPI-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To set up your project locally, follow these simple steps.

### Prerequisites

Ensure you have the following software installed:
* Python
  - MacOS: Follow this guide - [Install Python on MacOS](https://docs.python-guide.org/starting/install3/osx/)

### Installation

#### New Repository Setup

1. Fork the Project.
2. Clone the forked repo locally:
    ```sh
    git clone git@github.com:YOUR_USERNAME/PATIENT_SERVICE_API.git
    ```
3. Verify the remote repository configuration:
    ```sh
    git remote -v
    ```
4. Add the original repository as a remote upstream:
    ```sh
    git remote add upstream https://github.com/se-2024/PATIENT_SERVICE_API.git
    ```
5. Verify the new remote:
    ```sh
    git remote -v
    ```

#### Existing Repository Setup

1. Verify the current remote repository configuration:
    ```sh
    git remote -v
    ```
2. Add the original repository as a remote upstream:
    ```sh
    git remote add upstream https://github.com/se-2024/PATIENT_SERVICE_API.git
    ```
3. Verify the new remote:
    ```sh
    git remote -v
    ```
4. Reset your local main branch to match the remote upstream:
    ```sh
    git reset --hard upstream/main
    ```
5. Force push the changes to your repository:
    ```sh
    git push origin main -f
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Development

### Coding Standards

- [pre-commit](https://pre-commit.com/) - Git hook scripts for identifying simple issues before submission to code review.
- Code linting:
  - [Flake8](https://github.com/PyCQA/flake8) - A linter tool that checks your code for style and syntax errors.
- Code formatting:
  - [Black](https://github.com/psf/black) - A Python code formatter that automatically formats your code according to predefined rules.
  - [isort](https://github.com/PyCQA/isort) - A utility/library to sort imports alphabetically and automatically separate them into sections and by type.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Include useful examples of how the project can be used. Additional screenshots, code examples, and demos work well in this space. You may also link to more resources.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- TESTING -->
## Testing

### Unit and Integration Testing

- [pytest](https://docs.pytest.org/en/7.1.x/getting-started.html) - A Python testing framework for writing various types of software tests, including unit, integration, end-to-end, and functional tests.
- [pytest-sqlalchemy-mock](https://github.com/resulyrt93/pytest-sqlalchemy-mock) - Pytest fixtures to create an in-memory DB instance for tests and dump your raw test data.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fetch the latest from the upstream repository:
    ```sh
    git fetch upstream
    ```
2. Check out your fork's local main branch:
    ```sh
    git checkout main
    ```
3. Merge the latest code from the upstream main branch:
    ```sh
    git merge upstream/main
    ```
4. Create your feature branch:
    ```sh
    git checkout -b feature/AmazingFeature
    ```
5. Commit your changes:
    ```sh
    git commit -m 'Add some AmazingFeature'
    ```
6. Push to the branch:
    ```sh
    git push origin feature/AmazingFeature
    ```
7. Open a pull request.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/se-2024/PATIENT_SERVICE_API.svg?style=for-the-badge
[contributors-url]: https://github.com/se-2024/PATIENT_SERVICE_API/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/se-2024/PATIENT_SERVICE_API.svg?style=for-the-badge
[forks-url]: https://github.com/se-2024/PATIENT_SERVICE_API/network/members
[issues-shield]: https://img.shields.io/github/issues/se-2024/PATIENT_SERVICE_API.svg?style=for-the-badge
[issues-url]: https://github.com/se-2024/PATIENT_SERVICE_API/issues
[product-screenshot]: images/screenshot.png
[FastAPI]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/
