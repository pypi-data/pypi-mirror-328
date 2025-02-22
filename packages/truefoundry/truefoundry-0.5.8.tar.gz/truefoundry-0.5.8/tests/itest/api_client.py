import os
from pprint import pprint

import requests


class TruefoundryAPIClient:
    """Client for interacting with Truefoundry API"""

    def __init__(self):
        self.host = os.getenv("ITEST_TFY_HOST")
        self.api_key = os.getenv("ITEST_TFY_API_KEY")
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        if not self.host or not self.api_key:
            raise ValueError(
                "TFY_HOST and TFY_API_KEY environment variables are required"
            )

    def get_provider_account_id(self, provider_account_fqn: str) -> str:
        url = f"{self.host}/api/svc/v1/provider-accounts"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()

            # Parse the nested response
            data = response.json()
            if "providerAccounts" not in data:
                raise ValueError("Unexpected API response format")

            provider_accounts = data["providerAccounts"]

            # Find matching account
            for account in provider_accounts:
                if account["fqn"] == provider_account_fqn:
                    return account["id"]

            raise ValueError(
                f"Provider account with FQN {provider_account_fqn} not found. "
                f"Available FQNs: {[acc['fqn'] for acc in provider_accounts]}"
            )

        except (ValueError, requests.exceptions.RequestException) as e:
            print(f"Error in get provider account operation: {e}")
            raise

    def delete_provider_account(self, provider_account_fqn: str) -> None:
        try:
            provider_account_id = self.get_provider_account_id(provider_account_fqn)
            pprint(provider_account_id)
            url = f"{self.host}/api/svc/v1/provider-accounts/{provider_account_id}"
            response = requests.delete(url, headers=self.headers)
            response.raise_for_status()
            assert response.status_code == 200

        except (ValueError, requests.exceptions.RequestException) as e:
            print(f"Error in delete provider account operation: {e}")
            raise

    def get_ml_repo_id(self, repo_name: str) -> str:
        url = f"{self.host}/api/ml/api/2.0/mlflow/experiments/list"

        try:
            response = requests.get(
                url, headers=self.headers, params={"filter_name": repo_name}
            )
            response.raise_for_status()
            data = response.json()
            if not data["experiments"]:
                raise ValueError(f"Invalid API response structure: {data}")
            if (
                not data["experiments"][0]
                or data["experiments"][0]["name"] != repo_name
            ):
                raise ValueError(f"ML repository '{repo_name}' not found. ")
            return data["experiments"][0]["experiment_id"]

        except (ValueError, requests.exceptions.RequestException) as e:
            print(f"Error in get ML repository operation: {e}")
            raise

    def delete_ml_repo(self, repo_name: str) -> None:
        try:
            repo_id = self.get_ml_repo_id(repo_name)
            url = f"{self.host}/api/ml/api/2.0/mlflow/experiments/hard-delete"
            payload = {"experiment_id": repo_id}
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            assert response.status_code == 200

        except (ValueError, requests.exceptions.RequestException) as e:
            print(f"Error in delete ML repository operation: {e}")
            raise
