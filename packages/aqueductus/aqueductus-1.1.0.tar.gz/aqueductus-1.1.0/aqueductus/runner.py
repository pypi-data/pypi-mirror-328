import os
import re
from re import Match
from typing import Any, TypedDict

import yaml

from aqueductus.providers import Provider, ProviderFactory
from aqueductus.testers import TestFactory, TestResult
from aqueductus.utils import load_module


class Test:
    def __init__(
        self,
        name: str,
        provider: Provider,
        query: str,
        test_configs: dict[str, Any],
        providers: dict[str, Provider],
    ):
        self.name = name
        self.provider = provider
        self.query = query
        self.test_configs = test_configs
        self.providers = providers
        self.results: list[TestResult] = []

    def run(self) -> None:
        query_results = self.provider.execute_query(self.query)
        for test_type, test_config in self.test_configs.items():
            test = TestFactory.create_test(
                test_type, test_config, query_results, self.providers
            )
            self.results.append(test.run())


class TestConfig(TypedDict):
    providers: list[dict[str, Any]]
    tests: list[dict[str, Any]]


class TestRunner:
    # Regex to match ${ENV_VAR_NAME} or $ENV_VAR_NAME
    _ENV_VAR_PATTERN = re.compile(r"\${([^}]+)}|\$(\S+)")
    # Regex to match {{placeholder}}
    _PLACEHOLDER_PATTERN = re.compile(r"<<(.+)>>")

    def __init__(self, config_files: list[str]):
        self.placeholders = self._load_placeholders()
        self.config = self._load_config(config_files)
        self.providers = self._init_providers()
        self.tests = self._init_tests()

    def _load_placeholders(self) -> dict[str, Any]:
        environment = load_module("environment.py")

        # Return the PLACEHOLDERS variable if it exists
        if environment and hasattr(environment, "PLACEHOLDERS"):
            if not isinstance(environment.PLACEHOLDERS, dict):
                raise ValueError(
                    "PLACEHOLDERS in 'environment.py' must be a dictionary, "
                    f"got {type(environment.PLACEHOLDERS).__name__} instead"
                )
            return environment.PLACEHOLDERS

        return {}

    @staticmethod
    def _replace_env_vars_text(match: Match[str]) -> str:
        env_var_name = (match.group(1) or match.group(2)).strip()
        env_var_value = os.getenv(env_var_name)
        if env_var_value is None:
            raise ValueError(f"Environment variable '{env_var_name}' is not set")
        return env_var_value

    def _replace_placeholders_text(self, match: Match[str]) -> str:
        placeholder_name = match.group(1).strip()
        placeholder_value = self.placeholders.get(placeholder_name)
        if placeholder_value is None:
            raise ValueError(f"Placeholder variable '{placeholder_name}' is not set")
        return placeholder_value

    def _load_config(self, config_files: list[str]) -> TestConfig:
        merged_config: TestConfig = {"providers": [], "tests": []}
        for config_file in config_files:
            # TODO: Add yaml schema validation
            with open(config_file, "r") as f:
                yaml_text = f.read()
                yaml_text = self._ENV_VAR_PATTERN.sub(
                    self._replace_env_vars_text, yaml_text
                )
                yaml_text = self._PLACEHOLDER_PATTERN.sub(
                    self._replace_placeholders_text, yaml_text
                )

                config = yaml.safe_load(yaml_text)
                if "providers" in config:
                    merged_config["providers"].extend(config["providers"])
                if "tests" in config:
                    merged_config["tests"].extend(config["tests"])
        return merged_config

    def _init_providers(self) -> dict[str, Provider]:
        providers = {}
        for provider_config in self.config["providers"]:
            providers[provider_config["name"]] = ProviderFactory.create_provider(
                provider_config["type"],
                provider_config["config"],
            )
        return providers

    def _init_tests(self) -> list[Test]:
        tests = []
        for test_config in self.config["tests"]:
            provider = self.providers[test_config["provider"]]
            test_specific_configs = {
                k: v
                for k, v in test_config.items()
                if k in TestFactory.list_available_tests()
            }
            tests.append(
                Test(
                    name=test_config["name"],
                    provider=provider,
                    query=test_config["query"],
                    test_configs=test_specific_configs,
                    providers=self.providers,
                )
            )
        return tests

    def run_all(self) -> list[Test]:
        for test in self.tests:
            test.run()
        return self.tests
