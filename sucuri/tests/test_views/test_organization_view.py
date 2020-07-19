# Standard Library
from unittest import mock

# pytest
import pytest

from fastapi import HTTPException
from fastapi.testclient import TestClient

# IIB
from sucuri.main import get_app


app = get_app()

client = TestClient(app)


class TestOrganizationView:
    @pytest.fixture
    def organization(self):
        return {
            "name": "Live de Python",
            "about": "lives sobre temas pythônicos",
            "url": "https://www.youtube.com/eduardomendes",
            "social_media": [{"type": "twitter", "value": "@edumendes"}],
            "owner": 1,
            "members": [],
        }

    @pytest.fixture
    def organizations(self):
        return [
            {
                "name": "Live de Python",
                "about": "lives sobre temas pythônicos",
                "url": "https://www.youtube.com/eduardomendes",
                "social_media": [{"type": "twitter", "value": "@edumendes"}],
                "owner": 1,
                "members": [],
            },
            {
                "name": "Foo",
                "about": "aulas de foo",
                "url": "https://www.foo.com/",
                "social_media": [{"type": "twitter", "value": "@foo"}],
                "owner": 1,
                "members": [],
            },
            {
                "name": "Bar",
                "about": "lives sobre bar",
                "url": "https://www.bar.com/",
                "social_media": [{"type": "twitter", "value": "@bar"}],
                "owner": 1,
                "members": [],
            },
        ]

    def test_create_organization_should_return_200(self, organization):
        response = client.post("/organizations/", json=organization)
        assert response.status_code == 200
        assert response.json() == organization

    def test_get_organization_should_return_200(self, organization):
        with mock.patch(
            "sucuri.views.organization_view.get_organization"
        ) as mock_get_organization:
            mock_get_organization.return_value = organization
            response = client.get("/organizations/1")
            assert response.status_code == 200
            assert response.json() == organization

    def test_get_organization_should_return_organization_not_found(self):
        with mock.patch(
            "sucuri.views.organization_view.get_organization"
        ) as mock_get_organization:
            mock_get_organization.return_value = None
            response = client.get("/organizations/1")
            assert response.status_code == 404
            assert response.json() == {"detail": "Organization not found"}

    def test_get_organizations_should_return_existent_organizations(
        self, organizations
    ):
        with mock.patch(
            "sucuri.views.organization_view.get_organizations"
        ) as mock_get_organizations:
            mock_get_organizations.return_value = organizations
            response = client.get("/organizations/")
            assert response.status_code == 200
            assert len(response.json()) == 3

    def test_get_organizations_should_return_empty_list(self):
        with mock.patch(
            "sucuri.views.organization_view.get_organizations"
        ) as mock_get_organizations:
            mock_get_organizations.return_value = []
            response = client.get("/organizations/")
            assert response.status_code == 200
            assert len(response.json()) == 0

    def test_delete_organization_should_return_200(self):
        with mock.patch(
            "sucuri.views.organization_view.delete_organization"
        ) as mock_delete_organization:
            mock_delete_organization.return_value = None
            response = client.delete("/organizations/1")
            assert response.status_code == 200

    def test_update_organization_should_return_200(self, organization):
        response = client.put("/organizations/1", json=organization)
        assert response.status_code == 200

    def test_update_organization_should_return_organization_not_found(
        self, organization
    ):
        with mock.patch(
            "sucuri.views.organization_view.get_organization"
        ) as mock_get_organization:
            mock_get_organization.return_value = None
            response = client.put("/organizations/1", json=organization)
            assert response.status_code == 404
            assert response.json() == {"detail": "Organization not found"}
