Feature: Login with Credentials


  @completed
  Scenario Outline: Login with Valid Credentials
    Given I am on the Login Page
    When I Enter the Username as "<email>" and Password as "<password>"
    And Clicked on Login Button
    Then Logged In Successfully Message will be displayed
    Examples:
      | email              | password   |
      |test9684@test.com   | test1234   |

  @negative
  Scenario Outline: Login with InValid Credentials
    Given I am on the Login Page
    When I Enter the invalid Username as "<email>" and Invalid Password as "<password>"
    And Clicked on Login Button
    Then Proper Error Message will be displayed
    Examples:
      | email     | password |
      | #56677%   | 78899    |
      | tetedd23  | 333223   |
      | hdjhf     | yfsdfg   |


  @empty
  Scenario: Login without Entering any credentials clicks on login
    Given I am on the Login Page
    When I don't Enter any UserName and Password"
    And Clicked on Login Button
    Then Proper Error Message will be displayed
