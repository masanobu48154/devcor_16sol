import sys, requests, urllib3, json

#CSR1kv1 Credentials
URL  = 'https://10.0.0.20:443/'
USER = 'cisco'
PASS = 'cisco'

# Headers required for RESTCONF
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

# Disable warnings
urllib3.disable_warnings()

# Main method
def main():
    ###########################################
    # Retrieve Device Configuration in Python #
    ###########################################
    # URL for API calls
    url_ge1 = URL + 'restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1/ip/address'


    # GET call to CSR1kv1, SSL checking turned off
    response = requests.get(url_ge1, 
                            auth=(USER, PASS),
                            headers=headers, 
                            verify=False)

    # Print the returned JSON
    print(response.text)


    #####################################
    # Update Configuration Using Python #
    #####################################
    # URL for API calls
    url_ge3 = URL + 'restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=3/ip/address/primary/address'

    # New IP address
    ip_address = {"address": "192.168.0.88", "mask": "255.255.255.0"}

    # PUT call to CSR1kv1, SSL checking turned off
    response_change = requests.put(url_ge3, 
                            auth=(USER, PASS),
                            headers=headers, 
                            verify=False,
                            data=json.dumps(ip_address))

    # Print the response's status code
    print(response_change.status_code)

if __name__ == '__main__':
    main()