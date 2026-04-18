import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='CLI logs analyzer tool')
    parser.add_argument('log_file', help='Path to the log file to analyze')
    parser.add_argument('--output', '-o', help='Path to save the analysis report')
    parser.add_argument('-l', '--level', default='INFO', help='Log level')
    args = parser.parse_args()
    return args

def main():
    arg = parse_args()
    print(arg)

if __name__ == "__main__":
    main()