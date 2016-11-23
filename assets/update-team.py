#!/bin/python
"""
    This is a small script to fetch as much metadata about team members as one can, and then update the team.yml data file
"""
import yaml
team_file = open('_data/team.yml')
team = yaml.load(team_file)
print team
