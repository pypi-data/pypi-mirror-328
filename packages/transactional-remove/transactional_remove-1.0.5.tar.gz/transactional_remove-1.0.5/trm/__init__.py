def main():
    import argparse
    from .remove import rm
    from .rollback import rollback
    
    program = argparse.ArgumentParser(description="Transactional rm command, with power failure protocols")

    program.add_argument("-r", "--rm", help="Remove filesystem items", type=rm, nargs="+")
    program.add_argument("-b", "--rb", help="Rollback previously removed items", type=rollback, nargs="+")

    program.parse_args()

if __name__ == "__main__":
    main()