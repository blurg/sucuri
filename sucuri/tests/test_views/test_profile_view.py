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


def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


class TestProfileView:
    @pytest.fixture
    def profile(self):
        return {
            "name": "Zoey",
            "social_media": [{"type": "instagram", "value": "@zoey"}],
        }

    @pytest.fixture
    def profile_only_name(self):
        return {"name": "Zoey", "social_media": []}

    @pytest.fixture
    def broken_profile(self):
        return {"social_media": [{"type": "instagram", "value": "@zoey"}]}

    @pytest.fixture
    def profiles(self):
        return [
            {"name": "John", "social_media": [{"type": "twitter", "value": "@john"}]},
            {"name": "Paul", "social_media": [{"type": "instagram", "value": "@paul"}]},
            {"name": "Zoey", "social_media": [{"type": "instagram", "value": "@zoey"}]},
            {"name": "Anthony", "social_media": []},
        ]

    def test_create_profile_should_return_200(self, profile):
        response = client.post("/profiles/", json=profile,)
        assert response.status_code == 200
        assert response.json() == profile

    def test_create_profile_should_return_200_without_social_media(
        self, profile_only_name
    ):
        response = client.post("/profiles/", json=profile_only_name)
        assert response.status_code == 200
        assert response.json() == profile_only_name

    def test_create_profile_should_return_422(self, broken_profile):
        response = client.post("/profiles/", json=broken_profile,)
        assert response.status_code == 422

    def test_get_profiles_should_return_existent_profiles(self, profiles):
        with mock.patch("sucuri.views.profile_view.get_profiles") as mock_get_profiles:
            mock_get_profiles.return_value = profiles
            response = client.get("/profiles/")
            assert response.status_code == 200
            assert len(response.json()) == 4

    def test_get_profiles_should_return_empty_list(self):
        with mock.patch("sucuri.views.profile_view.get_profiles") as mock_get_profiles:
            mock_get_profiles.return_value = []
            response = client.get("/profiles/")
            assert response.status_code == 200
            assert len(response.json()) == 0

    def test_get_profile_should_return_200(self, profile):
        with mock.patch("sucuri.views.profile_view.get_profile") as mock_get_profile:
            mock_get_profile.return_value = profile
            response = client.get("/profiles/1")
            assert response.status_code == 200
            assert response.json() == profile

    def test_get_profile_should_return_profile_not_found(self):
        with mock.patch("sucuri.views.profile_view.get_profile") as mock_get_profile:
            mock_get_profile.return_value = None
            response = client.get("/profiles/1")
            assert response.status_code == 404
            assert response.json() == {"detail": "Profile not found"}

    def test_delete_profile_should_return_200(self):
        with mock.patch(
            "sucuri.views.profile_view.delete_profile"
        ) as mock_delete_profile:
            mock_delete_profile.return_value = None
            response = client.delete("/profiles/1")
            assert response.status_code == 200

    def test_update_profile_should_return_200(self, profile):
        response = client.put("/profiles/1", json=profile)
        assert response.status_code == 200

    def test_update_profile_should_return_profile_not_found(self, profile):
        with mock.patch("sucuri.views.profile_view.get_profile") as mock_get_profile:
            mock_get_profile.return_value = None
            response = client.put("/profiles/1", json=profile)
            assert response.status_code == 404
            assert response.json() == {"detail": "Profile not found"}
