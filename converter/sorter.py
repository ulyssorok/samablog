import os
import shutil
import re

base_dir = 'posts'

def format_file_name(original_name):
    name_without_prefix = original_name.replace("Personal — ", "")
    name_split = name_without_prefix.split(" - Sam Altman.pdf")
    return name_split[0] + ", Sam Altman.pdf"

def find_file_path(base_dir, file_name):
    for root, dirs, files in os.walk(base_dir):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

folders = {
    "Foundational_Startup_Advice": [
        "Personal — How To Be Successful - Sam Altman.pdf",
        "Personal — Startup Advice - Sam Altman.pdf",
        "Personal — Startup advice, briefly - Sam Altman.pdf",
        "Personal — The Only Way to Grow Huge - Sam Altman.pdf",
        "Personal — Super successful companies - Sam Altman.pdf",
        "Personal — Successful people - Sam Altman.pdf",
        "Personal — What to do if a bubble is starting - Sam Altman.pdf",
        "Personal — Startups, Role Models, Risk, and Y Combinator - Sam Altman.pdf",
        "Personal — Applying to YC - Sam Altman.pdf",
        "Personal — Employee Equity - Sam Altman.pdf",
        "Personal — Employee Retention - Sam Altman.pdf",
        "Personal — Fundraising Mistakes Founders Make - Sam Altman.pdf",
        "Personal — Party rounds - Sam Altman.pdf",
        "Personal — The separation of advice and money - Sam Altman.pdf",
        "Personal — Unit Economics - Sam Altman.pdf",
        "Personal — Value is created by doing - Sam Altman.pdf",
        "Personal — Productivity - Sam Altman.pdf",
        "Personal — How to hire - Sam Altman.pdf",
    ],
    "Innovation_and_Technology": [
        "Personal — Hard Tech is Back - Sam Altman.pdf",
        "Personal — Technology and wealth inequality - Sam Altman.pdf",
        "Personal — What happened to innovation? - Sam Altman.pdf",
        "Personal — Machine intelligence, part 1 - Sam Altman.pdf",
        "Personal — Machine intelligence, part 2 - Sam Altman.pdf",
        "Personal — The Software Revolution - Sam Altman.pdf",
        "Personal — Technology predictions - Sam Altman.pdf",
        "Personal — US Digital Currency - Sam Altman.pdf",
        "Personal — AI - Sam Altman.pdf",
        "Personal — Bitcoin Price Pressure - Sam Altman.pdf",
        "Personal — Electrons and Atoms - Sam Altman.pdf",
        "Personal — Energy - Sam Altman.pdf",
        "Personal — New RFS -- Breakthrough Technologies - Sam Altman.pdf",
        "Personal — Reinforcement Learning Progress - Sam Altman.pdf",
    ],
    "Business_Strategy_and_Operations": [
        "Personal — A founder-friendly term sheet - Sam Altman.pdf",
        "Personal — The Only Way to Grow Huge - Sam Altman.pdf",
        "Personal — Upside risk - Sam Altman.pdf",
        "Personal — Valuations - Sam Altman.pdf",
        "Personal — Growth and Government - Sam Altman.pdf",
        "Personal — Helion Needs You - Sam Altman.pdf",
        "Personal — Housing in the Bay Area - Sam Altman.pdf",
        "Personal — How things get done - Sam Altman.pdf",
        "Personal — The Post-YC Slump - Sam Altman.pdf",
        "Personal — The Worst Part of YC - Sam Altman.pdf",
    ],
    "Specific_Companies_and_Case_Studies": [
        "Personal — Airbnb and San Francisco - Sam Altman.pdf",
        "Personal — Cruise - Sam Altman.pdf",
        "Personal — FarmLogs - Sam Altman.pdf",
        "Personal — Helion - Sam Altman.pdf",
        "Personal — PG and Jessica - Sam Altman.pdf",
        "Personal — Quora - Sam Altman.pdf",
        "Personal — reddit - Sam Altman.pdf",
        "Personal — Uber vs Car Ownership - Sam Altman.pdf",
    ],
    "Societal_Issues_and_Personal_Thoughts": [
        "Personal — Advice for ambitious 19 year olds - Sam Altman.pdf",
        "Personal — Affordable Care - Sam Altman.pdf",
        "Personal — American Equity - Sam Altman.pdf",
        "Personal — Anonymity - Sam Altman.pdf",
        "Personal — The 2016 Election - Sam Altman.pdf",
        "Personal — The days are long but the decades are short - Sam Altman.pdf",
        "Personal — The Economy - Sam Altman.pdf",
        "Personal — Trump - Sam Altman.pdf",
        "Personal — What I Heard From Trump Supporters - Sam Altman.pdf",
        "Personal — Why Silicon Valley Works - Sam Altman.pdf",
    ],
    "Productivity_and_Personal_Growth": [
        "Personal — The days are long but the decades are short - Sam Altman.pdf",
        "Personal — Productivity - Sam Altman.pdf",
    ],
    "Current_Events_and_Politics": [
        "Personal — The 2016 Election - Sam Altman.pdf",
        "Personal — Housing in the Bay Area - Sam Altman.pdf",
        "Personal — The U.S. Digital Service - Sam Altman.pdf",
        "Personal — The United Slate - Sam Altman.pdf",
        "Personal — The Virus - Sam Altman.pdf",
        "Personal — Trump - Sam Altman.pdf",
    ],
}

for folder_name, file_list in folders.items():
    folder_path = os.path.join(base_dir, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    for file_name in file_list:
        formatted_file_name = format_file_name(file_name)
        source_path = find_file_path(base_dir, file_name)
        destination_path = os.path.join(folder_path, formatted_file_name)
        if source_path:
            shutil.move(source_path, destination_path)
