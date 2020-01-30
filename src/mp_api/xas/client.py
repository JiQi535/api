from typing import List, Optional
from pymatgen import Element
from mp_api.core.client import RESTer
from mp_api.xas.models import Edge


class XASRESTer(RESTer):
    def get_available_elements(
        self,
        edge: Optional[Edge] = None,
        absorbing_element: Optional[Element] = None,
        required_elements: Optional[List[Element]] = None,
    ):

        query_params = []
        if edge:
            query_params.append(f"edge={edge.value}")

        if absorbing_element:
            query_params.append(f"absorbing_element={str(absorbing_element)}")
        if required_elements:
            query_params.append(
                "&".join([f"elements={str(el)}" for el in required_elements])
            )

        query_string = "&".join(query_params)

        url = (
            f"/elements?{query_string}"
            if len(query_string) > 0
            else "/elements"
        )

        data = self._make_request(url)

        return data
