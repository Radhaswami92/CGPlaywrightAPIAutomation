Feature: Order Transaction

  Scenario Outline: Verify the successful creation of order via API endpoint and validate it through UI.

    Given the order is placed successfully via API endpoint with <username> and <password>
    And user lands on login Page
    When user logs in with <username> and <password>
    And navigate to Order History Page
    And user select the order and navigates to order details page
    Then user sucessfully validates the order id in the UI
    Examples:
      | username              | password       |
      | jeet.zaper@gmail.com  | Radhaswami@103 |




