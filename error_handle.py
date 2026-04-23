import json
from json import JSONDecodeError


def lead_user_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)

    except FileNotFoundError:
        print(f"Could not load the file {filename}")
        return []

    except JSONDecodeError:
        print(f"The {filename} is corrupted and is not a valid JSON file.")

    except Exception as e:
        print(f"Unexpected error occurred {e}")

    else:
        print(f"Data has been loaded: ")
        print(data)

    finally:
        print("Service Closed.")


my_data = lead_user_data("employees.json")