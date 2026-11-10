"""Installer invariants, using tiny local source fixtures and no network."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('installer', ROOT / 'install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name).resolve()
        self.target = self.base / 'project'
        self.cache = self.base / 'cache'
        self.entry = {'source': 'https://github.com/example/skills.git',
                      'commit': 'a' * 40, 'paths': ['SKILL.md', 'LICENSE'],
                      'entrypoints': ['SKILL.md'], 'license_paths': ['LICENSE']}
        self.release = self.cache / 'demo' / self.entry['commit']
        self.release.mkdir(parents=True)
        (self.release / 'SKILL.md').write_text('Original skill\n')
        (self.release / 'LICENSE').write_text('Original license\n')
        self.entry['tree_sha256'] = installer.lib.digest(self.release)
        self.entries = {'demo': self.entry}

    def run_install(self):
        return installer.install(self.target, self.entries, self.cache)

    def test_repeat_install_preserves_configuration_and_verifies_content(self):
        config = self.target / '.codex/config.toml'
        config.parent.mkdir(parents=True)
        config.write_text('model = "keep-my-model"\n')
        skill = self.run_install()
        before = installer.lib.digest(skill)
        self.run_install()
        self.assertEqual(before, installer.lib.digest(skill))
        self.assertEqual(config.read_text(), 'model = "keep-my-model"\n')
        self.assertFalse((self.target / 'AGENTS.md').exists())
        installed = self.target / '.design-workflow/library/demo' / self.entry['commit']
        installer.lib.verify(installed, self.entry)
        settings = json.loads((skill / 'installation.json').read_text())
        self.assertEqual((skill / settings['library']).resolve(), installed.parents[1])

    def test_existing_router_conflict_is_preserved_before_library_write(self):
        path = self.target / '.agents/skills/design'
        path.mkdir(parents=True)
        (path / 'SKILL.md').write_text('My existing skill')
        with self.assertRaisesRegex(ValueError, 'Existing Design skill differs'):
            self.run_install()
        self.assertEqual((path / 'SKILL.md').read_text(), 'My existing skill')
        self.assertFalse((self.target / '.design-workflow/library').exists())

    def test_bad_cache_never_exposes_router(self):
        (self.release / 'SKILL.md').write_text('Changed upstream bytes')
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            self.run_install()
        self.assertFalse((self.target / '.agents/skills/design').exists())

    def test_modified_installed_original_is_rejected(self):
        self.run_install()
        path = self.target / '.design-workflow/library/demo' / self.entry['commit'] / 'LICENSE'
        path.write_text('Modified license')
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            self.run_install()
        self.assertEqual(path.read_text(), 'Modified license')

    def test_symlinked_release_cannot_redirect_writes(self):
        parent = self.target / '.design-workflow/library'
        parent.mkdir(parents=True)
        (parent / 'demo').symlink_to(self.cache / 'demo', target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'symlinks'):
            self.run_install()

    def test_all_sources_verified_before_any_are_promoted(self):
        second = dict(self.entry, commit='b' * 40)
        self.entries['missing'] = second
        with self.assertRaises(ValueError):
            self.run_install()
        self.assertFalse((self.target / '.design-workflow/library/demo').exists())
        self.assertFalse((self.target / '.agents/skills/design').exists())

    def test_archive_traversal_and_unpinned_source_rejected(self):
        for value in ['../outside', '/absolute', 'a/../../escape', 'a\\escape']:
            with self.assertRaises(ValueError):
                installer.safe_rel(value)
        for change in [{'source': 'file:///private/source'}, {'commit': 'main'},
                       {'paths': ['../outside']}]:
            with self.assertRaises(ValueError):
                installer.validate({'demo': dict(self.entry, **change)})

    def test_lock_prevents_concurrent_install(self):
        self.target.mkdir()
        lock = self.target / '.design-workflow-install.lock'
        lock.write_text('')
        with self.assertRaisesRegex(ValueError, 'Another install'):
            self.run_install()
        self.assertTrue(lock.exists())


if __name__ == '__main__':
    unittest.main()
