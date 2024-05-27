# Lesson: Unit Testing and Integration Testing

## Overview

This lesson covers the concepts of unit testing and integration testing in software development. You will learn the purpose of these tests, the differences between them, and how to implement them effectively using Python's `unittest` framework. Additionally, the lesson includes an introduction to mocking, parameterization, and fixtures.

## Unit Testing

### Definition
Unit testing is the process of testing individual functions or methods in isolation to ensure they return expected results for different sets of inputs. The primary goal of a unit test is to verify that a specific function works correctly when all external dependencies are functioning as expected.

### Key Points
- **Test Logic in Isolation:** Focus on testing the logic within the function itself.
- **Mock External Calls:** Use mocking for calls to other functions, especially those that involve network or database operations.
- **Standard Inputs and Corner Cases:** Ensure tests cover both typical inputs and edge cases.

### Example Command
To execute your unit tests, use the following command:
```sh
$ python -m unittest path/to/test_file.py
```

## Integration Testing

### Definition
Integration testing evaluates the interactions between different parts of your code, testing the complete code path from start to finish. These tests ensure that integrated components work together as intended.

### Key Points
- **End-to-End Testing:** Validate the entire flow of your application.
- **Minimal Mocking:** Only mock low-level functions that make external calls, such as HTTP requests, file I/O, or database operations.

## Learning Objectives

By the end of this lesson, you should be able to:

1. **Differentiate Between Unit and Integration Tests:**
   - Understand that unit tests focus on individual functions, while integration tests evaluate the interactions between multiple components.

2. **Implement Common Testing Patterns:**
   - **Mocking:** Replace parts of your system under test with mock objects to isolate the behavior of the function you are testing.
   - **Parameterized Tests:** Write tests that run multiple times with different inputs, improving test coverage.
   - **Fixtures:** Set up necessary preconditions and clean up after tests, ensuring a consistent test environment.

## Resources

### Read or Watch
- **[unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)**
- **[unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)**
- **[How to mock a readonly property with mock?](https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock)**
- **[parameterized](https://pypi.org/project/parameterized/)**
- **[Memoization](https://en.wikipedia.org/wiki/Memoization)**