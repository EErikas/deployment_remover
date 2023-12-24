# GitHub Deployments Deletion Script
This Python script allows you to interact with GitHub deployments by listing, deleting a specific deployment, or deleting all deployments in a repository.

## Prerequisites
Before using the script, make sure you have the following:

- Python 3 installed on your machine.

- The requests library installed. You can install it using the following command:
    ```bash
    pip install requests
    ```

## Running the Script
For every command you need to provide: 
- Your GitHub username 
- Your GitHub Repository name
- GitHub token that has option `repo_deployments` enabled.

There are the fllowing options to run the script:
### List Deployments:
To list all deployments in the repository, use the `--list` option:
```bash
python github_deployments.py <your_username> <your_repository> <your_token> --list
```
### Delete a Specific Deployment:
To delete a specific deployment by ID, use the `--delete` option followed by the deployment ID:
```bash
python github_deployments.py <your_username> <your_repository> <your_token> --delete <deployment_id>
```

### Delete All Deployments:
To delete all deployments in the repository, use the `--delete_all` option:
```bash
python github_deployments.py <your_username> <your_repository> <your_token> --delete <deployment_id>
```

## Notes
The script uses the GitHub API, so make sure your personal access token has the necessary permissions to list and delete deployments in the repository. Tokens can be created here: https://github.com/settings/tokens

If you encounter any issues or errors, check the script output for details, including the response code and message from the GitHub API.

Feel free to customize the script or extend its functionality based on your requirements.