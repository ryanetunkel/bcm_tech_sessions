from pathlib import Path

from pytest_demo.examples.fixtures import tmp_path as module


def test_check_if_manifest_exist_without_tmp_path():
    dir = Path(__file__).resolve().parent
    assert module.check_if_manifest_exist(dir)


def test_check_if_manifest_exist_with_tmp_path(tmp_path):
    # Does not exist
    assert not module.check_if_manifest_exist(tmp_path)
    # Now create file
    manifest_path = tmp_path / "Manifest.txt"
    manifest_path.write_text("test")
    assert module.check_if_manifest_exist(tmp_path)
