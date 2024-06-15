import base64
from github import Github
from github import InputGitTreeElement

# Replace with your actual GitHub token
access_token = "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"

g = Github(access_token)


repo = g.get_repo('jonbruce2002/git-test')

with open('wstest.py', 'r') as file:
    data = file.read()

repo.create_file('wstest.py', 'upload csv', data, branch='main')
