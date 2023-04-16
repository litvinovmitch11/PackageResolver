from manager import Manager
import argparse

parser = argparse.ArgumentParser(
    prog='PackageResolver',
    description='Find dependencies in package versions')

parser.add_argument('filename', type=str, help='Name of file with dependencies')
parser.add_argument('package_name', type=str, help='Package name for which you want to get the latest version')
parser.add_argument('-v', '--package_version', type=int,
                    help='Possible set of all transitive dependencies for given package name and version')

args = parser.parse_args()

manager = Manager(args.filename)
if args.package_version:
    if manager.set_versions(args.package_name, args.package_version):
        print('Available combination of versions:')
        versions = manager.get_versions()
        for name in versions:
            print(f'{name}: {versions[name]}')
    else:
        print('No available combination of versions')
else:
    print(f'Last version of package "{args.package_name}" is {manager.get_last_version(args.package_name)}')
