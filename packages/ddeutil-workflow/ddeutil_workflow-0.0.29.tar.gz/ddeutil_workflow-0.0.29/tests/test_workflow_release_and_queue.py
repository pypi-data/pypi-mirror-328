from datetime import datetime
from unittest import mock

import pytest
from ddeutil.workflow.conf import Config
from ddeutil.workflow.workflow import WorkflowQueue, WorkflowRelease


def test_workflow_queue():
    wf_queue = WorkflowQueue()

    assert not wf_queue.is_queued


def test_workflow_queue_from_list():
    wf_queue = WorkflowQueue.from_list()

    assert not wf_queue.is_queued

    wf_queue = WorkflowQueue.from_list([])

    assert not wf_queue.is_queued

    wf_queue = WorkflowQueue.from_list(
        [datetime(2024, 1, 1, 1), datetime(2024, 1, 2, 1)]
    )

    assert wf_queue.is_queued

    wf_queue = WorkflowQueue.from_list(
        [WorkflowRelease.from_dt(datetime(2024, 1, 1, 1))]
    )

    assert wf_queue.is_queued

    with pytest.raises(TypeError):
        WorkflowQueue.from_list(["20240101"])

    with pytest.raises(TypeError):
        WorkflowQueue.from_list("20240101")

    wf_queue = WorkflowQueue.from_list(
        [datetime(2024, 1, 1, 1), datetime(2024, 1, 2, 1)]
    )

    assert not wf_queue.check_queue(WorkflowRelease.from_dt("2024-01-02"))
    assert wf_queue.check_queue(WorkflowRelease.from_dt("2024-01-02 01:00:00"))


@mock.patch.object(Config, "max_queue_complete_hist", 4)
def test_workflow_queue_mark_complete():
    wf_queue = WorkflowQueue(
        complete=[
            WorkflowRelease.from_dt(datetime(2024, 1, 1, i)) for i in range(5)
        ],
    )
    wf_queue.mark_complete(WorkflowRelease.from_dt(datetime(2024, 1, 1, 10)))
    assert len(wf_queue.complete) == 4


def test_workflow_release():
    workflow_release = WorkflowRelease.from_dt(dt=datetime(2024, 1, 1, 1))

    assert repr(workflow_release) == repr("2024-01-01 01:00:00")
    assert str(workflow_release) == "2024-01-01 01:00:00"

    assert workflow_release == datetime(2024, 1, 1, 1)
    assert not workflow_release < datetime(2024, 1, 1, 1)
    assert not workflow_release == 2024010101

    workflow_release = WorkflowRelease.from_dt(dt="2024-01-01")

    assert repr(workflow_release) == repr("2024-01-01 00:00:00")
    assert str(workflow_release) == "2024-01-01 00:00:00"

    with pytest.raises(TypeError):
        assert workflow_release < 1
