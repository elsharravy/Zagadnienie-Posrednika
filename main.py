from flask import Flask, render_template, request, jsonify
import json
import calculator, data

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('Posrednik.html')

@app.route('/generate', methods=['POST'])
def solvePosrednik():
    x = 3
    y = 2
    popyt = [ int(request.form['dc1']), int(request.form['dc2']), int(request.form['dc3']) ]
    podaz = [ int(request.form['ss1']), int(request.form['ss2']) ]
    sell = [int(request.form['spc1']), int(request.form['spc2']), int(request.form['spc3'])]
    buy = [int(request.form['pps1']), int(request.form['pps2'])]
    cost_matrix = [ [ int(request.form['t11']), int(request.form['t21']) ],[ int(request.form['t12']), int(request.form['t22']) ], [ int(request.form['t13']), int(request.form['t23']) ]   ]

    print( "----------Dane zczytane ze strony:" )
    print("Popyt: " + str(popyt))
    print("Podaż: " + str(podaz))
    print("Cena sprzedaży: " + str(sell))
    print("Cena kupna: " + str(buy))
    print("Macierz kosztów: " + str(cost_matrix))
        
    dat = data.data(popyt,podaz,sell,buy,cost_matrix,x,y)
    dat = calculator.calculator.calculator_enter(dat)
    dat = calculator.calculator.calculator_optimalization(dat)
    dat = calculator.calculator.calculator_exit(dat)

    pm = dat.profit_matrix
    ot = dat.opt_matrix
    zyski_jednostkowe = [ pm[0][0:2],pm[1][0:2],pm[2][0:2] ]
    transport_optymalny = [ ot[0][0:2],ot[1][0:2],ot[2][0:2] ]
    dochod = dat.profit_total
    koszt_kupno = dat.buy_cost_total
    koszt_transport = dat.transport_cost_total
    koszt_total = koszt_kupno + koszt_transport
    przychod = dat.income_total

    print( "----------Dane obliczone:" )
    print("Zysk jednostkowy: " + str(zyski_jednostkowe))
    print("Transport optymalny: " + str(transport_optymalny))
    print("Dochód: " + str(dochod))

    return render_template('Posrednik.html',
    zyski_jednostkowe=zyski_jednostkowe,
    transport_optymalny=transport_optymalny,
    dochod=dochod,
    przychod=przychod,
    koszt_kupno=koszt_kupno,
    koszt_transport=koszt_transport,
    koszt_total=koszt_total,
    form_data=request.form)


if __name__ == '__main__':
    app.run(debug=True)
