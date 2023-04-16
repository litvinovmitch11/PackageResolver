from parser import Parser


class Manager:
    def __init__(self, name):
        self._name = name
        self._parser = Parser(name)
        self._parser.make_tree()
        self._tree = self._parser.get_tree()
        self._versions = dict()

    def get_last_version(self, package_name):
        return max(self._tree[package_name])

    # Да, корректно не работает... Знаю...
    def set_versions(self, package_name, package_version):
        package_dependencies = self._tree[package_name][package_version]
        if package_name in self._versions:
            if self._versions[package_name] == package_version:
                return True
            return False

        if all([(name in self._versions) and (self._versions[name] in package_dependencies[name])
                for name in package_dependencies]):
            self._versions[package_name] = package_version
            return True
        if package_name not in self._versions:
            self._versions[package_name] = package_version
        for name in package_dependencies:
            for v in package_dependencies[name]:
                if self.set_versions(name, v):
                    break
            else:
                return False
        return True

    def get_versions(self):
        return self._versions
