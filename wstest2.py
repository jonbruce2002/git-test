import base64
from github import Github, InputGitTreeElement  # Import InputGitTreeElement explicitly

# Replace with your actual GitHub token
access_token = "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"

g = Github(access_token)

repo = g.get_repo('jonbruce2002/git-test')

# Read the content of the file
file_path = 'wstest.py'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Create a new blob
blob = repo.create_git_blob(content, "utf-8")

# Get the branch where you want to update the file
branch = repo.get_branch("main")

# Create a new tree with the updated file
element = InputGitTreeElement(file_path, '100644', 'blob', blob.sha)
element_list = [element]

# Get the base tree
base_tree = repo.get_git_tree(branch.commit.sha)

# Create the new tree
tree = repo.create_git_tree(element_list, base_tree)

# Create a new commit
repo.create_git_commit("Updated wstest.py via script", tree, [branch.commit])

# Update the reference of the branch
branch.edit(commit=repo.get_git_commit(branch.commit.sha))

