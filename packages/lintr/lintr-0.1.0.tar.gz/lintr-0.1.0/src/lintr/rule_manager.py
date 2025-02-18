"""Rule Manager singleton for discovering and managing rules and rule sets."""

import importlib.metadata
from typing import Optional

from lintr.rules import Rule, RuleSet
from lintr.rules.factories import RuleSetFactory
from lintr.config import BaseLintrConfig, CustomRuleDefinition


class RuleManager:
    """Singleton class for discovering and managing rules and rule sets."""

    _instance: Optional["RuleManager"] = None
    _initialized: bool = False

    def __new__(cls, *args, **kwargs) -> "RuleManager":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__init__(*args, **kwargs)
        return cls._instance

    def __init__(self, custom_rules: dict[str, CustomRuleDefinition] = {}):
        if not RuleManager._initialized:
            self._rules: dict[str, type[Rule]] = {}
            self._rule_sets: dict[str, RuleSet] = {}
            self._factory = RuleSetFactory()
            self._discover_rules()
            self._add_custom_rules(custom_rules)
            self._discover_rule_sets()
            RuleManager._initialized = True

    def _discover_rules(self) -> None:
        """Discover all available rules from entry points."""
        # In Python 3.13, entry_points() returns a dict-like object
        entry_points = importlib.metadata.entry_points()
        rule_entry_points = entry_points.select(group="lintr.rules")

        for entry_point in rule_entry_points:
            try:
                # Load the rule class or factory
                rule_cls: type[Rule] = entry_point.load()
                self._rules[rule_cls.rule_id] = rule_cls
                self._factory.register_rule_class(rule_cls.rule_id, rule_cls)
            except Exception as e:
                # Log warning about invalid entry point
                print(f"Warning: Failed to load rule {entry_point.name}: {e}")

    def _add_custom_rules(self, custom_rules: dict[str, CustomRuleDefinition]) -> None:
        for rule_id, rule_definition in custom_rules.items():
            try:
                # Lookup the base class.
                base_cls = self._rules[rule_definition.base]
                # Create a new sub-class of base.
                rule_cls = type(
                    f"CustomRule{rule_id}",
                    (base_cls,),
                    {
                        "_id": rule_id,
                        "_description": rule_definition.description,
                        "_config": type(base_cls._config).model_validate(
                            rule_definition.config
                        ),
                    },
                )
                self._rules[rule_id] = rule_cls
                self._factory.register_rule_class(rule_id, rule_cls)
            except Exception as e:
                raise Exception(f"Failed to create custom rule {rule_id}: {e}") from e

    def _discover_rule_sets(self) -> None:
        """Discover all available rule sets from entry points."""
        # In Python 3.13, entry_points() returns a dict-like object
        entry_points = importlib.metadata.entry_points()
        rule_set_entry_points = entry_points.select(group="lintr.rule_sets")

        for entry_point in rule_set_entry_points:
            try:
                factory_func = entry_point.load()
                rule_set = factory_func()  # Call the factory function
                self._rule_sets[rule_set.id] = rule_set
            except Exception as e:
                # Log warning about invalid entry point
                print(f"Warning: Failed to load rule set {entry_point.name}: {e}")

    def load_rule_sets_from_config(self, config: BaseLintrConfig) -> None:
        """Load rule sets from configuration.

        Args:
            config: Lintr configuration.

        Raises:
            ValueError: If a rule set configuration is invalid.
        """
        # First pass: Create all rule sets with rules
        # This ensures all base rule sets exist before we try to add nested sets
        for rule_set_id, rule_set_config in config.rule_sets.items():
            if rule_set_id in self._rule_sets:
                print(f"Warning: Rule set {rule_set_id} already exists, skipping")
                continue

            if not rule_set_config.rules:
                continue

            try:
                rule_set = self.create_rule_set(
                    rule_set_id=rule_set_id,
                    description=rule_set_config.name,
                    rule_ids=rule_set_config.rules,
                )
                self._rule_sets[rule_set_id] = rule_set
            except ValueError as e:
                print(f"Error creating rule set {rule_set_id}: {e}")
                continue

        # Second pass: Create rule sets with nested sets
        for rule_set_id, rule_set_config in config.rule_sets.items():
            if rule_set_id in self._rule_sets or not rule_set_config.rule_sets:
                continue

            try:
                rule_set = self.create_rule_set(
                    rule_set_id=rule_set_id,
                    description=rule_set_config.name,
                )
                self._rule_sets[rule_set_id] = rule_set
            except ValueError as e:
                print(f"Error creating rule set {rule_set_id}: {e}")
                continue

        # Third pass: Add nested rule sets
        for rule_set_id, rule_set_config in config.rule_sets.items():
            if not rule_set_config.rule_sets:
                continue

            rule_set = self._rule_sets.get(rule_set_id)
            if not rule_set:
                continue

            has_valid_nested = False
            for nested_id in rule_set_config.rule_sets:
                nested_set = self._rule_sets.get(nested_id)
                if not nested_set:
                    print(
                        f"Warning: Nested rule set {nested_id} not found for {rule_set_id}"
                    )
                    continue
                try:
                    rule_set.add_rule_set(nested_set)
                    has_valid_nested = True
                except ValueError as e:
                    print(
                        f"Error adding nested rule set {nested_id} to {rule_set_id}: {e}"
                    )

            # If this rule set has no rules and no valid nested sets, remove it
            if not rule_set_config.rules and not has_valid_nested:
                del self._rule_sets[rule_set_id]

    def get_rule_class(self, rule_id: str) -> type[Rule] | None:
        """Get a rule class by its ID.

        Args:
            rule_id: ID of the rule to get.

        Returns:
            Rule class if found, None otherwise.
        """
        return self._rules.get(rule_id)

    def get_rule_set(self, rule_set_id: str) -> RuleSet | None:
        """Get a rule set by its ID.

        Args:
            rule_set_id: ID of the rule set to get.

        Returns:
            Rule set if found, None otherwise.
        """
        return self._rule_sets.get(rule_set_id)

    def get_all_rule_ids(self) -> set[str]:
        """Get all available rule IDs.

        Returns:
            Set of all rule IDs.
        """
        return set(self._rules.keys())

    def get_all_rule_set_ids(self) -> set[str]:
        """Get all available rule set IDs.

        Returns:
            Set of all rule set IDs.
        """
        return set(self._rule_sets.keys())

    def create_rule_set(
        self,
        rule_set_id: str,
        description: str,
        rule_ids: list[str] | None = None,
        nested_rule_set_ids: list[str] | None = None,
    ) -> RuleSet:
        """Create a new rule set programmatically.

        Args:
            rule_set_id: ID for the new rule set.
            description: Description of what the rule set checks.
            rule_ids: Optional list of rule IDs to include.
            nested_rule_set_ids: Optional list of rule set IDs to include.

        Returns:
            New rule set with the specified rules.

        Raises:
            ValueError: If a rule ID is not registered.
        """
        rule_set = self._factory.create_rule_set(
            rule_set_id=rule_set_id,
            description=description,
            rule_ids=rule_ids,
            nested_rule_set_ids=nested_rule_set_ids,
        )
        self._rule_sets[rule_set_id] = rule_set
        return rule_set

    def get_all_rules(self) -> dict[str, Rule]:
        """Get all available rules with their descriptions.

        Returns:
            Dictionary mapping rule IDs to rule instances with descriptions.
        """
        rules = {}
        for rule_id, rule_class in self._rules.items():
            rules[rule_id] = rule_class(
                rule_id, ""
            )  # Description will be set by the rule class
        return rules

    def get_all_rule_sets(self) -> dict[str, RuleSet]:
        """Get all available rule sets.

        Returns:
            Dictionary mapping rule set IDs to rule set instances.
        """
        return self._rule_sets.copy()
