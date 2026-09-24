from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl


class WorkLocationPreference(str, Enum):
    REMOTE = "remote"
    HYBRID = "hybrid"
    ON_SITE = "on_site"
    ANY = "any"


class ProjectExperience(BaseModel):
    """Represents a candidate's key project or prior internship experience."""
    title: str = Field(..., description="Project name or job title")
    technologies: List[str] = Field(default_factory=list, description="Tech stack used (e.g., Python, PyTorch)")
    description: str = Field(..., description="Summary of key accomplishments or responsibilities")


class UserProfile(BaseModel):
    """Core user profile containing preferences, skills, and background."""
    full_name: str = Field(..., description="Candidate's full name")
    email: EmailStr = Field(..., description="Contact email address")
    location: str = Field(..., description="Current base location (e.g., 'San Francisco, CA')")
    
    # Career Preferences
    target_roles: List[str] = Field(
        ..., 
        min_length=1, 
        description="Target job titles (e.g., ['Software Engineer Intern', 'AI/ML Intern'])"
    )
    preferred_locations: List[str] = Field(
        default_factory=list, 
        description="Locations open to work in"
    )
    work_preference: WorkLocationPreference = Field(
        default=WorkLocationPreference.ANY,
        description="Remote, Hybrid, On-site, or Any"
    )
    
    # Qualifications
    technical_skills: List[str] = Field(
        ..., 
        min_length=1, 
        description="Core technical competencies (languages, frameworks, tools)"
    )
    soft_skills: List[str] = Field(default_factory=list, description="Key interpersonal or domain skills")
    projects: List[ProjectExperience] = Field(default_factory=list, description="Key projects or work history")
    
    # Portfolio Links
    github_url: Optional[HttpUrl] = Field(None, description="GitHub profile URL")
    linkedin_url: Optional[HttpUrl] = Field(None, description="LinkedIn profile URL")
    portfolio_url: Optional[HttpUrl] = Field(None, description="Personal website or portfolio URL")

    # Agent Constraints
    min_match_threshold: float = Field(
        default=70.0, 
        ge=0.0, 
        le=100.0, 
        description="Minimum match score required to trigger application/drafting agents"
    )

    model_config = ConfigDict(
        use_enum_values=True,
        json_schema_extra={
            "example": {
                "full_name": "Alex Chen",
                "email": "alex.chen@example.com",
                "location": "New York, NY",
                "target_roles": ["Software Engineer Intern", "AI Engineer Intern"],
                "preferred_locations": ["New York, NY", "Remote"],
                "work_preference": "remote",
                "technical_skills": ["Python", "LangChain", "FastAPI", "PostgreSQL", "PyTorch"],
                "soft_skills": ["Problem Solving", "Collaboration"],
                "projects": [
                    {
                        "title": "Agentic AI Search Engine",
                        "technologies": ["Python", "FastAPI", "OpenAI API"],
                        "description": "Built an autonomous research agent using multi-agent DAGs."
                    }
                ],
                "github_url": "https://github.com/alexchen",
                "linkedin_url": "https://linkedin.com/in/alexchen",
                "min_match_threshold": 75.0
            }
        }
    )