# outerport/resources/documents.py
from typing import IO, List, Optional
import requests
from outerport.models.document import Document
from outerport.resources.base_resource import BaseResource


class DocumentsResource(BaseResource):
    def create(self, file: IO[bytes], file_name: Optional[str] = None) -> Document:
        """
        Upload a document and wait synchronously for it to finish processing.
        Returns a fully-populated Document object.

        :param file: The file to upload.
        :param file_name: The name of the file to upload.
        :return: The uploaded Document object.
        """
        url = f"{self.client.base_url}/api/v0/documents"
        headers = self.client._form_headers()

        if not file_name:
            file_name = getattr(file, "name", "uploaded_file")

        files = {"file": (file_name, file, "application/octet-stream")}
        resp = requests.post(url, headers=headers, files=files)
        resp.raise_for_status()

        data = resp.json()  # e.g. { "job_status_id": 1, "document_id": "123", ... }
        job_status_id = data.get("job_status_id")
        document_id = data.get("document_id")
        if not job_status_id or not document_id:
            raise ValueError("Upload response missing job_status_id or document_id.")

        # Wait for job to complete
        self.client.job_statuses.wait_for_completion(job_status_id)

        # Now retrieve the final Document from the server
        return self.retrieve(document_id)

    def list(self) -> List[Document]:
        """
        List all documents as a list of Document objects.

        :return: A list of Document objects.
        """
        url = f"{self.client.base_url}/api/v0/documents"
        headers = self.client._json_headers()
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        raw_list = resp.json()  # e.g. [ { "id": 1, ... }, { ... } ]

        return [Document.from_api(d, self.client) for d in raw_list]

    def retrieve(self, document_id: int) -> Document:
        """
        Retrieve a single Document by ID.

        :param document_id: The ID of the document to retrieve.
        :return: The Document object.
        """
        url = f"{self.client.base_url}/api/v0/documents/{document_id}"
        headers = self.client._json_headers()
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        data = resp.json()
        return Document.from_api(data, self.client)

    def delete(self, document_id: int) -> dict:
        """
        Delete the document from the server.

        :param document_id: The ID of the document to delete.
        :return: A dictionary containing the response from the server.
        """
        url = f"{self.client.base_url}/api/v0/documents/{document_id}"
        headers = self.client._json_headers()
        resp = requests.delete(url, headers=headers)
        resp.raise_for_status()
        return resp.json()

    def update_metadata(
        self,
        document_id: int,
        name: Optional[str] = None,
        folder_id: Optional[int] = None,
        summary: Optional[str] = None,
    ) -> Document:
        """
        Update a document's metadata.

        :param document_id: The ID of the document to update.
        :param name: Optional new name for the document.
        :param folder_id: Optional new folder ID for the document.
        :param summary: Optional new summary for the document.
        :return: The updated Document object.
        """
        url = f"{self.client.base_url}/api/v0/documents/{document_id}"
        headers = self.client._json_headers()

        # Only include non-None values in the payload
        payload = {}
        payload["name"] = name
        payload["folder_id"] = folder_id
        payload["summary"] = summary

        resp = requests.put(url, headers=headers, json=payload)
        resp.raise_for_status()
        data = resp.json()
        return Document.from_api(data, self.client)

    def update_file(
        self, document_id: int, file: IO[bytes], file_name: Optional[str] = None
    ) -> Document:
        """
        Update a document's file content and wait for processing to complete.

        :param document_id: The ID of the document to update.
        :param file: The new file content to upload.
        :param file_name: Optional name for the file.
        :return: The updated Document object.
        """
        url = f"{self.client.base_url}/api/v0/documents/{document_id}/file"
        headers = self.client._form_headers()

        if not file_name:
            file_name = getattr(file, "name", "updated_file")

        files = {"file": (file_name, file, "application/octet-stream")}
        resp = requests.put(url, headers=headers, files=files)
        resp.raise_for_status()

        data = resp.json()
        job_status_id = data.get("job_status_id")
        if not job_status_id:
            raise ValueError("Update response missing job_status_id.")

        # Wait for job to complete
        self.client.job_statuses.wait_for_completion(job_status_id)

        # Now retrieve the final Document from the server
        return self.retrieve(document_id)
