def are_anagrams(str1, str2):
    # Clean the strings
    cleanedstr1 = str1.lower().replace(" ", "")
    cleanedstr2 = str2.lower().replace(" ", "")
    # Compare the sorted characters
    return sorted(cleanedstr1) == sorted(cleanedstr2)
