import os
import subprocess
import toml

from git import Repo


class DryRunRelease():
    version_components = {'major': 0, 'minor': 1, 'patch': 2}

    def __init__(self, bump_type):
        self.bump_type = bump_type

        self.from_version, self.to_version = DryRunRelease.determine_version_numbers(
            self.bump_type)

        os.makedirs('release', exist_ok=True)

    @staticmethod
    def determine_version_numbers(version_increment: str):
        toml_str = DryRunRelease.read_current_toml()

        version_str = toml_str['project']['version']
        version_parts = version_str.split('.')

        version_parts[DryRunRelease.version_components[version_increment]] = str(
            int(version_parts[DryRunRelease.version_components[version_increment]]) + 1)
        new_version = '.'.join(version_parts)

        toml_str['project']['version'] = new_version

        return (version_str, new_version)

    def __repr__(self):
        return f"{self.from_version} + {self.bump_type} => {self.to_version}"

    def do_release(self):
        self.bump_version()
        self.execute_buildtool()
        self.write_changelog()
        self.write_changes()
        self.create_tag()
        self.push()
        self.create_github_release()

    def bump_version(self):
        toml_content = self.read_current_toml()
        toml_content['project']['version'] = self.to_version

        with open('pyproject.toml', 'wt', encoding='utf-8') as f:
            f.write(toml.dumps(toml_content))
        with open("release/version.new.txt", 'wt', encoding='utf-8') as f:
            f.write(self.to_version)
        with open("release/version.old.txt", 'wt', encoding='utf-8') as f:
            f.write(self.from_version)
        with open("release/changes.txt", 'wt', encoding='utf-8') as f:
            f.write(self.get_changes())

    def execute_buildtool(self):
        subprocess.run(['uv', 'sync'], check=True)

    def write_changes(self):
        pass  # only for reals

    def create_tag(self):
        pass  # only for reals

    def push(self):
        pass  # only for reals

    def get_changes(self, head=True):
        return DryRunRelease.get_release_changes(self.from_version, 'HEAD' if head else self.to_version)

    def write_changelog(self):
        existing = ""
        if os.path.exists('CHANGELOG.md'):
            with open('CHANGELOG.md', 'rt') as f:
                existing = f.read()

        with open('CHANGELOG.md', 'wt', encoding='utf-8') as f:
            f.write(f"## {self.to_version}\n\n")
            f.write(self.get_changes())
            f.write("\n\n")
            f.write(existing)

    def create_github_release(self):
        pass

    @staticmethod
    def read_current_toml():
        with open('pyproject.toml', 'rt', encoding='utf-8') as f:
            toml_content = toml.loads(f.read())
        return toml_content

    @staticmethod
    def get_release_changes(from_version, to_version="HEAD"):
        r = Repo('.')

        prefix = "release/"
        if to_version.upper().strip() == "HEAD":
            prefix = ""

        o = r.git.log(
            f"release/{from_version}...{prefix}{to_version}", oneline=True)
        return o


class LocalRelease(DryRunRelease):

    def write_changes(self):
        super().write_changes()

        r = Repo('.')
        r.git.add('pyproject.toml')
        r.git.add('CHANGELOG.md')
        r.git.add('uv.lock')
        r.git.commit(message=f"Release [{self.bump_type}] version to {
                     self.to_version}")

    def create_tag(self):
        r = Repo('.')
        r.git.tag(f"release/{self.to_version}")


class FullRelease(LocalRelease):
    def __init__(self, bump_type):
        super().__init__(bump_type)

    def bump_version(self):
        super().bump_version()

    def push(self):
        r = Repo('.')
        r.git.push('origin')
        r.git.push('origin', '--tags')

    def create_github_release(self):
        subprocess.run(['gh', 'release', 'create', self.to_version, '--notes-file=release/changes.txt',
                       '--latest=True', f"--title={self.to_version}"], check=True)
