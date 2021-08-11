import argparse

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(prog='test',
                                         description='Test class A')

        parser.add_argument('-c',
                            '--config',
                            metavar='file',
                            help='Path to file',
                            required=True)

        args = parser.parse_args()

        print("args.config = {0}\n".format(args.config))

    except (AttributeError, TypeError, RuntimeError) as err:
        logger.logError(err.message)

    except Exception as err:
        logger.logException(err.message)
