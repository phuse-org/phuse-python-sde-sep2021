import requests


class LibraryClient:
    """
    A simple client that makes accessing the CDISC library easier
    """
    BASE_URL = "https://library.cdisc.org/api"
    def __init__(self, token) -> None:
        # create a session so we don't have to reuse the token
        self._client = requests.Session()
        self._client.headers.update({"api-key": token})
        # use an in memory cache for requests
        self._cache = {}

    def get_link(self, link):
        """
        Follow a link from a header
        """
        key = link.get('href')
        if key not in self._cache:
            results = self._client.get(f"{self.BASE_URL}{link.get('href')}")
            if results.status_code != 200:
                raise ValueError("Unable to get dataset", results.content)
            self._cache[key] = results.json()
        return self._cache[key]

    def get_ig_dataset_by_version(self, version: str, dataset: str):
        """
        Get a named domain by version
        """
        key = f"{version}_{dataset}"
        if key not in self._cache:
            results = self._client.get(f"{self.BASE_URL}/mdr/sdtmig/{version}/datasets/{dataset}")
            if results.status_code != 200:
                raise ValueError("Unable to get dataset", results.content)
            self._cache[key] = results.json()
        return self._cache[key]

    def get_product_tabulation(self):
        """
        Gather the DataTabulation Product Group
        """
        key = "product_tabulation"
        if key not in self._cache:
            results = self._client.get(f"{self.BASE_URL}/mdr/products/DataTabulation")
            if results.status_code != 200:
                raise ValueError("Error getting DataTabulations: ", results.content)
            self._cache[key] = results.json()
        return self._cache[key]

    def get_sdtmig_versions(self):
        """
        Get the set of SDTM Implementation Guides
        """
        key = f"versions_sdtmig"
        if key not in self._cache:
            # note, we can reuse this as applicable, so requesting one gets both
            dt = self.get_product_tabulation()
            self._cache[key] = dt.get('_links').get('sdtmig')            
        return self._cache[key]

    def get_sdtm_versions(self):
        """
        Get the set of SDTM Models
        """
        key = f"versions_sdtm"
        if key not in self._cache:
            # note, we can reuse this as applicable
            dt = self.get_product_tabulation()
            self._cache[key] = dt.get('_links').get('sdtm')            
        return self._cache[key]

    def get_sdtm_ct_package(self, version):
        """
        Get a set CT for SDTM
        """
        key = f"sdtmct_{version}"
        if key not in self._cache:
            # note, we can reuse this as applicable
            results = self._client.get(f"{self.BASE_URL}/mdr/ct/packages/sdtmct-{version}")
            self._cache[key] = results            
        return self._cache[key]
