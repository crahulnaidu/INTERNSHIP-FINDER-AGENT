import os
import sys

# Add root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from pydantic import ValidationError
from schemas.profile import UserProfile, WorkLocationPreference
from schemas.listing import InternshipListing, ApplicationStatus


def test_user_profile_creation():
    profile_data = {
        "full_name": "Jane Doe",
        "email": "jane@example.com",
        "location": "San Francisco, CA",
        "target_roles": ["Backend Intern"],
        "technical_skills": ["Python", "SQL"],
        "github_url": "https://github.com/janedoe",
        "work_preference": WorkLocationPreference.REMOTE
    }
    profile = UserProfile(**profile_data)
    assert profile.full_name == "Jane Doe"
    assert profile.work_preference == "remote"


def test_user_profile_invalid_email():
    profile_data = {
        "full_name": "Jane Doe",
        "email": "invalid-email-string",
        "location": "San Francisco, CA",
        "target_roles": ["Backend Intern"],
        "technical_skills": ["Python"]
    }
    with pytest.raises(ValidationError):
        UserProfile(**profile_data)


def test_internship_listing_defaults():
    listing_data = {
        "canonical_url": "https://boards.greenhouse.io/company/jobs/12345",
        "source_platform": "Greenhouse",
        "title": "Software Engineer Intern",
        "company_name": "Tech Corp",
        "location": "Remote",
        "raw_description": "We are looking for a Python intern..."
    }
    listing = InternshipListing(**listing_data)
    assert listing.status == ApplicationStatus.DISCOVERED
    assert str(listing.canonical_url) == "https://boards.greenhouse.io/company/jobs/12345"