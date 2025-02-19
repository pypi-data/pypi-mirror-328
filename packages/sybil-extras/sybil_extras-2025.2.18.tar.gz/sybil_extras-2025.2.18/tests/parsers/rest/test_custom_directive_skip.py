"""
Tests for the custom directive skip parser for reST.
"""

from pathlib import Path

from sybil import Sybil
from sybil.evaluators.skip import SkipState
from sybil.parsers.rest.codeblock import PythonCodeBlockParser

from sybil_extras.parsers.rest.custom_directive_skip import (
    CustomDirectiveSkipParser,
)


def test_skip(tmp_path: Path) -> None:
    """
    The custom directive skip parser can be used to set skips.
    """
    content = """\

    .. code-block:: python

        x = []

    .. custom-skip: next

    .. code-block:: python

        x = [*x, 2]

    .. code-block:: python

        x = [*x, 3]
    """

    test_document = tmp_path / "test.rst"
    test_document.write_text(data=content, encoding="utf-8")

    skip_parser = CustomDirectiveSkipParser(directive="custom-skip")
    code_block_parser = PythonCodeBlockParser()

    sybil = Sybil(parsers=[code_block_parser, skip_parser])
    document = sybil.parse(path=test_document)
    skip_states: list[SkipState] = []
    for example in document.examples():
        example.evaluate()
        skip_states.append(skip_parser.skipper.state_for(example=example))

    assert document.namespace["x"] == [3]
    expected_skip_states = [
        SkipState(
            active=True,
            remove=True,
            exception=None,
            last_action="next",
        ),
        SkipState(
            active=True,
            remove=True,
            exception=None,
            last_action="next",
        ),
        SkipState(active=True, remove=False, exception=None, last_action=None),
        SkipState(active=True, remove=False, exception=None, last_action=None),
    ]
    assert skip_states == expected_skip_states
