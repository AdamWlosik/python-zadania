
Feature: FizzBuzz game

Scenario: Return "Fizz" when number is divisible by 3
    Given a number is divisible by 3
    When the number is checked with FizzBuzz
    Then it should return "Fizz"

Scenario: Return "Buzz" when number is divisible by 5
    Given a number is divisible by 5
    When the number is checked with FizzBuzz
    Then it should return "Buzz"

Scenario: Return "FizzBuzz" when number is divisible by both 3 and 5
    Given a number is divisible by both 3 and 5
    When the number is checked with FizzBuzz
    Then it should return "FizzBuzz"
