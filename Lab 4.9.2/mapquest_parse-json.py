import requests

def get_route_info(orig, dest):
    url = f"https://www.mapquestapi.com/directions/v2/route?key=fZadaFOY22VIEEemZcBFfxl5vjSXIPpZ&from={orig}&to={dest}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to retrieve data (status code {response.status_code})")
        return None

def display_trip_summary(json_data, orig, dest):
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print(f"API Status: {json_status} = A successful route call.\n")
        print("=============================================")
        route = json_data["route"]
        print(f"Directions from {orig} to {dest}")
        print(f"Trip Duration:   {route['formattedTime']}")
        print(f"Miles:           {route['distance']}")
        print(f"Fuel Used (Gal): {route['fuelUsed']}")
        print(f"Kilometers:      {str('{:.2f}'.format(route['distance'] * 1.61))}")
        print(f"Fuel Used (Ltr): {str('{:.2f}'.format(route['fuelUsed'] * 3.78))}")
        print("=============================================")
        for each in route["legs"][0]["maneuvers"]:
            print(f"{each['narrative']} ({str('{:.2f}'.format(each['distance'] * 1.61))} km)")
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print(f"Status Code: {json_status}; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print(f"Status Code: {json_status}; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print(f"For Status Code: {json_status}; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")

def main():
    while True:
        orig = input("Starting Location: ").strip()
        if orig.lower() == 'q':
            break
        dest = input("Destination: ").strip()
        json_data = get_route_info(orig, dest)
        if json_data:
            display_trip_summary(json_data, orig, dest)

if __name__ == "__main__":
    main()