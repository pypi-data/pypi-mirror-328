"""
DRONE HARMONY REST API Communication Module Python Class created by thau
on 7 SEP 2023 to do all the jobs relating to communication tasks
done with Drone Harmony Server
"""

import json
import random
from urllib.parse import quote

import requests

from pybimscantools import coordinatelist as cl
from pybimscantools import coordinatemodel as cm
from pybimscantools import textcolor


class DroneHarmony:
    """ This class is used to communicate with Drone Harmony Server """
    # The url the needs to be called all the time for REST API
    _base_url = "https://api.droneharmony.com/v1"

    def __init__(self, api_key: str, client_user_id: str) -> None:
        self.api_key = api_key
        self.client_user_id = client_user_id
        self.list = None
        self.coordinate_list = None
        self.coordinate_model = None

    def get_client_user_id(self) -> str:
        """ This function returns a client user id """
        return self.client_user_id

    def get_api_key(self) -> str:
        """ This function returns an API key """
        return self.api_key

    def get_base_url(self) -> str:
        """ This function returns a base url """
        return self._base_url

    def get_auth_token(self) -> (int, str, bool):
        """ This function gets an authorization token from DH Server """
        call_url = self._base_url + "/auth/" + self.client_user_id
        header = {"X-API-KEY": quote(self.api_key)}
        response = requests.get(call_url, headers=header, timeout=5)

        if response.status_code == 200:
            data = response.json()  # Assuming the response contains JSON data
            # if successful, return 1, authToken and ssoLink status(bool) in a tuple
            return (
                1,
                textcolor.colored_text(data["authToken"], "Orange"),
                data["ssoLinkPresent"],
            )
        elif response.status_code == 403:
            # if unsuccessful, return 0 and print out error
            print(
                textcolor.colored_text(
                    f"Forbidden: Bad or missing API Key. Status code: {response.status_code}",
                    "Red",
                )
            )
            return 0
        else:
            # if unsuccessful, return 0 and print out error
            textcolor.colored_text(
                f"Failed to fetch data. Status code: {response.status_code}", "Red"
            )
            return 0

        # After getting an authorization token, you need to do SSO-Link according to
        # DH API documentation. You will need to open ==>
        # https://app.droneharmony.com?at={auth_token}
        # and put the received authToken in the url. DH Web app will ask for a log-in,
        # if your client_user_id provided by you is not registered in DH database.
        # if it is, you will be re-directly to the DH Web app immediately.
        # It returns a tuple of (1, authToken, SSO-Link Status), if successful
        # It returns 0 and prints out error, if unsuccessful

    def prepare_geo_json(self,
                         coordinates: (cl.CoordinateList,
                                       cm.CoordinateModel),
                         site_name: str = "site_name",
                         color: str = "Gold",
                         scene_name: str = "scene_name") -> dict:
        """ This function prepares a json_dict for posting a site or a model """

        def return_geo_json(coordinates: cl.CoordinateList) -> list:
            """ This function returns a geo_json """
            self.list = coordinates
            num_coordinate = self.list.len()
            geo_json = []
            for i in range(0, num_coordinate):
                geo_json.append(
                    [
                        self.list.get_coordinate(i)[0],
                        self.list.get_coordinate(i)[1],
                    ]
                )
            return geo_json

        color_model = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        colors = {
            "Sky": 0,
            "Baby Blue": 1,
            "Carolina Blue": 2,
            "Dark Magenta": 3,
            "Parmesan": 4,
            "Fern": 5,
            "Jungle Green": 6,
            "Viridian": 7,
            "Canary Yellow": 8,
            "Gold": 9,
            "Dark Orange": 10,
            "Vivid Orange": 11,
        }
        if color not in colors:
            color = 9
        else:
            color = colors[color]

        if isinstance(coordinates, cl.CoordinateList):
            self.coordinate_list = cl.CoordinateList()
            self.coordinate_list = coordinates
            geo_json = [return_geo_json(self.coordinate_list)]
            json_dict = {
                "siteName": site_name + "_(API_Call)",
                "siteTags": ["Uploaded by REST API"],
                "scene": {
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "type": "Feature",
                            "properties": {
                                "color": color,
                                "name": scene_name,
                                "height": self.coordinate_list.get_height(),
                            },
                            "geometry": {"type": "Polygon", "coordinates": geo_json},
                        }
                    ],
                },
                "geoFences": {"type": "FeatureCollection", "features": []},
                "noFlyZones": {"type": "FeatureCollection", "features": []},
                "missions": [],
            }
            return json_dict
        elif isinstance(coordinates, cm.CoordinateModel):
            self.coordinate_model = cm.CoordinateModel()
            self.coordinate_model = coordinates
            num_model = self.coordinate_model.len()
            nested_features = []
            for i in range(0, num_model):
                nested_features.append(
                    {
                        "type": "Feature",
                        "properties": {
                            "color": color_model[int(random.uniform(0, 11))],
                            "name": scene_name + "_" + str(i),
                            "height": self.coordinate_model.get_height_coordinate_list_i(i),
                        },
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [return_geo_json(
                                self.coordinate_model.get_coordinate_list(i)
                            )
                            ],
                        },
                    }
                )
            json_dict = {
                "siteName": site_name + "_(API_Call)",
                "siteTags": ["Uploaded by REST API"],
                "scene": {
                    "type": "FeatureCollection",
                    "features": nested_features,
                },
                "geoFences": {"type": "FeatureCollection", "features": []},
                "noFlyZones": {"type": "FeatureCollection", "features": []},
                "missions": [],
            }
            return json_dict
        else:
            raise ValueError(
                "DroneHarmony.prepare_geo_json(): "
                "coordinates must be of type either CoordinateList or CoordinateModel"
            )

        # This function takes a CoordinateList or a CoordinateModel object and return a json_dict,
        # which is used to post a site or a model

    def read_all_site(self) -> tuple:
        """ This function reads all sites in the account """
        call_url = self._base_url + "/site/" + self.client_user_id
        header = {"X-API-KEY": quote(self.api_key)}
        response = requests.get(call_url, headers=header, timeout=5)

        if response.status_code == 200:
            ret_json = response.json()  # Assuming the response contains JSON data
            num_of_site = len(ret_json)  # How many sites are there in the project
            # iterate through the list and map the siteName and siteId
            if num_of_site != 0:
                list_of_dict = []
                for i, element in enumerate(ret_json):
                    site_dict = {
                        "siteName": element["siteName"],
                        "siteId": element["siteId"],
                    }
                    list_of_dict.append(site_dict)
                return 1, num_of_site, list_of_dict
            else:
                print("There is no site available in the project")
                return 1
        elif response.status_code == 400:
            # if unsuccessful, return 0 and print out error
            print(
                textcolor.colored_text(
                    "Bad request: SSO-link is not present for the user "
                    "or the user has manually removed "
                    f"the SSO-link. Status code: {response.status_code}",
                    "Red",
                )
            )
            return 0
        elif response.status_code == 403:
            # if unsuccessful, return 0 and print out error
            print(
                textcolor.colored_text(
                    f"Forbidden: Bad or missing API Key. Status code: {response.status_code}",
                    "Red",
                )
            )
            return 0
        elif response.status_code == 404:
            # if unsuccessful, return 0 and print out error
            print(
                textcolor.colored_text(
                    "Site not found: Site id provided was not found. User could have deleted"
                    "the site manually or it was never present. "
                    f"Status code: {response.status_code}",
                    "Red",
                )
            )
            return 0
        else:
            # if unsuccessful, return 0 and print out error
            print(
                textcolor.colored_text(
                    f"Failed to fetch data. Status code: {response.status_code}", "Red"
                )
            )
            return 0

        # This function reads all sites in the account
        # (Remember: all sites are stored in the Site Storage on the
        # left pane of the DH Web app) On the right pane of the
        # DH Web app is the site(s) that is being
        # current worked on.
        # It returns a tuple of (1, No. of sites, siteName & siteId (List of dict.), if successful
        # It returns 0 and prints out error, if unsuccessful

    def read_site(self, site_id: int) -> tuple:
        """ This function reads site specified in the argument (site_id) """
        call_url = self._base_url + "/site/" + self.client_user_id + "/" + site_id
        header = {"X-API-KEY": quote(self.api_key)}
        response = requests.get(call_url, headers=header, timeout=5)

        if response.status_code == 200:
            ret_json = response.json()  # Assuming the response contains JSON data
            # Reading scene
            scene = ret_json["scene"]["features"]  # An array
            no_of_scene = len(scene)
            list_of_dict_scene = []
            for i in range(0, no_of_scene):
                scene_dict = {
                    "name": scene[i]["properties"]["name"],
                    "guid": scene[i]["properties"]["guid"],
                }
                list_of_dict_scene.append(scene_dict)

            # Reading mission
            mission = ret_json["missions"]  # An array
            no_of_mission = len(mission)
            list_of_dict_mission = []
            for i in range(0, no_of_mission):
                mission_dict = {
                    "name": mission[i]["features"][0]["properties"]["missionName"],
                    "guid": mission[i]["features"][0]["properties"]["guid"],
                }
                list_of_dict_mission.append(mission_dict)
            return 1, no_of_scene, no_of_mission, list_of_dict_scene, list_of_dict_mission
        elif response.status_code == 400:
            # if unsuccessful, return 0 and print out error
            print(
                textcolor.colored_text(
                    "Bad request: SSO-link is not present for the user "
                    "or the user has manually removed "
                    f"the SSO-link. Status code: {response.status_code}",
                    "Red",
                )
            )
            return 0
        elif response.status_code == 403:
            # if unsuccessful, return 0 and print out error
            textcolor.colored_text(
                f"Forbidden: Bad or missing API Key. Status code: {response.status_code}",
                "Red",
            )
            return 0
        elif response.status_code == 404:
            # if unsuccessful, return 0 and print out error
            print(
                textcolor.colored_text(
                    "Site not found: Site id provided was not found. "
                    "User could have deleted"
                    "the site manually or it was never present. "
                    "Status code: {response.status_code}",
                    "Red",
                )
            )
            return 0
        else:
            # if unsuccessful, return 0 and print out error
            print(
                textcolor.colored_text(
                    f"Failed to fetch data. Status code: {response.status_code}", "Red"
                )
            )
            return 0

        # This function reads site specified in the argument (site_id)
        # It returns a tuple of (1, No. of scene, No. of mission,
        # [Names of scene], [Names of mission]), if successful
        # It returns 0 and prints out error, if unsuccessful

    def read_through(self) -> tuple:
        """ This function reads all sites in the account """
        print(
            textcolor.colored_text(
                "READING SITE(S) FROM DRONE HARMONY WEB APP", "Yellow"
            )
        )
        response = self.get_auth_token()
        if response[0] == 1:  # check if the call was successful
            if response[2]:  # check if the SSO-Link is present or not?
                sites = self.read_all_site()
                if sites[0]:  # when request is successful
                    for i in range(0, sites[1]):
                        print(
                            textcolor.colored_text(
                                f"{i + 1}. {sites[2][i]['siteName']}", "Pale"
                            )
                        )
                        current_site_id = sites[2][i]["siteId"]
                        scene_mission = self.read_site(current_site_id)
                        if scene_mission[0]:
                            for j in range(0, scene_mission[1]):
                                scene = scene_mission[3][j]["name"]
                                print(
                                    textcolor.colored_text(
                                        f"\t->Scene<- {scene}", "Pale"
                                    )
                                )
                            for k in range(0, scene_mission[2]):
                                mission = scene_mission[4][k]["name"]
                                print(
                                    textcolor.colored_text(
                                        f"\t->Mission<- {mission}", "Pale"
                                    )
                                )
                return sites
            else:
                print(
                    textcolor.colored_text(
                        "The SSO-Link is not registered. Remember to register it!",
                        "Red",
                    )
                    + "\n"
                    + textcolor.colored_text(
                        "Go to the browser and run this url", "Blue"
                    )
                    + "\n"
                    + "https://app.droneharmony.com?at="
                    + textcolor.colored_text(response[1], "Violet")
                )
        else:
            print(f"{response[1]}")

        # This function reads all sites in the account.

    def post_site(self, geo_json: dict) -> tuple:
        """ This function posts a site to DH Web App """
        print(
            textcolor.colored_text("POSTING A SITE TO DRONE HARMONY WEB APP", "Yellow")
        )
        body = json.dumps(geo_json)

        call_url = self._base_url + "/site/" + self.client_user_id
        header = {
            "Content-Type": "application/json",
            "X-API-KEY": quote(self.api_key),
        }

        response = requests.post(call_url, headers=header, data=body, timeout=5)
        if response.status_code == 200:
            data = response.json()  # Assuming the response contains JSON data
            # if successful, return 1 and print out success
            print(textcolor.colored_text("The site has been posted", "Green"))
            return 1, data
        elif response.status_code == 400:
            # if unsuccessful, return 0 and print error
            textcolor.colored_text(
                f"Bad request. Status code: {response.status_code}", "Red"
            )
            return 0
        elif response.status_code == 403:
            # if unsuccessful, return 0 and print error
            print(
                textcolor.colored_text(
                    f"Forbidden: Bad or missing API Key. Status code: {response.status_code}",
                    "Red",
                )
            )
            return 0
        elif response.status_code == 500:
            # if unsuccessful, return 0 and print error
            print(
                textcolor.colored_text(
                    f"Internal server error. Status code: {response.status_code}",
                    "Red",
                )
            )
            return 0
        else:
            # if unsuccessful, return 0 and print error
            print(
                textcolor.colored_text(
                    f"Failed to fetch data. Status code: {response.status_code}",
                    "Red",
                )
            )
            return 0

        # In the argument, 8 arguments are needed(siteName, color, "
        # sceneName, height, geo_json, Based_url,
        # Client_user_id, API_Key) to define
        # a polygon
        # This function takes the arguments and put them into a proper place in
        # a body of a REST API call with application/json content-type
        # it returns a tuple of (1, returned MSG from the server), if successful,
        # returns 0 and prints out error, if unsuccessful and
        # returns 0 and prints out eeror, when arguments passed in not correct.

    def delete_site(self, site_id: str) -> tuple:
        """ This function deletes a site specified in the argument (site_id) """
        call_url = self._base_url + "/site/" + self.client_user_id + "/" + site_id
        header = {"X-API-KEY": quote(self.api_key)}
        response = requests.delete(call_url, headers=header, timeout=5)

        if response.status_code == 200:
            data = response.content  # Assuming the response contains JSON data
            # if successful, return 1 and status code in a tuple and print out success
            print(
                textcolor.colored_text(
                    "The site has been deleted successfully", "Green"
                )
            )
            return 1, data
        elif response.status_code == 400:
            # if unsuccessful, return 0 and print out error
            print(
                textcolor.colored_text(
                    "Bad request: SSO-link is not present for the user or "
                    "the user has manually removed "
                    f"the SSO-link. Status code: {response.status_code}",
                    "Red",
                )
            )
            return 0
        elif response.status_code == 403:
            # if unsuccessful, return 0 and print out error
            print(
                textcolor.colored_text(
                    f"Forbidden: Bad or missing API Key. Status code: {response.status_code}",
                    "Red",
                )
            )
            return 0
        elif response.status_code == 404:
            # if unsuccessful, return 0 and print out error
            print(
                textcolor.colored_text(
                    "Site not found: Site id provided was not found. User could have deleted"
                    "the site manually or it was never present. "
                    f"Status code: {response.status_code}",
                    "Red",
                )
            )
            return 0
        else:
            # if unsuccessful, return 0 and print out error
            print(
                textcolor.colored_text(
                    f"Failed to fetch data. Status code: {response.status_code}", "Red"
                )
            )
            return 0

        # This function deletes a site specified in the argument (site_id)
        # It returns a tuple of (1, MSG), if successful
        # It returns 0 and prints out error, if unsuccessful

    def share_site(self, site_id: str, client_user_id_for_share: str) -> tuple:
        """ This function shares the site to the users who are defined on the list. """
        call_url = (
                self._base_url + "/site/" + self.client_user_id + "/" + site_id + "/share"
        )
        header = {
            "X-API-KEY": quote(self.api_key),
            "sharedUsers": client_user_id_for_share,
        }
        response = requests.post(call_url, headers=header, timeout=5)

        if response.status_code == 200:
            data = response.content  # Assuming the response contains JSON data
            # if successful, return 1 and status code in a tuple and print out success
            print(
                textcolor.colored_text(
                    "The site has been shared to a given list of users", "Green"
                )
            )
            return 1, data
        elif response.status_code == 400:
            # if unsuccessful, return 0 and print out error
            print(
                textcolor.colored_text(
                    "Bad request: SSO-link is not present for the user or "
                    "the user has manually removed "
                    f"the SSO-link. Status code: {response.status_code}",
                    "Red",
                )
            )
            return 0
        elif response.status_code == 403:
            # if unsuccessful, return 0 and print out error
            print(
                textcolor.colored_text(
                    f"Forbidden: Bad or missing API Key. Status code: {response.status_code}",
                    "Red",
                )
            )
            return 0
        elif response.status_code == 404:
            # if unsuccessful, return 0 and print out error
            print(
                textcolor.colored_text(
                    "Site not found: Site id provided was not found. User could have deleted"
                    "the site manually or it was never present. "
                    f"Status code: {response.status_code}",
                    "Red",
                )
            )
            return 0
        else:
            # if unsuccessful, return 0 and print out error
            print(
                textcolor.colored_text(
                    f"Failed to fetch data. Status code: {response.status_code}", "Red"
                )
            )
            return 0

        # This function shares the site to the users who are defined on the list.
        # It returns a tuple of (1, response from the server), if successful
        # It returns 0 and prints out error, if unsuccessful

    def delete(self) -> None:
        """ A wrap-up function that deletes a site from DH Web App """
        sites = self.read_through()
        print(
            textcolor.colored_text(
                "DELETING A SITE FROM DRONE HARMONY WEB APP", "Yellow"
            )
        )
        print(
            textcolor.colored_text(
                "Which site do you want to delete?\n"
                "Please provide the number in front of the desired site:",
                "Orange",
            )
        )
        feedback = input()
        if (
                feedback.isdigit() and 0 <= int(feedback) <= sites[1]
        ):  # if the feedback is a number and in the range
            # Deleting
            feedback = int(feedback)
            del_result = self.delete_site(sites[2][feedback - 1]["siteId"])
            if del_result[0]:
                print(del_result[1])
                print("The updated site(s) in DH Web App is: ")
                self.read_through()
            else:
                print(del_result[1])
        else:
            print(
                textcolor.colored_text(
                    "The provided number is not in the range.", "Red"
                )
            )

    def share(self) -> None:
        """ A wrap-up function that shares a site to other users """
        sites = self.read_through()
        print(textcolor.colored_text("SHARING A SITE TO OTHER USERS", "Yellow"))
        print(
            textcolor.colored_text(
                "Which site do you want to share with others?\n"
                "Please provide the number in front of the desired site:",
                "Orange",
            )
        )
        shared_site = input()
        if (
                shared_site.isdigit() and 0 <= int(shared_site) <= sites[1]
        ):  # if the shared_site is a number and in the range
            # asking for client_user_id to share with
            print(
                textcolor.colored_text(
                    "Please specify a list of users that the site will be shared to!",
                    "Orange",
                )
            )
            shared_users = input()
            if len(shared_users) >= 0:
                shared_site = int(shared_site)
                share_result = self.share_site(
                    sites[2][shared_site - 1]["siteId"], shared_users
                )
                if share_result[0]:
                    print(share_result[1])
                    print(
                        textcolor.colored_text(
                            "The site has been shared to this/these user(s)", "Violet"
                        )
                    )
                    print(share_result[2])
                else:
                    print(share_result[1])
            else:
                print(
                    textcolor.colored_text(
                        "The inputted client user id might not be in a list", "Red"
                    )
                )
        else:
            print(
                textcolor.colored_text(
                    "The provided number is not in the range.", "Red"
                )
            )

    ### Quick Test of Something
    # string = "{'siteId': 'd55593f2-7668-45d4-9d2e-b29059407e44', 'siteName': 'ZHAW', 'siteTags': [], 'lastModified': 1692259540020, 'scene': {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'properties': {'aslHeight': None, 'color': 0, 'name': 'ZHAW_TL_Building', 'guid': 'e5fd0c3f-cf5f-4a5a-b8c4-f6810d72de45', 'height': 20.0}, 'geometry': {'type': 'Polygon', 'coordinates': [[[8.730205965784664, 47.49680879160657], [8.730295819786663, 47.4963512130808], [8.730726314333554, 47.496387457069844], [8.730635119227047, 47.49684956573715], [8.730205965784664, 47.49680879160657]]]}}, {'type': 'Feature', 'properties': {'aslHeight': None, 'color': 0, 'name': 'ZHAW_TB_Building', 'guid': '28e08b41-c170-4e92-9f95-0f4040c2df83', 'height': 30.0}, 'geometry': {'type': 'Polygon', 'coordinates': [[[8.728986108968106, 47.4969456761269], [8.729858697043582, 47.49702072727733], [8.729895402109248, 47.49684981087637], [8.729021672522647, 47.49676871563034], [8.728986108968106, 47.4969456761269]]]}}, {'type': 'Feature', 'properties': {'aslHeight': None, 'color': 0, 'name': 'ZHAW_Mensa_Building', 'guid': '04ec61b5-9053-4054-aed9-a1e6f467471f', 'height': 10.0}, 'geometry': {'type': 'Polygon', 'coordinates': [[[8.72949262579275, 47.49676566503206], [8.729907697637804, 47.49679964350434], [8.7299338491757, 47.49668456965608], [8.729517436226137, 47.496646513682265], [8.72949262579275, 47.49676566503206]]]}}]}, 'geoFences': {'type': 'FeatureCollection', 'features': []}, 'noFlyZones': {'type': 'FeatureCollection', 'features': []}, 'missions': [{'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'properties': {'missionName': 'TL_Side_Scan', 'guid': '508e94d0-c5bf-4334-ba3c-99d3089f69fa'}, 'geometry': {'type': 'LineString', 'coordinates': [[8.73001161690044, 47.49657786230845, 12.5], [8.730004417816497, 47.49674429834298, 12.5], [8.730014697362368, 47.49669195009648, 12.5], [8.73002497690824, 47.49663960184999, 12.5], [8.73003525645411, 47.496587253603494, 12.5], [8.730045535999981, 47.496534905357, 12.5], [8.730045535999981, 47.496534905357, 17.333333333333332], [8.73003525645411, 47.496587253603494, 17.333333333333332], [8.73002497690824, 47.49663960184999, 17.333333333333332], [8.730014697362368, 47.49669195009648, 17.333333333333332], [8.730004417816497, 47.49674429834298, 17.333333333333332], [8.730004417816497, 47.49674429834298, 22.166666666666664], [8.730014697362368, 47.49669195009648, 22.166666666666664], [8.73002497690824, 47.49663960184999, 22.166666666666664], [8.73003525645411, 47.496587253603494, 22.166666666666664], [8.730045535999981, 47.496534905357, 22.166666666666664], [8.730045535999981, 47.496534905357, 27.0], [8.73003525645411, 47.496587253603494, 27.0], [8.73002497690824, 47.49663960184999, 27.0], [8.730014697362368, 47.49669195009648, 27.0], [8.730004417816497, 47.49674429834298, 27.0], [8.73001161690044, 47.49657786230845, 12.5]]}}, {'type': 'Feature', 'properties': {'azimuth': 0.0, 'type': 'liftoff'}, 'geometry': {'type': 'Point', 'coordinates': [8.73001161690044, 47.49657786230845, 12.5]}}, {'type': 'Feature', 'properties': {'azimuth': 99.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.730004417816497, 47.49674429834298, 12.5]}}, {'type': 'Feature', 'properties': {'azimuth': 82.6, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.730014697362368, 47.49669195009648, 12.5]}}, {'type': 'Feature', 'properties': {'azimuth': 82.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.73002497690824, 47.49663960184999, 12.5]}}, {'type': 'Feature', 'properties': {'azimuth': 82.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.73003525645411, 47.496587253603494, 12.5]}}, {'type': 'Feature', 'properties': {'azimuth': 82.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.730045535999981, 47.496534905357, 12.5]}}, {'type': 'Feature', 'properties': {'azimuth': 82.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.730045535999981, 47.496534905357, 17.333333333333332]}}, {'type': 'Feature', 'properties': {'azimuth': 82.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.73003525645411, 47.496587253603494, 17.333333333333332]}}, {'type': 'Feature', 'properties': {'azimuth': 82.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.73002497690824, 47.49663960184999, 17.333333333333332]}}, {'type': 'Feature', 'properties': {'azimuth': 82.6, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.730014697362368, 47.49669195009648, 17.333333333333332]}}, {'type': 'Feature', 'properties': {'azimuth': 99.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.730004417816497, 47.49674429834298, 17.333333333333332]}}, {'type': 'Feature', 'properties': {'azimuth': 99.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.730004417816497, 47.49674429834298, 22.166666666666664]}}, {'type': 'Feature', 'properties': {'azimuth': 82.6, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.730014697362368, 47.49669195009648, 22.166666666666664]}}, {'type': 'Feature', 'properties': {'azimuth': 82.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.73002497690824, 47.49663960184999, 22.166666666666664]}}, {'type': 'Feature', 'properties': {'azimuth': 82.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.73003525645411, 47.496587253603494, 22.166666666666664]}}, {'type': 'Feature', 'properties': {'azimuth': 82.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.730045535999981, 47.496534905357, 22.166666666666664]}}, {'type': 'Feature', 'properties': {'azimuth': 82.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.730045535999981, 47.496534905357, 27.0]}}, {'type': 'Feature', 'properties': {'azimuth': 82.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.73003525645411, 47.496587253603494, 27.0]}}, {'type': 'Feature', 'properties': {'azimuth': 82.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.73002497690824, 47.49663960184999, 27.0]}}, {'type': 'Feature', 'properties': {'azimuth': 82.6, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.730014697362368, 47.49669195009648, 27.0]}}, {'type': 'Feature', 'properties': {'azimuth': 99.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.730004417816497, 47.49674429834298, 27.0]}}, {'type': 'Feature', 'properties': {'azimuth': 0.0, 'type': 'landing'}, 'geometry': {'type': 'Point', 'coordinates': [8.73001161690044, 47.49657786230845, 12.5]}}]}, {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'properties': {'missionName': 'TB_Side_Scan', 'guid': '03580289-5d23-4c97-9158-ae04ae12532d'}, 'geometry': {'type': 'LineString', 'coordinates': [[8.730059675268844, 47.49675246502807, 15.0], [8.729638395317046, 47.496680702976164, 15.0], [8.729713716416274, 47.49668769390696, 15.0], [8.729789037515504, 47.496694684837756, 15.0], [8.729864358614732, 47.49670167576855, 15.0], [8.729939585424567, 47.496709060713265, 15.0], [8.729939585424567, 47.496709060713265, 20.0], [8.729864358614732, 47.49670167576855, 20.0], [8.729789037515504, 47.496694684837756, 20.0], [8.729713716416274, 47.49668769390696, 20.0], [8.729638395317046, 47.496680702976164, 20.0], [8.729638395317046, 47.496680702976164, 25.0], [8.729713716416274, 47.49668769390696, 25.0], [8.729789037515504, 47.496694684837756, 25.0], [8.729864358614732, 47.49670167576855, 25.0], [8.729939585424567, 47.496709060713265, 25.0], [8.729939585424567, 47.496709060713265, 30.0], [8.729864358614732, 47.49670167576855, 30.0], [8.729789037515504, 47.496694684837756, 30.0], [8.729713716416274, 47.49668769390696, 30.0], [8.729638395317046, 47.496680702976164, 30.0], [8.729638395317046, 47.496680702976164, 35.0], [8.729713716416274, 47.49668769390696, 35.0], [8.729789037515504, 47.496694684837756, 35.0], [8.729864358614732, 47.49670167576855, 35.0], [8.729939585424567, 47.496709060713265, 35.0], [8.730059675268844, 47.49675246502807, 15.0]]}}, {'type': 'Feature', 'properties': {'azimuth': 0.0, 'type': 'liftoff'}, 'geometry': {'type': 'Point', 'coordinates': [8.730059675268844, 47.49675246502807, 15.0]}}, {'type': 'Feature', 'properties': {'azimuth': 352.2, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729638395317046, 47.496680702976164, 15.0]}}, {'type': 'Feature', 'properties': {'azimuth': 352.2, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729713716416274, 47.49668769390696, 15.0]}}, {'type': 'Feature', 'properties': {'azimuth': 350.3, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729789037515504, 47.496694684837756, 15.0]}}, {'type': 'Feature', 'properties': {'azimuth': 333.5, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729864358614732, 47.49670167576855, 15.0]}}, {'type': 'Feature', 'properties': {'azimuth': 315.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729939585424567, 47.496709060713265, 15.0]}}, {'type': 'Feature', 'properties': {'azimuth': 315.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729939585424567, 47.496709060713265, 20.0]}}, {'type': 'Feature', 'properties': {'azimuth': 333.5, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729864358614732, 47.49670167576855, 20.0]}}, {'type': 'Feature', 'properties': {'azimuth': 350.3, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729789037515504, 47.496694684837756, 20.0]}}, {'type': 'Feature', 'properties': {'azimuth': 352.2, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729713716416274, 47.49668769390696, 20.0]}}, {'type': 'Feature', 'properties': {'azimuth': 352.2, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729638395317046, 47.496680702976164, 20.0]}}, {'type': 'Feature', 'properties': {'azimuth': 352.2, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729638395317046, 47.496680702976164, 25.0]}}, {'type': 'Feature', 'properties': {'azimuth': 352.2, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729713716416274, 47.49668769390696, 25.0]}}, {'type': 'Feature', 'properties': {'azimuth': 350.3, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729789037515504, 47.496694684837756, 25.0]}}, {'type': 'Feature', 'properties': {'azimuth': 333.5, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729864358614732, 47.49670167576855, 25.0]}}, {'type': 'Feature', 'properties': {'azimuth': 315.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729939585424567, 47.496709060713265, 25.0]}}, {'type': 'Feature', 'properties': {'azimuth': 315.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729939585424567, 47.496709060713265, 30.0]}}, {'type': 'Feature', 'properties': {'azimuth': 333.5, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729864358614732, 47.49670167576855, 30.0]}}, {'type': 'Feature', 'properties': {'azimuth': 350.3, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729789037515504, 47.496694684837756, 30.0]}}, {'type': 'Feature', 'properties': {'azimuth': 352.2, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729713716416274, 47.49668769390696, 30.0]}}, {'type': 'Feature', 'properties': {'azimuth': 352.2, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729638395317046, 47.496680702976164, 30.0]}}, {'type': 'Feature', 'properties': {'azimuth': 352.2, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729638395317046, 47.496680702976164, 35.0]}}, {'type': 'Feature', 'properties': {'azimuth': 352.2, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729713716416274, 47.49668769390696, 35.0]}}, {'type': 'Feature', 'properties': {'azimuth': 350.3, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729789037515504, 47.496694684837756, 35.0]}}, {'type': 'Feature', 'properties': {'azimuth': 333.5, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729864358614732, 47.49670167576855, 35.0]}}, {'type': 'Feature', 'properties': {'azimuth': 315.4, 'type': 'regular'}, 'geometry': {'type': 'Point', 'coordinates': [8.729939585424567, 47.496709060713265, 35.0]}}, {'type': 'Feature', 'properties': {'azimuth': 0.0, 'type': 'landing'}, 'geometry': {'type': 'Point', 'coordinates': [8.730059675268844, 47.49675246502807, 15.0]}}]}]}"
    # string2 = "{'siteId': '0c75a716-1942-46c0-a5ea-a0946cda0cc5', 'siteName': 'Stadium', 'siteTags': ['Stadium in Winterthur'], 'lastModified': 1692197862467, 'scene': {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'properties': {'aslHeight': None, 'color': 0, 'name': 'Stadium_stand', 'guid': 'cb78a07a-8a17-46d6-9255-83d3a633779c', 'height': 0.0}, 'geometry': {'type': 'Polygon', 'coordinates': [[[8.746697844257042, 47.49610108339875], [8.746822566976235, 47.49599416297598], [8.745619596233055, 47.4953707582098], [8.745505602349922, 47.49546680651946], [8.746418894519493, 47.49593345382551], [8.746405574341933, 47.495946847688735], [8.746697844257042, 47.49610108339875]]]}}]}, 'geoFences': {'type': 'FeatureCollection', 'features': []}, 'noFlyZones': {'type': 'FeatureCollection', 'features': []}, 'missions': []}"
    # new_string = string.replace("'", "\"")
    # new_string2 = string2.replace("'", "\"")
    # new_new_string = new_string.replace("None", "null")
    # print(new_new_string)
