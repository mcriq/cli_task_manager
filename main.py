#!/opt/homebrew/bin/python3
import json

def main():
    with open('./dummy_data.json', 'r') as file:
        data = json.load(file)
    for i in range(len(data['tasks'])):
        print(f"{i + 1}. {data['tasks'][i]['desc']}")

main()