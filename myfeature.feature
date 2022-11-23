Feature: add new collection
  Scenario Outline:  user successfully creates new collection
    Given I launch chrome browser
    And I am logged in to my metabase account
    When I click on personal collection option
    Then personal collection page opens up
    When I click on create new button
    Then new dashboard creation box is displayed
    When I enter dashboard name "<name>"
    And enter description "<description>"
    Then create button is "<enable>" enabled
    And click on create button
    Then new collection page with given name is created
    Examples:
      | name       | description                           | enable |
      | "NewDemo"  | "this is scenario outline description"| yes    |