from setuptools import setup

def main():
    setup(
        name="esoteric_time",
        app=['application.py'],
        data_files=["aquarius.mp3"],
        packages = ['src'],
        #package_data = {"esoteric_time": ["aquarius.mp3"]},
        maintainer='ptime',
        author_email='billc@whitehouse.gov',
    )

if __name__ == '__main__':
    main()