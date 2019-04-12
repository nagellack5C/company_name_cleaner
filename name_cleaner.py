def clean_name(name):
    """
    Given a company name, returns a name cleaned from various endings like Ltd., Corp. etc.
    This can be useful if you want to do an exact comparison of two company names but they are given in different forms
    (e.g. 'Apple' and 'Apple Corp.' - this function will return 'Apple' for both names)

    :param name: corporate name to be cleaned from undesirable endings
    :return: shortest name possible
    """
    with open("endings.txt") as endings_file:
        endings = sorted([ending.replace("\n", "") for ending in endings_file], key=lambda k: len(k), reverse=True)
    variations = set()
    variations.add(name)
    variations_changed = True
    while variations_changed:
        initial_variations_len = len(variations)
        for variation in variations.copy():
            for ending in endings:
                capital_ending = ending[0].upper() + ending[1:]
                capsed_ending = ending.upper()
                all_words_capsed_ending = ""
                if " " in ending:
                    all_words_capsed_ending = " ".join([i[0].upper() + i[1:] for i in ending.split(" ")])
                test_endings = sorted([
                    " " + ending,
                    " " + capsed_ending,
                    " " + capital_ending,
                    " " + all_words_capsed_ending,
                    " " + ending + ".",
                    " " + capsed_ending + ".",
                    " " + capital_ending + ".",
                    " " + all_words_capsed_ending + ".",
                    ", " + ending + ".",
                    ", " + capsed_ending + ".",
                    ", " + capital_ending + ".",
                    ", " + all_words_capsed_ending + ".",
                    ", " + ending,
                    ", " + capsed_ending,
                    ", " + capital_ending,
                    ", " + all_words_capsed_ending,
                    "," + ending,
                    "," + capsed_ending,
                    "," + capital_ending,
                    "," + all_words_capsed_ending
                ], key=lambda k: len(k), reverse=True)
                for test_ending in test_endings:
                    if variation.endswith(test_ending):
                        variations.add(variation[:len(variation) - len(test_ending)])
        if len(variations) == initial_variations_len:
            variations_changed = False
    variations = sorted(list(variations))
    return variations[0]

