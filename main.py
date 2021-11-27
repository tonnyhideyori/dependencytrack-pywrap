import requests
from apicomponents.project import DependencyTrackProject
from apicomponents.projectProperty import DependencyTrackProjectProperty
from apicomponents.vulnerability import DependencyTrackVulnerability
from apicomponents.finding import DependencyTrackFinding
from apicomponents.licence import DependencyTrackLicence
from apicomponents.metrics import DependencyTrackMetrics
from apicomponents.acl import DependencyTrackACL

class DependencyTrackAPI(DependencyTrackProject, DependencyTrackProjectProperty, DependencyTrackVulnerability, DependencyTrackFinding, DependencyTrackLicence, DependencyTrackMetrics, DependencyTrackACL):
    def __init__(self, apiurl, apikey):
        self.apiurl = apiurl
        self.apikey = apikey
        self.apicall = self.apiurl + "/api"
        self.session = requests.Session()
        self.session.headers.update({"X-Api-Key": f"{self.apikey}"})

    def version(self):
        response = self.session.get(self.apicall + "/version")
        return response.json()


# TODO: user API

# TODO: violationanalysis API

# TODO: team API

# TODO: service API

# TODO: default API

# TODO: search API

# TODO advance Repository API and put into apicomponents
    def get_repository(self, pageSize=100):
        """Returns a list of all repositories

        Args:
            pageSize (int, optional): [description]. Defaults to 100.

        Returns:
            list : list of repositories
        """
        repository_list = list()
        pageNumber = 1
        response = self.session.get(self.apicall + f"/v1/repository", params={"pageSize": pageSize, "pageNumber": pageNumber})
        for repos in range(0,len(response.json)):
            repository_list.append(response.json()[repos-1])
        while len(response.json()) == pageSize:
            pageNumber += 1
        response = self.session.get(
            self.apicall + f"/v1/repository", params={"pageSize": pageSize, "pageNumber": pageNumber})
        for repos in range(0, len(response.json)):
            repository_list.append(response.json()[repos-1])
        if response.status_code == 200:
            return repository_list
        elif response.status_code == 401:
                return (f"Unauthorized ", response.status_code)
    
# TODO: violation API

# TODO: policy API

# TODO: policyCondition API

# TODO: permission API

# TODO: oidc API

# TODO: licenseGroup API

# TODO: ladp API

# TODO: cwe API

# TODO: component API

# TODO: calculator API

# TODO: bom API

# TODO: badge API

    #TODO improve analysis API and put into apicomponents

    def get_analysis(self, project, component, vulnerability):
        """Retrieves an analysis trail

        Args:
            project (string): The UUID of the project
            component (string): The UUID of the component
            vulnerability (string): The UUID of the vulnerability

        Returns:
            json: 
        """
        response = self.session.get(self.apicall + f"/v1/analysis?project={project}&component={component}&vulnerability={vulnerability}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return (f"Unauthorized ", response.status_code)
        elif response.status_code == 404:
            return (f"The project, component, or vulnerability could not be found ", response.status_code)
        else:
            return response.status_code

