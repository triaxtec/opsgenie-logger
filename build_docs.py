import subprocess


def main():
    build_command = "sphinx-build -M html docs docs/build"
    subprocess.run(build_command, shell=True)


if __name__ == "__main__":
    main()
