from flask import Flask, request, jsonify
from csv_io import parse_categorized_csv
from transaction_manager import TransactionManager
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def sort_by_category(transactions):
    pass


def get_balance(transactions):
    total, plus, minus = 0, 0, 0
    for entry in transactions:
        p = round(float(entry['price']), 2)
        total += p
        if p > 0:
            plus += p
        if p < 0:
            minus += p
    return total, plus, minus


@app.route('/transactions')
def all_transactions():
    year = request.args.get('year', default='')
    month = request.args.get('month', default='')
    res = {'total': 0, 'plus': 0,
           'minus': 0, 'transactions': []}
    if len(year) > 0 and len(month) > 0:
        manager = TransactionManager(year, month)
        if os.path.isfile(BASE_DIR+manager.categorized_transactions_path):
            print('FILE exists! ', BASE_DIR +
                  manager.categorized_transactions_path)
            manager.get_categorized_transactions()
        else:
            print('FILE DNE! ', BASE_DIR +
                  manager.categorized_transactions_path)
            manager.merge_inputs()
            manager.sort_transactions_by_date()
            manager.categorize_inputs()
            manager.write_categorized_transactions()

        total, plus, minus = get_balance(manager.categorized_transactions)
        res = {'total': total, 'plus': plus,
               'minus': minus, 'transactions': manager.categorized_transactions}

    res = jsonify(res)
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res
