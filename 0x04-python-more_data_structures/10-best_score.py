#!/usr/bin/python3
def best_score(a_dictionary):
    return (
            None if not a_dictionary
            else max(a_dictionary, key=lambda key: a_dictionary[key])
            )
