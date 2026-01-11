Feature: Register New User

  @register
  Scenario: Register New User
    Given I am on the Webpage
    When I Enter all the Valid Details into the Register Page
    And Then I click on Register Button
    Then Register Successful Message will be displayed

  @alreadythere
  Scenario: User already exist
    Given I am on the Webpage
    When I Enter all the Valid Details into the Register Page
    And Then I click on Register Button
    Then User already exist message will be displayed

  @WithoutDetails
  Scenario: Do not enter anything on Registration page and click on register
    Given I am on the Webpage
    When I do not enter any mandatory details on the Registration page
    And Then I click on Register Button
    Then Error Message will be displayed to user

  @WithoutPrivacyPolicy
  Scenario: Registration without clicking privacy policy and any details
    Given I am on the Webpage
    When I do not enter any mandatory details on the Registration page and privacy policy
    And Then I click on Register Button
    Then Privacy Error Message will be displayed to User



