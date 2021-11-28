from flask import Flask, request, jsonify
from csv_io import parse_categorized_csv
from transaction import Transactions

app = Flask(__name__)
categorized_cc = "/output/categorized_cc.csv"
categorized_dict = parse_categorized_csv(categorized_cc)

'''
TO DO:
display month by month
• Spendings by category
• Budget by category
• Balance each month
'''


@app.route('/alltransactions')
def all_transactions():
    t = Transactions(categorized_dict)
    year = request.args.get('year', default='')
    month = request.args.get('month', default='')
    if len(year) > 0 and len(month) > 0:
        filtered = t.filter_by_yearmonth(year, month)
        filtered_sum = round(
            sum(float(entry['price']) for entry in filtered), 2)
        plus = round(
            sum(float(entry['price']) for entry in filtered if float(entry['price']) > 0), 2)
        minus = round(
            sum(float(entry['price']) for entry in filtered if float(entry['price']) < 0), 2)
        res = jsonify({'total': filtered_sum, 'plus': plus,
                      'minus': minus, 'transactions': filtered})
        res.headers.add('Access-Control-Allow-Origin', '*')
        print("filtered", res)
        return res

    total = round(
        sum(float(entry['price']) for entry in t.transactions), 2)
    plus = round(
        sum(float(entry['price']) for entry in t.transactions if float(entry['price']) > 0), 2)
    minus = round(
        sum(float(entry['price']) for entry in t.transactions if float(entry['price']) < 0), 2)
    res = jsonify({'total': total, 'plus': plus, 'minus': minus,
                  'transactions': t.transactions})
    res.headers.add('Access-Control-Allow-Origin', '*')
    print("not filtered", res)
    return res


@app.route('/savings')
def all_savings():
    return
