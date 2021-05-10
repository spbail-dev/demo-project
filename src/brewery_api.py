import requests
import sys

# Found this API on https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/
# API Documentation: https://www.openbrewerydb.org/documentation/01-listbreweries
BREWERY_API_URL = 'https://api.openbrewerydb.org/breweries?'


# TODO: This only gets the first 20 breweries from the API, would be nice to get the full list (see the API docs)
def get_breweries_by_state(state_name):
    """
    Simple function that takes a state name as an input and returns a list of breweries
    :return: A list of tuples containing brewery names and cities
    """
    state_name.replace(' ', '_')  # the API doesn't allow spaces in state names
    params = {
        'by_state': state_name,
        'per_page': 20
    }
    response = requests.get(BREWERY_API_URL, params=params)
    # TODO: check the response code here to catch an error if there are any problems

    breweries_json = response.json()
    return [(b['name'], b['city']) for b in breweries_json]


def main(args):
    print('\n===== Brewery Finder using openbrewerydb! =====\n')

    if len(args) == 2:  # Making sure the state name is provided and quoted correctly if it contains spaces
        state_name_input = args[1]
    else:
        raise ValueError('Invalid or missing argument: state name')

    # TODO: Make the output nicer by making state names uppercase
    print('Looking up breweries in ' + state_name_input + '...')
    breweries = get_breweries_by_state(state_name_input)

    print(f"Showing the first 20 breweries in {state_name_input}: \n")
    for b in breweries:
        print(b[0] + ', ' + b[1])


if __name__ == "__main__":
    main(sys.argv)
