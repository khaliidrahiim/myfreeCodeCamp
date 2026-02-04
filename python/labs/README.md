# Build an RPG Character

## Objective
Fulfill the user stories and get all tests to pass.

## User Stories

1. You should have a function named `create_character`
2. The function should accept, in order: character name, strength, intelligence, charisma
3. Character name validation:
   - Not a string → "The character name should be a string."
   - Empty string → "The character should have a name."
   - Longer than 10 characters → "The character name is too long."
   - Contains spaces → "The character name should not contain spaces."
4. Stats validation:
   - Not integers → "All stats should be integers."
   - Less than 1 → "All stats should be no less than 1."
   - More than 4 → "All stats should be no more than 4."
   - Don't sum to 7 → "The character should start with 7 points."
5. If all valid, return formatted string with character name and stats as dots

## Tests

1. You should have a function named `create_character`. ✓
2. Non-string name → "The character name should be a string." 
3. Empty name → "The character should have a name."
4. Name > 10 chars → "The character name is too long."
5. Name ≤ 10 chars should NOT be flagged as too long.
6. Name with space → "The character name should not contain spaces."
7. Non-integer stat → "All stats should be integers."
8. Stat < 1 → "All stats should be no less than 1."
9. Stat > 4 → "All stats should be no more than 4."
10. Stats don't sum to 7 → "The character should start with 7 points."
11. `create_character('ren', 4, 2, 1)` returns:
    ```
    ren
    STR ●●●●○○○○○○
    INT ●●○○○○○○○○
    CHA ●○○○○○○○○○
    ```
12. Valid values output stats correctly.

## Progress
- [x] Test 1: Function exists
- [x] Test 2: String validation
- [x] Test 3: Empty string validation
- [x] Test 4: Length validation
- [x] Test 5: Length validation edge case
- [x] Test 6: Space validation
- [x] Test 7: Integer validation
- [x] Test 8: Stat minimum validation
- [x] Test 9: Stat maximum validation
- [x] Test 10: Sum validation
- [x] Test 11: Output format
- [x] Test 12: Output correctness
