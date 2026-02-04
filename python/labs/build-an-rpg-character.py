full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intelligence, charisma):
    # Check if character_name is NOT a string
    if not isinstance(character_name, str):
        return 'The character name should be a string'
    # Check if character_name is an empty string
    if character_name == '':
        return 'The character should have a name'
    # Check if character_name is longer than 10 characters
    if len(character_name) > 10:
        return 'The character name is too long'
    # Check if character_name contains a space
    if ' ' in character_name:
        return 'The character name should not contain spaces'
    # Check if strength, intelligence, and charisma are integers
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int) or isinstance(strength, bool) or isinstance(intelligence, bool) or isinstance(charisma, bool):
        return 'All stats should be integers'
    # Check if strength, intelligence, and charisma are no less than 1
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    # Check if strength, intelligence, and charisma are no greater than 4
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    # Check if all stats add up to 7
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    # Return character name and stats
    return f'''{character_name}
STR {full_dot * strength}{empty_dot * (10 - strength)}
INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}
CHA {full_dot * charisma}{empty_dot * (10 - charisma)}'''