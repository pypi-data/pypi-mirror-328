import sys
import types
from threading import Event
from typing import Self

import pytest
from loguru import logger

from otter.config.models import BaseTaskDefinition, PreTaskDefinition, TaskDefinition
from otter.manifest.models import TaskManifest
from otter.task import PreTask, Task, TaskRegistry

dummy_task_module = types.ModuleType('dummy')
dummy_pre_task_module = types.ModuleType('dummy_pre')


class DummyDefinition(BaseTaskDefinition):
    dummy: bool = True


class Dummy(Task):
    def __init__(self, definition: TaskDefinition) -> None:
        super().__init__(definition)
        self.definition: DummyDefinition

    def run(self, *, abort: Event) -> Self:
        logger.info('dummy task')
        return self


dummy_task_module.DummyDefinition = DummyDefinition  # type: ignore[attr-defined]
dummy_task_module.Dummy = Dummy  # type: ignore[attr-defined]

sys.modules['dummy'] = dummy_task_module


class DummyPreDefinition(PreTaskDefinition):
    dummy_pre: bool = True


class DummyPre(PreTask):
    def __init__(self, definition: DummyPreDefinition) -> None:
        super().__init__(definition)
        self.definition: DummyPreDefinition

    def run(self, *, abort: Event) -> Self:
        logger.info('dummy PreTask')
        return self


dummy_pre_task_module.DummyPreDefinition = DummyPreDefinition  # type: ignore[attr-defined]
dummy_pre_task_module.DummyPre = DummyPre  # type: ignore[attr-defined]

sys.modules['dummy_pre'] = dummy_pre_task_module


@pytest.fixture
def patch_import_module(monkeypatch):
    monkeypatch.setattr(
        'importlib.import_module',
        lambda x: sys.modules[x.split('.')[-1]],
    )


@pytest.fixture
def patch_path_glob(monkeypatch):
    def mock_glob(*args, **kwargs):
        class MockPath:
            def __init__(self, name) -> None:
                self.name = name
                self.stem = name.rsplit('.')[0]

        # Yield a mock path object with the name set to your module's filename
        yield from [MockPath('dummy.py'), MockPath('dummy_pre.py')]

    monkeypatch.setattr('pathlib.Path.glob', mock_glob)


@pytest.fixture
def task_definition():
    return BaseTaskDefinition(name='test_task')  # type: ignore[attr-defined]


@pytest.fixture
def task_manifest():
    return TaskManifest(name='test_task')


@pytest.fixture
def PreTask(definition):
    return PreTask(definition=definition)


@pytest.fixture
def task(definition):
    return Task(definition=definition)


def test_register_task(patch_import_module, patch_path_glob):
    task_registry = TaskRegistry()
    task_registry.register_tasks()

    assert 'dummy' in task_registry.tasks
    assert task_registry.tasks['dummy'] is Dummy
    assert 'dummy' in task_registry.task_definitions
    assert task_registry.task_definitions['dummy'] is DummyDefinition
    assert 'dummy' in task_registry.task_manifests
    assert task_registry.task_manifests['dummy'] is TaskManifest
    assert 'dummy' not in task_registry.pre_tasks


def test_register_PreTask(patch_import_module, patch_path_glob):
    task_registry = TaskRegistry()
    task_registry.register_tasks()

    assert 'dummy_pre' in task_registry.pre_tasks


def test_is_PreTask(patch_import_module, patch_path_glob):
    task_registry = TaskRegistry()
    task_registry.register_tasks()

    assert not task_registry.is_PreTask(BaseTaskDefinition(name='dummy'))
    assert task_registry.is_PreTask(BaseTaskDefinition(name='dummy_pre'))


def test_instantiate_valid_task(patch_import_module, patch_path_glob, monkeypatch):
    task_registry = TaskRegistry()
    task_registry.register_tasks()
    new_task_definition = DummyDefinition(name='dummy', dummy=False)

    new_task = task_registry.instantiate_t(new_task_definition)

    assert isinstance(new_task, Task)
    assert isinstance(new_task, Dummy)
    assert isinstance(new_task._manifest, TaskManifest)
    assert isinstance(new_task.definition, BaseTaskDefinition)
    assert isinstance(new_task.definition, DummyDefinition)
    assert new_task.definition.dummy is False


def test_instantiate_invalid_task(patch_import_module, patch_path_glob):
    task_registry = TaskRegistry()
    task_registry.register_tasks()
    new_task_definition = BaseTaskDefinition(name='invalid')

    with pytest.raises(SystemExit) as e:
        task_registry.instantiate_t(new_task_definition)

    assert e.type is SystemExit
    assert e.value.code == 1


@pytest.mark.filterwarnings('ignore::UserWarning')
def test_instantiate_invalid_task_definition(patch_import_module, patch_path_glob):
    task_registry = TaskRegistry()
    task_registry.register_tasks()
    new_task_definition = DummyDefinition(name='dummy', dummy=False)
    new_task_definition.dummy = 'invalid'  # type: ignore[attr-assignment]

    with pytest.raises(SystemExit) as e:
        task_registry.instantiate_t(new_task_definition)

    assert e.type is SystemExit
    assert e.value.code == 1
