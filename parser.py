class Parser:
    def __init__(self, name_file):
        self._tree = {}
        self._name_file = name_file

    def make_tree(self):
        with open(self._name_file) as file:
            for line in file:
                package, dependencies_list = line.strip().split(':')
                name, version = package.split(' ')
                version = int(version)

                if name not in self._tree:
                    self._tree[name] = dict()

                self._tree[name][version] = dict()
                for packages in dependencies_list.split(','):
                    if packages != '':
                        depend_name, depend_versions = packages.strip().split(' ')
                        list_depend_version = depend_versions.split('..')
                        if len(list_depend_version) == 1:
                            self._tree[name][version][depend_name] = {int(list_depend_version[0])}
                        else:
                            self._tree[name][version][depend_name] = set(
                                range(int(list_depend_version[0]), int(list_depend_version[1]) + 1))

    def get_tree(self):
        return self._tree
