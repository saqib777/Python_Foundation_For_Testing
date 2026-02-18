# Python Test Automation Framework

A modular, CI-integrated automation framework built using Python, Pytest, Requests, Selenium, and GitHub Actions.

This repository represents a structured automation foundation covering API testing, UI automation, performance validation, and continuous integration. The goal of this project is not just to write tests, but to design a maintainable, extensible automation architecture aligned with real-world engineering standards.

---

## Project Philosophy

This framework was built with architectural intent. Instead of writing standalone scripts that directly call APIs or UI actions, the design enforces separation of concerns, reusability, and clarity. Each layer has a defined responsibility. HTTP communication is abstracted. Validation logic is centralized. Tests focus only on behavioral verification.

The structure reflects how production-grade automation should be organized: scalable, readable, CI-ready, and defensive against environmental inconsistencies.

---

## Architecture Overview

The project is divided into clearly defined layers:

* **API Layer (`src/api/`)**: Contains client abstractions and domain-specific API classes.
* **Validation Layer (`validators.py`)**: Contains reusable response validation logic.
* **Test Layer (`tests/`)**: Contains API, UI, and performance test modules.
* **CI Layer (`.github/workflows/`)**: Contains GitHub Actions configuration for automated execution.

This layered approach prevents duplication and enforces maintainability.

---

## API Automation Design

### Base Client Abstraction

All HTTP communication is routed through a base client class. This centralizes:

* Base URL configuration
* HTTP method handling
* Future logging extensions
* Potential retry mechanisms

Instead of calling `requests.get()` or `requests.post()` directly in tests, API classes such as `AuthAPI` and `UsersAPI` inherit from the base client. This ensures consistency and scalability.

Tests never directly manage request construction. They validate outcomes.

---

### Domain-Specific API Classes

* `AuthAPI` handles authentication endpoints (login, register).
* `UsersAPI` handles user retrieval endpoints.

Each class encapsulates endpoint logic while keeping tests clean and readable.

Example design principle: tests should read like behavior descriptions, not network instructions.

---

## Validation Layer

Response validation is centralized in `validators.py`.

Instead of repeatedly asserting structure inside test files, reusable validation functions enforce schema expectations.

Example:

* Token response validation ensures presence and type correctness.
* User object validation ensures required fields exist.

This prevents duplication and promotes consistency across tests.

Tests verify behavior. Validators verify structure.

---

## Defensive JSON Handling

External APIs are not always reliable. CI environments may expose edge cases that do not appear locally.

To prevent runtime crashes from malformed responses, a safe JSON extraction wrapper is used. This protects tests from unexpected `JSONDecodeError` exceptions.

This was particularly important during CI debugging, where local tests passed but CI failed due to response parsing issues.

Automation must anticipate failure modes.

---

## API Test Coverage

The API layer includes coverage for:

### Authentication Scenarios

* Successful registration
* Missing password validation
* Invalid credentials handling
* Response time validation
* Status code handling across environments

Because external APIs may return 403 in some environments, assertions were made resilient while still validating expected behavior.

### Users API Scenarios

* Retrieve list of users
* Retrieve single user by ID
* User not found handling
* JSON structure validation
* Response content verification

Edge cases addressed include:

* 403 responses in CI
* Non-JSON responses
* Empty body responses

These were identified during CI execution and rectified using defensive validation techniques.

---

## Performance Testing

Performance tests validate response timing thresholds and stability under repeated calls.

The goal is not load testing but regression-level performance assurance.

Performance coverage includes:

* Response time under defined threshold
* Multiple sequential request validation
* Stability verification under repetition

These tests are executed as part of CI to ensure no performance degradation occurs silently.

---

## UI Automation Foundation

UI tests are located under `tests/ui/` and demonstrate Selenium-based automation.

Covered concepts include:

* Dynamic content handling
* Element interaction
* Assertion strategy
* Marker-based test grouping

UI tests are modular and separated from API tests using Pytest markers. This allows selective execution.

UI tests are intentionally not fully integrated into CI at this stage to avoid browser dependency complexity during Phase B.

---

## Continuous Integration (CI)

GitHub Actions pipeline executes automatically on push and pull request.

Pipeline stages:

1. Checkout repository
2. Setup Python 3.11
3. Create virtual environment
4. Install dependencies
5. Verify Pytest collection
6. Execute API tests
7. Execute performance tests

During CI implementation, several issues were encountered and resolved:

* Import path resolution errors
* Validator import failures
* JSON decode failures in runner environment
* Status code inconsistencies between local and CI

These were resolved through structural corrections and defensive coding practices.

CI now reliably validates the framework.

---

## Running Locally

Clone the repository and navigate to the project directory.

Create a virtual environment using Python.

Activate the environment.

Install dependencies from `requirements.txt`.

Execute tests using Pytest markers:

* API tests
* Performance tests
* UI tests

This selective execution allows flexible validation.

---

## Technologies Used

* Python 3.11
* Pytest
* Requests
* Selenium
* GitHub Actions
* Virtual Environment (venv)

---

## What This Project Demonstrates

* Structured automation architecture
* Modular API abstraction
* Reusable validation layer
* Defensive automation design
* CI/CD integration
* Performance validation fundamentals
* Clean separation of concerns

This repository reflects a strong automation foundation aligned with SDET-level practices.

---

## Future Enhancements

Potential next steps include:

* JSON schema validation integration
* Retry and logging framework implementation
* Dockerized execution
* Parallel test execution
* Full UI integration in CI
* Load testing integration (Locust or JMeter)
* Reporting tools integration

---

## Project Status

Phase B complete.

The framework now includes API automation, UI foundation, performance validation, and CI integration. The structure is stable, extensible, and production-oriented.

This repository represents a complete automation foundation ready for expansion into advanced engineering practices.
