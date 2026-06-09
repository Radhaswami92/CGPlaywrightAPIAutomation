Feature: Login Practise Page Flow

  Scenario: Verify successful login on practice login page and navigation to shop page

    Given user navigates to login practice page
    When user enters username as 'rahulshettyacademy' and password as 'Learning@830$3mK2'
    And user selects the user checkbox
    And user selects admin from dropdown
    And user selects the confirmation checkbox
    And user clicks the Sign In button
    Then user should be navigated to the shop page
    And user should verify that iPhoneX is displayed on the shop page

