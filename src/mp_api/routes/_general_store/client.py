from typing import Dict

from mp_api.core.client import BaseRester
from mp_api.routes._general_store.models import GeneralStoreDoc


class GeneralStoreRester(BaseRester[GeneralStoreDoc]):  # pragma: no cover

    suffix = "_general_store"
    document_model = GeneralStoreDoc  # type: ignore
    primary_key = "submission_id"
    monty_decode = False
    use_document_model = False

    def set_user_settings(
        self, kind: str, markdown: str, meta: Dict
    ):  # pragma: no cover
        """
        Set general store data.
        Args:
            kind: Data type description
            markdown: Markdown data
            meta: Metadata
        Returns:
            Dictionary with written data and submission id.
        Raises:
            MPRestError
        """
        return self._post_resource(
            body=meta, params={"kind": kind, "markdown": markdown}
        ).get("data")

    def get_data(self, kind):  # pragma: no cover
        """
        Get general store data.
        Args:
            kind: Data type description
        Returns:
            List of dictionaries with kind, markdown, metadata, and submission_id.
        Raises:
            MPRestError
        """
        return self.search(kind=kind)
