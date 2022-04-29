import argparse 

import awswrangler as wr


def main():
    parser = argparse.ArgumentParser(description='Load sample CC Index data into a DynamoDB table.')
    parser.add_argument('table', help='DynamoDB table name')
    parser.add_argument('path', help='Path to the JSON file containing CC Index data')
    args = parser.parse_args()

    print(f"Loading data from '{args.path}' into {args.table} ...")
    wr.dynamodb.put_json(args.path, table_name=args.table)
    print('Done!')

if __name__ == '__main__':
    main()