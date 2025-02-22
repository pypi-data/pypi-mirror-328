import ast
import json
from dataclasses import asdict
from pathlib import Path
from typing import Dict, List, Set, Union

from dagsonar import (DagConfig, DagReference, ExprReference, Parser,
                      ShellScriptReference, TaskReference, compute_hash)


class TaskTracker:
    """Main class for tracking DAG task changes."""

    def __init__(self, history_file: Path = Path("task_history.json")):
        self.history_file = history_file
        self.dag_history = self._load_history()

    def _load_history(self):
        try:
            if self.history_file.exists():
                with open(self.history_file, "r") as f:
                    return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error loading history file: {e}")

    def save_history(self, reference: List[Dict[str, str | DagReference]]):
        with open(self.history_file, "w") as f:
            json.dump(reference, f, indent=2, cls=ReferenceEncoder)

    def start_monitoring(self):
        """Start monitoring DAG tasks for changes."""
        pass

    def track_tasks(
        self, dag_configs: Dict[str, DagConfig]
    ) -> List[Dict[str, str | DagReference]]:
        dag_references: List[Dict[str, str | DagReference]] = []
        for dag, config in dag_configs.items():
            if not config.path.exists():
                print(f"Warning: Dag file not found: {config.path}")
                continue
            else:
                history = list()
                parser = Parser(config.path)
                tasks = parser.get_tasks(config.tasks)
                for task in tasks:
                    tracks = self._process_task(task, parser)
                    history.append(tracks)
                dag_references.append(
                    {
                        "dag_id": dag,
                        "reference": DagReference(dag_id=dag, task_history=history),
                    }
                )

        return dag_references

    def check_for_changes(
        self, new_reference: List[Dict[str, Union[str, DagReference]]]
    ) -> List[Dict[str, str]]:
        """
        Returns a list of task IDs whose hash values have changed.
        """
        changed_tasks = []
        result = []

        for dag in new_reference:
            reference: Union[DagReference, str] = dag.get("reference", "")

            if not isinstance(reference, DagReference):
                continue

            dag_id = reference.dag_id
            new_hashes = {task.task_id: task.hash for task in reference.task_history}
            print(dag_id, new_hashes)

            history_reference = None
            if self.dag_history is None:
                continue

            for dag in self.dag_history:
                ref = dag.get("reference")
                if ref["dag_id"] == dag_id:
                    history_reference = ref

            if history_reference is None:
                continue

            old_hashes = {
                task["task_id"]: task["hash"]
                for task in history_reference["task_history"]
            }

            for task_id, new_hash in new_hashes.items():
                if task_id not in old_hashes or old_hashes[task_id] != new_hash:
                    changed_tasks.append(task_id)

            result.append({"dag": reference.dag_id, "tasks": changed_tasks})

        return result

    def _process_task(
        self, task: ast.FunctionDef | ast.Call, parser: Parser
    ) -> TaskReference:
        reference = TaskReference()
        if isinstance(task, ast.FunctionDef):
            reference.task_id = task.name
            reference.content = ast.dump(task)

            decorators = task.decorator_list
            decorated_bash = False
            for decorator in decorators:
                if isinstance(decorator, ast.Attribute):
                    decorated_bash = decorator.attr == "bash"

            def traverse(head, intend=0):
                # print("\t->" * intend + (ast.dump(head)))

                # Check .sh file to track
                if decorated_bash and isinstance(head, ast.Constant):
                    files = [
                        file for file in head.value.split(" ") if file.endswith(".sh")
                    ]
                    for file in files:
                        with open(file, "r") as f:
                            content = f.read()
                            reference.shell_scripts.append(
                                ShellScriptReference(
                                    path=Path(file),
                                    content=ast.dump(ast.Constant(content)),
                                )
                            )

                if isinstance(head, ast.Name):
                    var = parser.find_variable_reference(variable=head)
                    if var.value is not None:
                        reference.external_variables.append(
                            ExprReference(name=head.id, content=ast.dump(var))
                        )

                if isinstance(head, ast.Call):
                    if isinstance(head.func, ast.Name):
                        fn = parser.find_function_reference(fn=head.func)
                        if fn is not None:
                            reference.called_functions.append(
                                ExprReference(name=fn.name, content=ast.dump(fn))
                            )

                for child in ast.iter_child_nodes(head):
                    traverse(child, intend + 1)

            traverse(task)
        elif isinstance(task, ast.Call):
            bash_operator = (
                isinstance(task.func, ast.Name) and task.func.id == "BashOperator"
            )
            reference.task_id = task.func.id if isinstance(task.func, ast.Name) else ""
            reference.content = ast.dump(task)

            for arg in task.args:
                pass
            for keyword in task.keywords:
                if isinstance(keyword.value, ast.Name):
                    ref = parser.find_variable_reference(keyword.value)
                    keyword.value = ref
                    reference.external_variables.append(
                        ExprReference(
                            name=keyword.value.value, content=ast.dump(keyword)
                        )
                    )

                if (
                    bash_operator
                    and keyword.arg == "bash_command"
                    and isinstance(keyword.value, ast.Constant)
                ):
                    files = [
                        file
                        for file in keyword.value.value.split(" ")
                        if file.endswith(".sh")
                    ]
                    for file in files:
                        with open(file, "r") as f:
                            content = f.read()
                            reference.shell_scripts.append(
                                ShellScriptReference(
                                    path=Path(file),
                                    content=ast.dump(ast.Constant(content)),
                                )
                            )
        reference.hash = compute_hash(reference)
        return reference


class ReferenceEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(
            o, (DagReference, TaskReference, ShellScriptReference, ExprReference)
        ):
            return asdict(o)

        if isinstance(o, Path):
            return str(o)

        return super().default(o)
