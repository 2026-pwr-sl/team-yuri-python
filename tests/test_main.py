import json
import os
import sys
import tempfile
from pathlib import Path

import pytest

# Add src to path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import team
import utils


@pytest.fixture
def sample_team_data(tmp_path):
    """Create a temporary team_data.json for testing."""
    test_data = [
        {"id": "12345", "name": "cartman"},
        {"id": "12346", "name": "kyle"},
        {"id": "12347", "name": "kenny"},
        {"id": "12348", "name": "stan"},
    ]
    json_file = tmp_path / "team_data.json"
    json_file.write_text(json.dumps(test_data, indent=4))

    # Change to temp directory so utils finds the file
    original_dir = os.getcwd()
    os.chdir(tmp_path)
    yield tmp_path
    os.chdir(original_dir)


def test_count_members(sample_team_data):
    """Test that count_members returns correct number."""
    people = utils.load_team_data()
    assert utils.count_members(people) == 4


def test_load_team_data(sample_team_data):
    """Test that team data loads correctly and creates TeamMember objects."""
    people = utils.load_team_data()
    assert len(people) == 4
    assert people[0].name == "cartman"
    assert people[1].student_id == "12346"
    assert isinstance(people[0], team.TeamMember)


def test_search_member_by_name(sample_team_data, capsys):
    """Test searching for a member by exact name match."""
    people = utils.load_team_data()
    utils.search_member(people, name="kyle")
    captured = capsys.readouterr()
    assert "exact match" in captured.out
    assert "kyle" in captured.out


def test_search_member_by_id(sample_team_data, capsys):
    """Test searching for a member by student ID."""
    people = utils.load_team_data()
    utils.search_member(people, student_id="12345")
    captured = capsys.readouterr()
    assert "exact match" in captured.out
    assert "cartman" in captured.out


def test_search_member_partial_match(sample_team_data, capsys):
    """Test partial name matching."""
    people = utils.load_team_data()
    utils.search_member(people, name="en")
    captured = capsys.readouterr()
    assert "partial match" in captured.out
    assert "kenny" in captured.out


def test_search_member_no_match(sample_team_data, capsys):
    """Test when no member is found."""
    people = utils.load_team_data()
    utils.search_member(people, name="butters")
    captured = capsys.readouterr()
    assert "no match" in captured.out


def test_search_member_missing_params():
    """Test that search_member raises error with no search criteria."""
    people = []
    with pytest.raises(ValueError):
        utils.search_member(people)


def test_add_to_team_data(sample_team_data):
    """Test adding a new member to the team."""
    people = utils.load_team_data()
    new_member = team.TeamMember("butters", "12349")
    updated_people = utils.add_to_team_data(people, new_member)

    assert len(updated_people) == 5
    assert updated_people[-1].name == "butters"

    # Verify it was written to file
    reloaded = utils.load_team_data()
    assert len(reloaded) == 5


def test_team_member_creation():
    """Test TeamMember class initialization."""
    member = team.TeamMember("butters", "12349")
    assert member.name == "butters"
    assert member.student_id == "12349"
