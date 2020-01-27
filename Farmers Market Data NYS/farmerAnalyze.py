import folium
import json
from folium import Popup
import random

'''
Data provided by: https://data.ny.gov/Economic-Development/Farmers-Markets-in-New-York-State/qq4h-8p86
plots farmers markets based on long lat
'''

folium_map = folium.Map(location=[42.721038, -74.259177],
                        zoom_start=5,
                        tiles="CartoDB dark_matter")

with open('./data.json') as json_file:
    data = json.load(json_file)
map_data = data["data"]
column_data = data['meta']['view']['columns']

for i in map_data:

    '''
    8 = county
    9 = Name
    10 = Location
    11 = address
    12 = City
    13 = state
    14 = zipcode
    15 = contact
    16 = phone number
    17 = market Link
    18 = operating hours
    19 = operating season
        '''

    test = folium.Html('<table>\
        <tr>\
            <th>Information</th>\
            <th title="Name of the Farmers’ Market.">'+str(i[9])+'</th>\
        </tr>\
        <tr>\
            <td>County</td>\
            <td title="County the Farmers Market is located in.">'+str(i[8])+'</td>\
        </tr>\
        <tr>\
            <td>Address</td>\
            <td title="1st address line of the physical address for this location.">'+str(i[11])+'</td>\
        </tr>\
        <tr>\
            <td>City</td>\
            <td title="City name of the physical location.">'+str(i[12])+'</td>\
        </tr>\
        <tr>\
            <td>Zip</td>\
            <td title="ZIP code for the physical address for this location.">'+str(i[14])+'</td>\
        </tr>\
        <tr>\
            <td>Contact</td>\
            <td title="Contact person for the Market.">'+str(i[15])+'</td>\
        </tr>\
        <tr>\
            <td>Phone Number</td>\
            <td title="Phone number for this farmer\'s market location.">'+str(i[16])+'</td>\
        </tr>\
            <tr>\
            <td>Website</td>\
            <td title="Website or other link to this market’s online presence."><a href="'+(i[17][0] if i[17] != None else "google.com")+'">'+(str(i[17][0]) if i[17] != None else "None")+'</a></td>\
        </tr>\
            <tr>\
            <td>Operating Hours</td>\
            <td title="Day and Hours the market is open.">'+str(i[18])+'</td>\
        </tr>\
            <tr>\
            <td>Operating Season</td>\
            <td title="Month and day when the market opens and closes for the year.">'+str(i[19])+'</td>\
        </tr>\
    </table>', script=True)
    desc = Popup(test, parse_html=True, max_width=450)
    random_number = random.randint(1118481, 16777215)
    hex_number = str(hex(random_number))
    hex_number = '#' + hex_number[2:]
    marker = folium.CircleMarker(location=[i[25], i[26]], radius=7, tooltip=i[10], popup=desc, color=hex_number,
                                 fill_color='#c4761c')
    marker.add_to(folium_map)

folium_map.save("FarmersMarketNYS.html")
