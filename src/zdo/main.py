import argparse

def main():

    parser = argparse.ArgumentParser(
        prog='zdo',
        description='A JSON productivity and notetaking app.',
        epilog='Software Issues? Open an issue at https://github.com/jadevgit/zdo '
    )

    arguments = parser.parse_args()
    

main()
