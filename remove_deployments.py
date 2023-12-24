import argparse
import json
from typing import List, Dict
import requests


class Deployments:
    def __init__(self, user, repo, token) -> None:
        self.url = f'https://api.github.com/repos/{user}/{repo}/deployments'
        self.credentials = (user, token)

    @staticmethod
    def __error_msg(r) -> None:
        print(f'Command failed; Response code: {r.status_code}, {r.text}')

    def list_deployments(self) -> List[Dict]:
        response = requests.get(url=self.url, auth=self.credentials)
        if response.status_code == 200:
            return response.json()
        self.__error_msg(response)
        return []

    def delete_deployment(self, id) -> None:
        response = requests.delete(url=f'{self.url}/{id}', auth=self.credentials)
        if response.status_code == 204:
            print(f' -> Deployment {id} deleted successfully')
        else:
            self.__error_msg(response)

    def delete_all(self) -> None:
        deployments = self.list_deployments()
        if deployments:
            print(f'Starting deletion of {len(deployments)}: ')
            for deployment in deployments:
                self.delete_deployment(deployment['id'])
            print('Deletion completed!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='List/Delete GitHub deployments.')
    parser.add_argument('user', help='GitHub username')
    parser.add_argument('repo', help='GitHub repository name')
    parser.add_argument('token', help='GitHub personal access token')

    # Optional arguments
    parser.add_argument('--list', action='store_true', help='List deployments')
    parser.add_argument('--delete', type=int, metavar='DEPLOYMENT_ID',
                        help='Delete a specific deployment by ID',
    )
    parser.add_argument('--delete_all', action='store_true', 
                        help='Delete all deployments'
    )

    args = parser.parse_args()

    deployment_actions = Deployments(args.user, args.repo, args.token)
    if args.list:
        print(json.dumps(deployment_actions.list_deployments(), indent=2))
    elif args.delete:
        deployment_actions.delete_deployment(args.delete)
    elif args.delete_all:
        deployment_actions.delete_all()
    else:
        parser.print_help()
        exit(1)
