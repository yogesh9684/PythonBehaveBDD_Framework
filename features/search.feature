Feature: Search Functionality

  @completed1
  Scenario: Search the Valid Product
    Given I am on the WebPage
    When User enters the Valid Product on Search Bar
    And User clicks on Search button
    Then Application Displays the Product Matching the Search Criteria

  @completed2
  Scenario: Search the InValid Product
    Given I am on the WebPage
    When User enters the InValid Product on Search Bar
    And User clicks on Search button
    Then Application Displays the Error Message Search Not found

  @completed3
  Scenario: Do not Enter Anything on Search Bar and click on search
    Given I am on the WebPage
    When User do not enter anything on search bar
    And User clicks on Search button
    Then Application Displays the Error Message Search Not found




